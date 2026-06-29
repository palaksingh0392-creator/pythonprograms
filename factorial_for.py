# take input
num = int(input("Enter the value: "))
#logic
fact = 1
for i in range(1, num + 1):
    print(i)
    fact = fact * i
# print multiply
print("The factorial of numbers is:", fact)
