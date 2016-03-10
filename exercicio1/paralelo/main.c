#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int primo(int n);

int main(int argc, char *argv[]){
  int i, soma, n = strtol(argv[1], NULL, 10);;
  soma =0;

  #pragma omp parallel for
  for(i = 2; i < n; i++)
	if (primo(i))
	  #pragma omp atomic
	  soma++;
  
  printf("Existem %d primos entre 1 e %d\n", soma, n);
}
