// 배열을 이용한 리스트의 구현

#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

typedef struct
{
	int V[SIZE];
	int n;
}ArrayList;

void init(ArrayList* L)
{
	L->n = 0;
}

void traverse(ArrayList* L)
{
	for (int i = 0; i < L->n; i++)
		printf("[%d]", L->V[i]);
	printf("\n");
}

void add(ArrayList* L, int pos, int item)
{
	if (L->n == SIZE)
	{
		printf("fullListExceptionError\n");
		exit(1);
	}
	//invalidPosException... 0<=pos<=L->n

	for (int i = L->n - 1; i >= pos; i--)
		L->V[i + 1] = L->V[i];
	L->V[pos] = item;
	L->n++;
}

int remove(ArrayList* L, int pos)
{
	if (L->n == 0)
	{
		printf("emptyListExceptionError\n");
		exit(1);
	}
	//invalidPosException... 0<=pos<=L->n

	int item = L->V[pos];
	for (int i = pos + 1; i <= L->n - 1; i++)
	{
		L->V[i - 1] = L->V[i];
	}
	L->n--;
	return item;
}

void main()
{
	ArrayList list;

	init(&list);

	add(&list, 0, 10); traverse(&list);
	add(&list, 0, 20); traverse(&list);
	add(&list, 1, 30); traverse(&list);
	add(&list, 1, 40); traverse(&list);
	add(&list, 3, 50); traverse(&list);

	//gerchar();
	remove(&list, 1); traverse(&list);
	remove(&list, 2); traverse(&list);
}