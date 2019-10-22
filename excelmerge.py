import os
import pandas as pd

splits_dir="./splits/"

merge_dir='./merge/'
merge_file='merge.xlsx'

if not os.path.exists(merge_dir):
    os.mkdir(merge_dir)

split_names=[]
for filename in os.listdir(splits_dir):
    split_names.append(filename)

df_list=[]
for split_file in split_names:
    df_split=pd.read_excel(splits_dir+split_file)
    src=split_file.replace('.xlsx','')
    df_split['source_file']=src
    df_list.append(df_split)

df_merged=pd.concat(df_list)
#df_merged['source_file'].value_counts()

df_merged.to_excel(merge_dir+merge_file,index=False)
