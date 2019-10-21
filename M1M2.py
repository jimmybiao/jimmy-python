import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

picname='M1 vs M2.png'

if os.path.exists(picname):
    os.remove(picname)

time.sleep(1)

ms=ts.get_money_supply()
ms['month']=pd.to_datetime(ms['month'])
ms=ms.sort_values('month')
ms=ms.tail(100)
print(pd.DataFrame(ms,columns=['month','m1_yoy','m2_yoy']))

plt.figure(figsize=(12,6))
plt.plot(ms['month'],ms['m1_yoy'].astype('float'),color='green',label='M1')
plt.plot(ms['month'],ms['m2_yoy'].astype('float'),color='red',label='M2')
plt.legend()
plt.axis('tight')
plt.xlabel('year',size=12)
plt.ylabel('YOY percent',size=15)
plt.title('M1 and M2 Analysis',size=12)
plt.savefig(picname)
