#
# com-youtube.ungraph - clustering coefficient. G(1134890, 2987624). Average clustering: 0.0808  OpenTriads: 1465313402 (0.9979)  ClosedTriads: 3056386 (0.0021) (Mon Mar 12 12:41:55 2018)
#

set title "com-youtube.ungraph - clustering coefficient. G(1134890, 2987624). Average clustering: 0.0808  OpenTriads: 1465313402 (0.9979)  ClosedTriads: 3056386 (0.0021)"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Node degree"
set ylabel "Average clustering coefficient"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'ccf.com-youtube.ungraph.png'
plot 	"ccf.com-youtube.ungraph.tab" using 1:2 title "" with linespoints pt 6
