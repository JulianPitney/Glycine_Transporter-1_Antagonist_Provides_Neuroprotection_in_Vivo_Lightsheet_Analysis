#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

M1 = pd.read_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/T5654_cropped_Dendrite Set.xlsx')
M2 = pd.read_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/T5655_cropped_Dendrite Set.xlsx')
M3 = pd.read_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/T5662_cropped_Dendrite Set.xlsx')
M4 = pd.read_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/T5668_cropped_Dendrite Set.xlsx')

#M1 = T5654
#M2 = T5655
#M3 = T5662
#M4 = T5668


# In[3]:


M1.head()


# In[4]:


M1["diameter"] = round(M1["diameter"]*2)/2
M1["length"] = round(M1["length"]*2)/2
M1["volume"] = round(M1["volume"]*2)/2
M1_filter = M1[M1['diameter'] > 1]
M1_filter = M1_filter[M1_filter['diameter'] < 18]
M1_filter = M1_filter[M1_filter['length'] > 6]
M1_filter = M1_filter[M1_filter['length'] < 300]

M2["diameter"] = round(M2["diameter"]*2)/2
M2["length"] = round(M2["length"]*2)/2
M1["volume"] = round(M2["volume"]*2)/2
M2_filter = M2[M2['diameter'] > 1]
M2_filter = M2_filter[M2_filter['diameter'] < 18]
M2_filter = M2_filter[M2_filter['length'] > 6]
M2_filter = M2_filter[M2_filter['length'] < 300]

M3["diameter"] = round(M3["diameter"]*2)/2
M3["length"] = round(M3["length"]*2)/2
M3["volume"] = round(M3["volume"]*2)/2
M3_filter = M3[M3['diameter'] > 1]
M3_filter = M3_filter[M3_filter['diameter'] < 18]
M3_filter = M3_filter[M3_filter['length'] > 6]
M3_filter = M3_filter[M3_filter['length'] < 300]

M4["diameter"] = round(M4["diameter"]*2)/2
M4["length"] = round(M4["length"]*2)/2
M4["volume"] = round(M4["volume"]*2)/2
M4_filter = M4[M4['diameter'] > 1]
M4_filter = M4_filter[M4_filter['diameter'] < 18]
M4_filter = M4_filter[M4_filter['length'] > 6]
M4_filter = M4_filter[M4_filter['length'] < 300]


# In[5]:


M1_filter.head()


# In[6]:


M1_dia = M1_filter['diameter']#.plot(kind="hist", bins=100, xlim=(0,10), figsize=(14,6), rwidth=0.8)
M2_dia = M2_filter['diameter']#.plot(kind="hist", bins=100, xlim=(0,10), figsize=(14,6), rwidth=0.8)
M3_dia = M3_filter['diameter']#.plot(kind="hist", bins=100, xlim=(0,10), figsize=(14,6), rwidth=0.8)
M4_dia = M4_filter['diameter']#.plot(kind="hist", bins=100, xlim=(0,10), figsize=(14,6), rwidth=0.8)

# ncol=2
# nrow=2
# dia_distr, axes = plt.subplots(nrow, ncol)
# M1_dia.plot(ax=axes[0,0],kind="hist", bins=10, xlim=(0,19), ylim=(0,1500), figsize=(20,15), rwidth=0.7, title= 'T6001', legend = None)
# M2_dia.plot(ax=axes[1,0],kind="hist", bins=10, xlim=(0,19), ylim=(0,1500), figsize=(20,15), rwidth=0.7, title= 'T6107', legend = None)
# M3_dia.plot(ax=axes[0,1],kind="hist", bins=10, xlim=(0,19), ylim=(0,1500), figsize=(20,15), rwidth=0.7, title= 'T6109', legend = None)
# M4_dia.plot(ax=axes[1,1],kind="hist", bins=10, xlim=(0,19), ylim=(0,1500), figsize=(20,15), rwidth=0.7, title= 'T6110', legend = None)


