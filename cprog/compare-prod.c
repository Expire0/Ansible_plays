#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <linux/rtc.h>


//check hardware clock and sys clock 
//check if ntpdate -d  will be a better fix command. then hwclock or date -s
int main() {

int hour[50], htime , stime, n=0 , i;

char clean1[100];


//clean existing temp file 
FILE *prep = popen("rm -rf /var/tmp/check_clock.txt", "r");


// check hardware clock and add stdout to array
// change verbose to debug for older systems
FILE *ls = popen("/usr/sbin/hwclock --debug | grep read", "r");
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
//printf("Testing Sysclock with Char %c%c%c%c\n" , hour[42],hour[43],hour[45],hour[46]);

//converting char to int
int r = hour[42] - '0';
int x = hour[43] - '0';
int y = hour[45] - '0';
int z = hour[46] - '0';

//putting the int together . printing htime is for debugging only
htime= r * 1000 + x * 100 + y * 10 + z;
int htimeH = r * 10 + x;
int htimeM = y * 10 + z;
//printf("%i\n", htimeM);

//start comparision to os clock


FILE *os_time = popen("date -u +%H%M", "r");
char buf1[256];
while (fgets(buf1, sizeof(buf1), os_time) != 0) {
     //print char fro array- not needed unless debugging
	//printf("OS Time : %s", buf1);

}
pclose(os_time);

int a = buf1[0] - '0';
int b = buf1[1] - '0';
int c = buf1[2] - '0';
int d = buf1[3] - '0';

stime= a * 1000 + b * 100 + c * 10 + d;
int stimeH = a * 10 + b;
int stimeM = c * 10 + d;
//printf("%i",stimeM);
if (htime == stime) {
	printf("%s", "The SYS clock and HWclock are in sync\n");

}
else if (stime != htime)  {
	printf("%s" , "The OS and HW clocks are not in sync.\n");
	//consider removing this check
//	if (htimeH != stimeH) {
//		printf("%s", "The hour is off and needed to be fixed. \n");
//		FILE *temp = popen("touch /var/tmp/fixclock.txt" , "r");
//	}
        
	if  (htimeM > stimeM) {
		int timeD = htimeM - stimeM;
	//	int timeF = htimeH - 4;
	        if (timeD > 3) {
        		printf("%s%i%s", "The hwCLOCK ahead of the sysclock by ", timeD , " minutes.\n");
			int fix1 = snprintf(clean1, sizeof(clean1), "date -s \"%d:%d\"",htimeH,htimeM);
			FILE *FIX2 = popen(clean1, "r");
			FILE *temp = popen("touch /var/tmp/check_clock.txt" , "r");
	
		}
		}

       else if (htimeM < stimeM) {
                int timeD = stimeM - htimeM;
        //      int timeF = htimeH - 4;
		if (timeD > 3) {
                	printf("%s%i%s", "The HWCLOCK behind the sysclock by ", timeD , " minutes.\n");
               // 	int fix1 = snprintf(clean1, sizeof(clean1), "date -s \"%d:%d\"",htimeH,htimeM);
	                int fix1 = snprintf(clean1, sizeof(clean1), "hwclock --systohc");
                	FILE *FIX2 = popen(clean1, "r");
                	FILE *temp = popen("touch /var/tmp/check_clock.txt" , "r");
		}
        }



}

}
