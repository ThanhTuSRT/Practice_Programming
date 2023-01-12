#include <iostream>
#include <fstream>
#include <cstring>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    float w,h,bmi;
    cout << "W = ";
    cin >> w;
    cout << "h = ";
    cin >> h;
    bmi = w/(h*h);

    cout << "BMI = " << roundf(bmi*10)/10;
    return 0;
}

