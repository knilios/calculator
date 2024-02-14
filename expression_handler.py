class ExpressionHandler:
    def __init__(self) -> None:
        self.expression = "0"
    def add(self, char):
        if char == " " or char == "":
            self.expression = "0"
        if char == "=":
            return True
        if self.expression == "0":
            self.expression = char
        else:
            self.expression += char
        return False
    def clear(self):
        self.expression = "0"
        