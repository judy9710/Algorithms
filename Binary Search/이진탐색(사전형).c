#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 15


typedef struct
{
    int key;
    char value[10];
    
}element;

typedef struct
{
    element dict[SIZE];
    int size;
}DictType;

void init(DictType* d)
{
    d->size=0;
}

void insertKey(DictType* d)
{
    for(int i=0; i<SIZE; i++)
    {
        d->dict[i].key=rand()%30+1;
        for(int j=0; j<i; j++)
            if(d->dict[i].key==d->dict[j].key) //유일키를 위한 작업
                i--;
    }
}

void insertValue(DictType* d)
{
    for(int i=0; i<SIZE; i++)
    {
        for(int j=0; j<5; j++) //다섯글자짜리 문자
            d->dict[i].value[j]=rand()%26+97; //아스키코드로 a~z
        d->size++; //key value 들어가면 사이즈 하나 증가시킴
    }
}

void insertion_sort(DictType*d)
{
    int i,j;
    element item;
    for(i=1; i<SIZE; i++)
    {
        item = d->dict[i];
        for(j=i-1; j>=0 && d->dict[j].key >item.key; j--) //key 값 기준으로 정렬
            d->dict[j+1]=d->dict[j]; //오름차순 정렬
        d->dict[j+1]=item; 
    }
}

int rFindElement(DictType* d, int key, int l, int r)
{
    int mid;
    if(l<=r)
    {
        mid=(l+r)/2;
        if(key==d->dict[mid].key)
            return mid;
        else if(key<d->dict[mid].key)
            return rFindElement(d,key,l,mid-1);
        else
            return rFindElement(d,key,mid+1,r);
    }
    return -1;
}

int FindElement(DictType*d, int key, int l, int r)
{
    int mid;
    while(l<=r)
    {
        mid=(l+r)/2;
        if(key==d->dict[mid].key)
            return mid;
        else if(key < d->dict[mid].key)
            r=mid-1;
        else
            l=mid+1;
    }
    return -1;
}

element removeElement(DictType* d, int key)
{
    int index = FindElement(d,key,0,d->size-1); //반복문으로 구현한 키값찾기
    if(index==-1)
    {
        printf("삭제할 요소가 없습니다.\n");
        return;
    }
    else
    {
        element item = d->dict[index];
        for(int i=index; i<d->size-1; i++)
            d->dict[i]=d->dict[i+1]; //옮기기 작업
        d->size--;
        return item;
    }
}

void printDict(DictType* d)
{
    printf("key value \n=============\n");
    for(int i=0; i<d->size; i++)
    {
        printf("%2d ", d->dict[i].key);
        for(int j=0; j<5; j++)
            printf("%c", d->dict[i].value[j]);
        printf("\n");
    }
}

void makeDict(DictType* d)
{
    insertKey(d);
    insertValue(d);
}

int main()
{
    DictType d;
    init(&d);
    srand(time(NULL));
    makeDict(&d);
    printDict(&d);
    getchar();
    printf("\n");
    insertion_sort(&d);
    printDict(&d);
    getchar();
    
    printf("\n검색할 키값을 입력:");
    int key;
    scanf("%d", &key);
    int index = rFindElement(&d, key, 0, SIZE-1);
    if(index==-1)
        printf("\n검색에 실패하였음\n");
    else
    {
        printf("\n위치 %d에서 키: %d 값:", index+1, key);
        for(int j=0; j<5; j++)
            printf("%c", d.dict[index].value[j]);
        printf("이 검색되었음\n");
    }
    
    printf("\n삭제할 키값을 입력:");
    scanf("%d", &key);
    removeElement(&d, key);
    printDict(&d);
    return 0;
}
