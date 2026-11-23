n = 234
p = len(str(n))
s = sum(int(d) ** p for d in str(n))

if s == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")