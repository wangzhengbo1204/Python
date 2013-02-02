#-*- coding:utf-8 -*-
'''
Created on 2012-3-13

@author: GFTOwenWang
'''
import time
import threading
import random
from gftdata.share.utility.log import Log


g_mutex=threading.Lock()

class Process(object):
    
    def __init__(self):
        self.dict_provider = {}
        
    def process(self):
        global g_mutex
        thread_load = threading.Thread(target=self.get_providers, args=())
        thread_load.start()
        
        while True:
            g_mutex.acquire()
            for pid in self.dict_provider:
                if self.dict_provider[pid] == 0:
                    thread_down= threading.Thread(target=self.download, args=(pid,)) 
                    thread_down.start()
            g_mutex.release()
        
        print "init end"
        thread_load.join()
        #threading.Thread.join(thread_down)
        print "end join"

    def get_providers(self):
        global g_mutex
        
        while True:
            Log.info("load provider")
            g_mutex.acquire()
            for i in range(30):
                id = random.randint(1, 200)
                if id in self.dict_provider and self.dict_provider[id] == 1:
                    pass
                else:
                    self.dict_provider[id] = 0
            
            Log.info("load provider, len: %s" % len(self.dict_provider))
            g_mutex.release()
            Log.info("get provider sleep")
            time.sleep(1)
            Log.info("get provider walk up")
            
    def download(self, providerid):
        #providerid = ''.join(pids)
        Log.info("download for providerid: %s" % providerid)
        global g_mutex
        g_mutex.acquire()
        self.dict_provider[providerid]=2
        #del self.dict_provider[providerid]
        g_mutex.release()
        
            

if __name__ == "__main__":
    p = Process()
    p.process()
        
    