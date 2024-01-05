def createContactNum(arr):
    return "".join(map(str, f"({''.join(map(str, arr[0:3]))}) {''.join(map(str, arr[3:6]))}-{''.join(map(str, arr[6:10]))}"))

print(createContactNum([1,2,3,4,5,6,7,8,9,0]))