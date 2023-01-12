#include <stdio.h>
#include <iostream>
#include <cstring>

using namespace std;
int main(){
    int a[10000],n,i;
    cout << "Nhap vao so phan tu: ";
    cin >> n;
    for(int i=1;i<n+1;i++)
    {
        cout << "Nhap so thu " << i << ": ";
        cin >> a[i];
    }

	int max=a[1];
	for(int i=1;i<n+1;i++){
	  if(max<a[i]) max = a[i];
	}
	cout << "So lon nhat la " << max;
	return 0;
}
