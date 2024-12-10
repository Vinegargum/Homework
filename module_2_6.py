#Дополнительное практическое задание по модулю 2
def find(k):
    key = ''
    if k <= 2 or k >= 21:
        return 'Введено некорректное число'
    else:
        for i in range(1, k+1):
            for j in range(i+1, k+1):
                if k % (i + j) == 0:
                    key += str(i) + str(j)
        return key
key = find(13)
print(key)
