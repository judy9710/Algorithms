/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 행렬에서 특정한 원소를 찾는 프로그램 작성하기

#define ROWS 8
#define COLS 8

void makeArray(int A[][COLS])
{
    for(int r=0; r<ROWS;r++)
        for(int c=0; c<COLS; c++)
            A[r][c]=rand()%100;
}

void printArray(int A[][COLS])
{
    for(int r=0; r<ROWS; r++)
    {    for(int c=0;c<COLS;c++)
            printf("%2d ", A[r][c]);
        printf("\n");
    }
    printf("\n");
}

int findRow(int A[],int key)
{
    for (int c=0; c<COLS; c++)
        if(A[c]==key)
            return c;
    return -1;
}

void findMatrix(int A[][COLS], int key)
{
    int r=0;
    int index;
    
    while (r<ROWS)
    {
        index=findRow(A[r],key);
        if(index>=0)
        {
            printf("%d행 %d열에서 %d 발견\n", r,index,key);
            return;
        }
        else
            r++;
        
    }
    printf("Not Found\n");
}


void main()
{
    int A[ROWS][COLS];
    srand(time(NULL));
    makeArray(A);
    printArray(A);
    
    int key;
    printf("Input a key value: ");
    scanf_s("%d",&key);
    findMatrix(A,key);
    
}