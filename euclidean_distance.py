import math

# Öklid Mesafesini Hesaplayan Fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Noktalar Listesi
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafeler Listesi
distances = []

# Nokta çiftleri arasındaki mesafeleri hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafeyi Bulma
min_distance = min(distances)
print("Minimum Öklid Mesafesi:", min_distance)
