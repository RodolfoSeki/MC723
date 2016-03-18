#!/bin/bash
while true; do
	ps -C ffmpeg -o pid=,%mem=,vsz= >> mem.log
  gnuplot gnuplot.script
  sleep 1
done
