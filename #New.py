#New

# class convert:
#     def __init__(self, date, month, year):
#         self.date = date
#         self.month = month
#         self.year = year

#     def day(self, day):
#       day = int(day)
#       if 4 <= day <= 20 or 24 <= day <= 30:
#           suffix = "th"
#       else:
#           suffix = ["st", "nd", "rd"][day % 10 - 1]
#       return suffix

#     def convert_date(self):
#         if self.month == 1:
#             self.month = "January"
#         elif self.month == 2:
#             self.month = "February"
#         elif self.month == 3:
#             self.month = "March"
#         elif self.month == 4:
#             self.month = "April"
#         elif self.month == 5:
#             self.month = "May"
#         elif self.month == 6:
#             self.month = "June"
#         elif self.month == 7:
#             self.month = "July"
#         elif self.month == 8:
#             self.month = "August"
#         elif self.month == 9:
#             self.month = "September"
#         elif self.month == 10:
#             self.month = "October"
#         elif self.month == 11:
#             self.month = "November"
#         elif self.month == 12:
#             self.month = "December"
#         else:
#             print("Invalid month")

#         return self.month + " " + str(self.date) + self.day(self.date) + ", " + str(self.year)
      


# date = int(input("Enter the date: "))
# month = int(input("Enter the month: "))
# year = int(input("Enter the year: "))
# date_format = convert(date, month, year)
# print(date_format.convert_date())




class Convert:
  def __init__(date, day, month, year):
    date.date = day
    date.month = month
    date.year = year

  def day(date, day):
      day = int(day)
      if 4 <= day <= 20 or 24 <= day <= 30:
          suffix = "th"
      else:
          suffix = ["st", "nd", "rd"][day % 10 - 1]
      return suffix

  def convert_date(date):
      months = ["January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December"]

      if 1 <= date.month <= 12:
          month_str = months[date.month - 1]
      else:
          return "Invalid month"

      return f"{date.date}{date.day(date.date)} {month_str}, {date.year}"


date = int(input("Enter the date: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
date_format = Convert(date, month, year)
print(date_format.convert_date())