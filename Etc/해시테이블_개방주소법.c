#include <stdio.h>
#include <stdlib.h>
//개방주소법 알고리즘

#define M 13

typedef struct
{
    int key;
    int probeCount; //특정한 키값이 몇 번의 탐색 후 삽입이 되는지 알기 위한 변수
}Bucket; 

typedef struct
{
    Bucket A[M]; //여러개 슬롯으로 이루어지게끔 2차원으로도 구현 가능
}HashType;

void initHash(HashType* HT)
{
    for(int i=0; i<M; i++)
    {
        HT->A[i].key=0;
        HT->A[i].probeCount=0;//몇번의 조사 후 해당 위치 찾아지는지
    }
}

int h(int key)
{
    return key % M;
}

int h2(int key)
{
    return 11-(key % 11); //이중 해싱을 위함
}

int getNextBucketLinear(int v, int i)
{
    return (v+i)%M;
}

int getNextBucketQuadratic(int v, int i)
{
    return (v+i*i)%M;
}

int getNextBucketDouble(int v, int i, int key)
{
    return (v+i*h2(key))% M;
}

int isEmpty(HashType* HT, int b)
{
    return HT->A[b].key==0;
}

int FindElement(HashType* HT, int key)
{
    int v=h(key);
    int i=0;
    
    while(i<M)
    {
        int b=getNextBucketLinear(v,i);
      //int b=getNextBucketQuadratic(v,i);
    //  int b=getNextBucketDouble(v,i,key);
        if(isEmpty(HT, b))
        {
            return 0;
        }
        else if(HT->A[b].key==key)
            return key; 
        else
            i++;
    }
    return 0; //못 찾았다는 의미
}

void insertItem(HashType* HT, int key)
{
    int v=h(key);
    int i=0;
    int count=0;
    while(i<M)
    {
        count++;
        int b=getNextBucketLinear(v,i);
      //int b=getNextBucketQuadratic(v,i);
    //  int b=getNextBucketDouble(v,i,key);
        if(isEmpty(HT, b))
        {
            HT->A[b].key=key;
            HT->A[b].probeCount=count;
            return;
        }
        else
            i++;
    }
}

int removeElement(HashType* HT, int key)
{
    int v=h(key);
    int i=0;
    
    while(i<M)
    {
        int b=getNextBucketLinear(v,i);
      //int b=getNextBucketQuadratic(v,i);
    //  int b=getNextBucketDouble(v,i,key);
        if(isEmpty(HT, b))
        {
            return 0;
        }
        else if(HT->A[b].key==key)
        {
            HT->A[b].key=0;
            HT->A[b].probeCount=0;
            return key;
        }
        else
            i++;
    }
    return 0;
}

void printHashTable(HashType* HT)
{
    printf("Bucket Key Probe\n");
    printf("=========================");
    
    for(int i=0; i<M; i++)
        printf("HT[%02d] : %2d    %2d\n", i, HT->A[i].key, HT->A[i].probeCount);
}

int main()
{
    HashType HT;
    initHash(&HT);
    
    insertItem(&HT,25);
    insertItem(&HT,13);
    insertItem(&HT,16);
    insertItem(&HT,15);
    insertItem(&HT,7);
    insertItem(&HT,28);
    insertItem(&HT,31);
    insertItem(&HT,20);
    insertItem(&HT,1);
    insertItem(&HT,38);
    printHashTable(&HT);
    
    int key;
    printf("탐색할 키 입력:");
    scanf("%d", &key);
    if(FindElement(&HT, key))
        printf("\n키 값 %d이(가) 존재합니다. \n", key);
    else
        printf("\n키 값 %d이(가) 없습니다. \n", key);
        
    printf("\n 삭제할 키 입력:");
    scanf("%d", &key);
    if(removeElement(&HT, key))
        printf("\n키 값 %d이(가) 삭제되었습니다. \n", key);
    else
        printf("\n키 값 %d이(가) 없습니다.\n",key);
    printf("\n");
    printHashTable(&HT);
    
    return 0;
    
}
