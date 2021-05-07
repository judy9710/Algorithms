/* #include <stdio.h>
#include <stdlib.h>

#define MAX_ELEMENT 100

typedef struct
{
    int heap[MAX_ELEMENT + 1];
    int heap_size;
}HeapType;

void init(HeapType* h)
{
    h->heap_size = 0;
}

void upHeap(HeapType* h)
{
    int i, key;

    i = h->heap_size;
    key = h->heap[i];

    while ((i != 1) && (key < h->heap[i / 2])) //최소힙으로 구현
    {
        h->heap[i] = h->heap[i / 2];
        i /= 2;
    }
    h->heap[i] = key;
}

void printHeap(HeapType* h)
{
    for (int i = 1; i <= h->heap_size; i++)
        printf("[%d] ", h->heap[i]);
    printf("\n");
}

void insertItem(HeapType* h, int key)
{
    h->heap_size += 1;
    h->heap[h->heap_size] = key;
    upHeap(h);
}

typedef int element;
typedef struct {
    element data[MAX_ELEMENT + 1];
    int top;
}StackType;

void init_stack(StackType* s)
{
    s->top = 0;
}

int is_empty(StackType* s)
{
    return (s->top == 0);
}

int is_full(StackType* s)
{
    return (s->top == MAX_ELEMENT);
}

void push(StackType* s, element item)
{
    if (is_full(s)) {
        fprintf(stderr, "스택 포화 에러\n");
        return;
    }
    else s->data[++(s->top)] = item;
}

element pop(StackType* s)
{
    if (is_empty(s)) {
        fprintf(stderr, "스택 공백 에러\n");
        exit(1);
    }
    else return s->data[(s->top)--];
}

StackType binaryExpansion(int i, StackType* s)
{
    int item = i;
    while (i >= 2) {
        item %= 2;
        //printf("item:%d ", item);
        push(s, item);
        i /= 2; item = i;
    }
    push(s, i);

    printf("\n");
    printf("Values Inserted in Stack :");
    for (int j = 1; j <= s->top; j++)
        printf("[%d] ", s->data[j]);
    printf("\n");
    return *s;
}

int findLastNode(int v, int n)
{
    StackType s;

    init_stack(&s);

    binaryExpansion(n, &s);
    pop(&s);
    int bit;
    while (!is_empty(&s)) {
        bit = pop(&s);
        if (bit == 0)
            v = 2 * v;
        else
            v = 2 * v + 1;
    }
    printf("\n");
    printf("The last index where the final node is located: v=%d\n", v);
    return v;
}
void main()
{
    HeapType heap;

    init(&heap);

    int n;
    
    printf("Please Input heap size(<=100) : \n");

    scanf_s("%d", &n);

    printf("Create Size %d Heap !!!\n", n);

    for (int i = 0;i < n;i++) {
        insertItem(&heap, rand() % 100);
        printHeap(&heap);
    }
    printHeap(&heap);

    printf("Finish Heap Create \n");
    printf("\n");
    
    int lastnode_index;
    lastnode_index = findLastNode(1, n);

    printf("Last node value is : %d\n", heap.heap[lastnode_index]);

}*/