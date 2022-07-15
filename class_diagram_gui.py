import tkinter as tk
from info import GetSetting
import tiles
import tile

class ClassDiagramCreatorGUI(tk.Toplevel):
    def __init__(self, root, main):
        # Initialise toplevel window
        super(ClassDiagramCreatorGUI, self).__init__(root)

        # TopLevel settings
        self.resizable(0, 0)
        self.title("Create Class")

        # Initialise variables
        self.field_options = tuple(GetSetting("enum.field-type"))
        self.method_options = tuple(GetSetting("enum.method-type"))

        self.fields = []
        self.methods = []

        self.main = main
        self.root = root

        # Title

        self.titleLabel = tk.Label(self, text="Class Name: ")
        self.titleLabel.grid(row=0, column=0)

        self.title_entry = tk.Entry(self, width=40)
        self.title_entry.bind("<KeyRelease>", self.UpdateTitle)
        self.title_entry.grid(row=0, column=1, columnspan=2)

        # Field Type (private, protected, public)
        self.field_type_var = tk.StringVar(self)
        self.field_type_var.set(self.field_options[0])

        self.field_type = tk.OptionMenu(self, self.field_type_var, self.field_options[0],
                                        *self.field_options[1:len(self.field_options)])
        self.field_type.grid(row=1, column=0)

        # Fields entry (object)
        self.field_object = tk.Entry(self)
        self.field_object.grid(row=1, column=1)

        # Fields entry (name)
        self.field_name = tk.Entry(self)
        self.field_name.grid(row=1, column=2)

        self.field_button = tk.Button(self, text="Add Field", command=self.AddField)
        self.field_button.grid(row=2, column=0, columnspan=3)

        # Listbox area to display fields
        self.fields_listbox = tk.Listbox(self, width=50)
        self.fields_listbox.grid(row=1, column=3)


        # Method Type (private, protected, public)
        self.method_type_var = tk.StringVar(self)
        self.method_type_var.set(self.method_options[0])

        self.method_type = tk.OptionMenu(self, self.method_type_var, self.method_options[0], *self.method_options[1:len(self.method_options)])
        self.method_type.grid(row=5, column=0)

        # Method entry (return type)
        self.method_return_object = tk.Entry(self)
        self.method_return_object.grid(row=5, column=1)

        # Method entry (name)
        self.method_name = tk.Entry(self)
        self.method_name.grid(row=5, column=2)

        # TODO: Make better parameter menu
        # Add parameters
        self.parameters = tk.Entry(self)
        self.parameters.grid(row=6, column=0)

        # Method button
        self.method_button = tk.Button(self, text="Add Method", command=self.AddMethod)
        self.method_button.grid(row=7, column=0, columnspan=3)

        # Listbox area to display methods
        self.method_listbox = tk.Listbox(self, width=50)
        self.method_listbox.grid(row=5, column=3)

        # Big create button :D
        self.create_button = tk.Button(self, text="Create Class", command=self.Create, width=100)
        self.create_button.grid(row=8, column=0, columnspan=4)

        self.UpdateTitle()

    def AddField(self):
        # Check if field options are not empty
        if self.field_object.get() == "" or self.field_name.get() == "": return

        # Add to list
        self.fields.append(Field(self.field_type_var.get(), self.field_object.get(), self.field_name.get()))

        # Clear previous selection
        self.field_type_var.set(self.field_options[0])
        self.field_object.delete(0, tk.END)
        self.field_name.delete(0, tk.END)

        # Update listboxes and info
        self.UpdateInfo()

    def AddMethod(self):
        # Check if method options are not empty
        if self.method_return_object.get() == "" or self.method_name.get() == "": return

        # Add to list
        self.methods.append( Method(self.method_type_var.get(), self.method_return_object.get(), self.method_name.get(), self.parameters.get().split(", ")) )

        # Clear previous selection
        self.method_type_var.set(self.field_options[0])
        self.method_return_object.delete(0, tk.END)
        self.method_name.delete(0, tk.END)

        # Update listboxes and info
        self.UpdateInfo()

    def UpdateInfo(self):
        # Clear listboxes
        self.fields_listbox.delete(0, tk.END)
        self.method_listbox.delete(0, tk.END)

        # Update listboxes
        for field in self.fields:
            self.fields_listbox.insert(tk.END, field.__repr__())

        for method in self.methods:
            self.method_listbox.insert(tk.END, method.__repr__())

    def UpdateTitle(self, _=None):
        # Called whenever user types into the class title box, which lets us rename the window's title to the class title dynamically
        if self.title_entry.get() == "": self.title("Create Class")
        else: self.title(self.title_entry.get())

    def Create(self):
        # Generate new lists for methods/fields using the __repr__()
        fields = []
        methods = []
        for field in self.fields: fields.append(field.__repr__())
        for method in self.methods: methods.append(method.__repr__())

        # Create Class Diagram
        tile.tiles.append(tiles.ClassDiagram(self.root, self.main, self.title_entry.get(), fields, methods))

        # Delete TopLevel
        self.destroy()


class Field:
    def __init__(self, access, objectType, name):
        self.access = access
        self.object = objectType
        self.name = name

    def __repr__(self):
        return self.access.lower() + " " + self.object + " " + self.name

class UnscopedField:
    def __init__(self, objectType, name):
        self.object = objectType
        self.name = name

    def __repr__(self):
        return self.object + " " + self.name

class Method:
    def __init__(self, access, returnType, name, parameters):
        self.access = access
        self.returnType = returnType
        self.name = name
        self.parameters = tuple(parameters)

    def __repr__(self):
        return self.access.lower() + " " + self.returnType + " " + self.name + " (" + ", ".join(self.parameters) + ")"