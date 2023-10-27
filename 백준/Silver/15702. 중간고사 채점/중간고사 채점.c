#include <stdio.h>

int main(void)
{
    int numN,numM; // numN : 문제의개수, numM : 응시자의수
    int N[100],M[100]; // N[100] : 점수, M[100] : 개인의 점수
    
    int best[2]={0,0};

    scanf("%d %d",&numN,&numM);

    for(int i=0;i<numN;i++)
    {
        scanf("%d",&N[i]); //문제의 점수 받음
    }

    for(int i=0;i<numM;i++)
    {
        int now[2]={0,0}; //수험번호,점수
        scanf("%d",&now[0]);
        for(int j=0;j<numN;j++)
        {
            char var;
            scanf("%c",&var);
            if(var=='O') now[1]+=N[j];
            else if(var==' ') j--;
        }
        if((now[1]>best[1]) || (now[1]==best[1] && now[0]<best[0]) || best[0]==0)
        {
            best[0]=now[0];
            best[1]=now[1];
        }
    }
    printf("%d %d",best[0],best[1]);

    return 0;
}