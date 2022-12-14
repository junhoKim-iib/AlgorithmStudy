#include<stdio.h>
int main(){
	int n,cut,count = 0;
	scanf("%d", &n);
	cut = n;
	do {
		n = (n % 10) * 10 + (n % 10 + n / 10)%10;
		count++;
	} while (n != cut);
	printf("%d", count);
	return 0;
}