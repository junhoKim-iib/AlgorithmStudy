#include<stdio.h>
int main(){
	int n,k;
	scanf("%d %d", &n,&k);
	if (n == k)
		printf("==");
	else if (n > k)
		printf(">");
	else
		printf("<");
	return 0;
}