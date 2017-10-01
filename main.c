int main()
{
    asm volatile (
        ".rept 0x800\n\t"
        "int3\n\t"
        ".endr"
    );
}
