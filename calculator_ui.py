import copy
import winsound
import tkinter as tk
from tkinter import ttk
from commandpad import Commandpad
from keypad import Keypad
from expression_handler import ExpressionHandler
from evaluate import Evaluator
from operants import Operants
from history_handler import History

op = Operants()


class Calculator_UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator!")
        self.expression = ExpressionHandler()
        self.history = History()

    def make_keypad(self, keyname: list = op.numbers, columns: int = 3):
        return Keypad(self, keyname, columns)

    def make_operator_pad(self, keyname: list = op.operational):
        return Commandpad(self, keyname)

    def make_textfield(self):
        number_view = tk.Entry(self, justify="right")
        number_view.configure(state="readonly")
        return number_view

    def make_combobox(self):
        combobox = ttk.Combobox(self, state="readonly")
        combobox["values"] = op.special
        return combobox

    def make_menubar(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        menubar.add_cascade(
            label="History",
            command=self.create_new_windows
        )

    def create_new_windows(self, *args):
        # Create secondary (or popup) window.
        secondary_window = tk.Toplevel()
        secondary_window.title("Secondary Window")
        secondary_window.config(width=300, height=200)
        self.new_window_canvas, self.new_window_frame = self.make_new_chooser_bars(
            secondary_window)

    def make_new_chooser_bars(self, new_window):
        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox(
                "all"), width=200, height=200)
        canvas = tk.Canvas(new_window)
        frame = tk.Frame(canvas)
        frame.pack(expand=True, fill="x")
        myscrollbar = tk.Scrollbar(
            new_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)
        myscrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="x", expand=True)
        canvas.create_window((0, 0), window=frame, anchor='nw')
        frame.bind("<Configure>", myfunction)
        for i in self.history.history:
            button = tk.Button(frame, text=f"{i.display()} = {Evaluator().evaluate(
                i).display()}", command=lambda i=i: self.choose_history(i, new_window))
            button.pack(expand=True, side="top", fill="x")
        return canvas, frame

    def choose_history(self, arg: ExpressionHandler, windows:tk.Toplevel):
        self.expression = arg
        self.write_text(self.expression)
        windows.destroy()

    def history_button_handler(self, event, *args):
        self.expression = event["text"]
        self.write_text(self.expression)

    def init_components(self):
        options = {'font': ('Consolas', 14)}
        self.menu = self.make_menubar()
        self.number_view = self.make_textfield()
        self.combobox = self.make_combobox()
        self.buttomframe = tk.Frame(self)
        self.keypad_frame = self.make_keypad()
        self.operation_frame = self.make_operator_pad()
        self.number_view.pack(expand=True, fill=tk.BOTH, side="top")
        self.number_view.configure(options)
        self.combobox.pack(expand=True, fill=tk.BOTH, side="top")
        self.buttomframe.pack(expand=True, fill=tk.BOTH, side="top")
        self.keypad_frame.pack(expand=True, fill=tk.BOTH,
                               side="left", in_=self.buttomframe)
        self.operation_frame.pack(
            expand=True, fill=tk.BOTH, side="right", in_=self.buttomframe)
        self.keypad_frame.bind(self.bind_keyframe)
        self.operation_frame.bind(self.bind_keyframe)
        self.combobox.bind("<<ComboboxSelected>>", self.chooser_handler)

    def write_text(self, text: str, color: str = "black"):
        self.number_view.configure(fg="black")
        self.number_view.configure(state="normal")
        self.number_view.delete(0, tk.END)
        self.number_view.insert(0, text)
        self.number_view.configure(fg=color)
        self.number_view.configure(state="readonly")

    def bind_keyframe(self, event, *args):
        if event.widget["text"] == "DEL":
            self.expression.delete()
            self.write_text(self.expression.display())
            return
        if self.expression.add(event.widget["text"]):
            try:
                self.write_text(Evaluator().evaluate(
                    self.expression).display())
                self.history.add_history(copy.deepcopy(self.expression))
            except:
                self.write_text(self.expression.display(), 'red')
                winsound.MessageBeep()
            self.expression.clear()
        else:
            self.write_text(self.expression.display())

    def chooser_handler(self, *args):
        _input = self.combobox.get()
        self.expression.add(_input)
        self.number_view.delete(0, tk.END)
        self.write_text(self.expression.display())

    def run(self):
        self.init_components()
        self.mainloop()


if __name__ == "__main__":
    a = Calculator_UI()
    a.run()
