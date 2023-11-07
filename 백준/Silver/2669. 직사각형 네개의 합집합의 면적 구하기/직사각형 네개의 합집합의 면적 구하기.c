#include <stdio.h>

int main() {
    int plane[100][100]={0,};
    for(int _=0;_<4;_++)
    {
        int x1,y1,x2,y2;
        scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
        for(int x=x1;x<x2;x++)
        {
            for(int y=y1;y<y2;y++)
            {
                plane[x][y]=1;
            }
        }
    }
    int result=0;
    for(int x=0;x<100;x++)
    {
        for(int y=0;y<100;y++)
        {
            if(plane[x][y]) result++;
        }
    }
    printf("%d\n",result);
}
