import sys
import chilkat

mht = chilkat.CkMht()

#success = mht.UnlockComponent("a")
#if (success != True):
#    print mht.lastErrorText()
#    sys.exit()

success = mht.GetAndSaveMHT("http://www.sse.com.cn/sseportal/webapp/datapresent/SSEQueryBulletinOfTreasuryBillAct",r"C:\Users\GFTOwenWang\Desktop\temp2\chinabond.mht")
if (success != True):
    print mht.lastErrorText()
    sys.exit()
else:
    print "MHT Created!"