# codding : utf-8
# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

print('Введите длины сторон треугольника: side_tri1, side_tri2, side_tri3')
side_tri1 = int(input("side_tri1 = "))
side_tri2 = int(input("side_tri2 = "))
side_tri3 = int(input("side_tri3 = "))

if side_tri1 + side_tri2 <= side_tri3 or side_tri1 + side_tri3 <= side_tri2 or side_tri2 + side_tri3 <= side_tri1:
    print("Треугольник не существует")
elif side_tri1 != side_tri2 and side_tri1 != side_tri3 and side_tri2 != side_tri3:
    print("Разносторонний")
elif side_tri1 == side_tri2 == side_tri3:
    print("Равносторонний")
else:
    print("Равнобедренный")