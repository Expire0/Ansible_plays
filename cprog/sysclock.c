#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <linux/rtc.h>




int main() {

int hour[50], htime , n=0 , i;

FILE *ls = popen("/usr/sbin/hwclock --verbose | grep read", "r");
	char buf[256];
        while (fgets(buf, sizeof(buf), ls) != 0) {
        //printf("System Time : %s", buf);
            for (i=0; i < 52; i++) {
       // printf("%c", buf[i]);

                 hour[n] = buf[i];
                  n = n + 1;
    }
}


pclose(ls);

//for testing only.
printf("Testing Sysclock with Char %c%c%c%c\n" , hour[42],hour[43],hour[45],hour[46]);

//converting char to int
int r = hour[42] - '0';
int x = hour[43] - '0';
int y = hour[45] - '0';
int z = hour[46] - '0';

//putting the int together
htime= r * 1000 + x * 100 + y * 10 + z;

printf("%i\n", htime);

//start comparision to os clock

}
