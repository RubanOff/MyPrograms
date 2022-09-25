#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//Программа, которая проверяет слова на повторяющиеся буквы
bool check(char data[],int len)
{
    for (int i = 0; i < len - 1; i++)
    {
        if (data[i] == data[i + 1])
        {
            return 1;
        }
    }
    return 0;
}
int main()
{
    char data[] = {};
    scanf("%s", data);
    int len = strlen(data);

    if (check(data, len) == 1)
    {
        printf("True\n");
    }
    else
    {
        printf("False\n");
    }

    return 0;
}