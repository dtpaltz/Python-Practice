



def timeConversion(s):
    parts = s.split(':')
    ampm = (parts[-1])[-2:]
    parts[-1] = (parts[-1])[:-2]

    hour = int(parts[0])
    if ampm.lower() == 'pm' and hour < 12:
        parts[0] = hour + 12
    elif ampm.lower() == 'am' and hour == 12:
        parts[0] = '00'

    result = ':'.join(map(str, parts)).strip(' ')
    print(result)


timeConversion('07:05:45PM')
timeConversion('12:00:00PM')
timeConversion('12:00:00AM')
timeConversion('12:05:45AM')
