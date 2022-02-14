#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0), cin.tie(0);

	int N;
	int X;
  int arr[10000];
  
	cin >> N >> X;
  
  //방법1
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		if (arr[i] < X) cout << arr[i]<<" ";
	}

  //방법2
  for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		if (a < X) cout << a<<" ";
	}
  
}
