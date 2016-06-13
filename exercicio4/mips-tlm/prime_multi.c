#include <stdio.h>
#define LOCK_ADDRESS 0x6400000 /*endereço 104857600*/
#define MAX_DIV 10000


volatile int *lock=(int *) LOCK_ADDRESS;
volatile int vetor[MAX_DIV];
volatile int number_divs =0;
volatile int contador= 0;

void AcquireLock(){
        while (*lock);
}

void ReleaseLock(){
        *lock = 0;
}
main(){

    int n = 367567200;
    int i,limit,processador;

    AcquireLock();
    processador = contador++;
    ReleaseLock();
    limit = n/2;
    
    if(processador==0){
        i =2;
    }
    else{
        i = 3;
    }

    while(i <= limit){
        if(n%i==0) {
            AcquireLock();
            vetor[number_divs]=i;
            number_divs++;
            ReleaseLock();
        }
        i+=2;
    }
    
    if(processador == 0){
        printf("O numero %d tem %d divisores\n",n,number_divs);
        for(i=0;i<number_divs;i++){
           printf("%d ",vetor[i]);
        }
        printf("\n");
    }
    return 0;
}

