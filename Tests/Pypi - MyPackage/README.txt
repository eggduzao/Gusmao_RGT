Test Package named MyPackage
===========================

Package to do weird math stuff.

License information
-------------------

U can use whethever u want.

Build instructions
==================

Dude, will be very hard.

Testing some stuff
-------------------

I dunno what im doing here.

More specifically, the following systems are not supported any
longer:
- SunOS 4
- DYNIX
- dgux
- Minix
- NeXT
- Irix 4 and --with-sgi-dl
- Linux 1
- Systems defining __d6_pthread_create (configure.in)
- Systems defining PY_PTHREAD_D4, PY_PTHREAD_D6,
  or PY_PTHREAD_D7 in thread_pthread.h
- Systems using --with-dl-dld
- Systems using --without-universal-newlines
- MacOS 9
- Systems using --with-wctype-functions
- Win9x, WinME

64-bit platforms: The modules audioop, and imageop don't work.
        The setup.py script disables them on 64-bit installations.
        Don't try to enable them in the Modules/Setup file.  They
        contain code that is quite wordsize sensitive.  (If you have a
        fix, let us know!)

Solaris: When using Sun's C compiler with threads, at least on Solaris
        2.5.1, you need to add the "-mt" compiler option (the simplest
        way is probably to specify the compiler with this option as
        the "CC" environment variable when running the configure
        script).

Compiler switches for threads
.............................

Hay.

--Eduardo (home page: http://www.ihavenowebpagewatsoever.com)

