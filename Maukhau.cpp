#include <iostream>
#include <stdio.h>
#include <cstring>
#include <fstream>
#include <stdlib.h>
#include <string>

using namespace std;

int main()
{
    ifstream input("Matkhau.inp");
    fstream output;
    output.open("Matkhau.out", ios::out);

    string a,s="",s1="";
    int tong = 0,b = 1;
    input >> a;

    a.insert(a.begin() + 0,'.');
    for(int i=0;i<a.length()+1;i++)
    {
        s=s+a[a.length()-b];
        b++;
        if(s[i]!='.')
              s1=s1+s[i];
        else
        {
            tong = tong + atoi(s1.c_str());
            s1 = "";
        }
    }
    output << tong;
    input.close();
    output.close();
    return 0;
}
