class Time:
  def __init__(self, hours, minutes):
    self.hours = hours
    self.minutes = minutes

  def addTime(self, other):
    total_minutes = (self.hours * 60 + self.minutes) + (other.hours * 60 + other.minutes)
    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60
    return Time(new_hours, new_minutes)  # Return new Time object

  def displayTime(self):
    print(f"Time: {self.hours} hr {self.minutes} min")

  def displayMinute(self):
    total_minutes = self.hours * 60 + self.minutes
    print(f"Total Minutes: {total_minutes}")

time1 = Time(2, 50)
time2 = Time(1, 20)

result_time = time1.addTime(time2)

result_time.displayTime()
result_time.displayMinute()
