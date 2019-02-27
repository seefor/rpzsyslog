import re
import sys
import argparse

__author__ = 'sifbaksh@gmail.com'
__version__ = "$Revision: 1.6 $"
'''
TODO
- nothing

USAGE
python syslog_parser.py -i syslog.log -o customerxyz.txt

'''
# This will allow us to pass command line arguments
# FOR HELP - python syslog_test.py --h
parser = argparse.ArgumentParser(description='RPZ Syslog Parser')
parser.add_argument('-i', '--input', help='Input file name', required=True)
parser.add_argument('-o', '--output', help='Output file name', required=True)
args = parser.parse_args()

input_file = open(str(args.input))
n = 0
output_file = open(str(args.output), "w")
for line in iter(input_file):
    m = re.search('(?<=\s\[A\]\svia\s)(\S*)(?=\"\"\"$)', line)
    if m:
        n = n + 1
        print m.group(1)
        output_file.write(m.group(1))
        output_file.write("\n")

print "[+] Found %s domains in : %s" % (n, str(args.input))
print "[+] Please check %s for the output!" % str(args.output)

# # show values ##
print ("Input file: %s" % args.input )
print ("Output file: %s" % args.output )

output_file.close()
input_file.close()
