# Yellow Playground

Hello, fellows!

I hope that a linux assembly playground will be very helpful for you.

Make sure you have [gef](https://github.com/hugsy/gef#install) installed in your gdb, along with its [suggested libraries](https://github.com/hugsy/gef#dependencies), in specific "keystone".

Clone the repo:

```shell
git clone https://github.com/ThinerDAS/asm-playground.git
cd asm-playground
```

Then, type in shell:

```shell
gcc main.c -o main
```

and use gdb to open it:

```shell
gdb main
```

and inside gdb, type:

```shell
source play.py
play
```

Homework:

* Try out normal instructions like `mov`, `add`, etc. You will need to become familiar to some debugging commands in gdb, including `stepi`(`si`), `continue`(`c`), `break`(`b`), etc.
* Try out instructions related to stack and `rip`, like `push`, `pop`, `jmp`, `call`, `ret`, `leave`, etc.
* Try a C function call. Find out the address of `printf` and call `printf("Hello, %dth challenger!\n", 100);`. Find the address of `malloc`, allocate a memory, `malloc(0x100);`, with assembly and put the memory address to `rdi`.
* Try a syscall. Do `sys_read(0, rsp, 100)` to populate the stack, and `sys_execve(rsp, 0, 0)` to execute your program.
* Reread the programs we have compiled using `gcc` up to this time, and compile some more programs. Point out the calling convention inside the assembly.
