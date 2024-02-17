class Operants:
    """_summary_ : consists of setting of keys that you will need in the calculator.
    """
    def __init__(self) -> None:
        """_summary_
        __special is the special operators that will appear in the listbox
        __operational is the operational operators that will appear at the side keypad
        __numbers is the numbers that will appear ath the main keypad
        __replace is a dictionary of operation that needs to be change in order to match
            with python's operators' name
        """
        self.__special = ["log", "sqrt"]
        self.__operational = list("+-*/^=")
        self.__numbers = list('()π789456123 0.')
        self.__replace = {"^": "**", "π":"pi"}
        
    @property
    def special(self):
        return self.__special
    
    @property
    def operational(self):
        return self.__operational
    
    @property
    def numbers(self):
        return self.__numbers
    
    @property
    def replace(self):
        return self.__replace
    