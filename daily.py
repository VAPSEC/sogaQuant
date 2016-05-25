# -*- coding: utf-8 -*-
import os
import sys
import time

from quant.spider.MinData import *
from quant.spider.LhbData import *
from quant.spider.Index import *
from quant.spider.TouTiao import *
from quant.spider.TouTiaoDetail import *

from quant.stats.ElSearch import *
from quant.stats.Average import *
from quant.stats.LimitList import *
from quant.stats.MaCount import *
from quant.stats.RunTimeChange import *
from quant.stats.TdxAnalyse import *
from quant.stats.LhbCount import *


def get_tdx(indate):
    ffile = '/Users/solomon/Downloads/008/%s.xls' % date
    tfile = '/Users/solomon/Downloads/008/%s.csv' % date
    a = TdxAnalyse()
    a.run(ffile, tfile)


def get_factor(abc):
    os.system('php /htdocs/soga/trader/index.php Base get_fq_factor')


def get_video(abc):
    #while True:
        #block_time = int(self.tools.d_date('%H%M%S'))
        #os.system(' /bin/bash /htdocs/quant/soga/wdSpider/a.sh')
    TouTiaoSpider().run()
    #time.sleep(60)


def get_video_info(abc):
    #while True:
        #block_time = int(self.tools.d_date('%H%M%S'))
        #os.system(' /bin/bash /htdocs/quant/soga/wdSpider/a.sh')
    TouTiaoDetailSpider().run()


def get_es(abc):
    a = ElSearch(sys.argv)
    a.run()


def get_average(abc):
    a = Average(sys.argv)
    a.run()


def get_limit(abc):
    a = LimitList(sys.argv)
    a.run()


def get_macount(abc):
    a = MaCount(sys.argv)
    a.run()


#20分钟一次获取各股的长跌幅
def get_min_data(abc):
    s = MinDataSpider()
    s.run()


#5分钟一次获取各股的长跌幅
def get_change(abc):
    a = RunTimeChange(sys.argv)
    a.run()


def get_lhb_data(abc):
    LhbDataSpider().run()


def get_index_data(abc):
    IndexSpider().run()


def count_lhb_data(abc):
    LhbCount(sys.argv).run()


def get_wx_data(abc):

    WeiXinSpider().run()


def get_fund_data(abc):
    FundSpider().run()


def get_wd_data(abc):
    #wd
    #QuestionSpider().run()
    from elasticsearch import Elasticsearch
    es = Elasticsearch(host='172.16.11.240', port=9200)
    doc = {
        'request_url': 'http://www.baidu.com',
        'request_query': 22,
        'reponse_result': 22,
        'start_time': '2016-04-26 10:00'

    }
    es.index(index="yrb", doc_type='info', id=1, body=doc)
    es.indices.refresh(index="yrb")


class Job:
    interrupted = False

    def __init__(self, args):
        self.args = args

    def signal_handler(self, signum, frame):
        if signum == signal.SIGTERM or signum == signal.SIGINT:
            self.interrupted = True

    def run(self):
        print self.args

if __name__ == '__main__':
    import argparse
    import signal
    parser = argparse.ArgumentParser()

    parser.add_argument('--nimbus-host', default='127.0.0.1')
    parser.add_argument('--nimbus-port', type=int, default=6627)
    #args = parser.parse_args()
    #Job(args).run()
    #sys.exit()
    start = time.time()
    function = eval(sys.argv[1])
    function(sys.argv[2])
    end = time.time()
    print end-start
