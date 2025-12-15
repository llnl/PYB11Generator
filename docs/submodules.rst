.. _submodules:

==========
Submodules
==========

pybind11 supports the idea of specifying C++ bindings in submodules of other pybind11 modules as described in the `pybind11 docs <https://pybind11.readthedocs.io/en/stable/reference.html#_CPPv4N7module_13def_submoduleEPKcPKc>`_.  PYB11Generator works on a module by module basis (assuming you have a base ``*.py`` file describing what should be in the module), so supporting submodules requires telling PYB11Generator whether to treat such a module file as a submodule, and independently whether this module will in turn have any submodules.  Both of these tasks are handled by passing arguments to the invocation of the :ref:`PYB11generateModule function <PYB11-functions>`.  PYB11Generator's CMake rule ``PYB11Generator_add_module`` (documented in :ref:`PYB11Cmake`) provides simplifed support for creating and using submodules via the optional keywords ``IS_SUBMODULE`` and ``SUBMODULES``. 

As an example, suppose we want have two submodules ``Asub`` and ``Bsub`` of module ``my_module``:

::

   my_module
   |
   |-- Asub
   |-- Bsub

We can write three Python PYB11Generator module files for binding each of these modules as normal.

``my_module_PYB11.py``::

  from PYB11Generator import *

  """A dummy main module that has a couple of submodules"""

``Asub_PYB11.py``::

  from PYB11Generator import *

  PYB11includes = ['"A.hh"']

  class A:

      def pyinit(self):
          "Default constructor"

      def func(self, x="int"):
          "A::func"
          return "int"

``Bsub_PYB11.py``::

  from PYB11Generator import *

  PYB11includes = ['"B.hh"']

  class B:

      def pyinit(self):
          "Default constructor"

      def func(self, x="int"):
          "B::func"
          return "int"

Now we can create the module ``my_module`` with its submodules ``Asub`` and ``Bsub`` by creating three CMake targets::

  PYB11Generator_add_module(my_module
    SUBMODULES Asub Bsub
    DEPENDS Asub Bsub)

  PYB11Generator_add_module(Asub
    IS_SUBMODULE ON)

  PYB11Generator_add_module(Bsub
    IS_SUBMODULE ON)

Note that our only new requirements are that we need to specify to the rule building ``my_module`` that it has two submodules, while for both ``Asub`` and ``Bsub`` we need to flip on the ``IS_SUBMODULE`` flag to treat them as submodules. At compilation time this results in ``Asub`` and ``Bsub`` being built as static libraries which are linked to the final dynamic module ``my_module``.
