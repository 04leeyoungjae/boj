#include <stdio.h>

int dinamic_program_0[50]={1,0,}; //인덱스 = n값
int dinamic_program_1[50]={0,1,};

void fibonacci(int n) {
    if (dinamic_program_0[n]<0)
    {
        fibonacci(n-1);
        fibonacci(n-2);
        dinamic_program_0[n]=dinamic_program_0[n-1]+dinamic_program_0[n-2];
        dinamic_program_1[n]=dinamic_program_1[n-1]+dinamic_program_1[n-2];
    }
    return;
}

int main(void)
{
    for(int i=2;i<50;i++) // 0이 의미가 있는 값으로 이용되기에 초기화로 -1사용
    {
        dinamic_program_0[i]=-1;
        dinamic_program_1[i]=-1;
    }
    int testcase;
    scanf("%d",&testcase);
    for(int i=0;i<testcase;i++)
    {
        int num;
        scanf("%d",&num);
        fibonacci(num);
        printf("%d %d\n",dinamic_program_0[num],dinamic_program_1[num]);
    }
    return 0;
}