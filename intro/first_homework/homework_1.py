# 1 Машина времени
current = int(input("Введите текущий год: "))
transfer = int(input("На сколько лет вы хотите переместиться? "))
result = str(current + transfer)

print("Вы оказались в " + result + " году")

# 2 Магическое число

YourNumber = int(input("Введите любое число: "))
result_2 = int((YourNumber + 7) * 3 / 2)

print(result_2)

# 3 Калькулятор возраста

YearOfBirth = int(input("Введите свой год рождения: "))
Year = 2025
print("Вам " + str(Year - YearOfBirth) + " лет")

# 4 Приветствие по имени
name = str(input("Введите своё имя: "))
surname = str(input("Введите свою фамилию: "))

print("Привет, " + name + " " + surname)

# 5 Кот в килограммах
weight = float(input("Введите вес кота: "))
print("Ваш кот весит: " + str(weight) + " кг - это очень мило!")

# 6 День рождения
day = str(input("Введите день твоего рождения: "))
month = str(input("Введите месяц твоего рождения: "))

print("Ты родился " + " " + day + " " + month)

# 7 Секретное число

YourNumber_2 = int(input("Введите число: "))
print(YourNumber_2 + 42, YourNumber_2 - 42)

# 8 Перевёрнутая математика
YourNumber_3 = int(input("Введите первое число: "))
YourNumber_4 = int(input("Введите второе число: "))

print(YourNumber_3 + YourNumber_4, str(YourNumber_3) + str(YourNumber_4))

# 9 100 рублей на всех
amount = int(input("Введите количество пришедших друзей: "))
result_3 = round(100 / amount, 2)

print("Каждый получит по " + str(result_3) + " рубля")

# 10 Удвоитель слов
word = str(input("Введите любое слово: "))
print((word + " ")*2)
