#include <iostream>
#include <fstream>
#include <cstring>
#include <stdio.h>

using namespace std;

int KTSCP(int x)
{
    for(int i=0;i<1000000;i++)
    {
        if(i*i==x)
            return true;
    }
}
int main()
{
    ifstream input("kt.text");
    fstream output;
    output.open("ktout.text",ios::out);

    int a;
    input >> a;
    int n[a];
    for(int i=0;i<a;i++)
    {
        input >> n[i];
    }
    for(int i=0;i<a;i++)
    {
        if(KTSCP(n[i])==true)
        {
            output << n[i] << " ";
        }
    }
    input.close();
    output.close();
    return 0;
}
