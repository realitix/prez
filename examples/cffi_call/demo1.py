from cffi import FFI

ffi = FFI()

ffi.cdef('int printf(const char *format, ...);')
C = ffi.dlopen(None)

arg = ffi.new("char[]", b'world')

import ipdb; ipdb.set_trace()

#C.printf(b"hi there, %d.\n", arg)
