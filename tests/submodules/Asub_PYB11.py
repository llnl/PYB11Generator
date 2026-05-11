from PYB11Generator import *

PYB11includes = ['"A.hh"']

class A:

    def pyinit(self):
        "Default constructor"

    @PYB11virtual
    def func(self, x="int"):
        "A::func"
        return "int"

    @PYB11pure_virtual
    def double_string_method(self):
        return "std::pair<double, std::string>"

def Amod_func(a = "A&"):
    return "void"
