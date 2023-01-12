#include <iostream>
#include <cstring>
#include <fstream>
#include <stdio.h>

using namespace std;

int main()
{
    int n[10000],a,gt=0,dem=0;
    cout << "Nhap so xe: ";
    cin >> a;

    cout << "Nhap khoi luong cua tuong xe: ";
    for(int i=1;i<a+1;i++)
    {
        cin >> n[i];
    }

    for(int i=1;i<a+1;i++)
    {
       gt=gt+n[i];
    }
    cout << "Tong khoi luong la: " << gt << endl;

    for(int i=1;i<a+1;i++)
    {
        if(n[i]>20)
        {
            cout << "Vi tri xe vuot qua khoi luong quy dinh la: ";
            break;
        }
    }
    for(int i=1;i<a+1;i++)
    {
        if(n[i]>20)
            cout << i << " ";
        else
            dem=dem+1;
    }

    if(dem==a)
    {
        cout << "Khoi luong cua cac xe tren deu khong vuot qua khoi luong quy dinh.";
    }
    return 0;
}

