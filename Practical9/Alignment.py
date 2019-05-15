#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:36:35 2019

@author: yanzhiwen
"""
# input BLOSUM62 matrix in an excel form
import xlrd
blosum62 = xlrd.open_workbook(r'1.xlsx')
sheet1 = blosum62.sheet_by_name('Sheet1')

#input three sequences and match each animo aicds to the table
humanseq='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouseseq='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
randomseq='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'

dict = {'A':0,'R':1,'N':2,'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19}

#define a function that could compare two sequence
def alignment(aseq,bseq):
    newalignment=[]
    edit_distance = 0
    score=0
    #match each animo acids in two seq with the matrix and find out the score
    for i in range(len(aseq)): 
        a = aseq[i]
        b = bseq[i]
        line = dict[a]  
        row = dict[b]
        score += sheet1.cell(line,row).value
        #this is for bonus project if score>=0 then add + 
        #and wirtten in blast-like way
        #also count the edit_distance
        if aseq[i]!=bseq[i] and score >= 0:
            edit_distance += 1 
            newalignment.append('+')
        if aseq[i]!=bseq[i] and score < 0:
            edit_distance += 1 
            newalignment.append('_')
        if aseq[i] == bseq[i]:
            newalignment.append(humanseq[i])

#print out all the result
    print('edit_distance:',edit_distance)
    print('score/len(aseq):',score/len(aseq))
    identity=(len(aseq)-edit_distance)/len(aseq)
    print('identity:',identity)
    #print(finalscore/len(aseq))
    print(aseq)
    print("".join(newalignment))
    print(bseq)

alignment(humanseq,mouseseq)
alignment(humanseq,randomseq)
alignment(mouseseq,randomseq)