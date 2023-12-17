class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")
        month_map = [31, 28, 31, 30, 31, 30,\
                     31, 31, 30, 31, 30, 31]
        
        day_of_year = int(day) + sum(month_map[:int(month) - 1])
        year = int(year)
        if(int(month) > 2 and year % 4 == 0):
            if(year % 100 == 0):
                day_of_year += year % 400 == 0
            else:
                day_of_year += 1
        
        return day_of_year