#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:47:06 2019

@author: yanzhiwen
"""

import xml.dom.minidom
import re
import pandas as pd

#import file
DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')

#creat dataframe to save store data
df = pd.DataFrame(columns = ["id", "name", "definition", "childnodes"]) 

#count childnodes 
def countingnodes(id,aset):
    for term in terms:
        parents = term.getElementsByTagName('is_a')
        geneid = term.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                aset.add(geneid)
                countingnodes(geneid,aset)

                
for term in terms:   
    # get content in defstr
    defstr = term.getElementsByTagName('defstr')[0]
    text = defstr.childNodes[0].data 
    #find description contains the word 'autophagosome'
    if re.search(r'autophagosome',text):
        # get id, name and childnodes
        id =term.getElementsByTagName ("id")[0].childNodes[0].data
        name = term.getElementsByTagName ("name")[0].childNodes[0].data
        aset=set()
        countingnodes(id,aset)
        
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'defination':[text],'childnodes':[len(aset)]}))
        
#save to excel    
df.to_excel(r'/Users/wanwan/Documents/IBI/L8/autophagosome.xlsx', encoding='utf-8', index=False, header=False)


              