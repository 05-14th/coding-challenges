def findMissingNum(arr):
    n = len(arr) + 1
    total_sum = (n * (n+1)) // 2
    current_sum = sum(arr)
    missing_num = total_sum - current_sum
    return missing_num

my_array = [1,5,6,7,8,2,3]
missing_num = findMissingNum(my_array)
print(my_array)
print(f"The missing number is {missing_num}")