import time

class Model:

    def __init__(self, array, S):
        self.S = S   
        self.array = array

    def train(self):
        self.execution_time = None
        self.key_cmp = 0
        if self.S == 1:
            print("Merge Sort")
            merge_func = self.merge_insertion_sort
        else:
            print("Merge Insertion Sort")
            merge_func = self.merge_sort
        start_time = time.perf_counter()
        merge_func(0, len(self.array)-1)
        end_time = time.perf_counter()
        self.execution_time = end_time - start_time

    def merge(self, n, m):
        mid = (n + m) // 2
        left = self.array[n:mid + 1]
        right = self.array[mid + 1:m + 1]

        i = j = 0

        temp = []

        while i < len(left) and j < len(right):
            self.key_cmp += 1
            if left[i] <= right[j]:  # Stable sort: left[i] goes first if equal
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1

        # Add any remaining elements
        while i < len(left):
            temp.append(left[i])
            i += 1

        while j < len(right):
            temp.append(right[j])
            j += 1

        # Copy merged values back into original array
        self.array[n:m+1] = temp


    def merge_insertion_sort(self, n, m):
        
        if (m-n <= 0):
            return
        
        if m-n+1 <= self.S:
            self.insertion_sort(n, m)
            return
        
        mid = (n+m)//2
        if (m-n>1):
            self.merge_insertion_sort(n, mid)
            self.merge_insertion_sort(mid+1, m)
        
        self.merge(n, m)

    def merge_sort(self, n, m):
        if (m-n <= 0):
            return
        
        mid = (n+m)//2
        if (m-n>1):
            self.merge_sort(n, mid)
            self.merge_sort(mid+1, m)
        
        self.merge(n, m)

    def insertion_sort(self, n, m):
        i = n+1
        while i <= m:
            j = i
            while j > n:
                self.key_cmp += 1
                if self.array[j] < self.array[j-1]:
                    tmp = self.array[j]
                    self.array[j] = self.array[j-1]
                    self.array[j-1] = tmp
                    j -= 1
                else:
                    break
            i+=1