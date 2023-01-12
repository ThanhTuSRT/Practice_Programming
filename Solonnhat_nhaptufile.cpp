#include <stdio.h>
#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;
int main(){
int a[100000],n;
    ifstream input("solonnhatinp.text");
    fstream output;
    output.open("solonnhatout.text", ios::out);

    input >> n;
    for(int i=1;i<n+1;i++){
        input >> a[i];
    }
    int max=a[1];
	for(int i=1;i<n+1;i++){
	  if(max<a[i]) max = a[i];
	}
	output << "So lon nhat la " << max;
    input.close();
    output.close();
    return 0;
}
