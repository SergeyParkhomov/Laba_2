print("Введите функцию из списка: сложение, вычитание, умножение, деление, возведение в степень, логарифм")
q = str(input())
fl = True
if q == "сложение":
    try:
        print("Введите первое слагаемое:")
        a = float(input())
        print("Введите второе слагаемое:")
        b = float(input())
        print("Результат:", round(a + b, 2))
        fl = False
    except:
        print("Введенный элемент не является числом")
        fl = False
elif q == "вычитание":
    try:
        print("Введите уменьшаемое:")
        a = float(input())
        print("Введите вычитаемое:")
        b = float(input())
        print("Разность:", round(a - b, 2))
        fl = False
    except:
        print("Введенный элемент не является числом")
        fl = False
elif q == "умножение":
    try:
        print("Введите первый множитель:")
        a = float(input())
        print("Введите второй множитель:")
        b = float(input())
        print("Результат:", round(a * b, 2))
        fl = False
    except:
        print("Введенный элемент не является числом")
        fl = False
elif q == "деление":
    try:
        print("Введите делимое:")
        a = float(input())
        print("Введите делитель:")
        b = float(input())
        print("Частное:", round(a / b, 2))
        fl = False
    except:
        print("Введенный элемент не является числом")
        fl = False
elif q == "возведение в степень":
    try:
        print("Введите основание степени:")
        a = float(input())
        print("Введите показатель степени:")
        b = float(input())
        print("Результат:", round(a ** b, 2))
        fl = False
    except:
        print("Введенный элемент не является числом")
        fl = False
elif q == "логарифм":
    import math
    try:
        print("Введите основание логарифма:")
        a = float(input())
        print("Введите аргумент:")
        b = float(input())
        print("Результат:", round(math.log(b, a), 2))
        fl = False
    except:
        print("Введенный элемент не является числом")
        fl = False
elif fl:
    print("Проверьте правильность введенного запроса и перезапустите программу")