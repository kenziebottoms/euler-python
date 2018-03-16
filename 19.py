# project euler no. 19
#   find how many Sundays fell on the first of the month from 1 Jan 1901 to 31 Dec 2000?
#     answer = 171

def find_weekday(year,month,day):
  month -= 1
  days_in_month = {0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}
  current_month = 0
  current_weekday = 1 + day
  for i_year in range(1901,year):
    if i_year % 4 == 0:
      current_weekday += 366
    else:
      current_weekday += 365
  for i_month in range(month):
    current_weekday += days_in_month[i_month]
    if year % 4 == 0 and i_month == 1:
        current_weekday += 1
  return (current_weekday % 7)

def count_sundays(lower_bound,upper_bound,day_of_week):
  count = 0
  for year in range(lower_bound,upper_bound):
    for month in range(12):
      if find_weekday(year,month,1) == 0:
        count += 1
        print month,year
  return count

print count_sundays(1901,2001,0)
