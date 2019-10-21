import camelot as cl
import os
import time

os.chdir('d:\pythontest\canh-pwb')
tables=cl.read_pdf('canh-pwb.pdf',split_text=True)
tables[0].to_excel('canh-pwb.xlsx')

time.sleep(5)

