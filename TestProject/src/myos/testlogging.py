#-*- coding:utf-8 -*-
'''
Created on 2012-11-18 @author: GFTOwenWang
'''
import logging
import logging.handlers
import time


def func1():
    form = logging.Formatter(fmt="%(name)s %(filename)s(%(lineno)s) %(asctime)s %(message)s")
    logm=logging.getLogger('main')
    logm.setLevel(logging.DEBUG)
    
    handd = logging.handlers.TimedRotatingFileHandler(filename='log/debug.txt',when='D')
    handd.setLevel(logging.DEBUG)
    handd.setFormatter(form)
    logm.addHandler(handd)
    
    handi = logging.handlers.TimedRotatingFileHandler(filename='log/info.txt',when='D')
    handi.setLevel(logging.INFO)
    handi.setFormatter(form)
    logm.addHandler(handi)
    
    handw = logging.handlers.TimedRotatingFileHandler(filename='log/warn.txt',when='D')
    handw.setLevel(logging.WARN)
    handw.setFormatter(form)
    logm.addHandler(handw)
    
    hande = logging.handlers.TimedRotatingFileHandler(filename='log/error.txt',when='D')
    hande.setLevel(logging.ERROR)
    hande.setFormatter(form)
    logm.addHandler(hande)
    
    handc = logging.handlers.TimedRotatingFileHandler(filename='log/critical.txt',when='D')
    handc.setLevel(logging.CRITICAL)
    handc.setFormatter(form)
    logm.addHandler(handc)
    
    hands = logging.StreamHandler()
    hands.setFormatter(form)
    logm.addHandler(hands)
    
    while True:
        logm.debug('debug:msg')
        logm.info('info:msg')
        logm.warn('warn:msg')
        logm.error('error:msg')
        logm.critical('critical:msg')
        
        time.sleep(5)
    
    
    
if __name__ == "__main__":
    func1()