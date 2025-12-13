.. _submodules:

==========
Submodules
==========

pybind11 supports the idea of specifying C++ bindings in submodules of other pybind11 modules as described in the `pybind11 docs <https://pybind11.readthedocs.io/en/stable/reference.html#_CPPv4N7module_13def_submoduleEPKcPKc>`_.  PYB11Generator works on a module by module basis (assuming you have a base ``*.py`` file describing what should be in the module), so supporting submodules requires telling PYB11Generator whether to treat such a module file as a submodule, and independently whether this module will in turn have any submodules.  Both of these tasks are handled by passing arguments to the invocation of the :ref:`PYB11generateModule function <PYB11-functions>`.  PYB11Generator's CMake rule ``PYB11Generator_add_module`` (documented in :ref:`cmake`) provides simplifed support for creating and using submodules via the optional keywords ``IS_SUBMODULE`` and ``SUBMODULES``. 

As an example, suppose we want to have two submodules ``Asub`` and ``Bsub`` of module ``my_module``:

::

   my_module
   |
   |-- Asub
   |-- Bsub

We can write three normal module Python PYB11Generator files for binding each of these modules as normal.

``my_module_PYB11.py``::

  from PYB11Generator import *

  """A dummy main module that has a couple of submodules"""

``Asub_PYB11.py``::

  from PYB11Generator import *

  PYB11includes = ['"A.hh"']

  class A:

      def pyinit(self):
          "Default constructor"

      @PYB11virtual
      def func(self, x="int"):
          "A::func"
          return "int"

``Bsub_PYB11.py``::

  from PYB11Generator import *

  PYB11includes = ['"B.hh"']

  class B:

      def pyinit(self):
          "Default constructor"

      @PYB11virtual
      def func(self, x="int"):
          "B::func"
          return "int"
