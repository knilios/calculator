import tkinter as tk
from tkinter import ttk
from commandpad import Commandpad
from keypad import Keypad
from expression_handler import ExpressionHandler
from evaluate import Evaluator
from operants import Operants

op = Operants()

class Calculator_UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator!")
        self.expression = ExpressionHandler()
        
    def make_keypad(self, keyname:list = op.numbers, columns:int = 3):
        return Keypad(self, keyname, columns)
        
    def make_operator_pad(self, keyname:list = op.operational):
        return Commandpad(self, keyname)
    
    def make_textfield(self):
        number_view = tk.Entry(self, justify="right")
        number_view.configure(state="readonly") # 
        return number_view
    
    def make_combobox(self):
        combobox = ttk.Combobox(self)
        combobox["values"] = op.special
        return combobox
        
    def init_components(self):
        options = {'font': ('Consolas', 14)}
        self.number_view = self.make_textfield()
        self.combobox = self.make_combobox()
        self.buttomframe = tk.Frame(self)
        self.keypad_frame = self.make_keypad()
        self.operation_frame = self.make_operator_pad()
        self.number_view.pack(expand=True, fill=tk.BOTH, side="top")
        self.number_view.configure(options)
        self.combobox.pack(expand=True, fill=tk.BOTH, side="top")
        self.buttomframe.pack(expand=True, fill=tk.BOTH, side="top")
        self.keypad_frame.pack(expand=True, fill=tk.BOTH, side="left", in_=self.buttomframe)
        self.operation_frame.pack(expand=True, fill=tk.BOTH, side="right", in_=self.buttomframe)
        self.keypad_frame.bind(self.bind_keyframe)
        self.operation_frame.bind(self.bind_keyframe)
        
    def bind_keyframe(self, event, *args):
        self.number_view.configure(fg="black")
        self.number_view.configure(state="normal")
        if self.expression.add(event.widget["text"]):
            try: 
                self.number_view.delete(0, tk.END)
                self.number_view.insert(0, Evaluator().evaluate(self.expression).display())
            except:
                self.number_view.delete(0, tk.END)
                self.number_view.insert(0, self.expression.display())
                self.number_view.configure(fg="red")
            self.expression.clear()
        else:
            self.number_view.delete(0, tk.END)
            self.number_view.insert(0, self.expression.display())
        self.number_view.configure(state="readonly")
    
    def run(self):
        self.init_components()
        self.mainloop()
        
        
if __name__ == "__main__":
    a = Calculator_UI()
    a.run()