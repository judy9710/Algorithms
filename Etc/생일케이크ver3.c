#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode
{
    int data;
    struct ListNode* link;
}ListNode;


typedef struct
{
    ListNode* head;
}LinkedListType;

void init3(LinkedListType* L)
{
    L->head = NULL;
}

void buildCircularList(LinkedListType* L, int n)
{
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));

    node->data = 1;
    //  node->link = NULL;
    L->head = node;

    for (int i = 2; i <= n; i++)
    {
        ListNode* new = (ListNode*)malloc(sizeof(ListNode));
        node->link = new;
        node = new;
        node->data = i;

    }
    node->link = L->head;
    
    return;

}

void runSimulation4(LinkedListType* L, int n, int k)
{
    ListNode* node;
    ListNode* pnextt;
    node = L->head;

    while (node != node->link) {
        for (int i = 1; i <= k - 1; i++)
            node = node->link;
        pnextt = node->link;
        node->link = (node->link)->link;
        free(pnextt);
        node = node->link;
    }
    int value;
    value = node->data;
    printf("%d\n", value);
}
void printList4(LinkedListType* L, int n)
{
    ListNode* p = L->head;
    for (int i = 1; i <= n; i++) {
        printf("[%d] -> ", p->data);
        p = p->link;
    }
    printf("AND\n");
}

void main()
{
    LinkedListType list;
    int n;
    printf("\n�� ���� ���ʸ� ������� ?\n");
    scanf_s("%d", &n);
    printf("%d ���� ���ʰ� �ִ� ��������ũ�� ��������ϴ� !!\n", n);
    buildCircularList(&list, n); printList4(&list, n);

    int k;
    printf("k���� �Է��ϼ��� : \n");
    scanf_s("%d", &k);
    printf("�ùķ��̼� ���� !!!\n");
    runSimulation4(&list, n, k);
}