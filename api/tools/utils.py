from datetime import datetime

def string_to_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d')

def date_to_string(date):
    return date.strftime('%Y-%m-%d')
