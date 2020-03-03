#include <stdio.h>

int rndm()
{
  long v0 = rand()%10;
  long v1 = rand()%10*v0;
  long v2 = (rand()%100+v1)%10;
  return (rand()%10+v2);
}

int main()
{
  char v5[] = 'pD#gN[3I';
  printf("FLAG: ");
  for ( int i = 0; i <= 26; ++i )
  {
    long v5 = rndm();
    long v1 = rndm();
    char v3 = v5[i];
    if ( (((v1 >> 31) + v1) & 1) != v1 >> 31 )
      v3 = v5 + (v5 ^ v3);
    putchar((v5 ^ v3));
  }
  return putchar(10);
}
