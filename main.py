"""
Read README.md for more info!
This is a project planning desktop app in python using tkinter, which is aimed at programming projects.
"""

import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image,ImageTk

import Tiles
import Tile

import ArrowHandler

from info import GetSetting

# To-Do list.

# Main stuff
    # Allow multiple boards
    # Save/Load system
    # Export board to pdf
    # Add settings in toolbar when widget selected
# Tiles to make:
    # UML class diagrams
    # Flow chart symbols
    # 3D models?
    # Links
    # To-Do lists
    # Columns (to store other widgets)
    # Colours
    # Document links
    # Audio
    # Video
    # Maps?
    # Drawings
    # Logic gate simulation (could be cool?)
# Other touches:
    # Make class diagrams have a 'colour' mode, which replaces things like +/-/# and other characters with colours for a nicer view
    # Allow customisation of colours to the top of tiles
    # Allow labels to arrows
    # Allow resizing of images

class Main:
    def __init__(self):
        # Initialise main window
        self.root = tk.Tk()
        self.root.title("Project Planner")
        self.root.configure(bg=GetSetting("colours.background"))
        self.root.state("zoomed")

        # Make a canvas where we can draw arrows on
        self.canvas = tk.Canvas(bg=GetSetting("colours.background"))
        self.canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Bar at the side where you can drag and drop notes from
        # TODO: Make drag and drop from toolbar
        self.toolbar = tk.Frame(self.root, bg=GetSetting("colours.toolbar"), highlightbackground="#444444", highlightthickness=2)
        self.toolbar.place(relx=0, rely=0, relheight=1, relwidth=0.1)

        # Create toolbar options
        # TODO: Add icons for these
        self.noteButton = tk.Button(self.toolbar, text="Note", command=lambda: self.Create(Tiles.Note))
        self.noteButton.pack()

        self.boardButton = tk.Button(self.toolbar, text="Board", command=lambda: self.Create(Tiles.Board))
        self.boardButton.pack()

        self.headerButton = tk.Button(self.toolbar, text="Header", command=lambda: self.Create(Tiles.Header))
        self.headerButton.pack()

        self.imageButton = tk.Button(self.toolbar, text="Image", command=lambda: self.CreateImage())
        self.imageButton.pack()

        self.classDiagramButton = tk.Button(self.toolbar, text="Class Diagram", command=lambda: self.CreateClassDiagram())
        self.classDiagramButton.pack()

        # Handler for arrows
        self.arrowHandler = ArrowHandler.ArrowHandler(self.canvas)

        # Update loop for arrows
        self.root.after(1, self.Update)

        self.root.mainloop()

    def Create(self, tile):
        # Create a tile
        Tile.tiles.append(tile(self.root, self))

    def CreateImage(self):
        # Special case for creating an image (we need a file select box to come up)

        # File dialog come up
        allowedFileExtensions = tuple(GetSetting("files.extensions.images"))
        filePath = fd.askopenfilename(filetypes=[allowedFileExtensions])

        # Now load the image
        _image = Image.open(filePath)
        _image.thumbnail((300, 300))
        image = ImageTk.PhotoImage(_image)
        Tile.tiles.append(Tiles.Image(self.root, self, image))

    def CreateClassDiagram(self):
        # Special case for creating a class diagram
        # We want to add a way to input all the methods and fields into a GUI, then construct the diagram ourselves
        # TODO: Class diagram GUI
        self.Create(Tiles.ClassDiagram)

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
