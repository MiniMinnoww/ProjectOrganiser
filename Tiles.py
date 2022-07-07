import Tile
from DraggableObject import *
import tkinter as tk
from info import GetSetting

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
        self.dragManager = DragManager(self.widget)
        self.dragManager.AddDraggable(self.widget)

    def Delete(self, _):
        # Check if delete is to delete the tile, or just the text (by seeing if there is text current in it)
        if self.widget.get() == "":
            Tile.tiles.pop(Tile.tiles.index(self))
            self.widget.destroy()


class Board(Tile.Tile):
    def __init__(self, root, main):
        super(Board, self).__init__()
        self.root = root

        # All main widgets are labelled 'self.widget'
        self.widget = tk.Label(self.root, relief=tk.RIDGE, bg="#FFFFFF")
        self.widget.place(x=500, y=500, height=100, width=100)

        # TODO: Add double click and single click functionality (single = select, double = open board)

        # Add delete option
        self.widget.bind("<Delete>", self.Delete)

        # Add right click detection to add arrows
        self.widget.bind("<ButtonPress-3>", lambda _: main.OnArrowStart(self.widget))
        self.widget.bind("<ButtonRelease-3>", lambda _: main.OnArrowStop())

        # Detect selecting
        self.widget.bind("<ButtonPress-1>", self.Select, True)

        # Detect opening
        self.widget.bind("<Double-Button-1>", self.Open, True)

        # Add dragging capability
        self.dragManager = DragManager(self.widget)
        self.dragManager.AddDraggable(self.widget)

    def Delete(self, _):
        Tile.tiles.pop(Tile.tiles.index(self))
        self.widget.destroy()

    def Select(self, _):
        # TODO: Add select option
        pass

    def Open(self, _):
        # TODO: Add way to open board
        pass


class Image(Tile.Tile):
    def __init__(self, root, main, image):
        super(Image, self).__init__()
        self.root = root
        self.image = image
        print(type(self.image))

        # All main widgets are labelled 'self.widget'
        self.widget = tk.Label(self.root, relief=tk.RIDGE, image=self.image)
        self.widget.place(x=500, y=500)

        # TODO: Add single click functionality to select

        # Add delete option
        self.widget.bind("<Delete>", self.Delete)

        # Add right click detection to add arrows
        self.widget.bind("<ButtonPress-3>", lambda _: main.OnArrowStart(self.widget))
        self.widget.bind("<ButtonRelease-3>", lambda _: main.OnArrowStop())

        # Detect selecting
        self.widget.bind("<ButtonPress-1>", self.Select, True)

        # Add dragging capability
        self.dragManager = DragManager(self.widget)
        self.dragManager.AddDraggable(self.widget)

    def Delete(self, _):
        Tile.tiles.pop(Tile.tiles.index(self))
        self.widget.destroy()

    def Select(self, _):
        # TODO: Add select option
        pass


class Header(Tile.Tile):
    def __init__(self, root, main):
        super(Header, self).__init__()

        self.root = root

        # All main widgets are labelled 'self.widget'
        self.widget = tk.Entry(self.root, relief=tk.RIDGE, bg=GetSetting("colours.background"), font="Helvetica 20 bold", justify=tk.CENTER)
        self.widget.place(x=500, y=500, height=50, width=200)

        # Add delete option
        self.widget.bind("<Delete>", self.Delete)

        # Add right click detection to add arrows
        self.widget.bind("<ButtonPress-3>", lambda _: main.OnArrowStart(self.widget))
        self.widget.bind("<ButtonRelease-3>", lambda _: main.OnArrowStop())

        # Add dragging capability
        self.dragManager = DragManager(self.widget)
        self.dragManager.AddDraggable(self.widget)

    def Delete(self, _):
        # Check if delete is to delete the tile, or just the text (by seeing if there is text current in it)
        if self.widget.get() == "":
            Tile.tiles.pop(Tile.tiles.index(self))
            self.widget.destroy()


class ClassDiagram(Tile.Tile):
    def __init__(self, root, main):
        super(ClassDiagram, self).__init__()

        self.root = root

        # The main widget is labelled 'self.widget'
        self.widget = tk.Frame(self.root, relief=tk.RIDGE, bg="#FFFFFF")
        self.widget.place(x=500, y=500, height=800, width=200)

        self.header = tk.Entry(self.widget, relief=tk.RIDGE, font="Helvetica 20 bold", justify=tk.CENTER)
        self.header.pack()

        self.fields = tk.Text(self.widget, relief=tk.RIDGE, wrap=tk.WORD)
        self.fields.pack()

        self.methods = tk.Text(self.widget, relief=tk.RIDGE, wrap=tk.WORD)
        self.methods.pack()

        # Add delete option
        self.widget.bind("<Delete>", self.Delete)

        # Add right click detection to add arrows
        self.widget.bind("<ButtonPress-3>", lambda _: main.OnArrowStart(self.widget))
        self.widget.bind("<ButtonRelease-3>", lambda _: main.OnArrowStop())

        # Add dragging capability
        self.dragManager = DragManager(self.widget)
        self.dragManager.AddDraggable(self.widget)
        self.dragManager.AddDraggable(self.header)
        self.dragManager.AddDraggable(self.fields)
        self.dragManager.AddDraggable(self.methods)

    def Delete(self, _):
        # Delete
        Tile.tiles.pop(Tile.tiles.index(self))
        self.widget.destroy()


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
