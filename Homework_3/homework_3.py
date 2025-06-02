# 1
sum = 0
for i in range(1, 101):
    sum += i
    print(f"Эх, опять прибавляю {i}")
print(f"Ладно, вот тебе сумма {sum}")

# 2
str = input("Введите любую строку: ")
for i in str:
    print(f"тык-тык... {i}")

# 3
num = int(input("Введите любое число: "))
res = 0
for i in range(1, 11):
    res = num * i
    print(f"{num} умножить на {i} равно {res}")
    if (num * i % 5 == 0):
        print("Фу, 5 опять...")

# 4
num_2 = int(input("Введите любое число: "))
sum_2 = 0

for i in range(1, num_2 + 1):
    if (i % 2 == 0):
        sum_2 += 1
        print(f"{i}")
print(f"Всего было найдено {sum_2} чётных чисел")

# 5

num_3 = int(input("Введите любое число: "))

for i in range(1, num_3 + 1):
    if (i % 3 == 0):
        continue
    print(i)

# 6
num_4 = int(input("Введите число: "))
sum = 0
while (num_4 != 0):
    sum += num_4
    num_4 = int(input("Введите число: "))
print(f"Сумма введенных Вами чисел равна: {sum}")

# 7
num_5 = int(input("Введите число: "))
if (num_5 % 2 == 0):
    print("О, ты выбрал чётное число!")
else:
    print("Ха! Нечётное! А ты весёлый.")

# 8
str_2 = input("Введите любую строку: ")
sum_3 = 0
for i in str_2:
    if (i == "а"):
        sum_3 += 1
print(f"{sum_3} букв 'а' в строке")

# 9
num_6 = int(input("Введите число: "))
if (num_6 % 7 == 0):
    print("Семёрка... ты наш человек!")
else:
    print("Хм, подозрительно...")

# 10 Задача про палиндром
str_3 = input("Введите строку: ").upper().strip()
print(str_3)
if str_3[::-1] == str_3:
    print("Это палиндром!")
else:
    print("Это не является палиндромом!")
