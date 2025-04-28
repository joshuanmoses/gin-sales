<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>Gin Sales Predictor 🍸📈</h1>
  <p><strong>Author:</strong> Joshua N. Moses</p>

  <h2>Overview</h2>
  <p>Gin Sales Predictor uses a pre-trained machine learning model to estimate the volume of gin a distillery would sell based on the temperature of the day. It's a fun demonstration of applying simple predictive analytics to a real-world scenario!</p>

  <h2>Project Structure</h2>
  <ul>
    <li><code>gin_sales_gpt.py</code> - Python script to interact with the prediction model.</li>
    <li><code>gin_sales_model.pkl</code> - Pre-trained sales prediction model file.</li>
    <li><code>requirements.txt</code> - List of Python dependencies required to run the project.</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/joshuanmoses/gin-sales.git</code></pre>
    </li>
    <li>Navigate into the project directory:
      <pre><code>cd gin-sales</code></pre>
    </li>
    <li>Install the dependencies:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
  </ol>

  <h2>Usage</h2>
  <p>To start the predictor, simply run:</p>
  <pre><code>python gin_sales_gpt.py</code></pre>
  <p>Follow the prompts to input a temperature value and receive a gin sales prediction.</p>

  <h2>Example</h2>
  <pre><code>
Enter the temperature in degrees Celsius: 27
🔮 Predicted Gin Sales: 512.35 liters
  </code></pre>

  <h2>Dependencies</h2>
  <ul>
    <li>joblib</li>
    <li>scikit-learn</li>
    <li>numpy</li>
  </ul>

</body>
</html>
