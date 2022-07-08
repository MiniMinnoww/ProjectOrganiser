from tiles import JoinedArrow
import tkinter as tk


class ArrowHandler:
    def __init__(self, canvas):
        self.arrows = []
        self.currentStart = None
        self.canvas = canvas

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
