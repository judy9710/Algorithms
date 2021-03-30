#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 15
#define SWAP(x,y,t) ((t)=(x),(x)=(y),(y)=(t))

//삽입정렬은 어느정도 정렬된 리스트에서 빠른 것에서 착안
void inc_insertion_sort(int list[], int first, int last, int gap)
{
    int i,j,key;
    for(i=first+gap;i<=last; i=i+gap)
    {
        key=list[i];
        for(j=i-gap;j>=first&&list[j]>key; j=j-gap){
            list[j+gap]=list[j];
        }
        list[j+gap]=key;
    }
}

void shell_sort(int list[], int n){
    int i, gap;
    for(gap=n/2; gap>0; gap=gap/2){
        if (gap%2==0) gap++;
        for(i=0; i<gap; i++)
            inc_insertion_sort(list,i,n-1,gap);
    }
}

void main()
{
    int list[MAX_SIZE];
    srand(time(NULL));
    
    for(int i=0; i<MAX_SIZE; i++)
    {
        list[i]=rand()%100;
        for(int j=0; j<i; j++) //중복을 허용하지 않음
            if(list[i]==list[j])
                i--;
    }
    
    for(int i=0; i<MAX_SIZE; i++)
        printf("%d ", list[i]);
    printf("\n\n");
    
    shell_sort(list,MAX_SIZE);
    for(int i=0; i<MAX_SIZE; i++)
        printf("%d ", list[i]);
        

}