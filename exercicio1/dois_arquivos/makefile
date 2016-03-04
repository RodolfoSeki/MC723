all: primo

primo: main.o calc_primo.o
	gcc main.o -O1 calc_primo.o -o primo
	
main.o: main.c
	gcc -c main.c

calc_primo.o: calc_primo.c
	gcc -c calc_primo.c

clean:
	rm *o primo
