#include <stdio.h>
#include <fstream>
#include <iostream>
#include <cstring>

using namespace std;
int main()
{
    ifstream input("xlnxauinp.text");
    fstream output;
    output.open("xlnxauout.text", ios::out);

    string s;
    int t=0,max=0,d=0;
    input >> s;

    /*for(int i=0;i<s.length();i++)
    {
        if(isdigit(s[i]))
        {
            d=d+1;
        }
    }*/
    for(int i=0;i<s.length()+1;i++)
    {
        if(isdigit(s[i]))
        {
            t=t*10+char(s[i]-48);
        }
        else
        {
            if(t>max)
            {
                max=t;
                d=0;
            }
            else
            {
                if(t==max)
                {
                    d=d+1;
                    t=0;
                }
            }
        }
    }
    output << max << " " << endl << d;
    input.close();
    output.close();
    return 0;
}
