
data_entry = input()
data_entry_list = data_entry.split()
n1, m1, n2, m2 = map(int, data_entry_list)

def get_path(n, m):
    path = [1]
    current = 1
    while True:
        for _ in range(m - 1):
            current += 1
            if current > n:
                current = 1
        if current == 1:
            break
        path.append(current)
    return path

path_1 = get_path(n1, m1)
path_2 = get_path(n2, m2)

print(*path_1, *path_2)