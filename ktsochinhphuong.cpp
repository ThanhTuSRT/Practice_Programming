#include <iostream>
#include <cstring>
#include <stdio.h>

using namespace std;
int KTSCP(int x)
{
    for(int i=0;i<10000000;i++)
    {
        if(i*i==x)
             return true;
    };
}
int main()
{
    int a,n[100000];
    cout << "Nhap a: ";
    cin >> a;

    cout << "Nhap day so cua ban: ";
    for(int i=0;i<a;i++)
    {
        cin >> n[i];
    }
    int b;
    cout << "So chinh phuong la: ";

    for(int i=0;i<a;i++)
    {
        if(KTSCP(n[i])==true)
            cout << n[i] << " ";
    }
    return 0;
}
