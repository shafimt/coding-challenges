

number = int(input("Enter a positive integer: "))
sum = 0
for i in range(number, 0, -1):  
    sum += i
print("Iterative Sum for", number, "=", sum)
