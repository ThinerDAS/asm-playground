Hello, fellows!
I think that, a linux assembly playground will be very helpful for you.
Make sure you have "gef" installed in your gdb, along with its libraries, in specific "keystone". Then, type in shell:
    gcc main.c -o main
and use gdb to open it:
    gdb main
and inside gdb, type:
    source play.py
    play
