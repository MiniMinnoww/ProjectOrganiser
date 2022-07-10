from tiles import JoinedArrow
import tkinter as tk
import tile

class ArrowHandler:
    def __init__(self, canvas, root):
        self.arrows = []
        self.currentStart = None
        self.canvas = canvas
        self.root = root

    def ArrowStart(self, widget):
        # Set current start to the widget where the arrow was started
        self.currentStart = widget

    def ArrowEnd(self, root: tk.Tk):
        # Get the widget under the mouse
        widget = root.winfo_containing(root.winfo_pointerx(), root.winfo_pointery())
        if widget == self.canvas:
            # This means the arrow was draw to no widget, so just put it at the mouse pointer position
            self.arrows.append(JoinedArrow(root, self.currentStart, (root.winfo_pointerx(), root.winfo_pointery())))
        else:
            # Make the arrows target a widget
            self.arrows.append(JoinedArrow(root, self.currentStart, widget))

    def Update(self):
        for arrow in self.arrows:
            arrow.Update(self.canvas)

    def get_save_data(self):
        data = []
        for arrow in self.arrows:
            data.append(arrow.get_save_data())
        return data

    def load_save_data(self, data):
        if not data: return
        for arrow in data:
            # Get first and second tiles
            firstTileID = arrow[0]
            secondTileID = arrow[1]
            firstTile = None
            secondTile = None
            for _tile in tile.tiles:
                if _tile.UID == firstTileID: firstTile = _tile
                elif _tile.UID == secondTileID: secondTile = _tile
            self.arrows.append(JoinedArrow(self.root, firstTile, secondTile))
