#include <stdio.h>
#include <string.h>

int main()
{
  int b = 1;
  char c[16];

  gets(&c);

  if(strlen(c) != 8)
  {
    printf("ERROR: input harus 8\n");
  }
  else
  {
    if (b == 0xdeadf00d)
    {
      printf("You win\n");
    }
    else 
    {
      printf("You lose\n");
      printf("b = %d\n", b);
    }
  }

  return 0;
}
