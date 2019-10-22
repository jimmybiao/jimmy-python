import os
import pandas as pd

splits_dir="./splits/"
source_excel="Address.xlsx"

if not os.path.exists(splits_dir):
    os.mkdir(splits_dir)

df_source=pd.read_excel(source_excel)
#df_source.head()
#df_source.index
#print(df_source.shape)

#split into 10 excel files
split_size=df_source.shape[0]//10;
if df_source.shape[0]%10!=0:
    split_size+=1

#print(split_size)

df_subs=[]
for i in range(0,10):
    begin=i*split_size
    end=begin+split_size
    df_sub=df_source.iloc[begin:end]
    df_subs.append((i,df_sub))

for idx,df_sub in df_subs:
    df_sub.to_excel(splits_dir+str(idx)+'.xlsx',index=False)


