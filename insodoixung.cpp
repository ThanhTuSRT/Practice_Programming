#include <iostream>
#include <stdio.h>
#include <cstring>
#include <sstream>

using namespace std;

int KT(int x)
{
    stringstream so1;
    so1 << x;
    string so = so1.str();
    string s1 = "";
    int dodai=so.length();
    for(int i=1;i<dodai+1;i++)
    {
        s1=s1+so[dodai-i];
    }
    if(s1!=so)
        {
            return false;
        }
    return true;
}

int main()
{
    int a;
    cout << "Nhap a: ";
    cin >> a;
    cout << "Cac so doi xung tu 0 den " << a << " la: ";
    for(int i=0;i<=a;i++)
    {
        if(KT(i)==true)
            cout << i << " ";
    }
    return 0;
}
