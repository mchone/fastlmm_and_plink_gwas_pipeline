#!/public/home/hwu/mcbin/python2.7.12/bin/python2.7
import sys
import csv
data = []
with open(sys.argv[1]) as f:
 f_csv = csv.reader(f)
 headers = next(f_csv)
 pvalue = [float(row[3]) for row in f_csv]

import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from geneview.gwas import qqplot

ax = qqplot(pvalue, color="#02cde8", xlabel="Expected p-value(-log10)", ylabel="Observed p-value(-log10)")

prefix = (sys.argv[1].split("."))[0]

plt.savefig(prefix + "_qqplot.png",dpi=900)
#plt.savefig(prefix + "_qqplot.svgz")
