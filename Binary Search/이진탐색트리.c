#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode{
    int key;
    struct TreeNode* parent, *left, *right;
}TreeNode;

typedef struct
{
    TreeNode* root;
}TreeType; //이렇게 구조체로 선언안하면 root 바뀔 때마다 모든 함수에서 루트
//리턴해야하는 번거로움이 있음

void initTree(TreeType* T)
{
    T->root=(TreeNode*)malloc(sizeof(TreeNode));
    T->root->parent=T->root->left=T->root->right=NULL;
}

int isExternal(TreeNode* w)
{
    return (w->left==NULL && w->right == NULL);
}

//page 172 수도코드
void expandExternal(TreeNode* w)
{
    TreeNode* l=(TreeNode*)malloc(sizeof(TreeNode));
    TreeNode* r=(TreeNode*)malloc(sizeof(TreeNode));
    l->left=NULL;
    l->right=NULL;
    l->parent=w;
    r->left=NULL;
    r->right=NULL;
    r->parent=w;
    w->left=l;
    w->right=r;
    
}

TreeNode* treeSearch(TreeNode* v, int k)
{
    if (isExternal(v))
        return v;
    if(k==v->key)
        return v;
    else if(k<v->key)
        return treeSearch(v->left,k);
    else
        return treeSearch(v->right,k);
}

int findElement(TreeType* T, int k)
{
    TreeNode* w = treeSearch(T->root, k);
    if(isExternal(w))
        return 0;
    else
        return w->key;
}

void insertItem(TreeType* T, int k)
{
    TreeNode* w = treeSearch(T->root, k);
    if(!isExternal(w))//isInternal 대신 사용
        return;
    else
    {
        w->key=k;
        expandExternal(w);
    }
}

TreeNode* sibling(TreeNode* z)
{
    if(z->parent->left==z)
        return z->parent->right;
    else
        return z->parent->left;
}

TreeNode* reduceExternal(TreeType* T, TreeNode*z) //175 page
{
    TreeNode* w = z->parent;
    TreeNode* g = w->parent;
    TreeNode* zs = sibling(z);
    zs->parent=g;
    
    if(g==NULL) //g가 null이면 zs 가 루트가됨
    {
        T->root=zs;
    }
    else
    {
        if(w==g->left)
            g->left=zs;
        else //if w==g->right
            g->right=zs;
    }
}

TreeNode* inOrderSucc(TreeNode* w)
{
    w=w->right;
    while(w->left!=NULL)
        w=w->left;
    return w;
}

int removeElement(TreeType* T, int k)
{
    TreeNode* w=treeSearch(T->root, k);
    if(isExternal(w))
        return 0;
    TreeNode* z, *y;
    z=w->left; 
    if(!isExternal(z))
        z=w->right;
    if(isExternal(z))
        reduceExternal(T,z);
    else
    {
        z = inOrderSucc(w);
        y= z->parent;
        w->key=y->key;
        reduceExternal(T, z);
    }
    return k;
}

void preOrder(TreeNode* root)
{
    if (isExternal(root))
        return;
    printf("[%d] ",root->key);
    preOrder(root->left);
    preOrder(root->right);
}

int main()
{
    TreeType* T = (TreeType*)malloc(sizeof(TreeType));
    initTree(T);
    
    insertItem(T,9);
    insertItem(T,2);
    insertItem(T,1);
    insertItem(T,7);
    insertItem(T,5);
    insertItem(T,3);
    insertItem(T,4);
    insertItem(T,8);
    insertItem(T,15);
    insertItem(T,11);
    preOrder(T->root); printf("\n");
    getchar();
    
    printf("삭제할 키 입력: ");
    int key;
    scanf("%d", &key);
    removeElement(T,key);
    preOrder(T->root); 

    return 0;
}
