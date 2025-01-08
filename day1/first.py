a = int(input("enter a number: "))
sum = 0
num_digits = len(str(a))
temp = a

while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

if sum == a:
    print(f"{a} yes of course")
else:
    print(f"{a} no shit")
