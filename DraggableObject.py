class DragManager:
    def AddDraggable(self, widget):
        # Add events to dragging, moving and dropping the tile
        # TODO: Make 1 central drag manager and not multiple for each tile (could use up more memory?)
        widget.bind("<ButtonPress-1>", self.OnStart)
        widget.bind("<B1-Motion>", self.OnDrag)
        widget.bind("<ButtonRelease-1>", self.OnDrop)

        # Used to calculate offset for where user clicked on the widget compared to its (0,0) point
        self.offsetX = 0
        self.offsetY = 0

    def OnStart(self, event):
        x, y = event.widget.winfo_pointerxy()
        # Get offset between mouse pointer and widget position
        self.offsetX = x - float(event.widget.place_info()["x"])
        self.offsetY = y - float(event.widget.place_info()["y"])

    def OnDrag(self, event):
        x, y = event.widget.winfo_pointerxy()
        # Use offset to properly calculate position
        x -= self.offsetX
        y -= self.offsetY

        width = event.widget.place_info()["width"]
        height = event.widget.place_info()["height"]

        event.widget.place_forget()
        event.widget.place(x=x, y=y, width=width, height=height)
        pass

    def OnDrop(self, event):
        # Place tile
        x, y = event.widget.winfo_pointerxy()
        x -= self.offsetX
        y -= self.offsetY

        width = event.widget.place_info()["width"]
        height = event.widget.place_info()["height"]

        event.widget.place_forget()
        event.widget.place(x=x, y=y, width=width, height=height)
