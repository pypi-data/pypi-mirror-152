#pragma once

#include "python_headers.h"

inline PyCFunction castPyCFunctionWithKeywords(PyCFunctionWithKeywords func) {
  return (PyCFunction)(void(*)(void))func;
}
