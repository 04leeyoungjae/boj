#include <stdio.h>

int my_abs(int a,int b)
{
    int result=a-b;
    if (b>a) return -result;
    return result;
}

int main() {
    int origin,target;
    int favorite;
    int frequency;
    scanf("%d %d",&origin,&target);
    scanf("%d",&favorite);
    int result=my_abs(origin,target);
    for(int i=0;i<favorite;i++)
    {
        scanf("%d",&frequency);
        if(my_abs(frequency,target)+1<result) result=my_abs(frequency,target)+1;
    }
    printf("%d\n",result);
}
