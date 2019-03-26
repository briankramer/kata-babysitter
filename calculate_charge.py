from datetime import datetime

family_a = [
    ('5:00PM', 15),
    ('11:00PM', 20)
]

family_b = [
    ('5:00PM', 12),
    ('10:00PM', 8),
    ('12:00AM', 16),
]

family_c = [
    ('5:00PM', 21),
    ('9:00PM', 15),
]

def convert_string_to_time(time_str):
    '''Convert string to time so that we can keep format laid out in GitHub: 5:00PM'''
    try:
        return datetime.strptime(time_str, '%I:%M%p').time()
    except ValueError:
        return None

def is_time_in_legal_range(time):
    return (time <= datetime(year=1900, month=1, day=1, hour=4).time()
        or time >= datetime(year=1900, month=1, day=1, hour=17).time())

def is_start_time_before_end_time(start_time, end_time):
    # if start time is PM and end time is AM, return True
    if start_time.hour >= 12 and end_time.hour < 12:
        return True
    return end_time >= start_time

def calc_hours(start_time, end_time, cutoff_time):
    # this fn assumes is_time_in_legal_range has already been run
    # if end PM and cutoff AM, use end as cutoff time
    cutoff = cutoff_time.hour
    if cutoff < 17 and end_time.hour >= 17:
        cutoff = end_time.hour
    if cutoff < start_time.hour: # start PM and cutoff AM
        return 24 - start_time.hour + cutoff
    return cutoff - start_time.hour
