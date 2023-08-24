#include <stdio.h>
#include<string.h>
#define MAX_STACK_SIZE 1000000

struct A
{
        int stack[MAX_STACK_SIZE];
        int top_index;
        int cur_size;
};

void push(struct A *s){
        int data;
        scanf("%d",&data);
        s->top_index++;
        s->stack[s->top_index]=data;
        s->cur_size++;
}

int size(struct A *s){
        return s->cur_size;
}

int empty(struct A *s){
        if(size(s)) return 0; return 1;
}

int pop(struct A *s){
        if (empty(s)) return -1;
        s->top_index--;
        s->cur_size--;
        return s->stack[s->top_index+1];
}

int top(struct A *s){
        if (empty(s)) return -1; return s->stack[s->top_index];
}

int main(){
        struct A s;
        s.top_index=-1;
        s.cur_size=0;
        int t; //테스트케이스
        scanf("%d",&t);
        for(int i=0;i<t;i++){
                char command[20];
                scanf("%s",command);
                if (strcmp(command,"1")==0) push(&s);
                else if(strcmp(command,"2")==0) printf("%d\n",pop(&s));
                else if(strcmp(command,"3")==0) printf("%d\n",size(&s));
                else if(strcmp(command,"4")==0) printf("%d\n",empty(&s));
                else if(strcmp(command,"5")==0) printf("%d\n",top(&s));
        }
        return 0;
}