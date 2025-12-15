PYB11Generator_add_module(submodules
  SUBMODULES Asub Bsub
  DEPENDS Asub Bsub
  INSTALL ${CMAKE_INSTALL_PREFIX}/tests/submodule)

PYB11Generator_add_module(Asub
  IS_SUBMODULE ON
  INSTALL ${CMAKE_INSTALL_PREFIX}/tests/submodule)

PYB11Generator_add_module(Bsub
  IS_SUBMODULE ON
  INSTALL ${CMAKE_INSTALL_PREFIX}/tests/submodule)
