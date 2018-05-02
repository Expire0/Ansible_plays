#include <stdio.h>
#include <time.h>
#include <stdlib.h>

/* Reference http://en.cppreference.com/w/c/chrono/asctime 
https://www-s.acm.illinois.edu/webmonkeys/book/c_guide/1.2.html#strings
*/

int main(){

        char test[10] = "dipps";
        time_t result = time(NULL);

        char os_c = system("hwclock --show");
        printf("%s\n", test);
        printf("UTC:%s", asctime(localtime(&result)));  /* print the current OS time. */
        printf("%s" ,  os_c);



        if (os_c > asctime(localtime(&result)))
                printf("true");
        else
                printf("false");
}



/* 
https://github.com/balabit-deps/balabit-os-6-util-linux/blob/18ecbf6e3c975d642b7c7282fe447ce7a8313884/sys-utils/rtcwake.c



balabit-deps/balabit-os-6-util-linux – rtcwake.c
Showing the top two matches Last indexed on Mar 6
84		enum clock_modes clock_mode;	/* hwclock timezone */
85		time_t sys_time;		/* system time */
86		time_t rtc_time;		/* hardware time */
…	
176		/* Convert rtc_time to normal arithmetic-friendly form,
177		 * updating tm.tm_wday as used by asctime().
178		 */
179		tm.tm_sec = rtc.tm_sec;

*/
