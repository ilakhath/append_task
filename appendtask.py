# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:22:00 2023

@author: moham
"""

import pandas as pd
df=pd.read_csv(r"D:\appen_task_updated\appen_task_updated\SPEEDTEST_NEAR_A32_RM0000_1S.csv")
df.columns
df.shape
df.shape[0]
print("no of rows are",df.shape[0])
df.shape[1]
print("no of columns are",df.shape[1])


df1=pd.read_csv(r"D:\appen_task_updated\appen_task_updated\SPEEDTEST_NEAR_A53_RM0000_1S.csv")
df1
df1.shape
df1.shape[0]
print("no of rows are",df1.shape[0])
df1.shape[1]
print("no of columns are",df1.shape[1])



df2=pd.read_csv(r"D:\appen_task_updated\appen_task_updated\SPEEDTEST_NEAR_ONEPLUS_RM0000_500MS.csv")
df2
df2.shape[0]
print("no of rows are",df2.shape[0])
df2.shape[1]
print("no of columns are",df2.shape[1])





df3=pd.read_csv(r"D:\appen_task_updated\appen_task_updated\SPEEDTEST_NEAR_S22_RM0000_500MS.csv")
df3
df3.shape[0]
print("no of rows are",df3.shape[0])
df3.shape[1]
print("no of columns are",df3.shape[1])






df4=pd.read_csv(r"D:\appen_task_updated\appen_task_updated\SPEEDTEST_NEAR_IPHONE_RM0000_500MS.csv")

df4
df4.shape[0]
print("no of rows are",df4.shape[0])
df4.shape[1]
print("no of columns are",df4.shape[1])





df.columns
df1.columns
df2.columns
df3.columns
df4.columns

same_columns=['TIME_STAMP', 'Lon', 'Lat','LTE KPI Band Combination','LTE KPI MAC DL Throughput[Mbps]',
              'LTE KPI PCell Serving PCI','LTE KPI PCell Serving Band','LTE KPI PCell Serving Band(DL)',
              'LTE KPI PCell Serving RSRP[dBm]', 'LTE KPI PCell SINR[dB]','LTE KPI PCell WB CQI CW0',
              'LTE KPI PCell WB CQI CW1', 'LTE KPI PCell WB RI','LTE KPI PCell DL MCS0', 'LTE KPI PCell DL MCS1',
              'LTE KPI Pcell PDSCH PRB Number(Avg)', 'LTE KPI PCell PDSCH BLER[%]','LTE KPI PCell PDSCH Throughput[Mbps]',
              'LTE KPI RLC DL Throughput[Mbps]','LTE KPI PDCP DL Throughput[Mbps]','LTE KPI PDSCH Throughput[Mbps]',
              '5G KPI PCell RF Serving PCI','5G KPI PCell RF NR-ARFCN','5G KPI PCell RF Subcarrier Spacing',
              '5G KPI PCell RF Serving SSB Idx','5G KPI SCell[1] RF Serving SS-RSRP [dBm]','5G KPI PCell Layer1 DL BLER [%]',
              '5G KPI PCell Layer1 DL RB Num (Avg)','5G KPI PCell Layer1 DL Layer Num (Avg)','5G KPI PCell Layer1 DL MCS (Avg)',
              '5G KPI PCell Layer1 PDSCH Throughput [Mbps]'
              '5G KPI Total Info Layer2 MAC DL Throughput [Mbps]',
              '5G KPI Total Info Layer2 RLC DL Throughput [Mbps]',
              '5G KPI Total Info Layer2 PDCP DL Throughput(+Split Bearer) [Mbps]',
              '5G KPI Total Info DL CA Type','Event Technology']


              
              




differ_columns=['LTE KPI CA Type','LTE KPI SCell[1] Serving PCI','LTE KPI PCell PDSCH Throughput[Mbps]', 
                'LTE KPI SCell[1] Serving PCI',
'LTE KPI SCell[1] Serving Band',
'LTE KPI SCell[1] Serving BandWidth(DL)',
'LTE KPI SCell[1] Serving RSRP[dBm]', 'LTE KPI SCell[1] SINR[dB]',
'LTE KPI SCell[1] WB CQI CW0', 'LTE KPI SCell[1] WB CQI CW1',
'LTE KPI SCell[1] WB RI', 'LTE KPI SCell[1] DL MCS0',
'LTE KPI SCell[1] DL MCS1', 'LTE KPI SCell[1] PDSCH PRB Number(Avg)',
'LTE KPI SCell[1] PDSCH BLER[%]',
'LTE KPI SCell[1] PDSCH Throughput[Mbps]',
'LTE KPI SCell[2] PDSCH Throughput[Mbps]',
'LTE KPI SCell[3] PDSCH Throughput[Mbps]',
'LTE KPI SCell[4] PDSCH Throughput[Mbps]',
'LTE KPI SCell[5] PDSCH Throughput[Mbps]',
'LTE KPI SCell[6] PDSCH Throughput[Mbps]',
'LTE KPI SCell[7] PDSCH Throughput[Mbps]','5G KPI PCell RF Band','5G KPI Total Info BandCombination',
'5G-NR Samsung NR-PHY PRB PCell DL Info PRB Num(Avg)''5G KPI SCell[7] RF RI','5G KPI SCell[7] RF CQI',
'5G KPI PCell RF CQI']




df_append=pd.concat([df,df1,df2,df3,df4],axis=1)
df.shape[0]
print("no.of rows after appending",df_append.shape[0])
df_append.shape[1]
print("no.of columns after appending",df_append.shape[1])
df_append.columns

list_append_columns=[df_append.columns]
list_append_columns







missed_columns_names=['LTE KPI Band Combination','LTE KPI MAC DL Throughput[Mbps]','LTE KPI PCell Serving PCI','LTE KPI PCell Serving Band'
                   'LTE KPI PCell Serving BandWidth(DL)','LTE KPI PCell Serving RSRP[dBm]','LTE KPI PCell SINR[dB]','LTE KPI PCell WB CQI CW0'
                   'LTE KPI PCell WB CQI CW1','LTE KPI PCell WB RI','LTE KPI PCell DL MCS0',' LTE KPI PCell DL MCS1','LTE KPI Pcell PDSCH PRB Number(Avg)'
                   'LTE KPI PCell PDSCH BLER[%]',' LTE KPI PCell PDSCH Throughput[Mbps]','LTE KPI SCell[1] Serving PCI','LTE KPI SCell[1] Serving Band',
                   'LTE KPI SCell[1] Serving BandWidth(DL)','LTE KPI SCell[1] Serving RSRP[dBm]','LTE KPI SCell[1] SINR[dB]','LTE KPI SCell[1] WB CQI CW0',
                   'LTE KPI SCell[1] WB CQI CW1','LTE KPI SCell[1] WB RI','LTE KPI SCell[1] DL MCS0','LTE KPI SCell[1] DL MCS1','LTE KPI SCell[1] PDSCH PRB Number(Avg)',
                   'LTE KPI SCell[1] PDSCH BLER[%]','LTE KPI SCell[1] PDSCH Throughput[Mbps','LTE KPI RLC DL Throughput[Mbps]','LTE KPI PDCP DL Throughput[Mbps]',
                   'LTE KPI PDSCH Throughput[Mbps]','5G KPI PCell RF Serving PCI','5G KPI PCell RF NR-ARFCN','5G KPI PCell RF Band','5G KPI PCell RF Subcarrier Spacing',
                   '5G KPI PCell RF Serving SSB Idx','5G KPI PCell RF Serving SS-RSRP [dBm]','5G KPI PCell RF Serving SS-SINR [dB]','5G KPI PCell Layer1 DL BLER [%]',
                   '5G KPI PCell Layer1 DL RB Num (Avg)','5G KPI PCell Layer1 DL Layer Num (Avg)','5G KPI PCell Layer1 DL MCS (Avg)','5G KPI PCell Layer1 PDSCH Throughput',
                   '5G KPI SCell[7] RF RI','5G KPI SCell[7] RF CQI',' 5G KPI Total Info Layer2 MAC DL Throughput [Mbps]','5G KPI Total Info Layer2 RLC DL Throughput [Mbps]',
                   '5G KPI Total Info Layer2 PDCP DL Throughput(+Split Bearer) [Mbps]','5G KPI Total Info DL CA Type','Event Technology']
                   
                   










