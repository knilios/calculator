from expression_handler import ExpressionHandler

class History:
    def __init__(self) -> None:
        self.__history = []
        
    def add_history(self, exprsn:ExpressionHandler) -> None:
        self.__history.append(exprsn)
        
    @property
    def history(self):
        return self.__history
    
    def __str__(self) -> str:
        return self.__history
    
    def __repr__(self) -> str:
        return self.__history
    
    
if __name__ == "__main__":
    a = History()
    e = ExpressionHandler()
    e.add("34+33")
    f = ExpressionHandler()
    f.add("9-8")
    a.add_history(e)
    print(list(map(lambda x: x.display(), a.history)))
    a.add_history(f)
    print(list(map(lambda x: x.display(), a.history)))
    