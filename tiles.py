import tile
from draggable_object import *
import tkinter as tk
from info import GetSetting

# Each tile has a ID (self.ID) which is used for save load system.

class Note(tile.Tile):
    def __init__(self, root, main):
        super(Note, self).__init__()

        self.root = root
        self.ID = 0

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
            tile.tiles.pop(tile.tiles.index(self))
            self.widget.destroy()

    def get_save_info(self):
        info = {
            "text": self.widget.get(),
            "position": (self.widget.place_info()["x"], self.widget.place_info()["y"]),
            "dimensions": (self.widget.place_info()["height"], self.widget.place_info()["width"])
        }
        return self.ID, info

    def load_save_info(self, save):
        # Text
        self.widget.delete(0, tk.END)
        self.widget.insert(0, save["text"])

        # Position & Dimensions
        self.widget.place_forget()
        self.widget.place(x=save["position"][0], y=save["position"][1], height=save["dimensions"][0], width=save["dimensions"][1])


class Board(tile.Tile):
    def __init__(self, root, main):
        super(Board, self).__init__()
        self.root = root

        self.ID = 1

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
        tile.tiles.pop(tile.tiles.index(self))
        self.widget.destroy()

    def Select(self, _):
        # TODO: Add select option
        pass

    def Open(self, _):
        # TODO: Add way to open board
        pass

    def get_save_info(self):
        info = {
            "position": (self.widget.place_info()["x"], self.widget.place_info()["y"]),
            "dimensions": (self.widget.place_info()["height"], self.widget.place_info()["width"])
        }
        return self.ID, info

    def load_save_info(self, save):
        # Position & Dimensions
        self.widget.place_forget()
        self.widget.place(x=save["position"][0], y=save["position"][1], height=save["dimensions"][0], width=save["dimensions"][1])


class Image(tile.Tile):
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
        tile.tiles.pop(tile.tiles.index(self))
        self.widget.destroy()

    def Select(self, _):
        # TODO: Add select option
        pass


class Header(tile.Tile):
    def __init__(self, root, main):
        super(Header, self).__init__()

        self.root = root

        self.ID = 3

        # All main widgets are labelled 'self.widget'
        self.widget = tk.Entry(self.root, relief=tk.GROOVE, bg=GetSetting("colours.background"), font="Helvetica 20 bold", justify=tk.CENTER)
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
            tile.tiles.pop(tile.tiles.index(self))
            self.widget.destroy()

    def get_save_info(self):
        info = {
            "text": (self.widget.get()),
            "position": (self.widget.place_info()["x"], self.widget.place_info()["y"]),
            "dimensions": (self.widget.place_info()["height"], self.widget.place_info()["width"])
        }
        return self.ID, info

    def load_save_info(self, save):
        # Text
        self.widget.delete(0, tk.END)
        self.widget.insert(0, save["text"])

        # Position & Dimensions
        self.widget.place_forget()
        self.widget.place(x=save["position"][0], y=save["position"][1], height=save["dimensions"][0], width=save["dimensions"][1])


class ClassDiagram(tile.Tile):
    def __init__(self, root, main, title, fields, methods):
        print(title)
        super(ClassDiagram, self).__init__()

        self.root = root

        # The main widget is labelled 'self.widget'
        self.widget = tk.Frame(self.root, relief=tk.RIDGE, bg="#FFFFFF")
        self.widget.place(x=500, y=500, height=400, width=200)

        self.header = tk.Label(self.widget, text=title, relief=tk.FLAT, font="Helvetica 20 bold", justify=tk.CENTER, bg="#FFFFFF")
        self.header.pack()

        self.fields = tk.Listbox(self.widget, relief=tk.RIDGE, width=50)
        for field in fields:
            self.fields.insert(tk.END, field)
        self.fields.pack(fill=tk.BOTH, expand=True)

        self.methods = tk.Listbox(self.widget, relief=tk.RIDGE, width=50)
        for method in methods:
            self.methods.insert(tk.END, method)
        self.methods.pack(fill=tk.BOTH, expand=True)

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
        tile.tiles.pop(tile.tiles.index(self))
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
