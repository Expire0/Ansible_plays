#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <linux/rtc.h>




int main() {

FILE *ls = popen("/usr/sbin/hwclock -r", "r");
	char buf[256];
        while (fgets(buf, sizeof(buf), ls) != 0) {
        //printf("System Time : %s", buf);
    for (int i=3; i < 12 && i > 2; i++) {
        printf("%c", buf[i]);
    }
}

pclose(ls);

}
