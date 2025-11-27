import statistics
import sys

if len(sys.argv) < 2:
    print("Ошибка: укажите имя файла в аргументе командной строки")
    sys.exit(1)
filename = sys.argv[1]
with open(filename, "r") as f:
    numbers = [int(line.strip()) for line in f if line.strip()]
median = statistics.median(numbers)
key_number = min(numbers, key=lambda x: abs(x - median))

total = sum(abs(key_number - x) for x in numbers)

if total > 20:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
else:
    print(total)