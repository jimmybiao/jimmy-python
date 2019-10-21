import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

picname='CPI vs PPI.png'
if os.path.exists(picname):
    os.remove(picname)

time.sleep(1)

cpi=ts.get_cpi()
cpi['cpi']=cpi['cpi']-100.0 #convert to percentage
cpi['month']=pd.to_datetime(cpi['month'])
cpi=cpi.sort_values('month')

ppi=ts.get_ppi()
ppi['ppiip']=ppi['ppiip']-100.0
ppi['month']=pd.to_datetime(ppi['month'])
ppi=ppi.sort_values('month')

#plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(12,6))
plt.plot(cpi['month'],cpi['cpi'],color='green',label='CPI')
plt.plot(ppi['month'],ppi['ppiip'],color='red',label='PPI')
plt.legend()
plt.axis('tight')
plt.xlabel('year',size=12)
plt.ylabel('percent',size=15)
plt.title('CPI and PPI Analysis',size=12)
plt.savefig(picname)
