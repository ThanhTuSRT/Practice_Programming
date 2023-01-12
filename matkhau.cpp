#include <iostream>
#include <fstream>
#include <cstring>
#include <stdio.h>
#include <sstream>
#include <cstdlib>

using namespace std;

int main()
{
    ifstream input("MATKHAUVAO.text");
    fstream output;
    output.open("MATKHAURA.text", ios::out);

    int tong=0,n;
    string s,a;
    getline(input,s);
    for(int i=0;i<s.length();i++)
    {
        if(isdigit(s[i]))
        {
            a = s[i];
            char* c = new char[a.length()];
            strcpy(c,a.c_str());
            n = atoi(c);
            tong =tong+n;
        }
    }
    output << tong;
    input.close();
    output.close();
    return 0;
}
