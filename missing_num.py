import random as rand
import numpy as np

n = int(input("Enter the maximum value: "))
num_storage = []
randomIndex = rand.randint(0, n - 1)

for i in range(1,n + 1,1):
    num_storage.append(i)

missingNum = num_storage[randomIndex]
num_storage.pop(randomIndex)
shuffledNum = np.array(num_storage)
np.random.shuffle(shuffledNum)

print(shuffledNum)
print(f"The missing number is {missingNum}")
