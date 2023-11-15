import tkinter as tk

from PIL import Image, ImageTk
class QuadTree:
    def __init__(self, data):
        self.data = data

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        if isinstance(self.data[0][0], list):
            return 1 + QuadTree(self.data[0][0]).depth
        else:
            return 1

    @staticmethod
    def fromFile(filename):
        # Placeholder for loading a quadtree from a file
        pass

    @staticmethod
    def fromList(data):
        return QuadTree(data)

    def paint(self):
        """ Textual representation of the QuadTree"""
        for row in self.data:
            print(row)

class TkQuadTree(QuadTree):
    def __init__(self, data, canvas):
        super().__init__(data)
        self.canvas = canvas

    def paint(self, x=0, y=0, size=100):
        """ TK representation of a Quadtree"""
        for element in self.data:
            print(element)
            if isinstance(element, list):
                # If the current node is a quadtree, recursively paint its children
                new_size = size / 2
                TkQuadTree(element[0], self.canvas).paint(x, y, new_size)
                TkQuadTree(element[1], self.canvas).paint(x + new_size, y, new_size)
                TkQuadTree(element[2], self.canvas).paint(x, y + new_size, new_size)
                TkQuadTree(element[3], self.canvas).paint(x + new_size, y + new_size, new_size)
            else:
                # If the current node is a leaf, paint it on the canvas
                color = "black" if element else "white"
                self.canvas.create_rectangle(x, y, x + size, y + size, fill=color)

# Example usage with a simple Tkinter window
root = tk.Tk()
root.title("TKQuadTree")

canvas_width = 400
canvas_height = 400

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.create_rectangle(100,200,200,100, fill="red", outline="darkblue")
canvas.create_rectangle(400,300,100,600, fill="orange", outline="green", width="2")
canvas.create_rectangle(300,40,20,10, fill="blue", outline="orange", width="2")
canvas.create_rectangle(50,0,30,100, fill="yellow", outline="orange", width="4")
canvas.pack()

quad_tree_data = [

        0
    ,

       0
    ,

        [0, [1, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]
    ,

        [[1, 0, 0, 0], [0, 1, 0, 0], 0, 0]

]

quad_tree = TkQuadTree(quad_tree_data, canvas)
quad_tree.paint()
root.mainloop()