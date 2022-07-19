import tkinter as tk

class Label(tk.Label):
    def __init__(self, root, parent, **kwargs):

        super(Label, self).__init__(root, kwargs)
        self.parent = parent


class Entry(tk.Entry):
    def __init__(self, root, parent, **kwargs):
        super(Entry, self).__init__(root, kwargs)
        self.parent = parent


class Frame(tk.Frame):
    def __init__(self, root, parent, **kwargs):
        super(Frame, self).__init__(root, kwargs)
        self.parent = parent