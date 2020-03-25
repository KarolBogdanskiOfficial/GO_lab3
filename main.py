import PointMenagment as pm
import Tree
import GUI
import pprint
import tkinter as tk

#tutaj znajduje się konsolowe przedstawienie działania programu
all_points = pm.load_points("data.txt")
tree = Tree.build_tree(all_points)

pp = pprint.PrettyPrinter(indent = 4)
pp.pprint(tree) 

test_point = [13, 25]      #testowy punkt dla którego wyszukujemy najbliższy punkt z chmury
result = Tree.tree_closest_point(tree, test_point)
print("Podany punkt: ")
print(test_point)
print(" najbliższy punkt: ")
print(result)

                        #GUI
root = tk.Tk()
root.title("GUI obrazujące działanie drzewa KD")

GUI.start_window(root)

root.mainloop()