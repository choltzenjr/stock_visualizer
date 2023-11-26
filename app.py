from flask import Flask, render_template, request, flash
import pandas
from stock import plot_stock_data

# Create a Flask application instance called 'app'
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'pass123'

# Function to retrieve the list of stock symbols from a CSV file
def get_symbol_list():
    symbol_list = []
    csvFile = pandas.read_csv('stocks.csv', usecols=['Symbol'])        
    symbol_list = csvFile['Symbol'].tolist()
    return symbol_list

# Define a Flask view function named 'index' using the app.route() decorator
@app.route('/', methods=('GET', 'POST'))
def index():
    symbol_list = get_symbol_list()
    chart_choices = ['line', 'bar']
    time_choices = ['TIME_SERIES_INTRADAY', 'TIME_SERIES_DAILY', 'TIME_SERIES_WEEKLY', 'TIME_SERIES_MONTHLY']
    success = False

    if request.method == "POST":
        # Get user-submitted data
        stock = request.form['stock']
        chart_type = request.form['chart'] 
        time_series = request.form['time']   
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        # Display error messages if required fields are not provided
        if not stock:
            flash('Stock is required')
        elif not chart_type:
            flash('Chart type is required')
        elif not time_series:
            flash('Time series is required')
        elif not start_date:
            flash('Start date is required')
        elif not end_date:
            flash('End date is required')
        else:
            # Call the plot_stock_data function and set success to True
            graph = plot_stock_data(stock, chart_type, time_series, start_date, end_date)
            success = True
            
    # Render the template with appropriate data based on the success flag
    if not success:
        return render_template('index.html', symbol_list=symbol_list, chart_choices=chart_choices, time_choices=time_choices)
    else:
        return render_template('index.html', symbol_list=symbol_list, chart_choices=chart_choices, time_choices=time_choices, graph=graph)

# Run the Flask application
app.run(host="0.0.0.0")
