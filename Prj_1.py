P = int(input("Enter your principal: "))
R = int(input("Enter your rate: "))
T = int(input("Enter your time: "))

A = P * (1 + (R / 100) * T)

print(A)
P = int(input("Enter your principal: "))
R = int(input("Enter your rate: "))
n = int(input("Enter your number: "))
t = int(input("Enter your time: "))

A = P * (1 + R / n) ** (n * t)

print(A)
PMT = int(input("Enter your dollar price: "))
R = int(input("Enter your rate: "))
n = int(input("Enter your number of periods: "))
t = int(input("Enter your time: "))

A = ((PMT) * (1 + R / n) ** (n * t) - 1) / (R / n)

print(A)
