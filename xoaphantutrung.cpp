#include <stdio.h>
#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int main()
{
    int n;
    ifstream input("xoaptinp.text");
    fstream output;
    output.open("xoaptout.text", ios::out);

    string s;
    getline(input,s);
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
    output << s;
    input.close();
    output.close();
    return 0;
}
