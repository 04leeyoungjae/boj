#include <stdio.h>

void print_underscore(int num_recursion)
{
    for(int i=0;i<num_recursion;i++)
    {
        printf("____");
    }
    return;
}

void recursive(int max_recursion)
{
    for(int num_recursion=0;num_recursion<max_recursion;num_recursion++)
    {
        print_underscore(num_recursion);
        puts("\"재귀함수가 뭔가요?\"");
        print_underscore(num_recursion);
        puts("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.");
        print_underscore(num_recursion);
        puts("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.");
        print_underscore(num_recursion);
        puts("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"");
    }
    
    print_underscore(max_recursion);
    puts("\"재귀함수가 뭔가요?\"");
    print_underscore(max_recursion);
    puts("\"재귀함수는 자기 자신을 호출하는 함수라네\"");

    for(int num_recursion=max_recursion;num_recursion>=0;num_recursion--)
    {
        print_underscore(num_recursion);
        puts("라고 답변하였지.");
    }

    return;
}

int main()
{
    int max_recursion; 
    scanf("%d",&max_recursion);
    puts("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
    recursive(max_recursion);
    return 0;
}