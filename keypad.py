import tkinter as tk
from tkinter import ttk


#TODO Keypad should extend Frame so that it is a container
class Keypad():

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        #TODO call the superclass constructor with all args except
		# keynames and columns
        self.parent = parent
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        dimention = (columns, int(len(self.keynames)//columns))
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        :param *dimention: the dimentions of the keypad ex: (3,4)
        """
        self.button = []
        keypad_frame = tk.Frame(self.parent)
        # Init buttons
        options = {'sticky': tk.NSEW}
        for i in self.keynames:
            self.button.append(tk.Button(keypad_frame, text=str(i)))
        # customize buttons
        for i in range(0, dimention[0] * dimention[1], dimention[0]):
            for j in range(0, dimention[0]):
                self.button[i+j].grid(row=int(i/dimention[0]), column=j, sticky="nsew")
        # weighing
        for i in range(dimention[1]):
            keypad_frame.rowconfigure(i, weight=1)
        keypad_frame.rowconfigure(1, weight=1)
        for i in range(dimention[0]):
            keypad_frame.columnconfigure(i, weight=1)
        self.frame = keypad_frame

    def bind(self, todo):
        """Bind an event handler to an event sequence."""
        #TODO Write a bind method with exactly the same parameters
        # as the bind method of Tkinter widgets.
        # Use the parameters to bind all the self.buttons in the keypad
        # to the same event handler.
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
            

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for i in self.button:
            i.configure(kwargs)

    #TODO Write a property named 'frame' the returns a reference to 
    # the the superclass object for this keypad.
    # This is so that a programmer can set properties of a keypad's frame,
    # e.g. keypad.frame.configure(background='blue')

if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
