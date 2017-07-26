## compute_input.py

import sys, json, numpy as np

# import sys, json, numpy as np
# from get_metric_data import Build as MetricBuild
# #Read data from stdin
# def read_in():
#     lines = sys.stdin.readlines()
#     #Since our input would only be having one line, parse our JSON data from that
#     return json.loads(lines[0])
#
# def main():
#     #get our data from read_in()
#     ticker, periods = read_in()
#     periodtickermetric = MetricBuild(ticker, periods)
#     # print periodtickermetric
#     # print "End Date: " + periodtickermetric.end
#     # print "Total Income This Period " + str(periodtickermetric.income_total)
#     # print "Holding Period Return " + str(float(periodtickermetric.hprr) -1)
#     # print "Arithmetic Mean Return " + str(periodtickermetric.amr)
#     # print "Holding Period Return (Multiplicative): " + str(float(periodtickermetric.hprr_total) -1)
#     # print "Geometric Mean Return: " + str(periodtickermetric.gmr)
#     return str(periodtickermetric)
#
#
# # #start process
# if __name__ == '__main__':
#     main()

# #Read data from stdin
# def read_in():
#     lines = sys.stdin.readlines()
#     #Since our input would only be having one line, parse our JSON data from that
#     return json.loads(lines[0])
#
# def main():
#     #get our data as an array from read_in()
#     lines = read_in()
#
#     #create a numpy array
#     np_lines = np.array(lines)
#
#     #use numpys sum method to find sum of all elements in the array
#     lines_sum = np.sum(np_lines)
#
#     #return the sum to the output stream
#     print lines_sum
#
# #start process
# if __name__ == '__main__':
#     main()
# print sys.stdin.readlines()
# import fileinput
# for line in fileinput.input():
#   process(line)
# print sys.argv[1]
# print "1: " + sys.argv[0]
# print "2: " + sys.argv[1]
# print "3: " + sys.argv[2]

# periods = sys.argv[2].split(',')
# print periods

from get_metric_data import Build as MetricBuild
#Read data from stdin
ticker = sys.argv[1]
periods = sys.argv[2].split(',')
periodtickermetric = MetricBuild(ticker, periods)
print periodtickermetric.ticker

# for c in sys.argv[0]
# print "4: " + sys.argv[3]
# print "5: " + sys.argv[4]
