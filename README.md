<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>Gin Sales Predictor 🍸📈</h1>
  <p><strong>Author:</strong> Joshua N. Moses</p>

  <h2>Overview</h2>
  <p>Gin Sales Predictor uses a pre-trained machine learning model to estimate the volume of gin a distillery would sell based on the temperature of the day. It's a creative application of predictive analytics for sales forecasting based on weather patterns.</p>

  <h2>Project Structure</h2>
  <ul>
    <li><code>gin_sales_gpt.py</code> - Python script to interact with the prediction model.</li>
    <li><code>gin_sales_model.pkl</code> - Pre-trained machine learning model file.</li>
    <li><code>requirements.txt</code> - List of Python dependencies required to run the project.</li>
    <li><code>Dockerfile</code> - Instructions to containerize and run the application using Docker.</li>
  </ul>

  <h2>Installation</h2>
  <p>You can run the application either <strong>locally</strong> on your machine or <strong>inside a Docker container</strong>.</p>

  <h3>Local Installation</h3>
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
    <li>Run the application:
      <pre><code>python gin_sales_gpt.py</code></pre>
    </li>
  </ol>

  <h3>Using Docker</h3>
  <ol>
    <li>Build the Docker image:
      <pre><code>docker build -t gin-sales-app .</code></pre>
    </li>
    <li>Run the Docker container:
      <pre><code>docker run -it gin-sales-app</code></pre>
    </li>
    <li>Follow the prompts to input a temperature value and receive a sales prediction!</li>
  </ol>

  <h2>Usage Example</h2>
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
