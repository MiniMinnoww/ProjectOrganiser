import tile
from draggable_object import *
import tkinter2 as tk2
import tkinter as tk
from info import GetSetting
import uid_manager
from PIL import Image as PImage
from PIL import ImageTk

# Each tile has a ID (self.ID) which is used for save load system.

class Note(tile.Tile):
    def __init__(self, root, main):
        super(Note, self).__init__()

        self.root = root
        self.ID = 0
        self.UID = uid_manager.get_uid()

        # All main widgets are labelled 'self.widget'
        self.widget = tk2.Entry(self.root, self, relief=tk.RIDGE, bg="#FFFFFF")
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
            "dimensions": (self.widget.place_info()["height"], self.widget.place_info()["width"]),
            "uid": self.UID
        }
        return self.ID, info

    def load_save_info(self, save):
        # Text
        self.widget.delete(0, tk.END)
        self.widget.insert(0, save["text"])

        # UID
        self.UID = save["uid"]

        # Position & Dimensions
        self.widget.place_forget()
        self.widget.place(x=save["position"][0], y=save["position"][1], height=save["dimensions"][0], width=save["dimensions"][1])


class Board(tile.Tile):
    def __init__(self, root, main):
        super(Board, self).__init__()
        self.root = root

        self.ID = 1
        self.UID = uid_manager.get_uid()

        # All main widgets are labelled 'self.widget'
        self.widget = tk2.Label(self.root, self, relief=tk.RIDGE, bg="#FFFFFF")
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
            "dimensions": (self.widget.place_info()["height"], self.widget.place_info()["width"]),
            "uid": self.UID
        }
        return self.ID, info

    def load_save_info(self, save):
        # Position & Dimensions
        self.widget.place_forget()
        self.widget.place(x=save["position"][0], y=save["position"][1], height=save["dimensions"][0], width=save["dimensions"][1])

        # UID
        self.UID = save["uid"]

# TODO: save image
class Image(tile.Tile):
    def __init__(self, root, main, filePath=None):
        super(Image, self).__init__()
        self.filePath = filePath
        self.root = root
        self.UID = uid_manager.get_uid()
        self.widget = tk2.Label(self.root, self, relief=tk.RIDGE)
        self.ID = 4
        if filePath is not None:
            _image = PImage.open(self.filePath)
            _image.thumbnail((300, 300))
            image = ImageTk.PhotoImage(_image)
            self.image = image

            # All main widgets are labelled 'self.widget'

            self.widget.configure(image=self.image)
            self.widget.place(x=500, y=500, width=image.width(), height=image.height())
        else:
            self.widget.place(x=500, y=500, width=10, height=10)

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

    def get_save_info(self):
        info = {
            "file-path": self.filePath,
            "position": (self.widget.place_info()["x"], self.widget.place_info()["y"]),
            "dimensions": (self.widget.place_info()["height"], self.widget.place_info()["width"]),
            "uid": self.UID
        }
        return self.ID, info

    def load_save_info(self, save):
        # Image
        self.filePath = save["file-path"]
        _image = PImage.open(self.filePath)
        _image.thumbnail((300, 300))
        image = ImageTk.PhotoImage(_image)
        self.image = image
        self.widget.configure(image=self.image)

        # Position & Dimensions
        self.widget.place_forget()
        self.widget.place(x=save["position"][0], y=save["position"][1], height=image.height(), width=image.width())

        # UID
        self.UID = save["uid"]


class Header(tile.Tile):
    def __init__(self, root, main):
        super(Header, self).__init__()

        self.root = root

        self.ID = 3
        self.UID = uid_manager.get_uid()

        # All main widgets are labelled 'self.widget'
        self.widget = tk2.Entry(self.root, self, relief=tk.GROOVE, bg=GetSetting("colours.background"), font="Helvetica 20 bold", justify=tk.CENTER)
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
            "dimensions": (self.widget.place_info()["height"], self.widget.place_info()["width"]),
            "uid": self.UID
        }
        return self.ID, info

    def load_save_info(self, save):
        # Text
        self.widget.delete(0, tk.END)
        self.widget.insert(0, save["text"])

        # Position & Dimensions
        self.widget.place_forget()
        self.widget.place(x=save["position"][0], y=save["position"][1], height=save["dimensions"][0], width=save["dimensions"][1])

        # UID
        self.UID = save["uid"]

# TODO: Save class diagrams
class ClassDiagram(tile.Tile):
    def __init__(self, root, main, title, fields, methods):
        print(title)
        super(ClassDiagram, self).__init__()

        self.root = root

        # The main widget is labelled 'self.widget'
        self.widget = tk2.Frame(self.root, self, relief=tk.RIDGE, bg="#FFFFFF")
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
    def __init__(self, root: tk.Tk, main, firstTile, secondTile):
        self.root = root
        self.offsetFirst = (0, 0)
        self.offsetSecond = (0, 0)
        # First and second tiles
        try:
            self.first = firstTile.widget
            self.second = secondTile.widget
        except:
            self.first = firstTile
            self.second = secondTile

        # Get arrow tiles
        try: self.firstTile = self.first.parent
        except: pass
        try: self.secondTile = self.second.parent
        except: pass

        if self.first is None or self.second is None:
            main.arrowHandler.arrows.pop(main.arrowHandler.arrows.index(self))
            return

        # Now we need to calculate offset for both widgets
        # Firstly, get the position of the center of our first widget
        x = int(self.first.place_info()["width"]) / 2
        y = int(self.first.place_info()["height"]) / 2
        self.offsetFirst = (x, y)

        # Now get position of the center for our second widget
        x = int(self.second.place_info()["width"]) / 2
        y = int(self.second.place_info()["height"]) / 2
        self.offsetSecond = (x, y)

    def Update(self, canvas):
        # Get widget position
        x0 = int(self.first.place_info()["x"])
        y0 = int(self.first.place_info()["y"])

        # Now, use the line_intersection_on_rect to calculate the right position for the arrow
        coords = line_intersection_on_rect(int(self.second.place_info()["width"]),
                                           int(self.second.place_info()["height"]),
                                           int(self.second.place_info()["x"]) + self.offsetSecond[0],
                                           int(self.second.place_info()["y"]) + self.offsetSecond[1],
                                           x0 + self.offsetFirst[0],
                                           x0 + self.offsetFirst[1])
        canvas.create_line(x0 + self.offsetFirst[0], y0 + self.offsetFirst[1], coords[0], coords[1], arrow=tk.LAST, fill="#000000")

    def get_save_data(self):
        return [self.firstTile.UID, self.secondTile.UID]

sign = lambda x: -1 if x < 0 else (1 if x > 0 else (0 if x == 0 else None))


# Thanks to https://stackoverflow.com/questions/1585525/how-to-find-the-intersection-point-between-a-line-and-a-rectangle for this part :D

def line_intersection_on_rect(width, height, xB, yB, xA, yA):

  w = width / 2
  h = height / 2

  dx = xA - xB
  dy = yA - yB

  ## if A=B return B itself
  if dx == 0 and dy == 0: return xB, yB

  tan_phi = h / w
  tan_theta = abs(dy / dx)

  # tell me in which quadrant the A point is

  qx = sign(dx)
  qy = sign(dy)


  if tan_theta > tan_phi:
    xI = xB + (h / tan_theta) * qx
    yI = yB + h * qy
  else:
    xI = xB + w * qx
    yI = yB + w * tan_theta * qy


  return xI, yI
