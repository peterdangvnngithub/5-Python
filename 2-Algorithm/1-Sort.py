# QuickSort
class Sort:
    def __init__(self):
        pass
    
    def QuickSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot   = arr[len(arr) // 2]
        left    = []
        middle  = []
        right   = []

        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
        return self.QuickSort(left) + middle + self.QuickSort(right)
    
    def max_subarray_sum(self, arr):
        max_sum = float('-inf')         # Khởi tạo max_sum với giá trị âm vô cực
        current_sum = 0
        left = 0

        for right in range(len(arr)):
            current_sum += arr[right]
            
            if current_sum > max_sum:
                max_sum = current_sum
            
            while current_sum < 0:
                current_sum -= arr[left]
                left += 1
        
        return max_sum

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sort_instance = Sort()
result = sort_instance.max_subarray_sum(arr)
print(result)
    
# arr = [3, 6, 8, 10, 1, 2, 1]

# sorted_arr = sort_instance.QuickSort(arr)
# print(sorted_arr)