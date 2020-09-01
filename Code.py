import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("F:\Academics\Paper with Aruna ma'am\CET-Cutoff-2Colleges.csv")

rank=input()
category=input()
branch1=input()
branch2=input()
branchSpecificOrCollegeSpecific=input()

index_of_category=df.columns.get_loc(category)
index_of_category

Index_Labels_For_Branch1 = df.query("Branch==@branch1").index.tolist() 
Index_Labels_For_Branch2 = df.query("Branch==@branch2").index.tolist() 
print(Index_Labels_For_Branch1)
print(Index_Labels_For_Branch2)

ict={}

def return_Dictionary_Of_Ranks_And_Indexes(Index_labels):
    dict={}
    for i in Index_labels:
        dict[int(df.iloc[i][category])]=int(i)
    return(dict)

def print_OptionEntry_For_Branch_Specific(dict1,dict2):
    slno=1
    for j in sorted(dict1):
    #print(j)
    #print(type(int(j)))
        if(int(rank)<int(j)):
            #print("Hi")
            branch_index=dict1[j]
            #print(branch_index)
            branch=df.iloc[branch_index]['Branch']
            college=df.iloc[branch_index]['College']
            print("{}. {} in {}".format( slno, branch, college))
            slno+=1
            
    for j in sorted(dict2):
    #print(j)
    #print(type(int(j)))
        if(int(rank)<int(j)):
            #print("Hi")
            branch_index=dict2[j]
            #print(branch_index)
            branch=df.iloc[branch_index]['Branch']
            college=df.iloc[branch_index]['College']
            print("{}. {} in {}".format( slno, branch, college))
            slno+=1   
        
def print_OptionEntry_For_College_Specific(dict): 
    slno=1
    for j in sorted(dict):
    #print(j)
    #print(type(int(j)))
        if(int(rank)<int(j)):
            #print("Hi")
            branch_index=dict[j]
            #print(branch_index)
            branch=df.iloc[branch_index]['Branch']
            college=df.iloc[branch_index]['College']
            print("{}. {} in {}".format( slno, branch, college))
            slno+=1



dict_For_Branch1=return_Dictionary_Of_Ranks_And_Indexes(Index_Labels_For_Branch1)
dict_For_Branch2=return_Dictionary_Of_Ranks_And_Indexes(Index_Labels_For_Branch2)
dict={**dict_For_Branch1,**dict_For_Branch2}#merge more than one dict into a single dict
print(dict)
print(dict_For_Branch1)
print(dict_For_Branch2)
print_OptionEntry_For_College_Specific(dict)
