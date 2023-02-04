#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int eq(int a,int b, int c)
{
float root1,root2,delta;

delta =(b * b) - (4 * a *c);

if (delta  == 0)
{
root1 =(-b/2*a);
printf("la racine est : %.2f" ,root1);
}
else if (delta > 0)
{
root1 = (-b + sqrt(delta) / (2 * a));
root2 = (-b - sqrt(delta) / (2 * a));
printf("les racines sont : %.2f ; %.2f",root1,root2);
}
else
{
printf("pas de racine");
}
return 0;
}
int main()
{
float a,b,c;
printf("Saisissez les coefficients de l'equation:");
printf("A :?");
scanf("%f",&a);
printf("B :?");
scanf("%f",&b);
printf("C :?");
scanf("%f",&c);

eq(a,b,c);
return 0;
}
