

#Exercise 1
def max_kernel(num_list, k):
    result = []
    length = len(num_list)
    for i in range(length - k + 1):
        max = num_list[i]
        for j in range(i + 1, i + k):
            if max < num_list[j]:
                max = num_list[j]
        result.append(max)
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))


#Exercise 2
def character_count(word):
    character_statistic = {}
    for character in word:
        if character in character_statistic:
            character_statistic[character] += 1
        else:
            character_statistic[character] = 1
    return character_statistic


assert character_count('Baby') == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))


#Exercise 3
def count_word(file_path):
    counter = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1
    return counter


file_path = 'D:\\AIO EXERCISE\\AIO-Exercise\\week_2\\P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])


#Exercise 5
def check_the_number(N):
    list_of_numbers = []
    results = ''
    for i in range(1, 5):
        list_of_numbers.append(i)
    if N in list_of_numbers:
        results = 'True'
    if N not in list_of_numbers:
        results = 'False'
    return results


N = 7
assert check_the_number(N) == 'False'
N = 2
results = check_the_number(N)
print(results)


#Exercise 6
def my_function(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max = max, min = min, data = my_list ) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max = max, min = min, data = my_list))


#Exercise 7
def my_function(x, y):
    x.extend(y)
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]
assert my_function(list_num1, my_function(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]
list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print(my_function(list_num1, my_function(list_num2, list_num3)))


#Exercise 8
def my_function(n):
    min = n[0]
    for element in n:
        if min > element:
            min = element
    return min


my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100
my_list = [1, 2, 3, -1]
print(my_function(my_list)) 


#Exercise 9
def my_function(n):
    max = n[0]
    for element in n:
        if max < element:
            max = element
    return max


my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001
my_list = [1, 9, 9, 0]
print(my_function(my_list))


#Exercise 10
def My_function(intergers, number=1):
    result = []
    for i in intergers:
        if number == i:
            result.append(True)
        else:
            result.append(False)
    return any(result)


my_list = [1, 3, 9, 4]
assert My_function( my_list, -1) == False
my_list = [1, 2, 3, 4]
print(My_function(my_list, 2))


#Exercise 11
def my_function(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


assert my_function([4, 6, 8]) == 6
print(my_function())


#Exercise 12
def my_function(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]))


#Exercise 13
def my_function(y):
    var = 1
    while(y > 1):
        var *= y
        y -= 1
    return var


assert my_function(8) == 40320
print(my_function(4))


#Exercise 14
def my_function(x):
    return x[::-1]

x = 'I can do it'
assert my_function(x) == 'ti od nac I'
x = 'apricot'
print(my_function(x))


#Exercise 15
def function_helper(x):
    if x > 0:
        return 'T'
    else:
        return 'N'
    

def my_function(data):
    res = [function_helper(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']
data = [2, 3, 5, -1]
print(my_function(data))


#Exercise 16
def function_helper(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def my_function(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res


lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]
lst = [9, 9, 8, 1, 1]
print(my_function(lst))