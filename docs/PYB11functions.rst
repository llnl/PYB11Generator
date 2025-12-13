.. _PYB11-functions:

PYB11 special functions and classes
===================================

This section describes the special functions and classes defined in PYB11Generator for use in createing python bindings.  Note we use the convention that PYB11 internals always start with the ``PYB11`` prefix.

.. #############################################################################
.. py:function:: PYB11generateModule(pymodule[, modname=None, filename=None, multiple_files=False, generatedfiles=None, default_holder_type=None, is_submodule=False, submodules=[], dry_run=False])

  Inspect the function and class definitions in ``pymodule``, and write a C++ file containing pybind11 statements to bind those interfaces.

  :param pymodule: the module to be introspected for the interface

  :param modname: optionally specify a different name for the generated Python module to be imported under.  Defaults ``None`` results in `<pymodule>``.

  :param filename: a file name for the generated C++ file.  If specified, the output is written to the given name, otherwise output will be written to ``<pymodule>.cc``

  :param multiple_files: optionally create multiple pybind11 source files to compile rather than a single monolithic output file

  :param generatedfiles: output filename to hold list of generatted pybind11 files for compilation (default ``None`` results in ``<pymodname>_PYB11_generated_files``)

  :param default_holder_type: optionally override the holder type for new objects (default ``None`` results in ``py::smart_holder``, see `pybind11 docs <https://pybind11.readthedocs.io/en/stable/advanced/smart_ptrs.html>`_).

  :param is_submodule: optionally specify this module should be treated and bound as a submodule (default ``False``, see :ref:`submodules`_.)

  :param submodules: optionally specify a set of submodules of this module (default ``[]``, see `PYB11submodules`_.)

  :param dry_run: optional flag to do a dry run only; if ``True``, no pybind11 code/files are written, but the names of such files are written to ``generatedfiles``. Default ``False``.

.. #############################################################################
.. py:function:: PYB11TemplateFunction(func_template, template_parameters[, cppname = None, pyname = None, docext = ""])

  Instantiate a function template (``func_template``) that was decorated by ``@PYB11template``.

  :param func_template: The template function definition

  :param template_parameters: A single string (for a single template parameter function) or tuple of strings (for multiple template parameters), one for each template parameter defined by ``@PYB11template`` on ``func_template``.

  :param cppname: The name of the C++ function template, if different from that used for ``func_template``.

  :param pyname: The name of the resulting Python function; defaults to the name of the instance created for this invocation of ``PYB11TemplateFunction``.

  :param docext: An optional string extension to be applied to the docstring associated with ``func_template``.

.. #############################################################################
.. py:function:: PYB11attr([value=None, pyname=None])

  Create an attribute in a module; corresponds to the pybind11 command ``attr``.

  :param value: define the C++ name this variable corresponds to.  If ``None``, defaults to the name of the local python variable.

  :param pyname: define the generated python attribte name.  If ``None``, defaults to the name of the local python variable.

.. #############################################################################
.. py:function:: PYB11readwrite([static=False, pyname=None, cppname=None, returnpolicy=None, doc=None])

  Define a readwrite class attribute; corresponds to pybind11 ``def_readwrite``.

  :param static: If ``True``, specifies the bound attribute is static.

  :param pyname: Optionally specify the Python name of the attribute.  If ``None``, assumes the Python name is the name of Python variable instance.

  :param cppname: Optionally specify the C++ name of the attribute.  If ``None``, assumes the C++ name is the name of Python variable instance.

  :param returnpolicy: Specify a special return policy for how to handle the memory of the return value.  Read pybind11 documentation at :ref:`pybind11:return_value_policies`.

  :param doc: Optionally give a docstring.

.. #############################################################################
.. py:function:: PYB11readonly([static=False, pyname=None, cppname=None, returnpolicy=None, doc=None])

  Define a readonly class attribute; corresponds to pybind11 ``def_readonly``.

  :param static: If ``True``, specifies the bound attribute is static.

  :param pyname: Optionally specify the Python name of the attribute.  If ``None``, assumes the Python name is the name of Python variable instance.

  :param cppname: Optionally specify the C++ name of the attribute.  If ``None``, assumes the C++ name is the name of Python variable instance.

  :param returnpolicy: Specify a special return policy for how to handle the memory of the return value.  Read pybind11 documentation at :ref:`pybind11:return_value_policies`.

  :param doc: Optionally give a docstring.

.. #############################################################################
.. py:function:: PYB11property([returnType = None, getter = None, setter = None, doc = None, getterraw = None, setterraw = None,  getterconst = True, setterconst = False, static = None, constexpr = False, returnpolicy = None])
                 
   Helper to setup a class property.

   :param returnType: Specify the C++ type of the property

   :param getter: A string with the name of the getter method.  If ``None``, assumes the getter C++ specification looks like ``returnType (klass:::param)() const``.

   :param setter: A string with the name of the setter method.  If ``None``, assumes the setter C++ specification looks like ``void (klass:::param)(returnType& val)``.

   :param doc: Specify a document string for the property.

   :param getterraw: Optionally specify raw coding for the getter method.  Generally this is used to insert a C++ lambda function.  Only one of ``getter`` or ``getterraw`` may be specified.

   :param setterraw: Optionally specify raw coding for the setter method.  Generally this is used to insert a C++ lambda function.  Only one of ``setter`` or ``setterraw`` may be specified.

   :param getterconst: Specify if ``getter`` is a const method.

   :param setterconst: Specify if ``setter`` is a const method.

   :param static: If ``True``, make this a static property.

   :param constexpr: Set to ``True`` if the property is a C++ constexpr expression.

   :param returnpolicy: Specify a special return policy for how to handle the memory of the return value.  Read pybind11 documentation at :ref:`pybind11:return_value_policies`.

