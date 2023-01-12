#include <stdio.h>
#include <iostream>
#include <cstring>

using namespace std;
int main(){
    int a,b,c;
	cout << "Nhap vao so thu nhat: ";
	cin >> a;
	cout << "Nhap vao so thu hai: ";
	cin >> b;
	cout << "Nhap vao so thu ba: ";
	cin >> c;

	int max=a;
	if(max<b) max=b;
	if(max<c) max=c;
	cout << "So lon nhat la " << max;
	return 0;
}
