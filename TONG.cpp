#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int main(){
    int a[100000];
    ifstream input("tongin.text");
    fstream output;
    output.open("tongout.text", ios::out);

    int n,c,b;
    int am=0;
    int duong=0;
    input >> n;
    for(int i = 0;i<n;i++){
        input >> a[i];
    }
    for(int i = 0;i<n;i++){
        if(a[i] < 0) {
               am=am+a[i];
        }
        else {
            duong=duong+a[i];
        }
    }

    int tong=am+duong;
    output << "Tong cac so am la " << am << endl;
    output << "Tong cac so duong la " << duong << endl;
    output << "So tien lai la " << tong;
    input.close();
    output.close();
    return 0;
}
