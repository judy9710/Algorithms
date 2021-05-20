#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 분리연쇄법의 구현

#define M 13

typedef struct HashNode
{
    int key;
    struct HashNode* next;
}HashType;

void init(HashType* HT)
{
    for(int i=0; i<M; i++)
    {
        HT[i].key=0;
        HT[i].next=NULL;
    }
}

int h(int key)
{
    return key % M;
}

void insertItem(HashType* HT, int key)
{
    int v = h(key);
    HashType* node = (HashType*)malloc(sizeof(HashType));
    node->key = key;
    node->next = HT[v].next; //원래 첫번째가 두번째가 되고
    HT[v].next=node; // 내가 첫번째가 됨
}

int removeElement(HashType* HT, int key)
{
    int v=h(key);
    int count= 0; //bucket에 해당 키 값이 여러개 있다면 그 개수 세기 위함
    HashType* p=&HT[v]; //삭제되려면 단순연결리스트이므로 이전 노드를 위치 기억
    HashType* q; //삭제될 노드
    
    while(p->next)//끝까지 간다
    {
        if(p->next->key == key)
        {
            count++;
            q=p->next;
            p->next=q->next;
            free(q);
        }
        else
            p=p->next;
    }
    return count;
    
}

int findElement(HashType* HT, int key)
{
    int v = h(key);
    int count;
    HashType* p;
    for(p=HT[v].next; p!=NULL; p=p->next)
        if(p->key==key)
            count++;
    return count;
}

void printHash(HashType* HT)
{
    HashType* p;
    for(int i=0; i<M; i++)
    {
        printf("HT[%02d] : ", i);
        for(p=HT[i].next; p!=NULL; p=p->next)
            printf("(%d) ", p->key);
        printf("\n");
    }
}

int main()
{
    HashType HT[M];
    init(HT);
    
    srand(time(NULL));
    
    for(int i=0; i<20; i++)
        insertItem(HT, rand()%90 +10); // 2자리수로 맞추기 위해서
    printHash(HT);
    
    printf("\n삭제할 키 입력 : ");
    int key;
    scanf("%d", &key);
    
    printf("\n키 값 %d가 %d개 삭제되었습니다\n\n", key, removeElement(HT, key));
    printHash(HT);
    
    return 0;
}