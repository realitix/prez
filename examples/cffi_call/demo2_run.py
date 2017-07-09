from _demo2 import ffi, lib

# root name
p = lib.getpwuid(0)
print(ffi.string(p.pw_name))

# realitix uid
p = lib.getpwnam(b"realitix")
print(p.pw_uid)
