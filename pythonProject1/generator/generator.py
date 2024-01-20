def number(limit):
    i = 0
    while i < limit:
        yield i
        i += 1

gen = number(5)
for num in gen:
    print(num)
