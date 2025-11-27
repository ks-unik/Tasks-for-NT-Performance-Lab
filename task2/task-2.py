import sys
import re

if len(sys.argv) < 3:
    print("Необходимо указать имя 2-х файлов в аргументе командной строки")
    sys.exit(1)

filename_1 = sys.argv[1]
with open(filename_1, "r") as ellipse_file:
    ellipse_list = [line.rstrip("\n") for line in ellipse_file.readlines()]

x_center, y_center = map(float, ellipse_list[0].split())
radius_a, radius_b = map(float, ellipse_list[1].split())

filename_2 = sys.argv[2]
with open(filename_2, "r") as coordinates_file:
    coordinates_list = [float(x) for x in re.split(r'\s+', coordinates_file.read()) if x]

if len(coordinates_list) % 2 != 0:
    raise ValueError("Неверное количество координат: должно быть чётное число значений")

for k in range(0, len(coordinates_list), 2):
    px, py = coordinates_list[k], coordinates_list[k+1]
    point_value = ((px - x_center)**2) / radius_a**2 + ((py - y_center)**2) / radius_b**2 - 1

    if point_value < 1e-9:
        print(0) 
    elif point_value < 0:
        print(1) 
    else:
        print(2) 
