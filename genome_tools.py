#!/usr/bin/python
try:
    import genome
    import genome_tools_config
except:
    print "it appears that genome_tools.py is not in the same directory as genome.py and genome_tools_config.py"
import sys
import subprocess

config = genome_tools_config

#debug
def print_input(*arg):
    subprocess.call(
"""
echo """ + '"' + " ".join(arg) + '"',
shell = True
    )
#/debug


def main():
    program = sys.argv[1]
    arguments = sys.argv[2:]
    command = program + "('" + "','".join(arguments) + "')"
    eval(command)


def nucmer_plot(qgenome_file_loc,tgenome_file_loc):
    subprocess.call(
"""
nucmer -l 100 -c 1000 """ + tgenome_file_loc + " " + qgenome_file_loc + """
dnadif -d out.delta
mummerplot --small --fat --postscript out.1delta
ps2pdf out.ps out.pdf""", shell = True
    )


def fqstats(fastq_location):
    """computes basic summary stats for fastq file"""
    lenlist = []
    fastq = open(fastq)
    fastq_line = fastq.readline()
    counter = 0
    while fastq_line != "":
        if counter % 4 == 1:
            lenlist.append(len(fastq_line))
        counter = counter + 1
        fastq_line = fastq.readline()
    read_number = len(lenlist)
    basepairs = sum(lenlist)
    mean_length = basepairs / read_number
    lenlist.sort()
    lenlist.reverse()
    median_length = lenlist[read_number / 2]
    percentile25 = lenlist[read_number / 4]
    percentile75 = lenlist[read_number * 3 / 4]
    nsum = 0
    n25 = False
    n50 = False
    n75 = False
    for length in lenlist:
        nsum = nsum + length
        if nsum > basepairs / 4 and not n25:
            n25 = nsum
        if nsum > basepairs / 2 and not n50:
            n50 = nsum
        if nsum > basepairs * 3 / 4 and not n70:
            n75 = nsum
    print str(read_number) + " reads"
    print "total basepairs=" + str(basepairs)
    print "median length=" + str(median_length)
    print "mean length=" + str(mean_length)
    print "25% of reads >" + str(percentile25)
    print "75% of reads >" + str(percentile75)
    print "n25=" + str(n25)
    print "n50=" + str(n50)
    print "n75=" + str(n75)
    
    
















if __name__ == "__main__":
    main()
