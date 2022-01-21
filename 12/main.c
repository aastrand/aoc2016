#include <stdio.h>

int main(int argc, char **argv)
{
    int a = 1;
    int b = 1;
    int c = 1;
    int d = 26;

    d += 7;
    while (d != 0)
    {
        c = a;
        a += b;
        b = c;
        d--;
    }

    a += 11 * 19;

    printf("%d\n", a);

    return 0;
}