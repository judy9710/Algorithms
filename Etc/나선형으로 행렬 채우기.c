/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

#define N 4
#define M 5

void spiral(int A[N][M])
{
    int left=0;
    int right=M-1;
    int top=0;
    int bottom=N-1;
    int value=1;
    while ((left<=right)&(top<=bottom))
    {
        for(int j=left; j<=right; j++)
        {
            A[top][j]=value;
            value++;
        }
        top++;
        
        if(top<=bottom)
            for (int i=top; i<=bottom; i++)
            {
                A[i][right]=value;
                value++;
            }
        right--;
        if(left<=right)
            for (int j=right; j>=left; j--)
            {
                A[bottom][j]=value;
                value++;
            }
        bottom--;
        if(top<=bottom)
        for (int i=bottom; i>=top; i--)
        {
            A[i][left]=value;
            value++;
        }
        left++;
    }
    
}

int main()
{
    int A[N][M]={0};
    spiral(A);
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<M; j++)
            printf("%2d",A[i][j]);
        printf("\n");
    }
}
