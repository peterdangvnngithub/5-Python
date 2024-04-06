import time
class Sort:
    def QuickSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) - 1]
        left = []
        middle = []
        right = []

        for x in arr:
            if x == pivot:
                middle.append(x)
            elif x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
        
        return self.QuickSort(left) + middle + self.QuickSort(right)

arr = [2, 5, 0, 3, 7, -1 , 0]
sort = Sort()
+
start_time = time.time()

print(sort.QuickSort(arr))

end_time = time.time()
print("Speed:" + str(end_time - start_time))