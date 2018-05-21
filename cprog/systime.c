#include <stdio.h>
#include <stdlib.h>

//system time in UTC

int main() {

FILE *os_time = popen("date -u +%H%M", "r");
char buf1[256];
while (fgets(buf1, sizeof(buf1), os_time) != 0) {
    printf("OS Time : %s", buf1);

}
pclose(os_time);



}
