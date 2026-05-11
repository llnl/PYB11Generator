#ifndef submodules_A
#define submodules_A

#include <utility>
#include <string>
#include <iostream>

struct A {
   A()                          { printf("A::A()\n"); }
  ~A()                          { printf("A::~A()\n"); }
  virtual int func(const int x) { printf("A::func(%d)\n", x); return x; }
  virtual std::pair<double, std::string> double_string_method() = 0;
};

inline
void Amod_func(A& a) {
  const auto stuff = a.double_string_method();
  std::cerr << "Amod_func(" << &a << ") : " << stuff.first << " " << stuff.second << std::endl;
}

#endif