.. #############################################################################
.. py:function:: PYB11TemplateMethod(func_template, template_parameters[, cppname = None, pyname = None, docext = ""])

  Instantiate a class method (``func_template``) that was decorated by ``@PYB11template``.

  :param func_template: The template method definition

  :param template_parameters: A single string (for a single template parameter method) or tuple of strings (for multiple template parameters), one for each template parameter defined by ``@PYB11template`` on ``func_template``.

  :param cppname: The name of the C++ method template, if different from that used for ``func_template``.

  :param pyname: The name of the resulting Python method; defaults to the name of the instance created for this invocation of ``PYB11TemplateMethod``.

  :param docext: An optional string extension to be applied to the docstring associated with ``func_template``.

.. #############################################################################
.. py:function:: PYB11TemplateClass(klass_template, template_parameters[, cppname = None, pyname = None, docext = ""])

  Instantiate a class template (``klass_template``) that was decorated by ``@PYB11template``.

  :param klass_template: The template class definition

  :param template_parameters: A single string (for a single template parameter class) or tuple of strings (for multiple template parameters), one for each template parameter defined by ``@PYB11template`` on ``klass_template``.

  :param cppname: The name of the C++ class template, if different from that used for ``klass_template``.

  :param pyname: The name of the resulting Python class; defaults to the name of the instance created for this invocation of ``PYB11TemplateClass``.

  :param docext: An optional string extension to be applied to the docstring associated with ``klass_template``.

.. #############################################################################
.. py:function:: PYB11enum(values[, name=None, namespace="", cppname=None, export_values=False, native_type="enum.Enum", doc=None])

   Declare a C++ enum for wrapping in pybind11 -- see `pybind11 docs <https://pybind11.readthedocs.io/en/stable/classes.html#enumerations-and-internal-types>`_.

   :param values: a tuple of strings listing the possible values for the enum

   :param name: set the name of enum type in Python.  ``None`` defaults to the name of the instance given this enum declaration instance.

   :param namespace: an optional C++ namespace the enum lives in.

   :param cppname: the C++ name of the enum.  ``None`` defaults to the same as ``name``.

   :param export_values: if ``True``, causes the enum values to be exported into the enclosing scope (like an old-style C enum).

   :param native_type: the Python native enum type to use as the base. Curent possibilites are ``enum.Enum``, ``enum.IntEnum``, ``enum.Flag``, and ``enum.IntFlat`` (default ``enum.IntEnum``).  See the pybind11 documentation on ``py::native_enum`` for more information.

   :param doc: an optional document string.

.. #############################################################################
.. py:function:: PYB11_bind_vector(element[, opaque=False, local=None])

   Bind an STL::vector explicitly.  This is essentially a thin wrapper around the pybind11 ``py::bind_vector`` function (see :ref:`pybind11:stl_bind`).

   :param element: the C++ element type of the ``std::vector``

   :param opaque: if ``True``, causes the bound STL vector to be "opaque", so elements can be changed in place rather than accessed as copies.  See :ref:`pybind11:stl_bind`.

   :param local: determines whether the binding of the STL vector should be module local or not; once again, see :ref:`pybind11:stl_bind`.

.. #############################################################################
.. py:function:: PYB11_bind_map(key, value[, opaque=False, local=None])

   Bind an STL::map explicitly.  This is a thin wrapper around the pybind11 ``py::bind_map`` function (see :ref:`pybind11:stl_bind`).

   :param key: the C++ key type

   :param value: the C++ value type

   :param opaque: if ``True``, causes the bound STL map to be "opaque", so elements can be changed in place rather than accessed as copies.  See :ref:`pybind11:stl_bind`.

   :param local: determines whether the binding of the STL map should be module local or not; once again, see :ref:`pybind11:stl_bind`.

.. #############################################################################
.. py:function:: PYB11_inject(fromcls, tocls[, virtual=None, pure_virtual=None])

   Convenience method to inject methods from class ``fromcls`` into ``tocls``.  This is intended as a utility to help avoiding writing redundant methods common to many classes over and over again.  Instead a convenience class can be defined containing the shared methods (typically screened from generation by ``@PYB11ignore``), and then ``PYB11_inject`` is used to copy those methods into the target classes.

   :param fromcls: Python class with methods we want to copy from.

   :param tocls: Python class we're copying methods to.

   :param virtual: if ``True``, force all methods we're copying to be treated as virtual.

   :param pure_virtual: if ``True``, force all methods we're copying to be treated as pure virtual.
