all: primo

primo: main.c calc_primo.c
	gcc main.c -lm -mtune=intel -O1 -fopenmp calc_primo.c -o primo

clean:
	rm primo
