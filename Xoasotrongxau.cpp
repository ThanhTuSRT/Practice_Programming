#include <stdio.h>
#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("xauinp.text");
    fstream output;
    output.open("xauout.text", ios::out);

    string s;
    getline(input,s);
    int d=0;
    for(int i=0;i<s.length();i++){
        input >> s;
    }
    for(int i=0;i<s.length();i++)
    {
        if(isdigit(s[i]))
        {
            d=d+1;
        }
    }
    for(int i=0;i<s.length();i++)
    {
        while(isdigit(s[i]))
        {
            s.erase(s.begin() + i);
        }
    }
    output << s << endl;
    output << d;

input.close();
output.close();
return 0;
}
