from datetime import datetime

def convert_string_to_time(time_str):
    return datetime.strptime(time_str, '%I:%M%p').time()
