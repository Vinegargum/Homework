#Задача "Счётчик вызовов"
calls = 0
def count_calls(): #подсчитывает вызовы отсальных функций
    global calls
    calls += 1
    return calls

def string_info(string): #делаем кортежик
    count_calls() #посчитали
    tuple = (len(string), string.lower(), string.upper())
    print(tuple)
    return tuple

def is_contains(string, list): #возвращает тру если строка в списке, фолс если нет
    count_calls() #посчитали
    list_2 = [x.lower() for x in list] #список в нижний регистр
    if string.lower() in list_2:
        print(True)
    else:
        print(False)
    return string, list

string_info('Good morning')
is_contains('good morning', ['good', 'good night', 'GOOD MORNINg'] )
string_info('Mother')
is_contains('mother', ['father', 'brother', 'sister'] )
print(calls)
