all: primo


primo: main.o calc_primo.o
	gcc main.o -fopenmp calc_primo.o -o primo
	
main.o: main.c
	gcc -fopenmp -c main.c

calc_primo.o: calc_primo.c
	gcc -fopenmp -c calc_primo.c

clean:
	rm primo
