

puntos = [
    (2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2), (12, 5), (14, 3),
    (3, 10), (6, 8), (11, 11), (13, 9), (15, 6), (18, 2), (17, 7),
    (19, 4), (21, 3), (20, 8), (23, 5), (25, 7), (24, 1), (26, 4),
    (30, 2), (28, 9), (31, 7), (34, 6), (33, 3), (36, 8), (38, 5)
]


def distancia(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

for i in range(len(puntos)):
    for j in range(len(puntos)):
        if i != j:  
            d = distancia(puntos[i], puntos[j])
            print(f"Distancia entre {puntos[i]} y {puntos[j]} = {d}")
