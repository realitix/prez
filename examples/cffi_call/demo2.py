from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source("_demo2",
   r"""#include <sys/types.h>
       #include <pwd.h>
    """)

ffibuilder.cdef("""
    struct passwd {
        char *pw_name;
        char *pw_passwd;
        int pw_uid;
        ...;
    };
    struct passwd *getpwuid(int uid);
    struct passwd *getpwnam(const char *name);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)


# from _demo2 import ffi, lib

# root name
# p = lib.getpwuid(0)
# ffi.string(p.pw_name)

# realitix uid
# p = lib.getpwnam(b"realitix")
# p.pw_uid
