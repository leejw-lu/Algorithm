#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int height[9];
    int sum = 0;
    int rest = 0;

    for (int i = 0; i < 9; i++) {
         cin >> height[i];
         sum += height[i];
    }
    
    sort(height, height + 9);
    rest = sum - 100;

    for (int i = 0; i < 9; i++) {
	for (int j = i + 1; j < 9; j++) {
	     if (height[i] + height[j] == rest) {
	        height[i] = -1;
	        height[j] = -1;
	        goto EXIT;
	     }
	 }
     }

    EXIT:
    for (int i = 0; i < 9; i++) {
	 if (height[i]!=-1) cout << height[i] << '\n';
    }
}
