num1 = 56
num2 = 98

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd_result = gcd(num1, num2)

print(f"{gcd_result}")
