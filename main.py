from script import fetch_all_stock_data 
import matplotlib.pyplot as plt
from stock import plot_stock_data

# Function to get a valid stock symbol from the user
def get_symbol():
    stock_symbol = input("\nEnter the stock symbol for the company (or 'exit' to quit): ")
    return stock_symbol

# Function to fetch stock data for a given symbol
def get_symbol_data(stock_symbol):
    while True:
        if stock_symbol.lower() == 'exit':
            exit()

        # Fetch data from API
        data = fetch_all_stock_data(stock_symbol)

        # Check for errors in the data
        if data.get('Error Message') is not None or 'Time Series (Daily)' not in data:
            print("Please enter a valid symbol.")
        else:
            return data

# Function to get the time series function from the user
def get_time_series_function():
    print("\nEnter the time series function:")
    print("1. TIME_SERIES_INTRADAY")
    print("2. TIME_SERIES_DAILY")
    print("3. TIME_SERIES_WEEKLY")
    print("4. TIME_SERIES_MONTHLY")
    time_series = input("Enter the number: ")

    # Return the function name if the number is valid, otherwise return None
    return time_series

# Function to get the type of graph the user wants to see
def get_graph_type():
    while True:
        print("\nSelect graph type:")
        print("1. Line Graph")
        print("2. Bar Graph")
        
        graph_choice = input("Enter the number (or 'exit' to quit): ")
        if graph_choice.lower() == 'exit':
            exit()
            
        if graph_choice in ['1', '2']:
            return graph_choice
        else:
            print("Invalid selection. Please enter 1 for Line Graph or 2 for Bar Graph.")

# Function to visualize stock data
def visualize_stock_data(data, graph_type):
    time_series_data = data.get('Time Series (Daily)', {})
    dates = list(time_series_data.keys())[:10]
    closing_prices = [float(value['4. close']) for value in time_series_data.values()][:10]
    
    if graph_type == '1':
        plt.plot(dates, closing_prices)
    elif graph_type == '2':
        plt.bar(dates, closing_prices)
    else:
        print("Invalid graph type.")
        return
    
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title("Stock Data Visualization")
    plt.xticks(rotation=45)
    plt.show()

# Function to get start and end dates from the user
def get_dates():
    start_date = input("\nEnter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    return start_date, end_date

# Function to handle the stock data visualization process
def get_plot_stock_data(stock_symbol, graph_type, time_series):
    if graph_type == '1':
        graph_type = 'line'
    elif graph_type == '2':
        graph_type = 'bar'
    
    while True:
        start_date, end_date = get_dates()

        # Validate user input for date range
        if end_date > start_date:
            # Call the plot_stock_data function with user input as arguments
            plot_stock_data(stock_symbol, graph_type, time_series, start_date, end_date)
            break
        else:
            print("Invalid date range. Please try again.")

# Main function
def main():
    print("Stock Data Visualizer")
    print("------------------------")
    stock_symbol = get_symbol()
    stock_data = get_symbol_data(stock_symbol)

    if stock_data:
        graph_type = get_graph_type()
        visualize_stock_data(stock_data, graph_type)
        
    time_series = get_time_series_function()
    
    if time_series is not None:
        get_plot_stock_data(stock_symbol, graph_type, time_series)
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
