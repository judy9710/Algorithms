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

void init(LinkedListType* L)
{
	L->head = NULL;
}

void addFirst(LinkedListType* L, int item)
{
	ListNode* node = (ListNode*)malloc(sizeof(ListNode));
	node->data = item;
	node->link = L->head;
	L->head = node;
}

void add(LinkedListType* L, int pos, int item)
{
	ListNode* node = (ListNode*)malloc(sizeof(ListNode));
	ListNode* before = L->head;
	for (int i = 0; i < pos - 1; i++)
		before = before->link;
	node->data = item;
	node->link = before->link;
	before->link = node;
}

void addLast(LinkedListType* L, int item)
{
	ListNode* node = (ListNode*)malloc(sizeof(ListNode));
	node->data = item;
	node->link = NULL;
	ListNode* temp = L->head;
	while(temp->link!=NULL)
	{
		temp = temp->link;
	}
	temp->link = node;
}

void deleteFirst(LinkedListType* L)
{
	ListNode* removed;
	removed = L->head;
	L->head = removed->link;
	free(removed);
}

void delete(LinkedListType* L, int pos)
{
	ListNode* temp = L->head;
	if (pos == 1)
	{
		L->head = temp->link;
		free(temp);
	}
	
	for (int i = 1; i < pos-1; i++)
		temp = temp->link; //삭제할 노드의 이전 노드
	ListNode* next = temp->link->link; //삭제할 노드의 다음 노드
	free(temp->link);
	temp->link = next;
}

void deleteLast(LinkedListType* L)
{
	ListNode* secondLast = L->head;
	while (secondLast->link->link != NULL)
	{
		secondLast = secondLast->link;
	}
	free(secondLast->link);
	secondLast->link = NULL;
}
int get(LinkedListType* L, int pos)
{
	ListNode* p = L->head;
	for (int i = 1; i < pos; i++)
		p = p->link;
	return p->data;
}

void set(LinkedListType* L, int pos, int item)
{
	ListNode* p = L->head;
	for (int i = 1; i < pos; i++)
		p = p->link;
	p->data = item;
}
void printList(LinkedListType* L)
{
	for (ListNode* p = L->head; p != NULL; p = p->link)
		printf("[%d] -> ", p->data);
	printf("NULL\n");
}
void main()
{
	LinkedListType list;
	init(&list);

	printf("\n첫번째에 원소들을 add 하겠습니다\n");
	addFirst(&list, 10); printList(&list);
	addFirst(&list, 20); printList(&list);
	addFirst(&list, 30); printList(&list);

	printf("\n원소들을 특정한 위치에 add 하겠습니다\n");
	add(&list, 1, 40); printList(&list);
	add(&list, 1, 50); printList(&list);
	add(&list, 3, 60); printList(&list);

	int pos;
	printf("\n몇번 노드의 값을 반환할까요?\n");
	scanf_s("%d", &pos);
	printf("%d번 노드의 값은 %d\n", pos, get(&list, pos));

	printf("\n마지막에 원소들을 add 하겠습니다\n");
	addLast(&list, 70); printList(&list);
	addLast(&list, 80); printList(&list);

	printf("\n첫번째 원소들을 delete 하겠습니다\n");
	deleteFirst(&list); printList(&list);
	deleteFirst(&list); printList(&list);

	int deleteposition;
	printf("\n몇번 노드를 delete 할까요?\n");
	scanf_s("%d", &deleteposition);
	delete(&list, deleteposition); printList(&list);

	printf("\n마지막 원소들을 delete 하겠습니다\n");
	deleteLast(&list); printList(&list);
	deleteLast(&list); printList(&list);
}