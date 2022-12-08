#include<stdio.h>
typedef struct {
	int zero;
	int one;
}ZeroOne;
ZeroOne count[41];
void fibonacci() {
	int fibo[41] = { 0, };
	fibo[0] = 0;
	fibo[1] = 1;
	count[0].zero = 1;
	count[1].one = 1;
	for (int i = 2; i <= 40; i++) {
		fibo[i] = fibo[i - 1] + fibo[i - 2];
		count[i].zero = count[i - 1].zero + count[i - 2].zero;
		count[i].one = count[i - 1].one + count[i - 2].one;
	}
}

int main()
{
	int test,num;
	scanf("%d", &test);
	fibonacci();
	for (int i = 0; i < test; i++){
		scanf("%d", &num);
		printf("%d %d\n", count[num].zero, count[num].one);
	}
	return 0;
}