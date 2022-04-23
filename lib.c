#include "lib.h"

int ints(int val1, int val2)
{
    int sum = val1 + val2;
    printf("result from c: %d\n", sum);
    return sum;
}

float floats(float val1, float val2)
{
    float sum = val1 + val2;
    printf("result from c: %.9g\n", sum);
    return sum;
}

double doubles(double val1, double val2)
{
    double sum = val1 + val2;
    printf("result from c: %.17g\n", sum);
    return sum;
}

char *strings(char *str1, char *str2)
{

    unsigned long int str1_len = strlen(str1);
    unsigned long int str2_len = strlen(str2);

    char *coctinated_str = (char *)malloc(sizeof(char) * (str1_len + str2_len));
    for (unsigned long int i = 0; i < str1_len; i++)
    {
        coctinated_str[i] = str1[i];
    }
    for (unsigned long int i = 0; i < str2_len; i++)
    {
        coctinated_str[i + str1_len] = str2[i];
    }

    printf("result from c: %s\n", coctinated_str);
    return coctinated_str;
}
