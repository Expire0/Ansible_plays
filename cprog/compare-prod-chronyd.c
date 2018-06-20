#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <linux/rtc.h>


//check hardware clock and sys clock 
//check if ntpdate -d  will be a better fix command. then hwclock or date -s
//issue 1 what happens if the system time is completely wrong?
//check ntp status on old servers and chronyd on new. 
int main() {

int hour[50], htime , stime, n=0 , i;

char clean1[100] , precheck1[100];


//clean existing temp file 
FILE *prep = popen("rm -rf /var/tmp/check_clock.txt", "r");


// check hardware clock and add stdout to array
// change verbose to debug for older systems
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
// validate is ntp or chronyd is running . 

FILE *pre1 = popen("systemctl status chronyd | grep running", "r");
        
        while (fgets(precheck1, sizeof(precheck1), ls) != 0) {
//        printf("Chronyd is  : %c%c%c%c%c%c%c", precheck1[19],precheck1[20],precheck1[21],precheck1[22],precheck1[23],precheck1[24],precheck1[25]); 
         char precheck2[50];
   int live = snprintf(precheck2, sizeof(precheck2),  "Chronyd is: %c%c%c%c%c%c%c", precheck1[19],precheck1[20],precheck1[21],precheck1[22],precheck1[23],precheck1[24],precheck1[25]);
// compare the output string 
        char out2[50];
	char out3[50];
	int rel;
	strcpy(out2, "Chronyd is: running");
	strcpy(out3, "running");
	rel = strcmp(out2, precheck2);
	if (rel == 0) {
            printf("Chronyd is running.  %d\n", rel); 
	}
}


pclose(pre1);

FILE *pre2 = popen("systemctl status chronyd | grep dead", "r");

        while (fgets(precheck1, sizeof(precheck1), ls) != 0) {
        printf("Chronyd is: %c%c%c%c\n", precheck1[21],precheck1[22],precheck1[23],precheck1[24]); 
         char precheck2[50];
   int live = snprintf(precheck2, sizeof(precheck2),  "Chronyd is: %c%c%c%c", precheck1[21],precheck1[22],precheck1[23],precheck1[24]);
// compare the output string 
        char out2[50];
        char out3[50];
        int rel;
        strcpy(out2, "Chronyd is: dead");
        strcpy(out3, "running");
        rel = strcmp(out2, precheck2);
        if (rel == 0) {
            printf("Chronyd is not running.Terminating application  %d\n", rel);
	    exit(0);
        }
}


pclose(pre2);


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
	printf("%s" , "The OS and HW clocks are not in sync.The sync is within the threshold\n");
	//consider removing this check
//	if (htimeH != stimeH) {
//		printf("%s", "The hour is off and needed to be fixed. \n");
//		FILE *temp = popen("touch /var/tmp/fixclock.txt" , "r");
//	}
       // if the hardware clock is higher. how do we verify if the clock is correct 
	if  (htimeM > stimeM) {
		int timeD = htimeM - stimeM;
		//need time offset if the system time is not utc
		int timeF = htimeH - 4;
	        if (timeD > 10) {
        		printf("%s%i%s", "The hwCLOCK ahead of the sysclock by ", timeD , " minutes.Self correcting\n");
			int fix1 = snprintf(clean1, sizeof(clean1), "hwclock --systohc");
			FILE *FIX2 = popen(clean1, "r");
			FILE *temp = popen("touch /var/tmp/check_clock.txt" , "r");
			FILE *temp2 = popen("echo $(date) The clock was off by more then 10 minutes >> /var/tmp/clock.log" , "r");
	
		}
		}
       //  possible patch for minutes in the 50 range (if htimeM < 50 &&  htimeM < stimeM)
       //  original line (htimeM < stimeM)
       else if (htimeM < stimeM)  {
                int timeD = stimeM - htimeM;
              int timeF = htimeH - 4;
		if (timeD > 10) {
                	printf("%s%i%s", "The HWCLOCK behind the sysclock by ", timeD , " minutes.Self Correcting\n");
               // 	int fix1 = snprintf(clean1, sizeof(clean1), "date -s \"%d:%d\"",htimeH,htimeM);
	                int fix1 = snprintf(clean1, sizeof(clean1), "hwclock --systohc");
                	FILE *FIX2 = popen(clean1, "r");
                	FILE *temp = popen("touch /var/tmp/check_clock.txt" , "r");
			FILE *temp2 = popen("echo $(date) The clock was off by more then 10 minutes >> /var/tmp/clock.log" , "r");
		}
        }



}

}
