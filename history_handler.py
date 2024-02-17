from expression_handler import ExpressionHandler

class History:
    def __init__(self) -> None:
        self.__history = []
        
    def add_history(self, exprsn:ExpressionHandler) -> None:
        self.__history.append(exprsn)
        
    @property
    def history(self):
        return self.__history
    