#include <iostream>
#include <fstream>
#include <cstring>
#include <stdio.h>
#include <math.h>

using namespace std;

int min(int a[], int n)
{
    int min = a[0];
    for (int i = 1; i < n; i++)
        if (min > a[i])
            min = a[i];
    return min;
}
int max(int a[], int n)
{
    int max = a[0];
    for (int i = 1; i < n; i++)
        if (max < a[i])
            max = a[i];
    return max;
}

int main()
{
    ifstream input("THANHLY.INP");
    fstream output;
    output.open("THANHLY.OUT", ios::out);

    int n, m, a[100000], kq,tam=0;
    input >> n >> m;
    int b[m];
    for (int i = 0; i < m; i++)
    {
        input >> a[i];
    }
    for(int i = 0; i < m - 1; i++){
        for(int j = i + 1; j < m; j++){
            if(a[i] < a[j])
            {
                tam = a[i];
                a[i] = a[j];
                a[j] = tam;        
            }
        }
    }
    for(int i=0;i<m;i++)
    {
        b[i] = a[i]*(i+1);
    }
    kq = max(b,m);
    output << kq;
    input.close();
    output.close();
    return 0;
}