#include <stdio.h>
#include <stdlib.h>
//Программа выводит введенные символы, пока не встретит -1
int main()
{
    int n = 1, i = 0, num;
    int *data = (int*) calloc(1, sizeof(int));
    while(num != -1)
    {
        scanf("%d", &num);
        data[i++] = num;
        data = (int*) realloc(data, (n+1)*sizeof(int));
        n++;
    }

    for(int j = 0; j < i - 1; j++)
    {
        printf("%d ", data[j]);
    }
    free(data);
}

