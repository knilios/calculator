from expression_handler import ExpressionHandler
from operants import Operants
from math import *

op = Operants()


class Evaluator:
    def __init__(self) -> None:
        pass

    def evaluate(self, expr: ExpressionHandler) -> ExpressionHandler:
        ex = expr.display()
        for i in op.replace:
            ex = ex.replace(str(i).strip(), str(op.replace[i]).strip())
        result = ''
        try:
            result = eval(ex)
        except NameError:
            raise ValueError
        a = ExpressionHandler()
        a.add(str(result))
        return a


if __name__ == "__main__":
    ex = ExpressionHandler()
    ex.add("12/12^3")
    ev = Evaluator()
    print(ev.evaluate(ex).display())
