#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# In[14]:


#파일 불러오기
path202301 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202301.csv"
rowDf202301 = pd.read_csv(path202301,index_col=6)
rowDf202301 = rowDf202301.reset_index()
rowDf202301 = rowDf202301.drop(columns="index")
rowDf202301 = rowDf202301.drop(columns="등록일자")


# In[15]:


rowDf202301


# In[16]:


#로우데이터의 20230101데이터를 날짜로 변환하기 위한 단계 1) 해당 값을 str로 변환
rowDf202301["사용일자"] = rowDf202301["사용일자"].astype("str")


# In[17]:


#문자 변환 후 to_datetime으로 날짜 변환 - 2023-01-01 의 형태
rowDf202301["사용일자"] = pd.to_datetime(rowDf202301["사용일자"])


# In[18]:


#2023-01-01의 형태의 값들을 월요일(0)~일요일(6)으로 변환 dt.dayofweek
rowDf202301["사용일자"] = rowDf202301["사용일자"].dt.dayofweek


# In[19]:


#그 중에 토요일(5), 일요일(6)인것만 선별해서 다시 할당
rowDf202301 = rowDf202301[(rowDf202301["사용일자"]==5) | (rowDf202301["사용일자"]==6)]


#그 중에 금요일(4), 토요일(5)인것만 선별해서 다시 할당
#rowDf202301 = rowDf202301[(rowDf202301["사용일자"]==4) | (rowDf202301["사용일자"]==5)]


# In[20]:


#필요한 열만 남기기
rowDf202301 = rowDf202301[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]


# In[21]:


#노선명, 역명, 사용일자 별로 정렬
rowDf202301 = rowDf202301.sort_values(["노선명","역명","사용일자"])


# In[22]:


#index reset. 기존 인덱스 제거 
rowDf202301 = rowDf202301.reset_index(drop=True)


# In[23]:


#노선명, 역명, 사용일자 별로 그룹바이
rowDf202301 = rowDf202301.groupby(["역명"])[["승차총승객수","하차총승객수"]].sum()


# In[24]:


rowDf202301.head(50)


# In[15]:


#2월부터 12월까지는 1월과 똑같이 진행한 뒤
#승차총승객수와 하차총승객수만 추출해서 df로 만들기


# In[13]:


#2월..
path202302 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202302.csv"
rowDf202302 = pd.read_csv(path202302,index_col=6)
rowDf202302 = rowDf202302.reset_index()
rowDf202302 = rowDf202302.drop(columns="index")
rowDf202302 = rowDf202302.drop(columns="등록일자")

