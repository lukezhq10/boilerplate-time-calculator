def add_time(start, duration, day=None):
  # start is a time string in form "XX:XX XM"
  # duration is a time string in form "hh:mm" where min is <60 and hh is any whole number
  # assume start times are valid times
  start_hour, start_min = start.split(" ")[0].split(':')
  am_pm = start.split(' ')[1]
  start_hour = int(start_hour)
  start_min = int(start_min)
  duration_hour, duration_min = duration.split(':')
  duration_hour = int(duration_hour)
  duration_min = int(duration_min)

  # account for overflow if PM
  if am_pm == 'PM':
    start_hour += 12

  # first, get new_hour
  new_hour = start_hour + duration_hour

  # second, get new_min
  new_min = start_min + duration_min

  # if new_min > 60: should update new_hour with the overflow
  # then new_min should be the remainder
  if new_min > 60:
    new_hour += new_min // 60
    new_min = new_min % 60

  # we will convert new_hour to 24-hour format to get the AM/PM then convert to 12 hour format at the end
  # need to account for overflow
  if new_hour >= 24:
    new_hour = new_hour % 24

  # third, get new am_pm and convert back to 12-hour format
  new_am_pm = 'AM'
  if new_hour >= 12:
    new_am_pm = 'PM'
    if new_hour > 12:
      new_hour -= 12

  # convert 0:00 to 12:00 to pass tests
  if new_hour == 0:
    new_hour = 12

  # format the return message
  new_time = f"{new_hour}:{new_min:02d} {new_am_pm}"

  # keep track of days passed
  # also need to consider minutes overflow
  if (start_min + duration_min > 60):
    days_passed = (start_hour + duration_hour + 1) // 24
  else:
    days_passed = (start_hour + duration_hour) // 24

  # if day is provided, return the resulting day after days_passed
  if day is not None:
    days_of_week = [
      'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
      'Sunday'
    ]
    current_day_index = days_of_week.index(day.capitalize())
    resulting_day_index = (current_day_index + days_passed) % 7
    resulting_day = days_of_week[resulting_day_index]
  else:
    resulting_day = None

  if resulting_day is not None:
    new_time += f", {resulting_day}"

  # new_time formatting to include days_passed
  if days_passed == 1:
    new_time += " (next day)"
  elif days_passed > 1:
    new_time += f" ({days_passed} days later)"

  return new_time