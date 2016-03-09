# Gera arquivo com saida de tempos do programa primo
self="${0##*/}"

[ $# -eq 1 ] || { echo "Uso: ./$self <nome_arquivo.out>"; exit 1; }

arquivo=$1

if [ -e "$1" ]; then
    rm $1
fi

for i in {1..50}; do
  echo "Rodando primo pela $i-ima vez"
  { time ./primo ; } 2>> $1
done

python2.7 media.py $1 50

exit 0
