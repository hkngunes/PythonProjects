import datetime
import re
import sys

def is_date_valid(year, month, day, hour, min, sec):
    result = None
    try:
        date = datetime.datetime(year=year,month=month,day=day,hour=hour, minute=min, second=sec)
        result = True
    except ValueError:
        result = False

    if result:
        if date > datetime.datetime.now():
            result = False
    return result

def is_line_valid(line):
    if re.search('.*@[0-9]{12}$', line):
        return True
    return False

def take_after_at(line):
    return line.split('@')[-1]

def convert_to_date(date_in_str):
    (year_str, month_str, day_str, hour_str, min_str, sec_str) = list(map(''.join, zip(*[iter(date_in_str)]*2)))
    (year, month, day, hour, min, sec) = list(map(lambda x: int(x), (year_str, month_str, day_str, hour_str, min_str, sec_str) ))
    return (year+2000, month, day, hour, min, sec)

def find_divergents():
    output_list = []
    for line in sys.stdin:
        if re.search('XXX', line):
            break
        if is_line_valid(line):
            date_in_str = take_after_at(line)
            (year, month, day, hour, min, sec) = convert_to_date(date_in_str)
            if is_date_valid(year, month, day, hour, min, sec):
                continue
        print(line)
        output_list.append(line)
    for line in output_list:
        print(line)

find_divergents()

