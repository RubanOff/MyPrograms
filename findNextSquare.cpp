#include <stdio.h>
#include <math.h>
//Программа выводит следующий квадрат(Input -> 121, Output -> 144; Input -> 120, Outpit -> -1)

long int findNextSquare(long int sq)
{
    double n;
    n = sqrt(sq);
    if (n == (int)n)
    {
       return (n+1)*(n+1); 
    }
    return -1;
}

int main()
{
    int sq;
    scanf("%d", &sq);
    printf("%ld\n", findNextSquare(sq));
}