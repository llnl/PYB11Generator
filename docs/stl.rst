.. _stl:

==============
STL containers
==============

In many cases STL containers (such as ``vector``, ``deque``, ``map``, etc.) can be used transparently with pybind11: python lists will automatically convert to ``std::vector`` and vice versa for example with no extra work or notation needed.  The main caveat to this convenience, however, is that this is accomplished by copying the data in the container, which has two potential drawbacks: for large containers this may not be practical; second, any attempt to change data on either the C++ or Python side will be lost due to the fact you would be operating on a copy.  Even if your function/method specification is passing STL containers by reference, this silent copying will make modifying them across the Python/C++ interface impossible without further work.

If you need to pass an STL container without all this magic copying, it becomes necessary to directly bind such containers and define the behavior you want.  PYB11Generator provides some interfaces to pybind11's machinery for such bindings, but it is essential to first read and understand what `pybind11 is doing for STL types <https://pybind11.readthedocs.io/en/stable/advanced/cast/stl.html#stl-containers>`_.

PYB11Generator currently only provides Python convenience methods for handling two STL containers: ``std::vector`` via :func:`PYB11_bind_vector`, and ``std::map`` with :func:`PYB11_bind_map`.  It is possible to use the pybind11 semantics directly in C++ in combination with PYB11Generator to handle cases beyond ``std::vector`` and ``std::map`` of course, it simply involves using the `pybind11 C++ interface <https://pybind11.readthedocs.io/en/stable/advanced/cast/stl.html#stl-containers>`_ directly.

std::vector
===========

Suppose we want to bind ``std::vector<int>`` and ``std::vector<Aclass>`` in our module such that they will be modifiable through the interface (no copying).  We can accomplish this by adding two lines to our Python module definition::

  vector_of_int = PYB11_bind_vector("int", opaque=True)
  vector_of_Aclass = PYB11_bind_vector("Aclass", opaque=True)

When we import the resulting compiled module it will now include the types ``vector_of_int`` and ``vector_of_Aclass`` explicitly, and we need to deal in those types rather than the more convenient Python lists for arguments of those types.  The ``opaque`` argument here is what makes pybind11 treat these vector's as mutable references through the Python/C++ interface.  We also have the option of making these bindings local to the module or global: see :func:`PYB11_bind_vector` for the full description.

std::map
========

Making ``std::map`` instances mutable through the Python/C++ interface (opaque as described in pybind11 terms) is similar to our treatment of ``std::vector``.  If in our module we need to use ``std::map<std::string, Aclass>`` as an opaque argument we simply add a line::

  map_of_int_to_Aclass = PYB11_bind_map("int", "Aclass", opaque=True)

Just as in our prior ``std::vector`` examples, our module will now include a type ``map_of_int_to_Aclass`` which we can use explicitly to pass this container between Python and C++ mutably.

Shared ``type_caster`` definitions
==================================

Projects with multiple binding translation units can select one authoritative
C++ header by defining the compiler macro ``PYB11_SHARED_TYPE_CASTER_HEADER``
to a quoted include path. For example, a CMake target can use::

  target_compile_definitions(MyBindings PRIVATE
    "PYB11_SHARED_TYPE_CASTER_HEADER=\"MyTypeCasters.hh\"")

Every generated source includes its generated module header first. That header
includes the selected shared header after pybind11's headers (including
``stl.h``), but before user includes, preambles, trampolines, or binding code.
When selected, the generated ``PYB11opaque`` and ``opaque=True`` specialization
definitions are excluded with a preprocessor guard. STL class registrations are
still generated normally. Without this macro, the existing local declarations
remain active.

The shared header must provide all opaque declarations required by the project,
including types registered in other modules, and any custom ``type_caster``
definitions.
Use the same policy for handwritten C++ code that performs Python conversions.
Declaring a container opaque everywhere disables its automatic STL sequence
conversion; preserving list inputs or outputs requires separate API design.

Vector registration hook
========================

A project header may define the object-like macro ``PYB11_VECTOR_BINDING_HOOK``
to the qualified name of a function template taking one vector type and no
function arguments. Immediately after each generated ``py::bind_vector<Vector>``
call, the generator emits::

  #ifdef PYB11_VECTOR_BINDING_HOOK
    PYB11_VECTOR_BINDING_HOOK<Vector>();
  #endif

For example, the shared header can define this helper after its opaque
declarations::

  namespace MyBindings {
  template<typename Vector>
  inline void registerListConversion() {
    pybind11::implicitly_convertible<pybind11::list, Vector>();
  }
  }
  #define PYB11_VECTOR_BINDING_HOOK ::MyBindings::registerListConversion

The helper runs during module initialization after the vector's Python class
exists. Each vector registration invokes it once; header inclusion alone does
not execute it. Without the macro, no additional runtime behavior is generated.
The hook does not apply to ``bind_map``.

This example registers Python lists (including list subclasses) as implicit
inputs via the vector class's existing iterable constructor. It does not register
tuples, generators, dictionaries, or other iterable objects as implicit inputs.
Bound-vector inputs keep their existing conversion path. Converting a list uses
temporary vector storage and does not propagate mutations back to that list.
Normal pybind11 overload and conversion rules, including ``noconvert()``, apply.

Implicit input conversion does not restore list-valued results or property
snapshots. Nested conversion, pointer lifetimes, and calls through Python virtual
overrides must be validated for the project's types and pybind11 version.
