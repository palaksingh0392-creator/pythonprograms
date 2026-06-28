# take input
num = int(input("Enter the value: "))

# logic
sum = 0
mul = 1
for i in range(1, num + 1):
    print(i)
    sum = sum + i
    mul = mul * i
# print sum
print("The sum of numbers is:", sum)
# print multiply
print("The multiply of numbers is:", mul)
