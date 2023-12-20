import sys
def main(n, m):
    if m < 1:
        return 'Error'
    if n < 1:
        return 'Error'
    circular_array = list(range(1, n + 1))
    path = []

    current_index = 0
    for _ in range(n):
        path.append(circular_array[current_index])
        current_index += m - 1
        if current_index == 0:
            return path
        elif current_index > n - 1:
            current_index -= n
            if current_index == 0:
                return path

    return path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        result = main(n, m)
        print("".join(map(str, result)))