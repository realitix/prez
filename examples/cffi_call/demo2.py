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
