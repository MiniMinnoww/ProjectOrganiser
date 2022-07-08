import tkinter as tk
from info import GetSetting

class ClassDiagramCreatorGUI(tk.Toplevel):
    def __init__(self, root, main):
        # Initialise toplevel window
        super(ClassDiagramCreatorGUI, self).__init__(root)

        # Title entry
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=0, column=0, columnspan=2)

        # Fields entry
        self.field_name = tk.Entry(self)
        self.field_name.grid(row=1, column=0)

        self.fieldTypeVar = tk.StringVar(self)

        options = tuple(GetSetting("enum.field-type"))
        self.field_type = tk.OptionMenu(self, self.fieldTypeVar, options[0], *options[1:len(options)])

        self.field_type.grid(row=1, column=1)

