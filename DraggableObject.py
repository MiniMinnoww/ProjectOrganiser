class DragManager:
    def __init__(self, widget):
        self.widget = widget
    def AddDraggable(self, widget):
        # Add events to dragging, moving and dropping the tile
        # TODO: Make 1 central drag manager and not multiple for each tile (could use up more memory?)
        widget.bind("<ButtonPress-1>", self.OnStart, True)
        widget.bind("<B1-Motion>", self.OnDrag, True)
        widget.bind("<ButtonRelease-1>", self.OnDrop, True)

        # Used to calculate offset for where user clicked on the widget compared to its (0,0) point
        self.offsetX = 0
        self.offsetY = 0

    def OnStart(self, _):
        x, y = self.widget.winfo_pointerxy()
        # Get offset between mouse pointer and widget position
        self.offsetX = x - float(self.widget.place_info()["x"])
        self.offsetY = y - float(self.widget.place_info()["y"])

    def OnDrag(self, _):
        x, y = self.widget.winfo_pointerxy()
        # Use offset to properly calculate position
        x -= self.offsetX
        y -= self.offsetY

        width = self.widget.place_info()["width"]
        height = self.widget.place_info()["height"]

        self.widget.place_forget()
        self.widget.place(x=x, y=y, width=width, height=height)
        pass

    def OnDrop(self, event):
        # Place tile
        x, y = self.widget.winfo_pointerxy()
        x -= self.offsetX
        y -= self.offsetY

        width = self.widget.place_info()["width"]
        height = self.widget.place_info()["height"]

        self.widget.place_forget()
        self.widget.place(x=x, y=y, width=width, height=height)
