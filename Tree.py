import PointMenagment as pm
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file')

                                    #budowanie drzewa

def build_tree(points, depth=0):
    n = len(points)

    if n == 0:
        return None
    
    axis = depth % 2

    sorted_points = sorted(points, key=lambda point: point[axis])

    return {
        'point': sorted_points[n//2],
        'left': build_tree(sorted_points[:n//2], depth + 1),
        'right': build_tree(sorted_points[n//2 + 1:], depth + 1)
    }

#funkcja pomocnicza porównująca odległość między pivotem a dwoma punktami i zwracająca krótszą 
def closer_distance(pivot, p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1

    d1 = pm.distance(pivot, p1)
    d2 = pm.distance(pivot, p2)

    if d1 < d2:
        return p1
    else:
        return p2


                            #wyszukiwanie najbliższego punktu z drzewa 
def tree_closest_point(root, point, depth=0):
    if root is None:
        return None

    axis = depth % 2
    next_branch = None
    opposite_branch = None

    if point[axis] < root['point'][axis]:
        next_branch = root['left']
        opposite_branch = root['right']
    else:
        next_branch = root['right']
        opposite_branch = root['left']

    #naiwne przeszukiwanie drzewa KD stwarza ryzyko, że zdyskwalifikujemy gałąź
    #zawierającą prawdziwe rozwiązanie problemu
    #aby tego uniknąć piszemy instrukcję która rekursywnie sprawdza czy nie wystąpiła
    #taka sytuacja

    best = closer_distance(point,
                            tree_closest_point(next_branch,
                            point,
                            depth+1),
                            root['point'])

    if pm.distance(point, best) > abs(point[axis]-root['point'][axis]):
        best = closer_distance(point,
                            tree_closest_point(opposite_branch,
                            point,
                            depth+1),
                            best)

    return best    