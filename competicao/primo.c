#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

int primo(int n){
  int i;

  for(i = 2; i < n; i ++)
    if (n % i == 0)
      return 0;
  
  return 1;
}


int main(int argc, char *argv[])
{
  int n = strtol(argv[1], NULL, 10);;
  
  if(n ==2)
	printf("2\n");
  else
	printf("%d\n", primo(n));
}

