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
    # first check whether the time is AM or PM and then strip the AM/PM substrings
    if s[-2:] == 'PM':
        s = s.replace('PM', '')
        # noon times just need the PM stripped
        # for all other times, the hour must be incremented by 12
        if s[:2] != '12':
            hour = int(s[:2])
            newHour = str(hour + 12)
            s = s.replace(s[:2], newHour)
    else:
        # same procedure but swapped 
        s = s.replace('AM', '')
        if s[:2] == '12':
            s = s.replace('AM', '')
            hour = int(s[:2])
            newHour = '00'
            s = s.replace(s[:2], newHour)
            
            
    return s
