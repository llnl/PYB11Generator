.. _PYB11submodules:

===================
Defining submodules
===================

pybind11 supports the idea of specifying C++ bindings in submodules of other pybind11 modules as described in the `pybind11 docs <https://pybind11.readthedocs.io/en/stable/reference.html#_CPPv4N7module_13def_submoduleEPKcPKc>`_.  PYB11Generator works on a module by module basis (assuming you have a base ``*.py`` file describing what should be in the module), so supporting submodules requires telling PYB11Generator whether to treat such a module file as a submodule, and independently whether this module will in turn have any submodules.  Both of these tasks are handled by passing arguments to the invocation of the :ref:`PYB11generateModule function <PYB11-functions>`.
