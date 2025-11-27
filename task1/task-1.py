
import argparse
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

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("c", type=int)
    parser.add_argument("d", type=int)

    args = parser.parse_args()

    n1, m1, n2, m2 = args.a, args.b, args.c, args.d
    numbers = [n1, m1, n2, m2]
    if any(x < 1 for x in numbers):
        raise ValueError("Введенные числа должны быть >= 1")

    path_1 = get_path(n1, m1)
    path_2 = get_path(n2, m2)

    print(*path_1, *path_2)


if __name__ == "__main__":
    main()
