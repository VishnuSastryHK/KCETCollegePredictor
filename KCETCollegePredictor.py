import streamlit as st
import pandas as pd


df = pd.read_csv("/home/vishnu/VishnuSastryHK/VirtualEnvs/StreamLit/CET-CutOffs2019.csv")
outputdframe = pd.DataFrame(columns = ['Branch', 'College', 'Location', 'Cutoff'])

opdfCheckChance = pd.DataFrame(columns = ['Branch', 'Cutoff','Chances', 'Difference between your rank and Cutoff'])

st.write("""# Sastry's KCET College Predictor """)

st.sidebar.subheader("""Enter the deatalis here 👇""")
rank = st.sidebar.text_input('Enter your Rank:')

if(rank=="" or rank.isnumeric()==False ):
    st.sidebar.text("""Invalid Rank""")
else:
    rank=int(rank)

Branch_List=st.sidebar.multiselect("Select preferred branch/branches:",("AI/ML","CS","IE","EC"))
category=st.sidebar.selectbox("Select Category:",("1G","1K"))

input_college=st.sidebar.multiselect("Select Preferred College/Colleges:",("University Visveswariah College of Engineering","B M S College of Engineering","BMS Institute of Technology"))



index_of_category=df.columns.get_loc(category)
Index_Labels_For_Branch=[]


##Code for - List of Colleges in which you can except a seat

for i in Branch_List:
    Index_Labels_For_Branch=(df.query("Branch==@i").index.tolist())
   
    for j in Index_Labels_For_Branch: 
        branch=df.iloc[j]['Branch']
        college=df.iloc[j]['College']
        location=df.iloc[j]['Location']
        cutoff=df.iloc[j][category]
        cutoff=int(cutoff)
        if(rank<cutoff):      
            outputdframe = outputdframe.append({'Branch' : branch, 'College' : college, 'Location' : location, 'Cutoff' : int(cutoff)}, 
                    ignore_index = True) 
            

outputdframe=outputdframe.sort_values(['Cutoff'], ascending = True,ignore_index=True) 


df2 = outputdframe.style.set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
df2.set_properties(**{'text-align': 'left'}).hide_index()

#st.write(outputdframe)
if(len(Branch_List)>0):
    st.text("\n\n")
    st.write("##### List of Colleges in which you can except a seat:")
    st.text("..........................................................................................")
    st.text("\n")
    st.dataframe(df2)


##Code for - Check your chances of getting into the preferred collges:


if(len(input_college)>0):
    st.text("\n\n\n\n\n\n")
    st.write("##### Check your chances of getting into the preferred collges:")
    st.text("\n\n..........................................................................................")
    listOfUnavailableBranches=[]


    for i in input_college:
        for j in Branch_List:

            lst=df.loc[(df['College'] == i),'Branch'].tolist()
            if(j not in lst):
               listOfUnavailableBranches.append(j)
            else:
                cutoff=df.loc[(df['College'] == i) & (df['Branch'] == j),category]
                
                cutoff=int(cutoff)
                if(rank<cutoff):
                    string=str(cutoff-rank)+ "   ;   Rank < Cutoff"
                    opdfCheckChance = opdfCheckChance.append({'Branch' : j,  'Cutoff' : cutoff,'Chances' : "High", 'Difference between your rank and Cutoff' : string } , ignore_index = True) 

                else:
                   string=str(rank-cutoff)+"   ;   Rank > Cutoff"
                   opdfCheckChance = opdfCheckChance.append({'Branch' : j,  'Cutoff' : cutoff,'Chances' : "Low", 'Difference between your rank and Cutoff' : string}, ignore_index = True) 
 
    
        st.write("####", i,":")
        st.text("\n")
        lenOfListOfUnavailableBranches=len(listOfUnavailableBranches)
        joined_list = ",".join(listOfUnavailableBranches)
    
        if((lenOfListOfUnavailableBranches)>0):
            if(lenOfListOfUnavailableBranches==1):
               st.write("This college doesn't offer ",joined_list," branch")
                
            else:
                st.write("This college doesn't offer ",joined_list," branches")
        
            listOfUnavailableBranches=[]

        if(opdfCheckChance.shape[0]>0):
            st.dataframe(opdfCheckChance)
            opdfCheckChance=opdfCheckChance[0:0]



##Code for - Option Entry / Preference List




def generateOptionEntry():
    outputdframe = pd.DataFrame(columns = ['Branch', 'College', 'Location', 'Cutoff'])
    count_rows=0
    
    for i in Branch_List:
        Index_Labels_For_Branch=(df.query("Branch==@i").index.tolist())
   
        for j in Index_Labels_For_Branch: 
            branch=df.iloc[j]['Branch']
            college=df.iloc[j]['College']
            location=df.iloc[j]['Location']
            cutoff=df.iloc[j][category]
            cutoff=int(cutoff)
            outputdframe = outputdframe.append({'Branch' : branch, 'College' : college, 'Location' : location, 'Cutoff' : int(cutoff)}, 
                        ignore_index = True)
            

    outputdframe=outputdframe.sort_values(['Cutoff'], ascending = True,ignore_index=True) 


    df2 = outputdframe.style.set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    df2.set_properties(**{'text-align': 'left'}).hide_index()


    if(len(Branch_List)>0):
        st.text("\n\n")
        st.write("##### Here is your Option Entry / Preference List:")
        st.text("..........................................................................................")
        st.text("\n")
        st.dataframe(df2)
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

#st.markdown(f'<div style="font-size: small">{document}</div>',unsafe_allow_html=True)
button=st.sidebar.button("Generate Option Entry / Preference List")
if(button==True):
    generateOptionEntry()



