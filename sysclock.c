#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <linux/rtc.h>




int main() {

char hour[6];

int n=0;


FILE *ls = popen("/usr/sbin/hwclock -r", "r");
	char buf[256];
        while (fgets(buf, sizeof(buf), ls) != 0) {
        //printf("System Time : %s", buf);
            for (int i=11; i < 17; i++) {
       // printf("%c", buf[i]);
                 hour[n] = buf[i];
                  n = n + 1;
    }
}

pclose(ls);

printf("%c%c%c%c" , hour[0],hour[1],hour[3],hour[4]);

}
