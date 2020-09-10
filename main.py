# Задание 1
print("ЗАДАНИЕ 1")

var1 = "ABC"
var2 = 3
var3 = var1 + str(var2)

print(var1)
print(var2)
print(var3)

userVar1 = input("Введите строку: ")
userVar2 = input("Введите вторую строку: ")

userVar3 = int(input("Введите число: "))
userVar4 = int(input("Введите второе число: "))

print("Вы ввели:")
print(userVar1)
print(userVar2)
print(userVar3)
print(userVar4)

# Задание 2
print("ЗАДАНИЕ 2")

timeInSecs: int = int(input("Введите время в секундах: "))

minutes: int = (timeInSecs - timeInSecs % 60) / 60

hours: int = (minutes - minutes % 60) / 60

print("{0:02.0f}:{1:02.0f}:{2:02.0f}".format(hours, minutes % 60, timeInSecs % 60))

# Задание 3
print("ЗАДАНИЕ 3")

userNum: int = int(input("Введите число: "))

foundNum = int(userNum) + int(str(userNum)+str(userNum)) + int(str(userNum)+str(userNum)+str(userNum))

print(foundNum)

# Задание 4
print("ЗАДАНИЕ 4")


# прошу число
userNum: int = -1
while userNum < 0:
    userNum: int = int(input("Введите неотрицательное целое число: "))

maxDigit: int = 0
while userNum > 0:
    restFromDivBy10: int = int(userNum % 10)
    if restFromDivBy10 > maxDigit:
        maxDigit: int = restFromDivBy10
        if maxDigit == 9:
            break
    userNum: int = int((userNum - restFromDivBy10) / 10)

print("Максимальный разряд в числе: {:d}".format(maxDigit))


# Задание 5
print("ЗАДАНИЕ 5")

income: float = float(input("Введите значениие выручки: "))
expenses: float = float(input("Введите значение расходов: "))
balance: float = income - expenses

if balance > 0:
    print("У Вас прибыль: {:.2f}.".format(balance))
    print("Ваша рентабельность: {:.2f}.".format(balance/income))
    numEmpl: float = float(input("Введите среднесписочную численность предприятия: "))
    print("Ваша прибыль на сотрудника: {:.2f}.".format(balance / numEmpl))
elif balance < 0:
    print("У Вас убыток: {:.2f}.".format(balance))
else:
    print("Вы отработали в \"ноль\".")

# Задание 6
print("ЗАДАНИЕ 6")

pathLength: float = float(input("Введите расстояние за первый день: "))
pathThreshold: float = float(input("Введите общий пороговый результат: "))

numOfDays: int = 0

fullPath: float = 0
while pathThreshold > 0:
    dailyPath = numOfDays * (1.1 ** numOfDays)
    pathThreshold = pathThreshold - dailyPath
    numOfDays += 1
    print("{0:d}-ый день: {1:.2f}".format(numOfDays, dailyPath))
    fullPath = fullPath + dailyPath

print("Номер дня: {:d}".format(numOfDays))
print("Спортсмен пробежал не менее: {:.2f}".format(fullPath))
