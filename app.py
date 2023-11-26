from flask import Flask, render_template, request, url_for, flash, redirect, abort
import pandas
from stock import plot_stock_data


# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True
# app.config['SESSION_COOKIE_SAMESITE'] = "None"
# app.config['SESSION_COOKIE_SECURE'] = True
#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'pass123'

#flash the secret key to secure sessions
app.config['SECRET KEY'] = 'pass123'

#get stock symbol from csv file
def get_symbol_list():
    symbol_list = []
    count = 0
    csvFile = pandas.read_csv('stocks.csv', usecols=['Symbol'])        
    list = csvFile['Symbol']
    for index in range(len(list)):
        symbol_list.append(list[index])
    return symbol_list


# use the app.route() decorator to create a Flask view function called index()
@app.route('/', methods=('GET', 'POST'))
def index():
    symbol_list = get_symbol_list()
    chart_choice=['line', 'bar']
    time_choice=['TIME_SERIES_INTRADAY', 'TIME_SERIES_DAILY', 'TIME_SERIES_WEEKLY', 'TIME_SERIES_MONTHLY']
    success = False


    if request.method == "POST":
        #get title and content submitted by user
        stock = request.form['stock']
        chart_type = request.form['chart'] 
        time_series = request.form['time']   
        # start_date = datetime.strptime(
        #              request.form['start_date'],
        #              '%Y-%m-%d')
        # end_date = datetime.strptime(
        #              request.form['end_date'],
        #              '%Y-%m-%d')   
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')



        # display error if not submitted
        # otherwise make a database connection and insert the post
        if not stock:
            flash('stock is required')
        elif not chart_type:
            flash('chart type is required')
        elif not time_series:
            flash('time series is required')
        elif not start_date:
            flash('start date is required')
        elif not end_date:
            flash('end date is required')
        else:
            graph = plot_stock_data(stock, chart_type, time_series, start_date, end_date)
            success = True
            
    if not success:
        return render_template('index.html', symbol_list=symbol_list, chart_choice=chart_choice, time_choice=time_choice)
    else:
        return render_template('index.html', symbol_list=symbol_list, chart_choice=chart_choice, time_choice=time_choice, graph=graph)

app.run(host="0.0.0.0")