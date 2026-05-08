from pair_return_type import *

class B(A):
    def int_int_method(self):
        print("B.int_int_method")
        return (1, 2)

    def double_string_method(self):
        print("B.double_string_method")
        return (4.0, "Trogdor!")


b = B()
print(b)
print(b.int_int_method())
print(b.double_string_method())

func(b)
