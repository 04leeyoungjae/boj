#include <stdio.h>

int comb(int n,int k)
{
    if (k>n) return 0;
    if (k==n || k==0) return 1;
    int total=1;
    for(int i=1;i<=k;i++)
    {
        total*= (float)(n-i+1)/i;
    }
    return (int)total;
}

int main(void)
{
    int n,k;
    scanf("%d %d",&n,&k);
    printf("%d",comb(n-1,k-1));
    return 0;
}