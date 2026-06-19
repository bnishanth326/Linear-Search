arr=[7,18,3,10,8]
key=int(input("enter the element to search"))
for i in range(len(arr)):
    if arr[i]==key:
        print("element found at index:",i)
        break
else:
    print("element not found")