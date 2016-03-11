#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <math.h>

int primo(int n){
  int i, j = sqrt(n);
  
  for(i = 2; i <= j; i++)
    if (n % i == 0)
      return 0;

  return 1;
}



int trial(int n_primo){
	int i,j,k;
	
	i =1;
	j =2;
	while(i < n_primo){
		if(primo(++j)){
			i++;
		}
	}
	
	
	return j;
}


int main(int argc, char *argv[])
{
  int n = strtol(argv[1], NULL, 10);;
  
  if(n==1)
	printf("2\n");
  else{
	printf("%d\n", trial(n));
  }
}

