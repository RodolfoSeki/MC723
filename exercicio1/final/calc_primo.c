#include <omp.h>
#include <math.h>

int primo(int n)
{
  int i;
  
  if(n%2 == 0 && n!=2)
    return 0;
    
  
  for(i = 3; i <= sqrt(n); i +=2)
    if (n % i == 0)
      return 0;
  
  return 1;
}
