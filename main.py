n = input("Введите восьмеричное число (8 разрядов): ")

s = 0
for digit in n:
    s += int(digit)

print("Сумма цифр числа:", s)
