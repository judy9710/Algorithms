// �迭 ver.2�� �̿��� ��������Ʈ�� ����
/*
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
	int* A;
}ArrayList;

void buildList2(ArrayList* L, int n)
{
	L->A = (int*)malloc(sizeof(n));
	for (int r = 0; r < n; r++)
	{
		L->A[r] = r + 1;
	}
	return;
}

void traverse2(ArrayList* L, int n)
{
	for (int i = 0; i < n; i++)
		printf("[%d]", L->A[i]);
	printf("\n");
	return;
}

int runSimulation2(ArrayList* L, int n, int k)
{
	int r = 0;
	while (n > 1)
	{
		r = ((r + k) % (n));
		for (int i = r; i < n-1;i++)
		{
			L->A[i] = L->A[i+1];
		}
		n--;
	}
	return L->A[0];
}

void main()
{
	ArrayList list;
	printf("\n����ũ ������ ���� n �� �����ϼ���: ");
	int n, N;
	scanf_s("%d", &n);
	buildList2(&list, n); traverse2(&list, n);
	printf("���� ����ũ�� �����Ǿ����ϴ�\n");
	printf("\nk �� ������ ������ ���� ���� ���� k ���� �Է��ϼ���\n");
	int k;
	scanf_s("%d", &k);
	printf("\n�ùķ��̼��� �����ϰڽ��ϴ�\n");
	int value;
	value = runSimulation2(&list, n, k);
	printf("\n%d��° ��ġ�� �ִ� ���ʰ� ������ �����Դϴ�\n", value);
	return;

}*/