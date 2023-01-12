#include <iostream>
#include <cstring>
#include <stdio.h>

using namespace std;

int main(){
    int a;
    cout << "Nhap a: ";
    cin >> a;
    cout << "Bang nhan " << a << endl;
    for(int n=1;n<11;n++){
        cout << a << " x " << n << " = " << a*n << endl;
    }
   return 0;
}
