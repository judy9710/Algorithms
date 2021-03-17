/******************************************************************************
Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.
*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 누적평균 구하기
#define SIZE 8

void makeArray(int A[])
{
    for (int i=0; i<SIZE; i++)
        A[i]=rand()%50+50;
     
}

void printArray(int A[])
{
    for(int i=0; i<SIZE; i++)
        printf("[%d]", A[i]);
    printf("\n");
}

void prefixAvg1(int A[])
{
    int X[SIZE];
    int sum;
    for(int i=0; i<SIZE; i++)
    {
        sum=0;
        for(int j=0; j<=i; j++)
            sum+=A[j];
        X[i]=sum/(i+1);
    }
    printArray(X);
}

void prefixAvg2(int A[])
{
    int X[SIZE];
    int sum=0;
    for (int i=0; i<SIZE; i++)
    {
        sum+=A[i];
        X[i]=sum/(i+1);
    }
    printArray(X);
}

void main()
{
    int A[SIZE];
    srand(time(NULL));
    makeArray(A);
    printArray(A);
    prefixAvg1(A);
    prefixAvg2(A);
    
}