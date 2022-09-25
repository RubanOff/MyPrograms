#include <stdio.h>
//Программа, которая возводит числа k и q, введенные с клавиатуры, в степень до 10
int power(int number, int degree);

int main()
{
    int k, q;
    scanf("%d %d", &k, &q);
    for (int i = 0; i < 10; ++i)
    {
        printf("%d %d %d\n", i, power(k,i), power(q,i));
    }
    return 0;
}

int power(int number, int degree)
{
    
    int j;
    j = 1;
    for (int i = 1; i <= degree; ++i)
    {
        j = j * number;
    }
    return j;

}