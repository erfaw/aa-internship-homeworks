def bubble_sort(iter):
    for i in range(len(iter)-1):
        for j in range(len(iter)-1-i):
            if iter[j] > iter[j+1]:
                temp = iter[j]
                iter[j] = iter[j+1]
                iter[j+1] = temp
        
    return iter

sample_list = [35, 73, 10, 11, 2]
sample_list = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(sample_list))
