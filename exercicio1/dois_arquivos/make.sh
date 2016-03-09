gcc -c calc_primo.c

gcc -c main.c

gcc main.o calc_primo.o -o primo

rm *.o
