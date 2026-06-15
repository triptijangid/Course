def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return False
nums = list(map(int, input("Enter integers separated by space: ").split()))
unique_nums = set(nums)
sorted_nums = sorted(list(unique_nums))
print("Sorted unique elements:", sorted_nums)
target = int(input("Enter element to search: "))
found = binary_search(sorted_nums, target)
if found:
    print("Element found!")
else:
    print("Element not found!")