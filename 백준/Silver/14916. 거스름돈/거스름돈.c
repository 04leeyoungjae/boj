#include <stdio.h>

int main(void){
    int n;
    int coin=0;
    scanf("%d",&n);
    if (n==1 || n==3)
    {
        coin=-1; // 거슬러줄수없음
    }
    else
    {
       while(n%5!=0)
        {
           n-=2;
           coin++;
        }
        coin+=n/5;;
    }
    printf("%d",coin);
    return 0;
}