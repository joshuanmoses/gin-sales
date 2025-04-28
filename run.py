import subprocess
url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_0.gguf"
output_file = "llama-2-7b-chat.Q4_0.gguf"
#virtual environment
python3 -m venv /home/jmoses/Models/llama-env
source /home/jmoses/Models/llama-env/bin/activate
#download model and wait until it has finished
subprocess.run(["wget", "-O", output_file, url], check=True)
#move model to project dir
mv ~/Downloads/output_file /home/jmoses/Projects/gin-sales2
cd /home/jmoses/Projects/gin-sales2
streamlit run app.py

