import Tile
from DraggableObject import *
import tkinter as tk


class Note(Tile.Tile):
    def __init__(self, root, main):
        super(Note, self).__init__()

        self.root = root

        # All main widgets are labelled 'self.widget'
        self.widget = tk.Entry(self.root, relief=tk.RIDGE, bg="#FFFFFF")
        self.widget.place(x=500, y=500, height=50, width=200)

        # Add delete option
        self.widget.bind("<Delete>", self.Delete)

        # Add right click detection to add arrows
        self.widget.bind("<ButtonPress-3>", lambda _: main.OnArrowStart(self.widget))
        self.widget.bind("<ButtonRelease-3>", lambda _: main.OnArrowStop())

        # Add dragging capability
        self.dragManager = DragManager()
        self.dragManager.AddDraggable(self.widget)

    def Delete(self, _):
        if self.widget.get() == "":
            Tile.tiles.pop(Tile.tiles.index(self))
            self.widget.destroy()


class BoardTile(Tile.Tile):
    def __init__(self, root, main):
        super(BoardTile, self).__init__()
        self.root = root

        # All main widgets are labelled 'self.widget'
        self.widget = tk.Label(self.root, relief=tk.RIDGE, bg="#FFFFFF")
        self.widget.place(x=500, y=500, height=100, width=100)

        # TODO: Add double click and single click functionality

        # TODO: Add delete option

        # Add right click detection to add arrows
        self.widget.bind("<ButtonPress-3>", lambda _: main.OnArrowStart(self.widget))
        self.widget.bind("<ButtonRelease-3>", lambda _: main.OnArrowStop())

        # Add dragging capability
        self.dragManager = DragManager()
        self.dragManager.AddDraggable(self.widget)


class JoinedArrow:
    # Arrow class
    # TODO: Add relative offset from the widgets top corner to place arrows all around the widget.
    def __init__(self, root: tk.Tk, firstTile, secondTile):
        self.root = root

        # First and second tiles
        self.first = firstTile
        self.second = secondTile

    def Update(self, canvas):
        # Need to check if our co-ordinates are co-ordinates (like (0, 0)) or if they are a widget
        if type(self.first) == tuple:
            # It is coordinates of the arrow.
            x0 = self.first[0]
            y0 = self.first[0]
        else:
            # Get widget position
            x0 = self.first.place_info()["x"]
            y0 = self.first.place_info()["y"]

        if type(self.second) == tuple:
            # It is coordinates of the arrow.
            x1 = self.second[0]
            y1 = self.second[0]
        else:
            # Get widget position
            x1 = self.second.place_info()["x"]
            y1 = self.second.place_info()["y"]

        # Now draw the arrow to the canvas
        canvas.create_line(x0, y0, x1, y1, arrow=tk.LAST, fill="#000000")
