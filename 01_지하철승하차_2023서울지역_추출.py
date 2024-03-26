#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[114]:


path2023_week = "/Users/yong/Desktop/python_project2/지하철 승하차/전처리완료/토일통합/2023_subway_토일통합.csv"
rowDf2023_week = pd.read_csv(path2023_week)


# In[115]:


df2023_week = rowDf2023_week.copy()
df2023_week.head()


# In[116]:


path_staName = "/Users/yong/Desktop/python_project2/지하철 승하차/서울시 지하철역 목록.csv"
staName = pd.read_csv(path_staName, encoding="cp949")


# In[117]:


staName_list = list(staName["지하철역"])


# In[118]:


len(staName)


# In[120]:


seoul_sum = pd.DataFrame(columns=range(25))


# In[121]:


seoul_sum


# In[122]:


seoul_sum = pd.DataFrame()

for i in range(len(staName_list)):
    for k in range(len(df2023_week["역명"])):
        if staName_list[i] == df2023_week.loc[k][0]:
            seoul_sum = pd.concat([seoul_sum, pd.DataFrame([df2023_week.loc[k]])], axis=0, ignore_index=True)


# In[ ]:


#df2023_week에서 역명 뒤 괄호 있으면 없애기


# In[124]:


df2023_week.loc[50][0]


# In[125]:


#문자열에서 ( 위치 반환하고


# In[126]:


df2023_week.loc[50][0].find("(")


# In[128]:


df2023_week.loc[50][0][:df2023_week.loc[50][0].find("(")]


# In[129]:


for i in range(len(df2023_week["역명"])):
    if df2023_week.loc[i][0].find("(") > 0:
        df2023_week.loc[i,"역명"] = df2023_week.loc[i][0][:df2023_week.loc[i][0].find("(")]


# In[130]:


staName["지하철역"]


# In[131]:


#staName 괄호 없애기


# In[142]:


for i in range(len(staName["지하철역"])):
    if staName.loc[i][0].find("(") > 0:
        staName.loc[i,"지하철역"] = staName.loc[i][0][:staName.loc[i][0].find("(")]


# In[ ]:





# In[143]:


staName[staName["지하철역"] == "신촌"]


# In[ ]:





# In[139]:


staName.loc[~(staName["지하철역"].isin(df2023_week["역명"]))]


# In[144]:


staName_list = list(staName["지하철역"])


# In[145]:


seoul_sum = pd.DataFrame()

for i in range(len(staName_list)):
    for k in range(len(df2023_week["역명"])):
        if staName_list[i] == df2023_week.loc[k][0]:
            seoul_sum = pd.concat([seoul_sum, pd.DataFrame([df2023_week.loc[k]])], axis=0, ignore_index=True)


# In[146]:


seoul_sum


# In[ ]:





# In[ ]:





# In[147]:


save_path_2023_seoul = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/2023_subway_seoul.csv"
seoul_sum.to_csv(save_path_2023_seoul, index=True, encoding='utf-8-sig')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




