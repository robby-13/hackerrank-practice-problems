'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Example:

-   s = '12:01:00PM'
      Return '12:01:00'
-   s = '12:01:00AM'
      Return '00:01:00'

'''

def timeConversion(s):
    # Write your code here
    # first check whether the time is AM or PM
    if s[-2:] == 'PM':
        # check if it is a noon time
        if s[:2] == '12':
            s = s.replace('PM', '')
        # for all other times, two things need to be done
        # 1.) strip the PM
        # 2.) increment the time by 12
        else:
            s = s.replace('PM', '')
            hour = int(s[:2])
            newHour = str(hour + 12)
            s = s.replace(s[:2], newHour)
    else:
        # check if midnight time:
        if s[:2] == '12':
            s = s.replace('AM', '')
            hour = int(s[:2])
            newHour = '00'
            s = s.replace(s[:2], newHour)
        # else, just need to strip the AM 
        else:
            s = s.replace('AM', '')
            
            
    return s
