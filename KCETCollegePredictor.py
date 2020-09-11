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

Branch_List=st.sidebar.multiselect("Select preferred branch/branches:",("AE",
"AI",
"AT",
"AU",
"BC",
"BI",
"BM",
"BT",
"CB",
"CC",
"CE",
"CH",
"CI",
"CO",
"CR",
"CS",
"CT",
"EC",
"EE",
"EI",
"EN",
"ER",
"ES",
"IE",
"IM",
"IP",
"MD",
"ME",
"MN",
"MR",
"MT",
"PE",
"PL",
"PT",
"RO",
"SE",
"ST",
"TC",
"TX",
"UP"))
category=st.sidebar.selectbox("Select Category:",("1G",	"1K",	"1R",	"2AG",	"2AK",	"2AR",	"2BG",	"2BK",	"2BR",	"3AG",	"3AK",	"3AR",	"3BG",	"3BK",	"3BR",	"GM",	"GMK",	"GMR",	"SCG",	"SCK",	"SCR",	"STG",	"STK",	"STR"))

input_college=st.sidebar.multiselect("Select Preferred College/Colleges:",("A J Institute Of Engineering And Technology",
"Acharya Institute of Technology ",
"Achutha Institute of Technology",
"ACS College of Engineering",
"Adhichunchanagiri Institute of Technology",
"Adichunchanagiri University(Formerly BGSIT)",
"AGM Rural Engineering College",
"Akshaya Institute of Technology",
"Alpha College Engineering",
"Alva`s Institute of Engineering and Technology",
"Alva`s Institute of Engineering and Technology (IInd Shift)",
"AMC Engineering College ",
"Amrutha Institute of Engineering and Mangement",
"Angadi Institute of Technology and Management",
"Anjuman Engineering College",
"APS College of Engineering",
"ATME College of Engineering",
"Atria Institute of Technology",
"B L D E As V.P. Dr. P. G. Hallakatti College of Engg. and Tech",
"B M S College of Engineering",
"B M S College of Engineering (Aided)",
"B M S Institute of Technology and Management",
"B N M Institute of Technology",
"B T L Institute of Technology and Management",
"Bahubali College of Engineering",
"Ballari Institute of Technology and Management",
"Bangalore College of Engineering and Technology ",
"Bangalore Institute of Technology",
"Bangalore Technological Institute",
"Bapuji Institute of Engineering and Technology",
"Basava Engineering School of Technology",
"Basavakalyana Engineering College ",
"Basaveshwara Engineering College",
"Bearys Institute of Technology",
"Bheemanna Khandre Institute of Technology",
"Biluru Gurubasava Mahaswamiji Institute of Technology",
"Brindavan College of Engineering",
"C Byre Gowda Institute of Technology",
"C M R Institute of Technology",
"Cambridge Institutute of Technology",
"Canara Engineering College",
"Cauvery Institute of Technology",
"Channabasaveshwara Institute of Technology ",
"City Engineering College",
"CMR University",
"Coorg Institute of Technology",
"Dayananda Sagar Academy of Technology",
"Dayananda Sagar College of Engineering",
"Dayananda Sagar College of Engineering(IInd Shift)",
"Dayananda Sagar University",
"DONBOSCO Institute of Technology ",
"Dr. Ambedkar Institute Of Technology",
"Dr. Sri. Sri. Sri. Shivakumara Mahaswamyji College of Engineering",
"Dr.T.Thimmaiah Institute of Technology",
"East Point College of Engineering and Technology",
"East West College of Engineering",
"East West Institute of Technology",
"G M Institute of Technology",
"G Madegowda Institute of Technology",
"G S S S Institute of Engineering and Technology for Women",
"Ghousia Engineering College",
"Girijabai Sail Institute of Technology",
"Gitam School Of Technology",
"Global Academy of Technology ",
"Gopalan College of Engineering and Management",
"Government Engineering College",
"Gurunanak Dev Engineering College",
"H K Es S L N College of Engineering",
"H M S Institute of Technology ",
"H.K.B.K.College of Engineering ",
"Hira Sugar Institute of Technology",
"Impact College of Engineering and Applied Sciences",
"Islamia Institute of Technology",
"J S S Academy of Technical Education",
"Jain Acharya Gundharnandi Maharaj Institute of Technology",
"Jain College of Engineering",
"Jain College of Engineering and Research",
"Jain College of Engineering and Technology",
"Jain Institute of Technology",
"Jawaharlal Nehru National College of Engineering",
"Jnanavikasa Institute of Technology",
"JSS Science and Technology University(Formerly SJCE)",
"JSS Science and Technology University(Formerly SJCE)",
"Jyothi Institute of Technology",
"K C T Engineering College",
"K L E Dr. M S Sheshagiri College of Engineering and Technology",
"K L E Institute of Technology",
"K L E Ss K L E College of Engineering and Technology",
"K L S Viswanathrao Deshpande Institute of Technology",
"K N S Institute of Technology ",
"K S Institute of Technology",
"K V G College of Engineering",
"K.L.S. Gogte Institute of Technology",
"K.S. School of Engineering And Management",
"Kalpatharu Institute of Technology",
"Karavali Institute of Technology",
"Khaja Banda Nawaz University",
"KLE Technological University(Formerly BVBCET)",
"Lingarajappa Engineering College",
"M S Engineering College",
"M S Ramaiah Institute of Technology",
"M V J College of Engineering",
"M V J College of Engineering(IInd Shift)",
"M.S. Ramaiah University of Applied Sciences",
"Maharaja Institute of Technology",
"Maharaja Institute of Technology-Mysore",
"Malnad College of Engineering",
"Mangalore Institute of Technology and Engineering",
"Mangalore Marine College and Technology",
"Mangalore, Dakshina Kannada Institute of Technology and Engineering",
"Maratha Mandal Engineering College",
"Moodalakatte Institute of Technology",
"Mysore College of Engineering and Management",
"Mysuru Royal Institute of Technology",
"N I E Institute of Technology",
"N M A M Institutute of Technology",
"Nagarjuna College of Engineering and Technology",
"Navodaya Institute of Technology",
"NDRK Institute of Technology",
"New Horizon College of Engineering ",
"New Horizon College of Engineering(IInd Shift)",
"Nitte Meenakshi Institutute of Technology",
"Nitte School of Architecture",
"P A College of Engineering",
"P A College of Engineering(IInd Shift)",
"P D A College of Engineering",
"P E S College of Engineering",
"P E S Institute of Technology and Management",
"P E S University",
"P E S University (Ring Road Campus)",
"Presidency University",
"Proudadevaraya Institute of Technology",
"R V Institute of Technology and Management",
"R. V. College of Engineering",
"R.L.Jalappa Institute of Technology",
"R.R.Institute of Technology",
"R.T.E Socity`s Rural Engineering College",
"Rajarajeswari College of Engineering",
"Rajeev Institute of Technology",
"Rajiv Gandhi Institute of Technology",
"Rao Bahadur Y.Mahabaleswarappa Engineering College",
"Reva University",
"RNS Institute of Technology",
"S D M Institute of Tech",
"S E A College of Engineering and Technology",
"S J B Institute of Technology",
"S J C Institute of Technology",
"S J M Institute of Technology",
"S K S J T Institute of Engineering",
"S.G.Balekundri Institute of Technology",
"Sahyadri College of Engg. and Management",
"Sai Vidya Institute of Technology",
"Sambhram Institute of Technology",
"Sambhram Institute of Technology(IInd Shift)",
"Sampoorna Institute of Technology and Research",
"Saptagiri College of Engineering.",
"Secab Institute of Engineering and Technology",
"Shaikh College of Engineering and Technology",
"Sharnbasva University (Formerly Godutai College for Women)",
"Sharnbasva University(Formerly Appa Inst. of Tech.)",
"Sha-Shib College of Engineering",
"Shetty Institute of Technology",
"Shreedevi Institute of Technology",
"Shreedevi Institute of Technology(IInd Shift)",
"Shri Madhwa Vadiraja Institute of Technology and Management",
"Shridevi Institute of Engineering and Technology",
"Siddaganga Institute of Technology",
"Sir M.Visveswaraya Institute of Technology",
"Smt. Kamala and Sri Venkappa M.Agadi College of Engg. and Tech.",
"Sri Basaveswara Institute of Technology",
"Sri Dharmasthala Manjunatheswara College of Engineering",
"Sri Krishna Institute of Technology",
"Sri Revana Siddeswara Institute of Technology",
"Sri Sairam College of Engineering(Formerly Shirdi Sai Engg) ",
"Sri Siddartha Institute of Technology",
"Sri Taralabalu Jagadguru Institute of Technology",
"Sri Venkateshwara College of Engineering",
"Sri Vinayaka Institute of Technology",
"Srinivas Institute of Technology",
"Srinivas University",
"St. Joseph Engineering College",
"T.John Engineering College",
"The National Institute of Engineering",
"The Oxford College of Engineering",
"Tontadarya College of Engineering",
"University B.D.T. college of Engineering",
"University Visveswariah College of Engineering",
"Veerappa Nisty Engineering College",
"Vemana Institute of Technology ",
"Vidya Vardhaka College of Engineering",
"Vidya Vikas Institute of Engineering and Technology ",
"Vijaya Vittala Institute of Technology",
"Vivekananada College of Engineering Technology",
"Vivekananada Institute of Technology",
"VSMs Somashekar R Kothiwale Institute of Technology",
"Yellamma Dasappa Institute of Technology",
"Yenepoya Institute of Technology"))



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



