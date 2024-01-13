def point_line_orientation(point, line_start, line_end):
    orientation = (line_end[1] - line_start[1]) * (point[0] - line_end[0]) - (line_end[0] - line_start[0]) * (point[1] - line_end[1])
    if orientation == 0:
        return "Точка находится на прямой"
    elif orientation > 0:
        return "Точка находится справа от прямой"
    else:
        return "Точка находится слева от прямой"

point = (3, 4)
line_start = (1, 1)
line_end = (5, 1)
result = point_line_orientation(point, line_start, line_end)
print(result)