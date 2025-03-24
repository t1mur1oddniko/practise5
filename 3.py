num = int(input("Введите четырёхзначное число: "))


original = num
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
    
if original != reversed_num:
    print("Кривое")
else:
    print("Настоящее")