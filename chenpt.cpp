#include <stdio.h>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;

int random(int a)
{
    srand(time(NULL));
    return rand() % a;
}

void thempt(int n[10000],int &a,int p)
{
    if(p>0 && p<=a)
    {
        for(int i=a;i>p-1;i--)
        {
            n[i]=n[i-1];
        }
        n[p-1]= random(10);
        a++;
    }
}
int main()
{
    int a,n[10000];
    cout << "Nhap a: ";
    cin >> a;

    cout << "Nhap mang cua ban: ";
    for(int i=0;i<a;i++)
    {
        cin >> n[i];
    }
    cout << "Mang ban vuan nhap la: ";
    for(int i=0;i<a;i++)
    {
        cout << n[i] << " ";
    }
    cout << endl;
    cout << "Nhap vi tri p: ";
    int p;
    cin >> p;

    thempt(n,a,p);
    for(int i=0;i<a;i++)
    {
        cout << n[i] << " ";
    }

    return 0;
}
