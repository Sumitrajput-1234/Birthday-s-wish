#include<stdio.h>
int main(){
    int a,b,temp;
    printf("enter two number:");
    scanf("%d %d",&a,&b);
    printf("before swapping:\n");
    printf("a=%d,b=%d\n",a,b);

    temp=a;
    a=b;
    b=temp;
    
    printf("after swapping:\n");
    printf("a=%d,b=%d",a,b);
    return 0;
}