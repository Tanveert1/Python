num = int(input("Enter the value : "))
if num <= 0:
    print("does not have factorial")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"{num}! =", fact)