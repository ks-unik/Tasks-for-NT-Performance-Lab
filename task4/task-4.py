import statistics
import sys

if len(sys.argv) < 2:
    print("Ошибка: укажите имя файла в аргументе командной строки")
    sys.exit(1)
filename = sys.argv[1]
with open(filename, "r") as f:
    line = f.readline()
    numbers = [int(x) for x in line.replace(",", " ").split()]
median = statistics.median(numbers)
print(median) 
key_number = min(numbers, key=lambda x: abs(x - median))
print(key_number)
total = 0
sums_diff = []
for el in numbers:
    diff = abs(key_number-el)
    total += diff
    print(total)
print(total)
if total > 20:
    print("«20 ходов недостаточно для приведения всех элементов массива к одному числу»")
