
def proc1():
    pas = input('Введите пароль')

    is_numeric = False
    is_lower = False
    is_upper = False
    is_spec = False

    for f in pas:
        if f.isnumeric():
            is_numeric = True
        if f.islower():
            is_lower = True
        if f.isupper():
            is_isupper = True

    if len(pas) > 6 and is_numeric and is_lower and is_isupper:
        print("Надежный пароль")
    else:
        print('Пароль ненадежный')

def proc2():
    a = int(input('Введите место в вагоне'))

    if a in range(0, 36) and a % 2 == 0:
        print('Ваше место верхнее в купе')
    elif a % 2 != 0:
        print('Ваше место нижнее в купе')

    elif a in range(36, 55) and a % 2 == 0:
        print('Ваше место боковое верхнее')
    else:
        print('Ваше место боковое нижнее')

def proc3():
    n = int(input('Введите год'))

    if n % 4 == 0 and n % 100 != 0:
        print('Год ', n, ' - високосный')
    else:
        print('Этот год не високосный')

def proc4():
    a = input('Введите первый основной цвет ')
    b = input('Введите второй основной цвет ')
    c = ""

    if a == 'Красный' and b == 'Синий' or b == 'Красный' and a == 'Синий':
        c = 'Фиолетовый'
    elif a == 'Красный' and b == 'Желтый' or b == 'Красный' and a == 'Желтый':
        c = 'Оранжевый'
    elif a == 'Синий' and b == 'Желтый' or b == 'Синий' and a == 'Желтый':
        c = 'Зеленый'
    else:
        print('Этот цвет не основной')

    print(c)

def proc5():
    N = 5
    chars = []

    for i in range(N):
        chars.append(input())

    line = ' '.join(chars)

    print(line)

proc1(), proc2(), proc3(), proc4(), proc5()
