from main import *
import datetime




# symbol: capitalized, 1-7 alpha characters
def symbol_test():
    #1 can use this to test 
    # name = "GOOGL"
    
    #2 
    name = get_symbol()
            
    result = "symbol test = ok"
    #a.) another check
    if name != name.upper():
        result = "need to be capitalized"
    if len(name) < 1 or len(name) > 7:
        result = "need to be 1-7 alphabets"
    if not name.isalpha():
        result = "needs to be all alphabets"
    return result
    



# time series: 1 numeric character, 1 - 4
def time_series_test():
     #choose option below
    # 1 test
    #user = '1'

    # 2 test
    user = get_time_series_function()
    
    choice = ['1','2','3','4']


    if user in choice:
        result = "time_series test = ok"
    else:
        result = "time_series test = fail"
    return result

    

# start date: date type YYYY-MM-DD
# end date: date type YYYY-MM-DD
def start_end_dates_test():
    start_date, end_date = get_dates()
    result = "date test = ok"
    try:
        datetime.date.fromisoformat(start_date)
        datetime.date.fromisoformat(end_date)
    except ValueError:
        result = "date test = fail, enter date in YYYY-MM-DD format"

    return result
    



print(start_end_dates_test())