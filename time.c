#include <stdio.h>
#include <time.h>
#include <stdlib.h>

/* Reference http://en.cppreference.com/w/c/chrono/asctime  */

int main(){

        char test[10] = "dipps";
        time_t result = time(NULL);

        char os_c = system("hwclock --show");
        printf("%s\n", test);
        printf("UTC:%s", asctime(localtime(&result)));  /* print the current OS time. */
        printf("%s" ,  os_c);
}
