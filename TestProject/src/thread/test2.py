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

        thread_down= threading.Thread(target=self.download, args=()) 
        thread_down.start()
        
        time.sleep(1000)

    def get_providers(self):
        global g_mutex
        
        while True:
            Log.info("load provider")
            print "a here"
            g_mutex.acquire()
            for i in range(30):
                id = random.randint(1, 1000)
                if id in self.dict_provider:
                    pass
                else:
                    self.dict_provider[id] = 0
            
            Log.info("load provider, len: %s" % len(self.dict_provider))
            g_mutex.release()
            print "a there"
            Log.info("get provider sleep")
            time.sleep(10)
            Log.info("get provider walk up")
            
    def download(self):
        global g_mutex
        while True:
            print 'b here'
            providerid = None
            g_mutex.acquire()
            print 'b there'
            for pid in self.dict_provider:
                #Log.info("for %s,%s" %( pid, self.dict_provider[pid]))
                if self.dict_provider[pid]==0:
                    #g_mutex.acquire()
                    self.dict_provider[pid] = 1
                    providerid = pid
                    break
                    #g_mutex.release()
            g_mutex.release()
            print 'b done'
            if providerid is None:
                #time.sleep(10)
                continue
            
            Log.info("download for providerid: %s" % providerid)
            
            g_mutex.acquire()
            self.dict_provider[providerid]=2
            #del self.dict_provider[providerid]
            g_mutex.release()
            
            

if __name__ == "__main__":
    p = Process()
    p.process()
        
    
    

