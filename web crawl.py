
# coding: utf-8

# In[79]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# In[4]:


print soup.prettify()


# In[18]:


url='http://www.ahsgq.com/aee/bm/bmlist.jsp?pageno=1&pagesize=175'
r = requests.get(url)
soup = BeautifulSoup(r.content,'lxml')
parent=soup.find('div',attrs={'class':"qygm"})
lis=parent.find_all('li')

company_code=[]
company_name=[]
company_project=[]

for each in lis:
    code=each.span.string
    company_code.append(code)
    
    name=each.h3.string
    company_name.append(name)
    
    project=each.find_all('p')[0].string
    company_project.append(project)


# In[19]:


result_dict={'company_code':company_code,'company_name':company_name,'company_project':company_project}
result=pd.DataFrame(result_dict)


# In[20]:


#安徽股交
result


# In[22]:


result.to_excel(u'安徽股交.xls')


# # JS 动态网页

# In[22]:


url='http://www.clnee.com/center/newSearch.jhtml?bkxx=2'
driver=webdriver.Chrome()


driver.get(url)

#r = requests.get(url)
#soup = BeautifulSoup(data,'lxml')



# In[24]:


print soup.prettify()


# In[75]:


parent=soup.find('div',attrs={'class':"gq_view_list"})
lis=parent.find_all('li')
#匹配SecuCode
reg1 = re.compile('(\w{1}\d{5})')
reg2 = re.compile('(\S*)')
a=lis[0].find_all('a')[1].string
code = re.findall(reg1,a)[0]
name = re.sub(u"[A-Za-z0-9【】]","",a)
b=lis[0].find('div',attrs={'class':"gq_view_list_intro"}).string
project=re.sub(u"[A-Za-z0-9  ]","",b)


# In[76]:


print project


# In[70]:


ste = re.sub(u"[A-Za-z0-9】【]","",a)
print ste


# In[114]:


url='http://www.clnee.com/center/newSearch.jhtml?bkxx=2'
driver=webdriver.Chrome()

driver.get(url)

SecuCode=[]
CompName=[]
MainProj=[]
Capital=[]
reg1 = re.compile('(\w{1}\d{5})')
reg2 = re.compile('(\S*)')

for page in range(17):# 共17页，这里是手工指定的
    soup = BeautifulSoup(driver.page_source, "html.parser")
    parent=soup.find('div',attrs={'class':"gq_view_list"})
    lis=parent.find_all('li')
    
    for each in lis:
        a=each.find_all('a')[1].string
        code = re.findall(reg1,a)[0]
        name = re.sub(u"[A-Za-z0-9【】]","",a)
        b=each.find('div',attrs={'class':"gq_view_list_intro"}).string
        project=re.sub(u"[A-Za-z0-9  ]","",b)
        capital=each.find('span',attrs={'class':"zczb"}).string
        SecuCode.append(code)
        CompName.append(name)
        MainProj.append(project)
        Capital.append(capital)
        
    if page<16:        
        driver.find_element_by_xpath("//button[contains(text(),'下一页')]").click()
        
    time.sleep(1) # 睡1秒让网页加载完再去读它的html代码
driver.quit()


# In[115]:


url='http://www.clnee.com/center/newSearch.jhtml?bkxx=0'
driver=webdriver.Chrome()

driver.get(url)

for page in range(115):# 共115页，这里是手工指定的
    soup = BeautifulSoup(driver.page_source, "html.parser")
    parent=soup.find('div',attrs={'class':"gq_view_list"})
    lis=parent.find_all('li')
    
    for each in lis:
        a=each.find_all('a')[1].string
        code = re.findall(reg1,a)[0]
        name = re.sub(u"[A-Za-z0-9【】]","",a)
        b=each.find('div',attrs={'class':"gq_view_list_intro"}).string
        project=re.sub(u"[A-Za-z0-9  ]","",b)
        capital=each.find('span',attrs={'class':"zczb"}).string
        SecuCode.append(code)
        CompName.append(name)
        MainProj.append(project)
        Capital.append(capital)
        
    if page<114:        
        driver.find_element_by_xpath("//button[contains(text(),'下一页')]").click()
        print page
    time.sleep(1) # 睡1秒让网页加载完再去读它的html代码
driver.quit()




# In[116]:


url='http://www.clnee.com/center/newSearch.jhtml?bkxx=1'
driver=webdriver.Chrome()

driver.get(url)

for page in range(36):# 共36页，这里是手工指定的
    soup = BeautifulSoup(driver.page_source, "html.parser")
    parent=soup.find('div',attrs={'class':"gq_view_list"})
    lis=parent.find_all('li')
    
    for each in lis:
        a=each.find_all('a')[1].string
        code = re.findall(reg1,a)[0]
        name = re.sub(u"[A-Za-z0-9【】]","",a)
        b=each.find('div',attrs={'class':"gq_view_list_intro"}).string
        project=re.sub(u"[A-Za-z0-9  ]","",b)
        capital=each.find('span',attrs={'class':"zczb"}).string
        SecuCode.append(code)
        CompName.append(name)
        MainProj.append(project)
        Capital.append(capital)
        
    if page<35:        
        driver.find_element_by_xpath("//button[contains(text(),'下一页')]").click()
        
    time.sleep(1) # 睡1秒让网页加载完再去读它的html代码
driver.quit()


# In[117]:


SecuCode[-1]


# In[108]:


len(SecuCode)


# In[118]:


result_dict_liaoning={'company_code':SecuCode,'company_name':CompName,'company_project':MainProj,'capital':Capital}
result_liaoning=pd.DataFrame(result_dict_liaoning)


# In[119]:


result_liaoning

