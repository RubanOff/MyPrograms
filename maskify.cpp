#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//Программа, которая превращает все цифры в #, кроме последних четырех (4556364607935616 -> ############5616)
char *maskify (char *masked, const char *string)
{
    if (strlen(string) > 4) 
    {
        for(int i = 0; i < strlen(string); i++)
        {
            if (i < strlen(string) - 4)
            {
                masked[i] = '#';
            }
            else
            {
                masked[i] = string[i];
            }
        }
    }
    else
    {
        strcpy(masked, string);
    }
    return masked;
}

int main()
{
    const char str[] = "";
    char * mas = (char*)calloc(strlen(str) + 1, sizeof(char));
    printf("%s\n", maskify(mas, str));

    return 0;
}