from PYB11Generator import *

PYB11preamble = """

// A singleton class
class Asingleton {
public:
  static Asingleton& instance()       { static Asingleton theInstance; return theInstance; }
  void where_am_I()             const { printf("A instance at %p\\n", (void*) &Asingleton::instance()); }
private:
  Asingleton()                        { printf("Asingleton::Asingleton()\\n"); }
  ~Asingleton()                       { printf("Asingleton::~Asingleton()\\n"); }
};
"""

@PYB11singleton
class Asingleton:
    
    @PYB11static
    @PYB11returnpolicy("reference")
    def instance(self):
        return "Asingleton&"

    def where_am_I(self):
        return
