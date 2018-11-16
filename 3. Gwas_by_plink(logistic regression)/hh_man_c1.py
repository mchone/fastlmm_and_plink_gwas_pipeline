#!/public/home/hwu/mcbin/python2.7.12/bin/python2.7
import sys
#import numpy as np
import csv
data = []
with open(sys.argv[1]) as f:
 f_csv = csv.reader(f)
 headers = next(f_csv)
 data = [[row[0], int(row[2]), float(row[3])] for row in f_csv]

import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from geneview.gwas import manhattanplot

###adjust figsize
plt.figure(figsize=(10,2))
#ax = manhattanplot(data, xlabel="Chromosome", ylabel="-Log10(P-value)")
#xtick = ['Chr' +c for c in map(str, range(1,12))]
#xtick_label_set = set(xtick)(add to manhattanplot)
#color="#f28b1e,#9a0dea,#ea0dcc,#63b8ff"(add to manhattanplot below)

ax = manhattanplot(data, xlabel="Chromosome", ylabel="-Log10(P-value)", s=5, alpha=0.5)
######adjust y-axe 

plt.ylim(0,15)

plt.axhline(y=7.94,linewidth=0.4 ,color='k', linestyle='dashed')

prefix = (sys.argv[1].split("."))[0]

plt.savefig(prefix + ".png",dpi=1200)
#plt.savefig(prefix + ".svgz")
#plt.savefig(prefix + ".")
