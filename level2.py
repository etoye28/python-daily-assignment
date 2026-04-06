def fl(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

nums = list(map(int, input("Enter nums separated by space: ").split()))
result = fl(nums)

if result is not None:
    print(f"The largest number is: {result}")
else:
    print("The list is empty")
