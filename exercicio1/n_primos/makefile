all: primo

primo: main.o calc_primo.o
	gcc -pg main.o calc_primo.o -o primo
	
main.o: main.c
	gcc -c main.c

calc_primo.o: calc_primo.c
	gcc -c calc_primo.c

clean:
	rm primo
