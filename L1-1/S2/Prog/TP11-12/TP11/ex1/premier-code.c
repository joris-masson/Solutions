#include <stdio.h>

int main ( )
{
    int x;
    printf(" quel mois ? ");
    scanf("%d", &x);
    if (x == 1)
      {printf("janvier ");}
    else if (x == 2)
      {printf("février ");}
   else if (x == 3)
      {printf("mars ");}
   else if (x == 4)
      {printf("avril ");}
   else if (x == 5)
      {printf("mai ");}
   else if (x == 6)
      {printf("juin ");}
   else if (x == 7)
      {printf("juillet ");}
   else if (x == 8)
      {printf("aout ");}
   else if (x == 9)
      {printf("septembre");}
  else if (x == 10)
      {printf("octobre ");}
  else if (x == 11)
      {printf("novembre ");}
  else if (x == 12)
      {printf("décembre");}
  else
      {printf ("erreur");}
     
    return 0;
  
}
