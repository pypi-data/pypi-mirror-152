#pragma once
#include <math.h>
// workaround for Python 2 issue: https://bugs.python.org/issue17120
// NOTE: It looks like this affects Python 3 as well.
#pragma push_macro("_XOPEN_SOURCE")
#pragma push_macro("_POSIX_C_SOURCE")
#undef _XOPEN_SOURCE
#undef _POSIX_C_SOURCE

#if WIN32
// Debug builds under Windows link to the debug build of Python, which has extra assertions enabled.
// Pytorch in Windows fails those assertions, so we #undef _DEBUG before including the header.
#pragma push_macro("_DEBUG")
#undef _DEBUG
#endif
#include <Python.h>
#if WIN32
#pragma pop_macro("_DEBUG")
#endif
#include <structseq.h>

#pragma pop_macro("_XOPEN_SOURCE")
#pragma pop_macro("_POSIX_C_SOURCE")

#if PY_MAJOR_VERSION < 3
#error "Python 2 has reached end-of-life and is no longer supported by PyTorch."
#endif
