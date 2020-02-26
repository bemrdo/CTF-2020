#include <stdio.h>
#include <string.h>

void print(char a, int b, char c[])
{
  printf("a = %c\n", a);
  printf("b = %d\n", b);
  printf("c = %s\n", c);
}

int main(int argc, char *argv)
{
  char a;
  int b;
  char c[16];

  a = 'A';
  b = 0xd3c0d3; //13877459 desimal
  strcpy(c, "testing");

  print(a, b, c);

  return 0;
}