rowDf202302["사용일자"] = rowDf202302["사용일자"].astype("str")
rowDf202302["사용일자"] = pd.to_datetime(rowDf202302["사용일자"])
rowDf202302["사용일자"] = rowDf202302["사용일자"].dt.dayofweek
rowDf202302 = rowDf202302[(rowDf202302["사용일자"]==5) | (rowDf202302["사용일자"]==6)]
#rowDf202302 = rowDf202302[(rowDf202302["사용일자"]==4) | (rowDf202302["사용일자"]==5)]
rowDf202302 = rowDf202302[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202302 = rowDf202302.sort_values(["노선명","역명","사용일자"])
rowDf202302 = rowDf202302.reset_index(drop=True)
rowDf202302 = rowDf202302.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[14]:


#3월..
path202303 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202303.csv"
rowDf202303 = pd.read_csv(path202303,index_col=6)
rowDf202303 = rowDf202303.reset_index()
rowDf202303 = rowDf202303.drop(columns="index")
rowDf202303 = rowDf202303.drop(columns="등록일자")

rowDf202303["사용일자"] = rowDf202303["사용일자"].astype("str")
rowDf202303["사용일자"] = pd.to_datetime(rowDf202303["사용일자"])
rowDf202303["사용일자"] = rowDf202303["사용일자"].dt.dayofweek
#rowDf202303 = rowDf202303[(rowDf202303["사용일자"]==5) | (rowDf202303["사용일자"]==6)]
rowDf202303 = rowDf202303[(rowDf202303["사용일자"]==4) | (rowDf202303["사용일자"]==5)]
rowDf202303 = rowDf202303[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202303 = rowDf202303.sort_values(["노선명","역명","사용일자"])
rowDf202303 = rowDf202303.reset_index(drop=True)
rowDf202303 = rowDf202303.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[15]:


#4월..
path202304 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202304.csv"
rowDf202304 = pd.read_csv(path202304,index_col=6)
rowDf202304 = rowDf202304.reset_index()
rowDf202304 = rowDf202304.drop(columns="index")
rowDf202304 = rowDf202304.drop(columns="등록일자")

rowDf202304["사용일자"] = rowDf202304["사용일자"].astype("str")
rowDf202304["사용일자"] = pd.to_datetime(rowDf202304["사용일자"])
rowDf202304["사용일자"] = rowDf202304["사용일자"].dt.dayofweek
#rowDf202304 = rowDf202304[(rowDf202304["사용일자"]==5) | (rowDf202304["사용일자"]==6)]
rowDf202304 = rowDf202304[(rowDf202304["사용일자"]==4) | (rowDf202304["사용일자"]==5)]
rowDf202304 = rowDf202304[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202304 = rowDf202304.sort_values(["노선명","역명","사용일자"])
rowDf202304 = rowDf202304.reset_index(drop=True)
rowDf202304 = rowDf202304.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[16]:


#5월..
path202305 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202305.csv"
rowDf202305 = pd.read_csv(path202305,index_col=6)
rowDf202305 = rowDf202305.reset_index()
rowDf202305 = rowDf202305.drop(columns="index")
rowDf202305 = rowDf202305.drop(columns="등록일자")

rowDf202305["사용일자"] = rowDf202305["사용일자"].astype("str")
rowDf202305["사용일자"] = pd.to_datetime(rowDf202305["사용일자"])
rowDf202305["사용일자"] = rowDf202305["사용일자"].dt.dayofweek
#rowDf202305 = rowDf202305[(rowDf202305["사용일자"]==5) | (rowDf202305["사용일자"]==6)]
rowDf202305 = rowDf202305[(rowDf202305["사용일자"]==4) | (rowDf202305["사용일자"]==5)]
rowDf202305 = rowDf202305[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202305 = rowDf202305.sort_values(["노선명","역명","사용일자"])
rowDf202305 = rowDf202305.reset_index(drop=True)
rowDf202305 = rowDf202305.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[17]:


#6월..
path202306 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202306.csv"
rowDf202306 = pd.read_csv(path202306,index_col=6)
rowDf202306 = rowDf202306.reset_index()
rowDf202306 = rowDf202306.drop(columns="index")
rowDf202306 = rowDf202306.drop(columns="등록일자")

rowDf202306["사용일자"] = rowDf202306["사용일자"].astype("str")
rowDf202306["사용일자"] = pd.to_datetime(rowDf202306["사용일자"])
rowDf202306["사용일자"] = rowDf202306["사용일자"].dt.dayofweek
#rowDf202306 = rowDf202306[(rowDf202306["사용일자"]==5) | (rowDf202306["사용일자"]==6)]
rowDf202306 = rowDf202306[(rowDf202306["사용일자"]==4) | (rowDf202306["사용일자"]==5)]
rowDf202306 = rowDf202306[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202306 = rowDf202306.sort_values(["노선명","역명","사용일자"])
rowDf202306 = rowDf202306.reset_index(drop=True)
rowDf202306 = rowDf202306.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[18]:


#7월..
path202307 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202307.csv"
rowDf202307 = pd.read_csv(path202307,index_col=6)
rowDf202307 = rowDf202307.reset_index()
rowDf202307 = rowDf202307.drop(columns="index")
rowDf202307 = rowDf202307.drop(columns="등록일자")

rowDf202307["사용일자"] = rowDf202307["사용일자"].astype("str")
rowDf202307["사용일자"] = pd.to_datetime(rowDf202307["사용일자"])
rowDf202307["사용일자"] = rowDf202307["사용일자"].dt.dayofweek
#rowDf202307 = rowDf202307[(rowDf202307["사용일자"]==5) | (rowDf202307["사용일자"]==6)]
rowDf202307 = rowDf202307[(rowDf202307["사용일자"]==4) | (rowDf202307["사용일자"]==5)]
rowDf202307 = rowDf202307[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202307 = rowDf202307.sort_values(["노선명","역명","사용일자"])
rowDf202307 = rowDf202307.reset_index(drop=True)
rowDf202307 = rowDf202307.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[19]:


#8월...... 손이 아프다
path202308 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202308.csv"
rowDf202308 = pd.read_csv(path202308,index_col=6)
rowDf202308 = rowDf202308.reset_index()
rowDf202308 = rowDf202308.drop(columns="index")
rowDf202308 = rowDf202308.drop(columns="등록일자")

rowDf202308["사용일자"] = rowDf202308["사용일자"].astype("str")
rowDf202308["사용일자"] = pd.to_datetime(rowDf202308["사용일자"])
rowDf202308["사용일자"] = rowDf202308["사용일자"].dt.dayofweek
#rowDf202308 = rowDf202308[(rowDf202308["사용일자"]==5) | (rowDf202308["사용일자"]==6)]
rowDf202308 = rowDf202308[(rowDf202308["사용일자"]==4) | (rowDf202308["사용일자"]==5)]
rowDf202308 = rowDf202308[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202308 = rowDf202308.sort_values(["노선명","역명","사용일자"])
rowDf202308 = rowDf202308.reset_index(drop=True)
rowDf202308 = rowDf202308.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[20]:


#9월..
path202309 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202309.csv"
rowDf202309 = pd.read_csv(path202309,index_col=6)
rowDf202309 = rowDf202309.reset_index()
rowDf202309 = rowDf202309.drop(columns="index")
rowDf202309 = rowDf202309.drop(columns="등록일자")

rowDf202309["사용일자"] = rowDf202309["사용일자"].astype("str")
rowDf202309["사용일자"] = pd.to_datetime(rowDf202309["사용일자"])
rowDf202309["사용일자"] = rowDf202309["사용일자"].dt.dayofweek
#rowDf202309 = rowDf202309[(rowDf202309["사용일자"]==5) | (rowDf202309["사용일자"]==6)]
rowDf202309 = rowDf202309[(rowDf202309["사용일자"]==4) | (rowDf202309["사용일자"]==5)]
rowDf202309 = rowDf202309[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202309 = rowDf202309.sort_values(["노선명","역명","사용일자"])
rowDf202309 = rowDf202309.reset_index(drop=True)
rowDf202309 = rowDf202309.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[21]:


#10월........
path202310 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202310.csv"
rowDf202310 = pd.read_csv(path202310,index_col=6)
rowDf202310 = rowDf202310.reset_index()
rowDf202310 = rowDf202310.drop(columns="index")
rowDf202310 = rowDf202310.drop(columns="등록일자")

rowDf202310["사용일자"] = rowDf202310["사용일자"].astype("str")
rowDf202310["사용일자"] = pd.to_datetime(rowDf202310["사용일자"])
rowDf202310["사용일자"] = rowDf202310["사용일자"].dt.dayofweek
#rowDf202310 = rowDf202310[(rowDf202310["사용일자"]==5) | (rowDf202310["사용일자"]==6)]
rowDf202310 = rowDf202310[(rowDf202310["사용일자"]==4) | (rowDf202310["사용일자"]==5)]
rowDf202310 = rowDf202310[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202310 = rowDf202310.sort_values(["노선명","역명","사용일자"])
rowDf202310 = rowDf202310.reset_index(drop=True)
rowDf202310 = rowDf202310.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[22]:


#11월...... 땀난다..
path202311 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202311.csv"
rowDf202311 = pd.read_csv(path202311,index_col=6)
rowDf202311 = rowDf202311.reset_index()
rowDf202311 = rowDf202311.drop(columns="index")
rowDf202311 = rowDf202311.drop(columns="등록일자")

rowDf202311["사용일자"] = rowDf202311["사용일자"].astype("str")
rowDf202311["사용일자"] = pd.to_datetime(rowDf202311["사용일자"])
rowDf202311["사용일자"] = rowDf202311["사용일자"].dt.dayofweek
#rowDf202311 = rowDf202311[(rowDf202311["사용일자"]==5) | (rowDf202311["사용일자"]==6)]
rowDf202311 = rowDf202311[(rowDf202311["사용일자"]==4) | (rowDf202311["사용일자"]==5)]
rowDf202311 = rowDf202311[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202311 = rowDf202311.sort_values(["노선명","역명","사용일자"])
rowDf202311 = rowDf202311.reset_index(drop=True)
rowDf202311 = rowDf202311.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[23]:


#12월... 마지막.. 
path202312 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/sub202312.csv"
rowDf202312 = pd.read_csv(path202312,index_col=6)
rowDf202312 = rowDf202312.reset_index()
rowDf202312 = rowDf202312.drop(columns="index")
rowDf202312 = rowDf202312.drop(columns="등록일자")

rowDf202312["사용일자"] = rowDf202312["사용일자"].astype("str")
rowDf202312["사용일자"] = pd.to_datetime(rowDf202312["사용일자"])
rowDf202312["사용일자"] = rowDf202312["사용일자"].dt.dayofweek
#rowDf202312 = rowDf202312[(rowDf202312["사용일자"]==5) | (rowDf202312["사용일자"]==6)]
rowDf202312 = rowDf202312[(rowDf202312["사용일자"]==4) | (rowDf202312["사용일자"]==5)]
rowDf202312 = rowDf202312[["노선명","역명","사용일자","승차총승객수","하차총승객수"]]
rowDf202312 = rowDf202312.sort_values(["노선명","역명","사용일자"])
rowDf202312 = rowDf202312.reset_index(drop=True)
rowDf202312 = rowDf202312.groupby(["역명","사용일자"])[["승차총승객수","하차총승객수"]].sum()


# In[24]:


#데이터 카피
df202301 = rowDf202301.copy()
df202302 = rowDf202302.copy()
df202303 = rowDf202303.copy()
df202304 = rowDf202304.copy()
df202305 = rowDf202305.copy()
df202306 = rowDf202306.copy()
df202307 = rowDf202307.copy()
df202308 = rowDf202308.copy()
df202309 = rowDf202309.copy()
df202310 = rowDf202310.copy()
df202311 = rowDf202311.copy()
df202312 = rowDf202312.copy()


# In[25]:


data_list = [df202301,df202302,df202303,df202304,df202305,df202306,df202307,df202308,df202309,df202310,df202311,df202312]


# In[26]:


df202301


# In[27]:


df_last = pd.concat(data_list, axis=1, join="outer")


# In[50]:


#pd.set_option('display.max.colwidth', 100)


# In[28]:


df_last.head()


# In[29]:


df_last.columns = ["1월승차","1월하차","2월승차","2월하차","3월승차","3월하차","4월승차","4월하차","5월승차","5월하차","6월승차","6월하차","7월승차","7월하차","8월승차","8월하차","9월승차","9월하차","10월승차","10월하차","11월승차","11월하차","12월승차","12월하차"]


# In[117]:


df_last.head()


# In[30]:


df_last = df_last.fillna(0)


# In[31]:


save_path_2023 = "/Users/yong/Desktop/python_project2/지하철 승하차/2023/2023_subway_금토.csv"


# In[32]:


df_last.to_csv(save_path_2023, index=True, encoding='utf-8-sig')


# In[ ]:





# In[ ]:


#pathSubName = "/Users/yong/Desktop/python_project2/지하철 승하차/서울시 지하철역 목록.csv"
#subName = pd.read_csv(path202301,index_col=6)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




