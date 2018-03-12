#
# com-youtube.ungraph - in-degree Distribution. G(1134890, 2987624). 164645 (0.1451) nodes with in-deg > avg deg (5.3), 82164 (0.0724) with >2*avg.deg (Mon Mar 12 12:41:55 2018)
#

set title "com-youtube.ungraph - in-degree Distribution. G(1134890, 2987624). 164645 (0.1451) nodes with in-deg > avg deg (5.3), 82164 (0.0724) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.com-youtube.ungraph.png'
plot 	"inDeg.com-youtube.ungraph.tab" using 1:2 title "" with linespoints pt 6
