#include <iostream>
#include <cstring>
#include <stdio.h>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

int random(int x)
{
    srand(time(NULL));
    return rand() % x;
}
void thempt(int n[100000], int &a, int p)
{
    if(p>=0 && p<=a)
    {
    for(int i=a;i>p-1;i--)
    {
        n[i]=n[i-1];
    }
    n[p-1] = random(10);
    a++;
    }
}

int main()
{
    ifstream input("cheninp.text");
    fstream output;
    output.open("chenout.text",ios::out);

    int a,n[100000],p;
    input >> a;

    for(int i=0;i<a;i++)
    {
        input >> n[i];
    }
    input >> p;

    thempt(n,a,p);
    for(int i=0;i<a;i++)
    {
        output << n[i] << " ";
    }

    input.close();
    output.close();
    return 0;
}
