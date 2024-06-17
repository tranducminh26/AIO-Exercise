


def word_count(file_path):
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


file_path = 'D:\AIO EXERCISE\AIO-Exercise\week_2\P1_data.txt'
result = word_count(file_path)
print(result)