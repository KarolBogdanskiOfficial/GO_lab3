import math
import os
from typing import List, Tuple

#zamiast klasy użyłem listy list - 
#np współrzędne punktu o indeksie 1 będą się znajdowały w all_points[1][1]
def load_points(path: str) -> List[Tuple[float, float]]:
    all_points = []
    
    with open(path, 'r') as file:
       for l in file:
        row = l.split()
        if row:
            all_points.append(
                (float(row[0]), float(row[1]))
            )

    return all_points

#pozwoliłem sobie założyć że każdy punkt ma przypisane id będące jego indeksem w chmurze
def get_point_by_id(
    all_points: List[Tuple[float, float]],
    id: int
) -> Tuple[float, float]:
     return all_points[id]

#jak sama nazwa wskazuje
def distance(
    point1: Tuple[float, float],
    point2: Tuple[float, float]
) -> float:
    x1, y1 = point1;
    x2, y2 = point2;

    dx = x1-x2;
    dy = y1-y2;

    return math.sqrt(dx * dx + dy * dy)

#funkcja naiwnie wyszukująca najbliższy punkt
def closest_point(
    all_points: List[Tuple[float, float]],
    new_point: Tuple[float, float]
) -> Tuple[float, float]:
    best_point = None
    best_distance = 0
    
    for current_point in all_points:
        current_distance = distance(new_point, current_point)

        if current_distance <= best_distance:
            best_distance = current_distance
            best_point = current_point

    return best_point
