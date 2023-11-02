#include <stdio.h>

int main()
{
    char word[110];
    scanf("%s", word);
    int result = 0;
    for (int i = 0; word[i]!='\0'; i++)
    {
        if (word[i] != 'c' && word[i] != 'd' && word[i] != 'l' && word[i] != 'n' && word[i] != 's' && word[i] != 'z')
        {
            result++;
        }
        else
        {
            if (word[i] == 'c' && (word[i + 1] == '=' || word[i + 1] == '-'))
            {
                i++;
                result++;
            }
            else if (word[i] == 'd' && (word[i + 1] == 'z' && word[i + 2] == '='))
            {
                i += 2;
                result++;
            }
            else if (word[i] == 'd' && word[i + 1] == '-')
            {
                i++;
                result++;
            }
            else if (word[i] == 'l' && word[i + 1] == 'j')
            {
                i++;
                result++;
            }
            else if (word[i] == 'n' && word[i + 1] == 'j')
            {
                i++;
                result++;
            }
            else if (word[i] == 's' && word[i + 1] == '=')
            {
                i++;
                result++;
            }
            else if (word[i] == 'z' && word[i + 1] == '=')
            {
                i++;
                result++;
            }
            else
            {
                result++;
            }
        }
    }
    printf("%d", result);
    return 0;
}