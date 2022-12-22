#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    
    int n;
    scanf("%d", &n);
    int len;
    char word[101];
    int count = 0;
    for (int i = 0; i < n; i++){
        int alpha[26] = {0,};
        scanf("%s", word);
        len = strlen(word);
        int j = 0;
        alpha[word[j]-'a']++;
        for (j = 1; j < len; j++)
        {
            if(word[j] == word[j-1]){
                continue;
            }
            else{
                alpha[word[j]-'a']++;
            }
            if(alpha[word[j]-'a']>1)
                break;
        }

        for(j = 0; j<26;j++){
            if(alpha[j]>1){
                break;
            }
        }
        if(j>25){
            count++;
        }  
    }
    printf("%d",count);
    return 0;
}