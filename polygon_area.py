# Polygon Area using Shoelace Formula

n = int(input("Enter number of sides of polygon: "))

points = []

for i in range(n):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    points.append((x, y))

area = 0

for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    area += (x1 * y2) - (x2 * y1)

area = abs(area) / 2

print("Area of Polygon =", area)
