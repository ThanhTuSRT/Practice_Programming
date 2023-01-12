#include <stdio.h>
#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int main()
{
    cout << "Nhap xau cua ban" << endl;
    string s;
    getline(cin,s);
    int i=1,j=i+1,d=s.length();
    for(int i= 1;i<s.length();i++)
    {
            if(s[i]==s[j+1])
            {
                s.erase(s.begin() + i+1);
                d=d+1;
                j=i+1;
            }
            else
            {
                i=i+1;
                j=i+j;
            }

    }
    cout << s;
    return 0;
}
