'''
Created on 2011-11-15

@author: GFTOwenWang
'''

from datetime import datetime, date 
import ftputil
import os
import time

host1 = '192.168.1.135'
user1='zzy'
passwd1='zzy'

ftphost1 = ftputil.FTPHost(host1, user1, passwd1)

host2 = '222.73.115.215'
user2='datafetcher'
passwd2='gftdata1110'

ftphost2 = ftputil.FTPHost(host2, user2, passwd2)

def test_func1(ftphost):
    #ftphost = ftputil.FTPHost(host, user, passwd)
    print ftphost.curdir
    print ftphost.pardir
    print ftphost.sep
    print ftphost.path
    print ftphost.listdir(ftphost.curdir)
    
def test_func2(ftphost):
    cwd= ftphost.getcwd()
    print cwd
    #new_path = os.path.join(cwd, '00/00')
    #new_path = "/home/datafetcher/00/00"
    new_path = '00/00'
    ftphost.chdir(new_path)
    cwd= ftphost.getcwd()
    print cwd
    new_path = '..'
    print new_path
    ftphost.chdir(new_path)
    cwd= ftphost.getcwd()
    print cwd
    
def test_func3(ftphost):
    new_path = 'testoriginal'
    ftphost.chdir(new_path)
    cwd= ftphost.getcwd()
    print cwd
    ftphost.upload('ftputil.html', './ftputil.html', 'b')
    ftphost.download('README.txt',r'd:\test\readme.txt','b')
    
def test_func4(ftphost):
    new_path = 'testoriginal'
    ftphost.chdir(new_path)
    cwd= ftphost.getcwd()
    print cwd
    ftphost.upload_if_newer('ftputil.html', './ftputil.html', 'b')
    ftphost.download_if_newer('README.txt',r'd:\test\readme.txt','b')
    
def test_func5(ftphost):
    info = ftphost.listdir('original/00/00/2F')
    print info
    info = ftphost.lstat('original/00/00/2F')
    print info
    info = ftphost.stat('original/00/00/2F')
    print info
    
def test_func6(ftphost):
    s= ftphost.path.getmtime("testoriginal/ftputil.html")
    print s
    __s_date = date(1899, 12, 31).toordinal() - 1
    print __s_date
    __s_date = date(2011, 12, 31).toordinal() - 1
    print __s_date
    print s - __s_date
    print time.gmtime(s)
    dt = datetime.fromordinal(s - __s_date)
    print dt
    
def test_func7():
    tmp_ftphost1 = ftputil.FTPHost(host1, user1, passwd1)
    tmp_ftphost2 = ftputil.FTPHost(host1, user1, passwd1)
    try:
        stat_result1 = tmp_ftphost1.stat("./testoriginal/readme.txt")
        stat_result2 = tmp_ftphost2.stat("./testoriginal/readme.txt")
        tmp_ftphost2.remove("testoriginal/readme.txt")
        # `host1` will still see the obsolete cache entry!
        print tmp_ftphost1.stat("testoriginal/readme.txt")
        # Will raise an exception since an `FTPHost` object
        #  knows of its own changes.
        print tmp_ftphost2.stat("testoriginal/readme.txt")
    except Exception as ex:
        print ex.message
    finally:
        tmp_ftphost1.close()
        tmp_ftphost2.close()
        
def test_func8():
    tmp_host1 = ftputil.FTPHost(host1, user1, passwd1)
    host2 = ftputil.FTPHost(host1, user1, passwd1)
    try:
        stat_result1 = tmp_host1.stat("testoriginal/readme.txt")
        stat_result2 = host2.stat("testoriginal/readme.txt")
        host2.remove("testoriginal/readme.txt")
        # Invalidate using an absolute path.
        absolute_path = tmp_host1.path.abspath(
                        tmp_host1.path.join(tmp_host1.curdir, "testoriginal/readme.txt"))
        tmp_host1.stat_cache.invalidate(absolute_path)
        # Will now raise an exception as it should
        print tmp_host1.stat("testoriginal/readme.txt")
        # Would raise an exception since an `FTPHost` object
        #  knows of its own changes, even without `invalidate`
        print host2.stat("testoriginal/readme.txt")
    finally:
        tmp_host1.close()
        host2.close()
        
def test_func9(ftphost):
    files=ftphost.path.walk("testoriginal",None,None)
    print files
    
if __name__ == '__main__':
    #test_func1(ftphost2)
    #test_func2(ftphost2)
    #test_func4(ftphost1)
    #test_func5(ftphost1)
    test_func6(ftphost1)
    #test_func7()
    #test_func8()
    #test_func9(ftphost1)
    
    