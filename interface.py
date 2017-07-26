import sys
from get_metric_data import Build as MetricBuild


ticker = sys.argv[1]
periods = sys.argv[2].split(',')
periodtickermetric = MetricBuild(ticker, periods)
# print periodtickermetric.ticker
