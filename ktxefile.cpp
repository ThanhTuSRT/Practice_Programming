#include <iostream>
#include <cstring>
#include <fstream>
#include <stdio.h>

using namespace std;

int main()
{
    ifstream input("ktxeinp.text");
    fstream output;
    output.open("ktxeout.text",ios::out);

    int n[10000],a,gt=0;
    input >> a;

    for(int i=1;i<a+1;i++)
    {
        input >> n[i];
    }

    for(int i=1;i<a+1;i++)
    {
       gt=gt+n[i];
    }
    output << gt << endl;

    for(int i=1;i<a+1;i++)
    {
        if(n[i]>20)
            output << i << " ";
    }
    input.close();
    output.close();
    return 0;
}
