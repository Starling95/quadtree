from __future__ import annotations

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
    def paint(self):
        """ TK representation of a Quadtree"""
        # Your Tkinter-specific code here
        pass

# Example usage
quad_tree_data = [
    [
        [0, 0],
        [0, 0]
    ],
    [
        [0, 0],
        [0, 0]
    ],
    [
        [0, [1, 0, 0, 1]],
        [[0, 0, 1, 1], [0, 1, 1, 0]]
    ],
    [
        [[1, 0, 0, 0], [0, 1, 0, 0]],
        [0, 0]
    ]
]

quad_tree = QuadTree.fromList(quad_tree_data)
quad_tree.paint()
print(f"Depth: {quad_tree.depth}")