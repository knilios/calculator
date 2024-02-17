operator = list("+-*/^=")
special_operators = ["log", "sqrt"]
class ExpressionHandler:
    def __init__(self) -> None:
        self.expression = ["0"]
        
    def add(self, char:str) -> bool:
        if char == " " or char == "":
            self.expression = ["0"]
        if char == "=":
            return True
        if self.expression == ["0"]:
            if char in special_operators: 
                self.expression += [char]
            else:
                self.expression = [char]
        else:
            self.expression += [char]
        return False
    
    def clear(self) -> None:
        self.expression = ["0"]
    
    def display(self) -> str:
        _new_string = ""
        for i in range(len(self.expression)):
            if self.expression[i] in special_operators:
                if self.expression[i-1] in operator:
                    _new_string += self.expression[i] + "("
                else:
                    _new_string = self.expression[i] + "(" + _new_string + ")"
            else:
                _new_string += self.expression[i]
        return _new_string
    
    def delete(self):
        if self.expression == ["0"]:
            return
        self.expression = self.expression[:-1:]
        if self.expression == []:
            self.expression = ["0"]
        return
        
        
if __name__ == "__main__":
    a = ExpressionHandler()
    a.add("1")
    a.add("1")
    a.add("1")
    a.add("log")
    a.add('+')
    a.add("sqrt")
    a.add("2")
    a.add("5")
    a.add(")")
    print(a.display())
    a.delete()
    print(a.display())
    a.delete()
    print(a.display())
    a.delete()
    print(a.display())
    a.delete()
    print(a.display())
    a.delete()
    print(a.display())
    a.delete()
    print(a.display())
    a.delete()
    print(a.display())
    a.delete()
    print(a.display())
    a.delete()
    print(a.display())
    
    