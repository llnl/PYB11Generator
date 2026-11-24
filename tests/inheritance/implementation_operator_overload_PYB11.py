from PYB11Generator import *

PYB11preamble = """
class OperatorBase {
public:
  bool operator==(const OperatorBase& rhs) const { return this == &rhs; }
};

class OperatorDerived: public OperatorBase {
};
"""


class OperatorBase:

    def pyinit(self):
        "Default OperatorBase()"

    def __eq__(self):
        "Compare OperatorBase instances"


class OperatorDerived(OperatorBase):

    def pyinit(self):
        "Default OperatorDerived()"

    @PYB11implementation("[](const OperatorDerived& self, const OperatorDerived& rhs) { return static_cast<const OperatorBase&>(self) == static_cast<const OperatorBase&>(rhs); }")
    def __eq__(self, rhs="const OperatorDerived&"):
        "Compare OperatorDerived instances using an explicit implementation"
        return "bool"
