from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_info = ''
    if request.method == 'POST':
        api_key = request.form['api_key']
        ticker_symbol = request.form['ticker_symbol']
        # Here you'd add the logic to fetch stock data using the provided API key and ticker symbol.
        # For example, using requests.get() to call an API endpoint.
        # stock_info = requests.get(f"API_ENDPOINT?symbol={ticker_symbol}&apikey={api_key}")
        # For demonstration, we'll just simulate a response.
        stock_info = f"Stock data for {ticker_symbol} with API key {api_key}"

    return render_template('index.html', stock_info=stock_info)

app.run(host='0.0.0.0', port=5000)

