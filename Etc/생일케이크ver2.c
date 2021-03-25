// 배열 ver.2을 이용한 생일케이트의 구현
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
	printf("\n케이크 양초의 개수 n 을 지정하세요: ");
	int n, N;
	scanf_s("%d", &n);
	buildList2(&list, n); traverse2(&list, n);
	printf("원형 케이크가 생성되었습니다\n");
	printf("\nk 개 떨어진 양초의 불을 끄기 위해 k 값을 입력하세요\n");
	int k;
	scanf_s("%d", &k);
	printf("\n시뮬레이션을 시작하겠습니다\n");
	int value;
	value = runSimulation2(&list, n, k);
	printf("\n%d번째 위치에 있는 양초가 마지막 양초입니다\n", value);
	return;

}*/