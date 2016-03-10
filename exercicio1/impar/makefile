all: primo

primo: main.o calc_primo.o
	gcc -O2 main.o -pg calc_primo.o -o primo
	
main.o: main.c
	gcc -pg -c main.c

calc_primo.o: calc_primo.c
	gcc -pg -c calc_primo.c

clean:
	rm primo
