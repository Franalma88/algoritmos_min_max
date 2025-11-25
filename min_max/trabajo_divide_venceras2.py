A = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2), (12, 5), (14, 3), (3, 10), (6, 8), (11, 11), (13, 9), (15, 6), (18, 2), (17, 7), (19, 4), (21, 3), (20, 8), (23, 5), (25, 7), (24, 1), (26, 4), (30, 2), (28, 9), (31, 7), (34, 6), (33, 3), (36, 8), (38, 5)]
def distance_between_everypoint(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            mid = ((a[i][0] + a[j][0]) / 2, (a[i][1] + a[j][1]) / 2)
            dist = ((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2) ** 0.5
            print(f"Puntos: {a[i]} y {a[j]}, Punto medio: {mid}, Distancia: {dist}")
distance_between_everypoint(A)