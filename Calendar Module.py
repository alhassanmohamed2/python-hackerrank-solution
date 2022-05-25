import calendar
def deterime_day(datee):
    day = calendar.weekday(int(datee[6:10]), int(datee[slice(0, 2)]), int(datee[slice(3, 5)]))
    #day = calendar.weekday(2000,5,12)
    #day = [datee[6:10], datee[slice(0, 2)], datee[slice(3, 5)]]
    weeks = {0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}
    
    return weeks[day]
    
    
    return day


if __name__ == '__main__':
    day = input()

    dd = deterime_day(day)
    print(dd)