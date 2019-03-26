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
        print('Time string is invalid format.')
        return None

def is_time_in_legal_range(time):
    '''Check if time between 5:00PM and 4:00AM'''
    return (time <= datetime(year=1900, month=1, day=1, hour=4).time()
        or time >= datetime(year=1900, month=1, day=1, hour=17).time())

def is_start_time_before_end_time(start_time, end_time):
    '''Check if the start time is before the end time.'''
    # if start time is PM and end time is AM, return True
    if start_time.hour >= 12 and end_time.hour < 12:
        return True
    elif start_time.hour < 12 and end_time.hour >= 12:
        return False
    return end_time >= start_time

def calc_hours(start_time, end_time, cutoff_time):
    '''Calculate the hours before a cutoff time, given a start and end time.'''
    # if end PM and cutoff AM, use end as cutoff time
    if not is_time_in_legal_range(start_time) or not is_time_in_legal_range(end_time):
        print('Time not in valid range.')
        return None
    if not is_start_time_before_end_time(start_time, end_time):
        print('End time is before start time.')
        return None
    cutoff = cutoff_time.hour
    if cutoff >= 17 and start_time.hour < 17:
        return 0
    if cutoff < 17 and end_time.hour >= 17:
        cutoff = end_time.hour
    if cutoff < start_time.hour: # start PM and cutoff AM
        return 24 - start_time.hour + cutoff
    return cutoff - start_time.hour

def get_family_rates(family):
    '''Get the family rates array.'''
    if family.lower() == 'a':
        return family_a
    elif family.lower() == 'b':
        return family_b
    elif family.lower() == 'c':
        return family_c
    print('Family not found.')
    return None

def calc_pay(start_time_str, end_time_str, family):
    '''Master function for calculating a night's pay.'''
    start_time = convert_string_to_time(start_time_str)
    end_time = convert_string_to_time(end_time_str)
    if not start_time or not end_time:
        return None
    family_rates = get_family_rates(family)
    if not family_rates:
        return None
    hours = calc_hours(start_time, end_time, end_time)
    if hours is None:
        return None
    return hours * family_rates[0][1]
