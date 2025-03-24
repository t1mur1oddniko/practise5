import turtle as t
import math

xc = int(input("Введите x-координату центра окружности: "))
yc = int(input("Введите y-координату центра окружности: "))
r = int(input("Введите радиус окружности: "))
x = int(input("Введите x-координату точки: "))
y = int(input("Введите y-координату точки: "))

distance = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)

if distance < r:
    print("Точка внутри окружности")
elif distance == r:
    print("Точка на окружности")
else:
    print("Точка вне окружности")

t.up()
t.setposition(xc, yc - r)
t.down()
t.circle(r)
t.up()
t.setposition(x, y)
t.down()
t.dot(10, color="red")
t.hideturtle()
print("\n")