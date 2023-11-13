from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Get current time and date
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Stock market timings (for example, NYSE)
    market_open = "09:30"
    market_close = "16:00"

    # Placeholder for live stock prices (replace with API call)
    stock_prices = {
        'PLTR': "Get PLTR price from API",
        'MSFT': "Get MSFT price from API"
    }

    # Render the web page with the above information
    return render_template('index.html', current_time=current_time, 
                           current_date=current_date, market_open=market_open, 
                           market_close=market_close, stock_prices=stock_prices)

app.run(host='0.0.0.0', port=5000)

