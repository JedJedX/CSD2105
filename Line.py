import matplotlib.pyplot as plt

def draw_horizontal_line_DDA(x1, y1, x2):
    dx = x2 - x1
    dy = 0  # เส้นตรงแนวนอนจะไม่มีการเปลี่ยนแปลงของ y

    length = abs(dx)
    x_increment = dx / length

    x = x1
    y = y1

    points = [(round(x), round(y))]

    for i in range(length):
        x += x_increment
        points.append((round(x), round(y)))

    return points

# จุดเริ่มต้นและจุดสิ้นสุดของเส้นตรงแนวนอน
x1, y1 = 2, 3
x2 = 10

line_points = draw_horizontal_line_DDA(x1, y1, x2)

# แสดงผลลัพธ์บนกราฟ
x_values, y_values = zip(*line_points)
plt.plot(x_values, y_values, marker='o')
plt.grid(True)
plt.show()