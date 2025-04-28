# app.py
import streamlit as st
import sqlite3
from datetime import datetime
from fpdf import FPDF
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json
import tempfile

# Load the LLaMA model
llm = LlamaCpp(
    model_path="/home/jmoses/Models/llama-2-7b-chat.Q4_0.gguf",
    n_ctx=2048,
    temperature=0.7,
    top_p=0.9,
    chat_format="llama-2"
)

# LangChain setup
parse_prompt = PromptTemplate(
    input_variables=["entry"],
    template="""
You are a liquor sales assistant. Extract structured data from the following entry:

Entry: {entry}

Return JSON with keys: date (YYYY-MM-DD), product, quantity (int), category (Bar, Restaurant, Retail), and customer.
"""
)
parse_chain = LLMChain(llm=llm, prompt=parse_prompt)

predict_prompt = PromptTemplate(
    input_variables=["temperature"],
    template="""
Given the current temperature of {temperature} degrees Fahrenheit, predict how many bottles of gin will likely be sold today. Return a number only.
"""
)
predict_chain = LLMChain(llm=llm, prompt=predict_prompt)

# DB init
conn = sqlite3.connect("/home/jmoses/Projects/sales.db", check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                date TEXT,
                product TEXT,
                quantity INTEGER,
                category TEXT,
                customer TEXT
            )''')
conn.commit()

# Save to DB
def save_sale(sale):
    c.execute("INSERT INTO sales (date, product, quantity, category, customer) VALUES (?, ?, ?, ?, ?)",
              (sale['date'], sale['product'], sale['quantity'], sale['category'], sale['customer']))
    conn.commit()

# Generate report PDF
def generate_pdf_report(month):
    c.execute("SELECT category, SUM(quantity) FROM sales WHERE strftime('%Y-%m', date) = ? GROUP BY category", (month,))
    results = c.fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"TTB Monthly Report for {month}", ln=True, align='C')
    pdf.ln(10)

    for category, total in results:
        pdf.cell(200, 10, txt=f"{category}: {total} units", ln=True)

    filename = f"/home/jmoses/Projects/ttb_report_{month}.pdf"
    pdf.output(filename)
    return filename

# Process uploaded JSONL file
def process_jsonl_file(file):
    for line in file:
        entry = line.decode("utf-8").strip()
        if entry:
            try:
                result = parse_chain.run(entry=entry)
                sale = json.loads(result.strip())
                save_sale(sale)
            except Exception as e:
                st.error(f"Error processing line: {entry}\n{e}")

# Streamlit UI
st.title("Liquor Sales Tracker GPT")

st.subheader("Add Single Entry")
entry = st.text_input("Sales Entry", placeholder="e.g. Sold 24 bottles of whiskey to Joe's Tavern on March 3.")
if st.button("Submit Entry") and entry:
    result = parse_chain.run(entry=entry)
    try:
        sale = json.loads(result.strip())
        save_sale(sale)
        st.success(f"Saved sale: {sale}")
    except Exception as e:
        st.error(f"Failed to parse GPT response: {result}")

st.divider()

st.subheader("Upload Bulk Sales Data (.jsonl)")
uploaded_file = st.file_uploader("Upload JSONL file with one entry per line.", type="jsonl")
if uploaded_file is not None:
    process_jsonl_file(uploaded_file)
    st.success("Finished processing uploaded sales data.")

st.divider()

st.subheader("Generate Monthly Report")
month = st.text_input("Month (YYYY-MM)", placeholder="2025-03")
if st.button("Generate PDF Report") and month:
    pdf_path = generate_pdf_report(month)
    with open(pdf_path, "rb") as f:
        st.download_button("Download PDF", data=f, file_name=pdf_path, mime="application/pdf")

st.divider()

st.subheader("Predict Today's Gin Sales")
temp = st.number_input("Enter current temperature (°F):", min_value=-50, max_value=150)
if st.button("Predict Gin Sales"):
    prediction = predict_chain.run(temperature=temp)
    st.info(f"Predicted gin sales today: {prediction.strip()} bottles")
