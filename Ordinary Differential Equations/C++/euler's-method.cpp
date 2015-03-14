#define f(x, y) (y - x) / (y + x)
#include<iostream>

void euler(double, double, double, double);
int main()
{
    euler(0.0, 1.0, 0.02, 0.1);
    return 0;
}

void euler(double x0, double y0, double h, double xn)
{
    double x, y;
    x = x0;

    std::cout << x0 << ", " << y0 << std::endl;
    while(x < xn)
    {
        y = y0 + h * f(x0, y0);
        x = x0 + h;
        std::cout << x << ", " << y << std::endl;
        x0 = x;
        y0 = y;
    }

}
