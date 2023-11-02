#include <stdio.h>

int check(char *word)
{
    for(int i=0;word[i];i++)
    {
        for(int j=i+1;word[j];j++)
        {
            if(word[j]!=word[j-1] && word[i]==word[j]) return 0; //앞글자랑 다른데 이미있는글자
        }
    }
    return 1;
}

int main(void)
{
    int num_word;
    int result=0;
    scanf("%d",&num_word);
    char word[110];
    for(int i=0;i<num_word;i++)
    {
        scanf("%s",word);
        result+=check(word);
    }
    printf("%d",result);
    return 0;
}