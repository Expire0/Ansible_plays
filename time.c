#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

/* Reference http://en.cppreference.com/w/c/chrono/asctime 
 * https://www-s.acm.illinois.edu/webmonkeys/book/c_guide/1.2.html#strings
 * https://blog.udemy.com/c-string-to-int/  
 * */
int main() {
	FILE *ls = popen("/usr/sbin/hwclock --show | awk '{print $5 }' | egrep -o \"[0-6][0-9]:[0-6][0-9]:\" | sed \'s/://g\' ", "r");
	char buf[256];
	while (fgets(buf, sizeof(buf), ls) != 0) {
    printf("System Time : %s", buf);

}
pclose(ls);
    // char os_c = system("date +%I:%M:%S");

      // check system time 
      FILE *os_time = popen("date +%I%M", "r");
        char buf1[256];
        while (fgets(buf1, sizeof(buf1), os_time) != 0) {
    printf("OS Time : %s", buf1);

}
pclose(os_time);
int a = atoi(buf);
int b = atoi(buf1);

if (b < a){
        int min = a - b ;
	//printf("The system clock is behind %d %d\n" , a, b);
        printf("The system clock is behind by %d minutes :\n" , min); 
}
else {
	printf("All good ");
}



}
