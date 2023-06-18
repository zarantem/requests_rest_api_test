import requests

date = input()
m = (str(date)[0])
c = (str(date)[1])
d = (str(date)[2])
y = (str(date)[3])
year = str(m+c+d+y)
m1 = (str(date)[5])
m2 = (str(date)[6])
month = str(m1+m2)
d1 = (str(date)[8])
d2 = (str(date)[9])
day = str(d1+d2)
link = f"https://isdayoff.ru/api/getdata?year={year}&month={month}&day={day}[&cc=xx&pre=[0|1]&covid=[0|1]]&sd=[0|1]"
response = requests.get(link).text
if response == '0':
    print('этот день рабочий')
elif response == '1':
    print('этот день не рабочий')
elif response == '2':
    print('этот день сокращенный рабочий')
elif response == '4':
    print('этот день рабочий')
elif response == '100':
    print('оишбка в дате')
elif response == '101':
    print('данных для этого дня нет')
else:
    print('ошибка сервиса')

