#include<stdio.h>
#include<string.h>
int main()
{
    char str[1000000];
    scanf("%[^\n]", str);
    char* p = strtok(str, " ");
    int count = 0;
    if (p == NULL) {
        printf("%d", 0);
        return 0;
    }
    else
        while (p != NULL) {
            p = strtok(NULL, " ");
            count++;
        }
    printf("%d", count);

    return 0;
}