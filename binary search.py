def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]
    value = 7
    index = binary_search(numbers, value)
    if index != -1:
        print(f"Found {value} at index {index}.")
    else:
        print(f"{value} was not found in the list.")
