#include <iostream>
using namespace std;

int main() {
	int arr[21];
	int reverse[21];

	int a, b;

	for (int i = 1; i <= 20; i++)  arr[i] = i;
	
	for (int i = 0; i < 10; i++) {
		cin >> a >> b;
		for (int j = a; j <= b; j++) {
			reverse[j] = arr[j];
		}
		int b2 = b;			//b--하면 for문안에 b가 변하게 되니까 b2설정.
		for (int j = a; j <= b; j++) {
			arr[j] = reverse[b2];
			b2--;
		}
	}

	//출력
	for (int i = 1; i <= 20; i++)  cout << arr[i] << " ";

	/*reverse배열 따로 만드는것 말고도 다른 방법으로는
        1. swap사용한 reverse함수만들기, 2. 내장함수reverse함수 이용*/

}
