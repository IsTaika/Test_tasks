import sys
import math


def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        x, y = map(float, lines[0].split())
        radius = float(lines[1])
    return x, y, radius


def read_points(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [tuple(map(float, line.split())) for line in lines]
    return points


def point_position(x_center, y_center, radius, x_point, y_point):
    distance = math.sqrt((x_point - x_center) ** 2 + (y_point - y_center) ** 2)
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error")
    else:
        circle_data_file = sys.argv[1]
        points_file = sys.argv[2]

        x_center, y_center, radius = read_circle_data(circle_data_file)
        points = read_points(points_file)

        for point in points:
            result = point_position(x_center, y_center, radius, *point)
            print(result)
