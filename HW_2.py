# Ввести одномерный массив A длиной m. Поменять в нём местами первый и последний элементы. Длину массива и его элементы ввести с клавиатуры. В программе описать процедуру для замены элементов массива. Вывести исходные и полученные массивы.

a = input().split()  # Ввод элементов через пробел с последующим их разделением в список.

b = []
b.append(a[-1])  # В новый массив сначала добавляем последний элемент исходного
b.extend(a[1:-1])  # ...затем промежуточные элементы исходного списка
b.append(a[0])  # ...и наконец добавляем самый первый элемент исходного массива.

print(a)
print(b)
