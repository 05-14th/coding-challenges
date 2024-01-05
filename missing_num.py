import random as rand

n = int(input("Enter the maximum value: "))
num_storage = []
randomIndex = rand.randint(0, n - 1)

for i in range(1,n + 1,1):
    num_storage.append(i)

missingNum = num_storage[randomIndex]
num_storage.pop(randomIndex)

print(num_storage)
print(f"The missing number is {missingNum}")
