#include<iostream>

using namespace std;

void han_num(int n) {
	if (n < 100) {
		cout << n;
		return;
	}
	if (n == 1000) {
		cout << 144;
		return;
	}
	int han_cnt = 99;
	
	int n1 = 0, n2 = 0,n3 = 0;
	for (int i = 100; i <= n; i++) {
		int num = i;
		n1 = num % 10;
		num /= 10;
		n2 = num % 10;
		num /= 10;
		n3 = num % 10;

		if ((n2 - n1) == (n3 - n2))
			han_cnt++;
	}
	cout << han_cnt;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int input;
	cin >> input;

	han_num(input);
	return 0;
}