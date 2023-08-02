// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
   int two,four,noofveh,noofwheels;
   scanf("%d%d",&noofveh,&noofwheels);
   four = (noofwheels - 2*noofveh)/2;
   two = noofveh - four;
   printf("TW=%d FW=%d",two,four);
   
   

    return 0;
}