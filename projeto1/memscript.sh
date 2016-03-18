#!/bin/bash
while true; do
	ps -C ffmpeg -o pid=,%mem=,vsz= >> /home/klox/Programas/MC723/projeto1/mem.log
	gnuplot /home/klox/Programas/MC723/projeto1/gnuplot.script
	sleep 1
done
