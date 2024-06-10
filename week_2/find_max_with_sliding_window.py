

def max_kernel(list, k):
    result = []
    length = len(list)
    for i in range(length - k + 1):
        max = list[i]
        for j in range(i + 1, i + k):
            if max < list[j]:
                max = list[j]
        result.append(max)
    return result       


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
result = max_kernel(num_list, 3)
print(result)