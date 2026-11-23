numbers = (1, 4, 7, 8, 10, 13, 16, 19, 22)
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]
print (evens)
print(odds)
print (sum(evens))
print (sum(odds))
