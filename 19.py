# project euler no. 19
#   find how many Sundays fell on the first of the month from 1 Jan 1901 to 31 Dec 2000?
#     answer = 171
days_in_month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def is_leap(year):
  if year % 400 == 0:
    return True
  return year % 4 == 0 and year % 100 != 0

def find_weekday(year,month,day):
  year_delt = year-1900
  days = day + 365*year_delt
  for i in range(1900,year,4):
    if is_leap(i):
      days += 1
  for i in range(1,month):
    days += days_in_month[i]
    if is_leap(year) and i == 2:
      days += 1
  return (days % 7)

def count_sundays(start_year,end_year):
  count = 0
  for year in range(start_year,end_year+1):
    for month in range(1,13):
      if find_weekday(year,month,1) == 0:
        count += 1
        print '*',
      print year, month
  return count

print count_sundays(1901,2000)