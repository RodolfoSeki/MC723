#include <stdio.h>

int primo(int n)
{
  int i;

  for(i = 2; i < n; i ++)
    if (n % i == 0)
      return 0;
  
  return 1;
}


main(int argc, char *argv[])
{
  int i, soma, n = strtol(argv[1], NULL, 10);;
  soma =0;

  for(i = 2; i < n; i++){
        if (primo(i))
          soma++;
  }

  printf("Existem %d primos entre 1 e %d\n", soma, n);
}

