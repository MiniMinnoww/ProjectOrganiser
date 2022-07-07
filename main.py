"""
Read README.md for more info!
This is a project planning desktop app in python using tkinter, which is aimed at programming projects.
"""

import tkinter as tk
import Tiles
import Tile
import ArrowHandler

# To-Do list.

# Main stuff
    # Allow multiple boards
    # Save/Load system
    # Export board to pdf
# Tiles to make:
    # UML class diagrams
    # Flow chart symbols
    # Images
    # 3D models?
    # Links
    # To-Do lists
    # Columns (to store other widgets)
    # Colours
    # Document links
    # Audio
    # Video
    # Headers
    # Maps?
    # Drawings
    # Logic gate simulation (could be cool?)
# Other touches:
    # Make class diagrams have a 'colour' mode, which replaces things like +/-/# and other characters with colours for a nicer view
    # Allow customisation of colours to the top of tiles
    # Allow labels to arrows

class Main:
    def __init__(self):
        # Initialise main window
        self.root = tk.Tk()
        self.root.title("Project Planner")
        self.root.configure(bg="#DDDDDD")
        self.root.state("zoomed")

        # Make a canvas where we can draw arrows on
        self.canvas = tk.Canvas(bg="#DDDDDD")
        self.canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Bar at the side where you can drag and drop notes from
        # TODO: Make drag and drop from toolbar
        self.toolbar = tk.Frame(self.root, bg="#DDDDDD", highlightbackground="#444444", highlightthickness=2)
        self.toolbar.place(relx=0, rely=0, relheight=1, relwidth=0.1)

        # Create toolbar options
        self.noteButton = tk.Button(self.toolbar, text="Note", command=lambda: self.Create(Tiles.Note))
        self.noteButton.pack()

        self.boardButton = tk.Button(self.toolbar, text="Board", command=lambda: self.Create(Tiles.BoardTile))
        self.boardButton.pack()

        # Handler for arrows
        self.arrowHandler = ArrowHandler.ArrowHandler(self.canvas)

        # Update loop for arrows
        self.root.after(1, self.Update)

        self.root.mainloop()

    def Create(self, tile):
        # Create a tile
        Tile.tiles.append(tile(self.root, self))

    def Update(self):
        # TODO: Only call when widgets are moved
        # Clear canvas
        self.canvas.delete("all")

        # Update arrows
        self.arrowHandler.Update()

        # Re-update for 1 ms
        self.root.after(1, self.Update)

    def OnArrowStart(self, widget):
        # Arrow has been initialised
        self.arrowHandler.ArrowStart(widget)

    def OnArrowStop(self):
        # Arrow has been stopped
        self.arrowHandler.ArrowEnd(self.root)


if __name__ == "__main__":
    # Create main instance
    main = Main()


# Due to round imports or something, we can't have a reference to the main class from the other Tiles
# Instead, we have these functions for Arrow start and end, which call the OnArrow(Start/Stop) from the main class

def ArrowPlace(widget):
    main.OnArrowStart(widget)


def ArrowEnd():
    main.OnArrowStop()
