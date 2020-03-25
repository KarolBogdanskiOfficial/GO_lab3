import PointMenagment as pm
import tkinter as tk
import Tree


test_point = [13, 25]     #testowy punkt dla którego wyszukujemy najbliższy punkt z chmury
#parametry okna
HEIGHT = 700
WIDTH = 700
MIDDLE = 350


#funkcja zwracająca współrzędne względem początku układu współrzędnych
def get_cartesian_coordinates(event):

    if event[0] > MIDDLE:
        x1= (MIDDLE - 10*event[0] - 5)
        x2 = (MIDDLE - 10*event[0] + 5)
    else:
        x1= (MIDDLE + 10*event[0] - 5)
        x2 = (MIDDLE + 10*event[0] + 5)
        
    if event[1] < MIDDLE:
        y1= (MIDDLE - 10*event[1] - 5)
        y2 = (MIDDLE - 10*event[1] + 5)
    else:
        y1= (MIDDLE + 10*event[1] - 5)
        y2 = (MIDDLE + 10*event[1] + 5)

    return x1, x2, y1, y2

#rysowanie punktów z chmury 
def paint(event, can):

    coor = get_cartesian_coordinates(event)

    x1, x2, y1, y2 = (coor[0], coor[1], coor[2], coor[3])
        
    can.create_oval(x1, y1, x2, y2, fill='red')

def draw_points(all_points, canvas):
    for i in range(len(all_points)):
        p = pm.get_point_by_id(all_points, i)
        paint(p, canvas)

                                        #OKNO GŁÓWNE GUI

def start_window(root):

    #canvas
    canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg= 'white')
    canvas.pack()

    #axis, niestety nie udało mi się zrobić podziałki
    canvas.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2)    #x
    canvas.create_line(WIDTH/2, HEIGHT, WIDTH/2, 0)     #y

    #pobierz i narysuj punkty - przycisk
    def draw_points_2(event):
        draw_points(event, canvas)

    draw_points_button = tk.Button(canvas,
                            text="rysuj punkty",
                            bg='#AFEEEE',
                            activebackground = 'pink',
                            fg='black',
                            command = lambda: draw_points_2(pm.load_points("data.txt"))
                            )

    draw_points_button.place(relx = 0.9, rely = 0)

    #narysuj podany punkt (kolor zielony) i pokoloruj najbliższy na fiołkowo
    #zastosowoałem małe oszustwo i najbliższy punkt nie jest kolorowany a zasłaniany nowym
    def find_closest(root, point):
        
        coor = get_cartesian_coordinates(point)
        x1, x2, y1, y2 = (coor[0], coor[1], coor[2], coor[3])

        canvas.create_oval(x1, y1, x2, y2, fill='#009933')

        closest = Tree.tree_closest_point(root, point)
        coor_closest = get_cartesian_coordinates(closest)

        x3, x4, y3, y4 = (coor_closest[0], coor_closest[1], coor_closest[2], coor_closest[3])
        canvas.create_oval(x3, y3, x4, y4, fill='#6666ff')

    find_closest_button = tk.Button(canvas,
                            text="najblizszy punkt",
                            bg='#ffcc00',
                            activebackground = 'pink',
                            fg='black',
                            command = lambda: find_closest(Tree.build_tree(pm.load_points("data.txt")), test_point)
                            )
                            

    find_closest_button.place(relx = 0.765, rely = 0)