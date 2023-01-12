#include <fstream>
#include <stdio.h>
#include <cstring>
#include <iostream>

using namespace std;

bool SNT(int x)
{
    if(x<2)
        return false;
    for(int i=2;i<x-1;i++)
        {
           if(x%i==0)
           {
                return false;
           }
        }
    return true;

}

int main()
{
    int n[1000],a,t;
    cout << "Nhap so phan tu: ";
    cin >> a;
    cout << "Nhap day so nguyen: ";
    for(int i=0;i<a;i++)
    {
        cin >> n[i];
    }
    cout << "Day so vua nhap la: ";
    for(int i=0;i<a;i++)
    {
        cout << n[i] << " ";
    }
    cout << endl << "So chan: ";
    for(int i=0;i<a;i++)
    {
            if(n[i]%2==0)
            {
                cout << n[i] << " ";
            }
    }
    cout << endl;
    cout << "So nguyen to: ";
    for(int i=0;i<a;i++)
    {
        if(SNT(n[i])==true)
        {
            cout << n[i] << " ";
        }
    }
    cout << endl;
    cout << "Day so sau khi dao nguoc la: ";
    for(int i=1;i<a+1;i++)
    {
        cout << n[a-i] << " ";
    }


    cout << endl;
    cout << "So am: ";
    for(int i=0;i<a;i++)
    {
        if(n[i]<0)
            cout << n[i] << " ";
    }
    cout << endl;
    cout << "So duong: ";
    for(int i=0;i<a;i++)
    {
        if(n[i]>0)
            cout << n[i] << " ";
    }

    return 0;
}
