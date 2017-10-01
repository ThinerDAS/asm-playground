def asm(s, addr=-1):
    # by default we assume that strings to assemble will be put at current $pc
    if addr == -1:
        addr = current_arch.pc
    return keystone_assemble(s, *get_keystone_arch(), raw=True, addr=addr)


def wm(addr, binary):
    return write_memory(addr, binary, len(binary))


class PlaygroundCommand(gdb.Command):
    """Wrapper."""

    _syntax_ = (
        "\tplayground [as|asm|assembly] [-a starting_address] assembly[;assembly;...;assembly]\n"
        "\tplayground [wm|writemem|write_memory] address data\n"
        "\tplayground [wb|writeb|write_binary] address data-in-hex\n"
        "\tplayground [p|patchi|patch_instruction]\n"
        "Example:\n"
        "\tplayground as add eax,4;syscall\n"
        "\tplayground as -a $pc+2 jmp 0x400500\n"
        "\tplayground wm 0x400600 \"Hello, world!\"\n"
        "\tplayground wb 0x400500 83c00a\n"
        "\tplayground p $pc sub rsp,0x10;mov edx,0;int 0x80\n")

    def __init__(self):
        super(PlaygroundCommand, self).__init__("playground", gdb.COMMAND_USER)

    def help(self):
        print('Usage:')
        print(self._syntax_.replace('playground', '\x1b[32mplayground\x1b[39m')
              .replace('\t', ' ' * 4))

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if not argv:
            self.help()
            return
        if argv[0] in ['as', 'asm', 'assembly']:
            # asm command, convert the assembly to binary
            addr = -1
            code = ""
            if argv[1] == '-a':
                # specify starting address, helpful for relative addressing
                addr = long(gdb.parse_and_eval(argv[2]))
                code = ' '.join(argv[3:])
            else:
                code = ' '.join(argv[1:])
            binary = asm(code, addr)
            print(''.join('\\x' + ('{:02x}'.format(int(i))) for i in binary))

            print(''.join(('{:02x}'.format(int(i))) for i in binary))
        elif argv[0] in [
                'w', 'wm', 'write', 'writem', 'writemem', 'write_memory'
        ]:
            # write memory
            addr = long(gdb.parse_and_eval(argv[1]))
            wm(addr, argv[2])

        elif argv[0] in ['wb', 'writeb', 'write_binary']:
            # write memory, binary
            addr = long(gdb.parse_and_eval(argv[1]))
            wm(addr, bytes.fromhex(argv[2]))

        elif argv[0] in ['p', 'patchi', 'patch_inst']:
            # write memory the assembled code
            addr = long(gdb.parse_and_eval(argv[1]))
            code = asm(' '.join(argv[2:]), addr)
            wm(addr, code)
        else:
            print("Unrecognized command in playground")
            self.help()
            return


PlaygroundCommand()
