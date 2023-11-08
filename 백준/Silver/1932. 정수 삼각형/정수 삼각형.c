#include <stdio.h>

int main(void)
{
    int size;
    scanf("%d",&size);
    int triangle[501][501];
    int copy[501][501];
    for(int row=0;row<size;row++) // row=0이 맨위
    {
        for(int col=0;col<=row;col++) 
        {
            scanf("%d",&triangle[row][col]);
            copy[row][col]=triangle[row][col];
        }
    }
    for(int row=0;row<size;row++)
    {
        for(int col=0;col<=row;col++)
        {
            if(triangle[row][col]+copy[row+1][col] > triangle[row+1][col]) triangle[row+1][col]=triangle[row][col]+copy[row+1][col];
            if(triangle[row][col]+copy[row+1][col+1] > triangle[row+1][col+1]) triangle[row+1][col+1]=triangle[row][col]+copy[row+1][col+1];
            //printf("%d ",triangle[row][col]);
        }
       // puts("");
    }
    int result=0;
    for(int row=size-1,col=0;col<=row;col++)
    {
        if(triangle[row][col]>result) result=triangle[row][col];
    }
    printf("%d\n",result);
}