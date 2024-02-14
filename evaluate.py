from expression_handler import ExpressionHandler

class Evaluator:
    def __init__(self) -> None:
        pass
    
    def evaluate(self, expr:ExpressionHandler) -> ExpressionHandler:
        ex = expr.expression
        ex.replace("^","**")
        result = ''
        try:
            result = eval(ex)
        except NameError:
            raise ValueError
        a = ExpressionHandler()
        a.expression = str(result)
        return a
    
    