// �迭 ver.1�� �̿��� ��������Ʈ�� ����
/*
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
	int *A;
}ArrayList;

void buildList(ArrayList* L, int n)
{
	L->A=(int *)malloc(sizeof(n));
	for (int r = 0; r < n; r++)
	{
		L->A[r] = r + 1;
	}
	return;
}

void traverse(ArrayList* L, int n)
{
	for (int i = 0; i < n; i++)
		printf("[%d]", L->A[i]);
	printf("\n");
	return;
}

int runSimulation(ArrayList* L, int n, int k)
{
	int r = 0; 
	int N = n;
	while (n > 1) 
	{
		int i = 0; 
		while (i < k) 
		{
			r = ((r + 1) % (N)); 
			if (L->A[r] != 0)
			{
				i++; 
			}
		}
		L->A[r] = 0;
		n--;
		while (L->A[r] == 0) 
		{
			r = ((r + 1) % (N)); 
		}
	}
	return L->A[r];
}

void main()
{
	ArrayList list;
	printf("\n����ũ ������ ���� n �� �����ϼ���: ");
	int n, N;
	scanf_s("%d", &n);
	buildList(&list, n); traverse(&list, n);
	printf("���� ����ũ�� �����Ǿ����ϴ�\n");
	printf("\nk �� ������ ������ ���� ���� ���� k ���� �Է��ϼ���\n");
	int k;
	scanf_s("%d", &k);
	printf("\n�ùķ��̼��� �����ϰڽ��ϴ�\n");
	int value;
	value=runSimulation(&list, n, k);
	printf("\n%d��° ��ġ�� �ִ� ���ʰ� ������ �����Դϴ�\n", value);
	return;
}*/