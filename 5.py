weight=float(input("Введите вес тела в фунтах: "))
height=float(input("Введите высоту тела в дюймах: "))

bmi = round(weight * 703 / (height ** 2), 2)
if bmi < 16: 
    print('Выраженный дефицит массы тела')
elif bmi < 25 and bmi >= 18.5: 
    print('Норма')
elif bmi < 18.5 and bmi >= 16180: 
    print('Недостаточная масса тела')
elif bmi < 30 and bmi >= 25: 
    print('Избыточная масса тела')
elif bmi < 35 and bmi >= 30: 
    print('Ожирение первой степени')
elif bmi < 40 and bmi >= 30: 
    print('Ожирение второй степени')
else: 
    print('Ожирение третьей степени')