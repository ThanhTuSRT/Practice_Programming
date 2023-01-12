#include <iostream>
#include <fstream>
#include <cstring>
#include <stdio.h>

using namespace std;

int main()
{
    ifstream input("ktsctinp.text");
    fstream output;
    output.open("ktsctout.text",ios::out);

    int n[10000],a=0,b=0;
    for (int i=0;i<5;i++)
    {
        input >> n[i];
        output << n[i] << " ";
    }

    output << endl;
    for(int i=0;i<5;i++)
    {
        b = b + n[i];
    }
    int dieukien,so=0;
    for(int i=0;i<5;i++)
    {
        if(n[i+1]-n[i]==n[i+2]-n[i+1])
        {
            so = so+1;
        }
    }
    if(so == 3)
    {
        for(int i=0;i<5;i++)
        {
         a = n[i+1] - n[i];
         break;
        }
        output << "Day so ban da nhap la cap so cong tien, voi cong sai =" << a << endl;
        output << "Tong cua cap so cong tren =" << b;
    }
    else
    {
        output << "Day so ban da nhap khong phai la cap so cong tien";
    }
    input.close();
    output.close();
    return 0;
}
