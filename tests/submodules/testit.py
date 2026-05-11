import submodules

class C(submodules.Asub.A):

    def double_string_method(self):
        print("C.double_string_method")
        return (4.0, "Trogdor!")

c = C()
print(c)
print(c.double_string_method())

submodules.Asub.Amod_func(c)
