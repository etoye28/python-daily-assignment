def ip(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if ip(num):
    print("a number is a prime number.")
else:
    print("a number is not a prime number.")
    