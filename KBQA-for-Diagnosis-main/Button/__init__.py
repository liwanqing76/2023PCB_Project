import IO
import config as conf


class Button(IO.IO):
    ESDprot=0
    filter=0


    # ------------------初始化的时候传入板子的参数----------------
    @conf.auto_type_checker
    def __init__(self,ESDprot:bool,filter:bool):
        super(Button,self).__init__(ESDprot,filter)
    # ---------------------------------------------------------

