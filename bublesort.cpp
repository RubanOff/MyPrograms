#include <stdio.h>
#include <stdlib.h>
//Bubble sort through dinamic massive
int main()
{
    int n;
    scanf("%d", &n);
    int *data = (int*) calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) 
    {
        scanf("%d", &data[i]);
    }

    for(int i = 0; i < n - 1; i++)
    {
        for(int j = 0; j < n - 1 - i; j++)
        {
            if(data[j] > data[j+1])
            {
                int temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;

            }

        }

    }
    for(int i = 0; i < n; i++)
    {
        printf("%d ", data[i]);
    }
    free(data);
}