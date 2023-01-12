#include <iostream>
#include <fstream>
#include <cstring>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    ifstream input("bmiinp.text");
    fstream output;
    output.open("bmiout.text",ios::out);

    float w,h,bmi;
    input >> w;
    input >> h;
    bmi = w/(h*h);

    output << "BMI = " << roundf(bmi*10)/10;
    input.close();
    output.close();
    return 0;
}
