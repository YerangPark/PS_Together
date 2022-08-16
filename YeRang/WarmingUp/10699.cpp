#include <stdio.h>
#include <time.h>

int main () {
    time_t curTime = time(NULL);
    struct tm *pLocal = localtime(&curTime);
    printf("%04d-%02d-%02d\n", pLocal->tm_year + 1900, pLocal->tm_mon + 1, pLocal->tm_mday);
    return 0;
}