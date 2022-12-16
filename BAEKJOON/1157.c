#include<stdio.h>
#include<string.h>
int main()
{
    char str[1000001]; 
    scanf("%s", str);
    int arr[26] = { 0, };
    int len = strlen(str);
    int big = 0;
    char flag = 0;
    for (int i = 0; i < len; i++) {
        if (str[i] >= 'a')
            arr[str[i] - 'a']++;
        else
            arr[str[i] - 'A']++;
    }
    for (int i = 1; i < 26; i++) {
        if (arr[big] < arr[i]) {
            big = i;
            flag = 0;
        }
        else if (arr[big]&&arr[big] == arr[i]) {
            flag = 1;
        }
    }
    if (flag)
        printf("?");
    else
        printf("%c\n", big+'A');
    return 0;
}