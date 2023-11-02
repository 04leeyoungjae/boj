#include <stdio.h>

#define MAX_N 10000

int counting(int n)
{
    int result=0;
    int copy=n;
    for(;n;n/=10) result+=n%10;
    return copy+result;
}

int main(void)
{
    int bool_lst[MAX_N]={0,}; //+10은 여유
    for(int i=1;i<MAX_N;i++)
    {
        if(counting(i)<10000) bool_lst[counting(i)]++;
    }
    for(int i=1;i<MAX_N;i++)
    {
        if(bool_lst[i]==0) printf("%d\n",i);
    }
    return 0;
}