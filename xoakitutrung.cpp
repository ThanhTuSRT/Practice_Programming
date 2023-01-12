#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cstring>

using namespace std;

int main()
{
    ifstream input("xoakttrunginp.text");
    fstream output;
    output.open("xoakttrungout.text",ios::out);

    string s;
    getline(input,s);

    int i=0,t=0,d=s.length(),j=i+1;
    for(int i=0;i<s.length();i++)
    {
        j=i+1;
        while(s[i]==s[j])
        {
            s.erase(s.begin() + i);
        }
    }

    /*for(int i=1;i<d;i++)
    {
       output << s[i];
    }*/
    output << s;
    input.close();
    output.close();
    return 0;
}
