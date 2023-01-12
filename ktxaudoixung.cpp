#include <iostream>
#include <fstream>
#include <cstring>
#include <stdio.h>

using namespace std;

int main()
{
    ifstream input("ktinp.text");
    fstream output;
    output.open("ktout.text", ios::out | ios::in);

    string s;
    getline(input,s);
    int d=0;
    /*for(int i=0;i<s.length();i++){
        input >> s;
    }*/
    for(int i=0;i<s.length();i++)
    {
        while(isdigit(s[i]))
        {
            s.erase(s.begin() + i);
        }
    }
    for(int i=0;i<s.length();i++)
    {
        while(s[i] == 32)
        {
            s.erase(s.begin() + i);
        }
    }

    string str = "";
    string n;
    for(int i=0;i<s.length();i++)
    {
        n = toupper(s[i]);
        str=str+n;
        output << n;
    }
    string s1="";
    int dodai = str.length();
    for(int i =1;i<dodai+1;i++)
        {
              s1=s1+str[dodai-i];
        }
    if(s1==str)
        {
                output << endl << "Xau " << str << " doi xung";
        }
    else
        {
                output << endl << "Xau " << str << " khong doi xung";
        }
    input.close();
    output.close();
    return 0;
}