# axes[0,0].set_xlabel("diameter")
# axes[1,0].set_xlabel("diameter")
# axes[0,1].set_xlabel("diameter")
# axes[1,1].set_xlabel("diameter")




#dia_distr.savefig('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/Diameter_distribution.png')


# In[7]:


#Sort vessels by bins, then count number in each bin.

print('T5654 vessels by diameter')
M1_dia_count= pd.cut(M1_filter['diameter'], 10).value_counts().sort_index()
print (M1_dia_count, '\n')

print('T5655 vessels by diameter')
M2_dia_count= pd.cut(M2_filter['diameter'], 10).value_counts().sort_index()
print (M2_dia_count)

print('T5662 vessels by diameter')
M3_dia_count= pd.cut(M3_filter['diameter'], 10).value_counts().sort_index()
print (M3_dia_count)

print('T5668 vessels by diameter')
M4_dia_count= pd.cut(M4_filter['diameter'], 10).value_counts().sort_index()
print (M4_dia_count)



M1_dia_count.to_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/diameter_count_by_bins/T5654_dia_count.xlsx')
M2_dia_count.to_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/diameter_count_by_bins/T5655_dia_count.xlsx')
M3_dia_count.to_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/diameter_count_by_bins/T5662_dia_count.xlsx')
M4_dia_count.to_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/diameter_count_by_bins/T5668_dia_count.xlsx')


# In[8]:


M1_count = M1_dia.count()
print(M1_count)


# In[9]:


M2_count = M2_dia.count()
print(M2_count)


# In[10]:


M3_count = M3_dia.count()
print(M3_count)


# In[11]:


M4_count = M4_dia.count()
print(M4_count)


# In[12]:


vessel_plot= pd.DataFrame({'Mouse':['T5654', 'T5655','T5662','T5668'], 'vessel count':[M1_count, M2_count, M3_count, M4_count]})
vessel_count=vessel_plot.plot.bar(x= 'Mouse', y='vessel count', rot =0, figsize=(14,6), color =['#FF8C00','#4682B4','#FF8C00','#4682B4','#FF8C00','#4682B4','#FF8C00','#4682B4','#FF8C00','#4682B4','#FF8C00'], legend=None)
vessel_count.set_ylabel("vessel count")
for p in vessel_count.patches:
    vessel_count.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
#plt.savefig('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/vessel count.png')


# In[13]:


display(vessel_plot)


# In[14]:


# #density = vessels/um3
# #pixel-um ratio(x y) = 1.43um (0.00143mm)
# #pixel-um ratio(z) = 5um (0.005mm)
# #pixel size of ROI (x,y,z) = 340*1080*200

size_roi = (340*0.00143)*(1080*0.00143)*(200*0.005)
density_M1 = vessel_plot['vessel count'][0]/size_roi
round_density_M1 = density_M1.round(decimals=0)
print("T5654 density (vessels/mm3)")
print(round_density_M1,'\n')

density_M2 = vessel_plot['vessel count'][1]/size_roi
round_density_M2 = density_M2.round(decimals=0)
print("T5655 density")
print(round_density_M2,'\n')

density_M3 = vessel_plot['vessel count'][2]/size_roi
round_density_M3 = density_M3.round(decimals=0)
print("T5662 density")
print(round_density_M3,'\n')

density_M4 = vessel_plot['vessel count'][3]/size_roi
round_density_M4 = density_M4.round(decimals=0)
print("T5668 density")
print(round_density_M4,'\n')

density_array = np.array(["T5654 (vessels/mm3)",density_M1,"T5655 (vessels/mm3)",density_M2,"T5662 (vessels/mm3)",density_M3,"T5668 (vessels/mm3)",density_M4])
print(density_array)
np.savetxt('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/density.txt', density_array,fmt='%s')


# In[15]:


