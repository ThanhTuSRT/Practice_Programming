#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cstring>


using namespace std;

int main()
{
    ifstream input("dnxinp.text");
    fstream output;
    output.open("dnxout.text", ios::out);

    string s;
    getline(input,s);
    int k;
    int dodai=s.length();
    cout << "Nhap k: ";
    cin >> k;
    string s1="";
    for(int i=k;i<=dodai;i++)
    {
        s1=s1+s[i];
    }
    for(int i=0;i<k;i++)
    {
        s1=s1+s[i];
    }
    output << s1;
    input.close();
    output.close();
    return 0;
}
