import tkinter as tk
from tkinter import ttk


# TODO Keypad should extend Frame so that it is a container
class Commandpad():

    def __init__(self, parent, keynames:list=[], **kwargs):
        # TODO call the superclass constructor with all args except
	# keynames and columns
        self.parent = parent
        self.keynames = keynames
        self.init_components()

    def init_components(self) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        :param *dimention: the dimentions of the keypad ex: (3,4)
        """
        _operants = self.keynames
        self.button = []
        operation_frame = tk.Frame(self.parent)
        operation_frame.pack(expand=True, fill=tk.BOTH, side="right")
        # Init buttons
        for i in range(len(_operants)):
            self.button.append(
                tk.Button(operation_frame, text=str(_operants[i])))
            self.button[i].grid(row=i, column=0, sticky="nsew")
            operation_frame.rowconfigure(i, weight=1)
        operation_frame.columnconfigure(0, weight=6)
        self.frame = operation_frame

    def bind(self, todo):
        """Bind an event handler to an event sequence."""
        for i in self.button:
            i.bind("<Button>", todo)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for i in self.button:
            i[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.button[0][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for i in self.button:
            i.configure(kwargs)

    def __getattr__(self, name):
        """if you excecute some method that does not exist in the class
        it will execute that method in self.frame instead

        Args:
            name (_type_): _description_

        Returns:
            tk.Frame: it returns the self.frame.<Something that you execute>
        """
        setattr(self, name, self)
        return getattr(self.frame, name)


if __name__ == '__main__':
    keys = list('+_*/=')
    root = tk.Tk()
    root.title("Commandpad Demo")
    commandpad = Commandpad(root, keynames=keys, columns=3)
    commandpad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
