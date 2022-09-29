#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
//abcd -> A-Bb-Ccc-Dddd, qWeRty -> Q-Ww-Eee-Rrrr-Ttttt-Yyyyyy

int main()
{
    int n;
    char c;
    scanf("%d%c", &n, &c);
    char* data = (char*)calloc(n, sizeof(char));
    for (int i = 0; i < n; i++)
    {
        scanf("%c", data + i);
    }
    
    int k = (n*(n+1))/2 + (n - 1);
    char* output = (char*)calloc(k + 1, sizeof(char));
    k = 0;
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < i + 1; ++j)
        {
            output[k] = data[i];
            output[k] = tolower(output[k]);
            if (j == 0)
            {
                output[k] = toupper(output[k]);
            }
            k++;
        }
        
        if (i != n - 1) 
        {
            output[k] = '-';
            k++;
        }
    }
    printf("%s", output);
}