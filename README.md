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
