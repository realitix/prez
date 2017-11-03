from cffi import FFI

ffi = FFI()

ffi.cdef('int printf(const char *format, ...);')
C = ffi.dlopen(None)

arg = ffi.new("char[]", b'amazing')

C.printf(b"cffi is %s\n", arg)
