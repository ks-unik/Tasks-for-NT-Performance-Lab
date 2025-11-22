
data_entry = input()
data_entry_list = data_entry.split()
n1, m1, n2, m2 = map(int, data_entry_list)

array_1 = list(range(1, n1 + 1))
array_2 = list(range(1, n2 + 1))
path_1 = [1]
path_2 = [1]

interval_1 = m1 - 1
interval_2 = m2 - 1

while True:
    last_number_1 = path_1[-1]
    next_number_1 = (last_number_1 + interval_1 - 1) % n1 + 1
    if next_number_1 == 1:
        break
    path_1.append(next_number_1)
print(path_1)
while True:
    last_number_2 = path_2[-1]
    next_number_2 = (last_number_2 + interval_2 - 1) % n2 + 1
    if next_number_2 == 1:
        break
    path_2.append(next_number_2)
print(path_2)