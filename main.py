from random import randint
from sympy import randprime
import math

def generating_prime_numbers_and_test_Fermat(variables, data, bits=8):
    t = math.ceil(-(math.log(0.0001, 2)))  # Вычисляем t для теста Ферма
    list_test_t = []  # Создаем список для хранения случайных чисел для теста Ферма
    while True:
        # Генерируем случайное простое число
        prime_number = randprime(2**(bits-1), 2**bits-1)
        if t > prime_number:
            t = prime_number
        flag = True  # Флаг для проверки простоты числа
        # Проверяем делимость на числа от 2 до 9
        for num in range(2, 10):
            if prime_number % num == 0:
                flag = False
                break
        if flag:
            list_test_t.clear()  # Очищаем список для нового числа
            len_test_t = t
            while len_test_t > 0:
                # Генерируем случайное число для теста Ферма
                test_t = randint(2, prime_number - 1)
                if test_t not in list_test_t:
                   list_test_t.append(test_t)
                   len_test_t -= 1
            # Производим t итераций теста Ферма
            for test_t in list_test_t:
                if pow(test_t, prime_number - 1, prime_number) != 1:
                    flag = False
                    break
        if flag:
            # Если число прошло тест Ферма, добавляем его в словарь
            data[variables] = prime_number
            return data

def geretion(bits):
    data = {}
    p = generating_prime_numbers_and_test_Fermat("p", data, bits)
    mod = data["p"]
    while True:
        a = randprime(2 ** (bits - 3), 2 ** (bits-2) - 1)
        b = randprime(2 ** (bits - 3), 2 ** (bits-2) - 1)
        if (-4*a**3-27*b**2) % mod != 0:
            data["a"] = a
            data["b"] = b
            return data

def check_m():
    while True:
        # data = geretion(bits=8)
        data = {}
        data["a"] = 4
        data["b"] = 1
        data["p"] = 101
        p = data["p"]
        a = data["a"]
        b = data["b"]
        # print(data)
        data_x_and_y = set()
        F_m_squared_mod = {(y**2) % p: y for y in tuple(range(0, int(p/2)))}
        for x in tuple(range(int(-p/2), int(p/2)+1)):
            y = (x**3 + a * x + b) % p #
            # print(x)
            if y == 0:
                data_x_and_y.add((x, y))
                print((x, y))
            elif y in F_m_squared_mod:
                print((x, -F_m_squared_mod[y]))
                print((x, F_m_squared_mod[y]))
                data_x_and_y.add((x, -F_m_squared_mod[y]))
                data_x_and_y.add((x, F_m_squared_mod[y]))
            # else:
            #     print("-")
        # m = len(tuple(data_x_and_y))
        m = len(data_x_and_y)
        # print(p+1-2*(p**0.5), m, p+1+2*(p**0.5))
        if p+1-2*(p**0.5) <= m <= p+1+2*(p**0.5):
            data["m"] = m+1# хз какая-то бесконечно удаленная точка (0, бесконечиность )
            return data

def prime_number_q():
    data = check_m()
    t = math.ceil(-(math.log(0.0001, 2)))
    list_test_t = []
    for q in range(data["m"], 0, -1):
        if data["m"]/q == data["m"]//q and q > 3: # удалить and q > 3

            # print(q)
            if t > q:
                t = q
            flag = True  # Флаг для проверки простоты числа
            # Проверяем делимость на числа от 2 до 9

            de = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30] # испрвавить удалить
            for num in de: # испрвавить
                if q % num == 0:
                    flag = False
                    break

            # for num in range(2, 10):
            #     if q % num == 0:
            #         flag = False
            #         print(flag)
            #         break
            if flag:
                list_test_t.clear()  # Очищаем список для нового числа
                len_test_t = t-3 # испаривить удалить -3
                # print("v", len_test_t)
                # print(q)
                while len_test_t > 0:
                    # Генерируем случайное число для теста Ферма
                    test_t = randint(2, q - 1)
                    if test_t not in list_test_t:
                       list_test_t.append(test_t)
                       len_test_t -= 1
                    # print(len_test_t)
                # Производим t итераций теста Ферма
                for test_t in list_test_t:
                    if pow(test_t, q - 1, q) != 1:
                        flag = False
                        break
            # print(flag)
            if flag:
                # Если число прошло тест Ферма, добавляем его в словарь
                data["q"] = q
                return data

print(prime_number_q())