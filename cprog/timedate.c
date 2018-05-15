#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main() {
     //os clock
    time_t currentTime;
    time(&currentTime);
    struct tm *osTime = localtime(&currentTime);
        //printf("%s", ctime(&currentTime));
    printf("%i:%i\n", osTime->tm_hour,osTime->tm_min);


    //attempt to get hw clock
    time_t currentTime:
    time(&currentTime)
    struct timespec sysTime = clock_gettime(&currentTime);
    printf("%i", sysTime->timespec_hour);

}