# density_plot= pd.DataFrame({'Mouse':['1', '5','9','10','11','12','13','14','15','17','19'], 'density':[round_density_m1, round_density_m5, round_density_m9, round_density_m10, round_density_m11, round_density_m12, round_density_m13, round_density_m14, round_density_m15, round_density_m17, round_density_m19]})
# den=density_plot.plot.bar(x= 'Mouse', y='density', rot =0, figsize=(14,6), color =['#FF8C00','#4682B4','#FF8C00','#4682B4','#FF8C00','#4682B4','#FF8C00','#4682B4','#FF8C00','#4682B4','#FF8C00'], legend=None)
# den.set_ylabel("vessel count (vessels/mm3)")
# for p in den.patches:
#     den.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

# plt.savefig('/Users/blast/Documents/aivia data/


# In[16]:


M1_len = M1_filter['length']#.plot(kind="hist", bins=100, xlim=(0,10), figsize=(14,6), rwidth=0.8)
M2_len = M2_filter['length']#.plot(kind="hist", bins=100, xlim=(0,10), figsize=(14,6), rwidth=0.8)
M3_len = M3_filter['length']#.plot(kind="hist", bins=100, xlim=(0,10), figsize=(14,6), rwidth=0.8)
M4_len = M4_filter['length']#.plot(kind="hist", bins=100, xlim=(0,10), figsize=(14,6), rwidth=0.8)



ncol=3
nrow=2
length_distr, axes = plt.subplots(nrow, ncol)
length_distr.subplots_adjust(wspace = 0.2 , hspace = 0.4)
M1_len.plot(ax=axes[0,0],kind="hist", bins=60, xlim=(0,200), ylim=(0,2000), figsize=(20,15), rwidth=0.7, title= 'T6001', legend = None)
M2_len.plot(ax=axes[0,1],kind="hist", bins=60, xlim=(0,200), ylim=(0,2000), figsize=(20,15), rwidth=0.7, title= 'T6107', legend = None)
M3_len.plot(ax=axes[0,2],kind="hist", bins=60, xlim=(0,200), ylim=(0,2000), figsize=(20,15), rwidth=0.7, title= 'T6109', legend = None)
M4_len.plot(ax=axes[1,0],kind="hist", bins=60, xlim=(0,200), ylim=(0,2000), figsize=(20,15), rwidth=0.7, title= 'T6110', legend = None)


axes[0,0].set_xlabel("length (um)")
axes[0,1].set_xlabel("length (um)")
axes[0,2].set_xlabel("length (um)")
axes[1,0].set_xlabel("length (um)")
axes[1,1].set_xlabel("length (um)")
axes[1,2].set_xlabel("length (um)")



#length_distr.savefig('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/length distribution.png')


# In[17]:


#Sort vessels by bins, then count number in each bin.

print('M1 vessels by length')
M1_len_count= pd.cut(M1_filter["length"], 60).value_counts().sort_index()
print (M1_len_count, '\n')

print('M2 vessels by length')
M2_len_count= pd.cut(M2_filter["length"], 60).value_counts().sort_index()
print (M2_len_count, '\n')

print('M3 vessels by length')
M3_len_count= pd.cut(M3_filter["length"], 60).value_counts().sort_index()
print (M3_len_count, '\n')

print('M4 vessels by length')
M4_len_count= pd.cut(M4_filter["length"], 60).value_counts().sort_index()
print (M4_len_count, '\n')


M1_len_count.to_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/vessel_count_length/T5654_len_count.xlsx')
M2_len_count.to_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/vessel_count_length/T5655_len_count.xlsx')
M3_len_count.to_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/vessel_count_length/T5662_len_count.xlsx')
M4_len_count.to_excel('/Users/blast/Documents/aivia data/2021-03-02 aivia output/figures/vessel_count_length/T5668_len_count.xlsx')


# In[18]:


M1_filtered['length'].head()
