from PYB11Generator import *

PYB11preamble = """
#include <utility>
#include <string>
#include <iostream>
#include <cstdio>

class A {
public:
  A()                   { printf("A::A()\\n"); }    
  virtual ~A()          { printf("A::~A()\\n"); }   
  virtual std::pair<int, int> int_int_method() = 0;
  virtual std::pair<double, std::string> double_string_method() = 0;
};

void
func(A& a) {
  std::cerr << "func.int_int       : " << a.int_int_method().first << " " << a.int_int_method().second << " "  << std::endl;
  std::cerr << "func.double_string : " << a.double_string_method().first << " " << a.double_string_method().second << std::endl;
}
"""

#...............................................................................
class A:

    def pyinit(self):
        "Default A()"

    @PYB11pure_virtual
    def int_int_method(self):
        return "std::pair<int, int>"

    @PYB11pure_virtual
    def double_string_method(self):
        return "std::pair<double, std::string>"

def func(a = "A&"):
    return "void"
