import datetime

def from_string_to_datetime (date_string:str,date_string_format:str="%d-%m-%Y")-> datetime.datetime:
    return datetime.datetime.strptime(date_string,date_string_format)

def from_string_to_date (date_string:str,date_string_format:str="%d-%m-%Y")-> datetime.date:
    return from_string_to_datetime(date_string,date_string_format).date()