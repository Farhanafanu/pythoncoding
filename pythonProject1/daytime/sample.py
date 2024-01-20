import datetime
now=datetime.datetime.now()
print(datetime.datetime.now())
print(now.strftime("%d/%m/%Y"))
print(datetime.date.today().month)
x=datetime.datetime(2023,7,8)
y=datetime.datetime(2023,8,12)
dif=y-x
print(dif)
end=datetime.datetime.now()
dif=end-now

print(dif)
