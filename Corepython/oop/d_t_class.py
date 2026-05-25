from datetime import datetime, date, timedelta

class DateTime:
    def __init__(self):
        pass

    def current_time(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        print('Current time:-',current_time)
        print('Current hour:-',now.hour)
        print('current minut:-',now.minute)
        print('Current second:-', now.second)

    def date(self):
        date = datetime(2002,12,23)
        print(date.day)
        print(date.month)
        print(date.year)
        print(date.strftime('%Y'))
        print(date.strftime('%a'))
        print(date.strftime('%b'))

    def time_enterval(self):
        current_date = date.today()
        print("Current date:-",current_date)

        tomorrow_date = current_date + timedelta(days=1)
        print("Tomorrow date:-", tomorrow_date)

        day_after_tomorrow = tomorrow_date +  timedelta(days=1)
        print("Day after tomorrow date:-", day_after_tomorrow)

        yesterday_date = current_date - timedelta(days=1)
        print("Yesterday date:-", yesterday_date)

    def calculate_age(self):
        birth_date = date(2002,12, 23)
        today = date.today()
        age = today.year - birth_date.year

        if(birth_date.month, birth_date.day < today.month, today.day):
            age -= 1
            print('age:', age)
        else:
            print('age')

c = DateTime()

count = 1
while(count):

    print()
    print('1.Print crrent time')
    print('2.Print birth date')
    print('3.Print current, tommrow, day after T, yesterday')
    print('4.Print calculate age')
    print('5.Exit')
    print()
    ch = int(input("Enter your input: "))

    if ch == 1:
        c.current_time()
    elif ch == 2:
        c.date()
    elif ch == 3:
        c.time_enterval()
    elif ch == 4:
        c.calculate_age()
    elif ch == 5:
        count = 0
    else:
        print('!!!!Warning!!!!')
        print('Invalid input')


