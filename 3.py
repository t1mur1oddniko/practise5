num = input("Введите число: ")

if num == num[::-1]:
    print("Настоящее")
else:
    print("Кривое")