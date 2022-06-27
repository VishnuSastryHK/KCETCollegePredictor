import streamlit as st
import pandas as pd
import requests
import io
from PIL import Image
image = Image.open('branch_code_img_faded.jpg')

#Page Configurations
st.set_page_config(page_title="KCETGo",page_icon="",layout="wide",initial_sidebar_state="expanded")

#Hide the top-right hamburger navbar
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


col_names = ["CETCode",	"College" ,"Location",	"Branch",	"1G",	"1K",	"1R", 	"2AG",	"2AK",	"2AR",	"2BG",	"2BK",	"2BR",	"3AG",	"3AK",	"3AR",	"3BG",	"3BK",	"3BR",	"GM",	"GMK",	"GMR",	"SCG",	"SCK",	"SCR",	"STG",	"STK",	"STR"]
#df = pd.read_csv("https://github.com/VishnuSastryHK/KCETCollegePredictor/blob/master/CET_Database_Final2019.csv", sep='[:,|_()]\s+',names=col_names, header=None, 
#delimiter=',' , engine="python")#)#,sep=r'\s*,\s*', sep="\s+|;|:", error_bad_lines=False)# names=col_names)
#print(df)
url = "https://github.com/VishnuSastryHK/KCETCollegePredictor/raw/master/CET_Database_Final2020.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))
outputdframe = pd.DataFrame(columns = ['Branch', 'College', 'Location', 'CET Code','Cutoff'])
pd.set_option('colheader_justify', 'left')

opdfCheckChance = pd.DataFrame(columns = ['Branch', 'Cutoff','Chances', 'Difference between your rank and Cutoff'])


st.write("""# KcetGo """)
st.write("""### Right Analysis and Prediction can lead to Right Choices !!\n Catch the right flight from KCET to your dreams """)

st.sidebar.subheader("""Enter the details here 👇""")
rank = st.sidebar.number_input('Enter your Rank*:', min_value=0, value=00, step=1)
rank=int(rank)

st.markdown('<style>' + open('style2.css').read() + '</style>', unsafe_allow_html=True)

Branch_List=st.sidebar.multiselect("Select preferred branch/branches*:",(
"AD",
"AE",                                                                        
"AI",
"AT",
"AU",
"BC",
"BD",
"BE",
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
"CY",
"DS",
"EC",
"EE",
"EI",
"EN",
"ER",
"ES",
"ET",
"IC",
"IE",
"II",
"IM",
"IO",
"IP",
"IT",
"LC",
"MC",
"MD",
"ME",
"MM",
"MR",
"MT",
"OP",
"PL",
"PT",
"RO",
"SE",
"SS",
"ST",
"TC",
"TX",
"UP",
"UR"))
st.sidebar.text("Scroll down for reference")
category=st.sidebar.selectbox("Select Category:*",("1G", "1K",	"1R",	"2AG",	"2AK",	"2AR",	"2BG",	"2BK",	"2BR",	"3AG",	"3AK",	"3AR",	"3BG",	"3BK",	"3BR",	"GM",	"GMK",	"GMR",	"SCG",	"SCK",	"SCR",	"STG",	"STK",	"STR"), index=15)
District_List=st.sidebar.multiselect("Select to filter by District:",("Bellary",
"Belgaum",
"Bengaluru",
"Bidar",
"Chamarajanagar",
"Chikballapur",
"Chikkamagaluru",
"Chitradurga",
"Dakshina Kannada",
"Davangere",
"Dharwad",
"Gadag",
"Hassan",
"Haveri",
"Gulbarga",
"Kodagu",
"Kolar",
"Koppal",
"Mandya",
"Mysore",
"Raichur",
"Ramanagara",
"Shimoga",
"Tumkur",
"Udupi",
"Uttara Kannada",
"Bijapur",
"Yadgir",
))

input_college=st.sidebar.multiselect("Select Preferred College/Colleges:",(
"Acharya Institute of Technology",
"Achutha Institute of Technology",
"ACS College of Engineering",
"Adhichunchanagiri Institute of Technology",
"Adichunchanagiri University(Formerly BGSIT)",
"AGM Rural Engineering College",
"AJ Institute Of Engineering And Technology",
"Akshaya Institute of Technology",
"Alliance University",
"Alpha College Engineering",
"Alva`s Institute of Engineering and Technology",
"AMC Engineering College ",
"Amrutha Institute of Engineering and Mangement",
"Angadi Institute of Technology and Management",
"ATME College of Engineering",
"Atria Institute of Technology",
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
"BLDE As V.P. Dr. P. G. Hallakatti College of Engg. and Tech",
"BMS College of Engineering",
"BMS College of Engineering (Aided)",
"BMS Institute of Technology and Management",
"BNM Institute of Technology",
"Brindavan College of Engineering",
"BTL Institute of Technology and Management",
"C Byre Gowda Institute of Technology",
"Cambridge Institutute of Technology",
"Canara Engineering College",
"Cauvery Institute of Technology",
"Channabasaveshwara Institute of Technology ",
"City Engineering College",
"CMR Institute of Technology",                                                                           
"CMR University",
"Coorg Institute of Technology",
"Dayananda Sagar Academy of Technology",
"Dayananda Sagar College of Engineering",
"Dayananda Sagar University",
"DONBOSCO Institute of Technology ",
"Dr. Ambedkar Institute Of Technology",
"Dr. Ambedkar Institute Of Technology (Aided)",
"Dr. Sri. Sri. Sri. Shivakumara Mahaswamyji College of Engineering",
"Dr.T.Thimmaiah Institute of Technology",
"East Point College of Engineering and Technology",
"East West College of Engineering",
"East West Institute of Technology",
"Ekalavya Institute of Technology",
"G Madegowda Institute of Technology",
"Ghousia Engineering College",                                                                          
"Gitam School Of Technology",
"Global Academy of Technology ",
"GM Institute of Technology",
"Gopalan College of Engineering and Management",
"Government Engineering College",
"GSSS Institute of Engineering and Technology for Women",
"Gurunanak Dev Engineering College",
"Hira Sugar Institute of Technology",
"HKBK College of Engineering ",
"HKEs SLN College of Engineering",
"HMS Institute of Technology ",
"Impact College of Engineering and Applied Sciences",
"Islamia Institute of Technology",
"Jain Acharya Gundharnandi Maharaj Institute of Technology",
"Jain College of Engineering",
"Jain College of Engineering and Research",
"Jain College of Engineering and Technology",
"Jain Institute of Technology",
"Jawaharlal Nehru National College of Engineering",
"Jnanavikasa Institute of Technology",
"JSS Academy of Technical Education",
"JSS Science and Technology University(Formerly SJCE)",
"JSS Science and Technology University(Formerly SJCE) (Aided)",
"Jyothi Institute of Technology",
"K L E Institute of Technology",
"K L E Ss K L E College of Engineering and Technology",
"Kalpatharu Institute of Technology",
"Karavali Institute of Technology",
"KCT Engineering College",
"Khaja Banda Nawaz University",
"KLE Dr. M S Sheshagiri College of Engineering and Technology",
"KLE Technological University(Formerly BVBCET)",
"KLS Gogte Institute of Technology",
"KLS Viswanathrao Deshpande Institute of Technology",
"KNS Institute of Technology ",
"KS Institute of Technology",
"KS School of Engineering And Management",
"KVG College of Engineering",
"Lingarajappa Engineering College",
"Maharaja Institute of Technology",
"Maharaja Institute of Technology-Mysore",
"Malnad College of Engineering",
"Malnad College of Engineering (Aided)",
"Mangalore Institute of Technology and Engineering",
"Mangalore Marine College and Technology",
"Mangalore, Dakshina Kannada Institute of Technology and Engineering",
"Maratha Mandal Engineering College",
"Moodalakatte Institute of Technology",
"MS Engineering College",
"MS Ramaiah Institute of Technology",
"MS Ramaiah University of Applied Sciences",
"MVJ College of Engineering",
"Mysore College of Engineering and Management",
"Mysuru Royal Institute of Technology",
"Nagarjuna College of Engineering and Technology",
"Navodaya Institute of Technology",
"NDRK Institute of Technology",
"New Horizon College of Engineering ",
"NIE Institute of Technology",
"Nitte Meenakshi Institutute of Technology",
"Nitte School of Architecture",
"NMAM Institutute of Technology",
"P E S Institute of Technology and Management",
"PA College of Engineering",
"PDA College of Engineering",
"PDA College of Engineering (Aided)",
"PES College of Engineering",
"PES College of Engineering (Aided)",
"PES University",
"PES University (Ring Road Campus)",
"Presidency University",
"Proudadevaraya Institute of Technology",
"R.R. Institute of Technology",
"Rajarajeswari College of Engineering",
"Rajeev Institute of Technology",
"Rajiv Gandhi Institute of Technology",
"Rao Bahadur Y.Mahabaleswarappa Engineering College",
"Reva University",
"RL Jalappa Institute of Technology",
"RNS Institute of Technology",
"RTE Socity`s Rural Engineering College",
"RV College of Engineering",
"RV Institute of Technology and Management",
"S D M Institute of Tech",
"S E A College of Engineering and Technology",
"S.G.Balekundri Institute of Technology",
"Sahyadri College of Engg. and Management",
"Sai Vidya Institute of Technology",
"Sambhram Institute of Technology",
"Sampoorna Institute of Technology and Research",
"Saptagiri College of Engineering.",
"Secab Institute of Engineering and Technology",
"Sharnbasva University (Formerly Godutai College for Women)",
"Sharnbasva University(Formerly Appa Inst. of Tech.)",
"Shetty Institute of Technology",
"Shreedevi Institute of Technology",
"Shri Madhwa Vadiraja Institute of Technology and Management",
"Shridevi Institute of Engineering and Technology",
"Siddaganga Institute of Technology",
"Sir M.Visveswaraya Institute of Technology",
"SJB Institute of Technology",
"SJC Institute of Technology",
"SJM Institute of Technology",
"SKSJT Institute of Engineering",
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
"The National Institute of Engineering (Aided)",
"The Oxford College of Engineering",
"Tontadarya College of Engineering",
"University B.D.T. college of Engineering",
"University Visveswariah College of Engineering",
"Veerappa Nisty Engineering College",
"Vemana Institute of Technology ",
"Vidya Vardhaka College of Engineering",
"Vidya Vikas Institute of Engineering and Technology ",
"Vijaya Vittala Institute of Technology",
"Visvesvaraya Technological University (VTU)",
"Vivekananada College of Engineering Technology",
"Vivekananada Institute of Technology",
"VSMs Somashekar R Kothiwale Institute of Technology",
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
        cetcode=df.iloc[j]['CETCode']
        cutoff=df.iloc[j][category]
        cutoff=int(cutoff)
        if(cutoff!=0):
            rank=int(rank)
            if(len(District_List)>0):
                for k in District_List:
                    if(k in location):
                        if(rank<cutoff):      
                            outputdframe = outputdframe.append({'Branch' : branch, 'College' : college, 'Location' : location, 'CET Code':cetcode, 'Cutoff' : int(cutoff)}, 
                            ignore_index = True) 
            else:
                if(rank<cutoff):      
                            outputdframe = outputdframe.append({'Branch' : branch, 'College' : college, 'Location' : location, 'CET Code':cetcode, 'Cutoff' : int(cutoff)}, 
                                ignore_index = True)
            

outputdframe=outputdframe.sort_values(['Cutoff'], ascending = True,ignore_index=True) 

df2=outputdframe.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])


if(len(Branch_List)>0):
    st.text("\n\n")
    st.write("##### List of Colleges in which you can except a seat:")
    st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.text("      ")
    st.markdown('<style>' + open('style2.css').read() + '</style>', unsafe_allow_html=True)
    st.markdown('<style>div[title="OK"] { color: green; } div[title="KO"] { color: red; } .data:hover{ background:rgb(243 246 255)}</style>', unsafe_allow_html=True)
    st.dataframe(df2)


##Code for - Check your chances of getting into the preferred collges:


if(len(input_college)>0):
    st.text("\n")
    st.text("\n")
    st.text("                        ")
    st.text("                        ")
    st.text("                        ")
    st.write("##### Check your chances of getting into the preferred colleges:")
    st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    listOfUnavailableBranches=[]
    listOfUnavailableBranchesForCategory=[]

    for i in input_college:
       
        lst=df.loc[(df['College']==i),'Branch'].tolist()
        #st.write(lst)

        for j in Branch_List:

            if(j in lst):
                cutoff1=df.loc[(df['College']==i) & (df['Branch'] == j),category]
                cutoff1=int(cutoff1)
                #st.write(cutoff1)
                
                if(cutoff1!= 0):
                    
                    if(rank<cutoff1):
                        string=int(cutoff1-rank);#+ "   ;   Rank < Cutoff"
                        opdfCheckChance = opdfCheckChance.append({'Branch' : j,  'Cutoff' : cutoff1,'Chances' : 'High', 'Difference between your rank and Cutoff' : string }, ignore_index = True) 
                    else:
                        string=int(-rank+cutoff1);#+"   ;   Rank > Cutoff"
                        opdfCheckChance = opdfCheckChance.append({'Branch' : j,  'Cutoff' : cutoff1,'Chances' : 'Low', 'Difference between your rank and Cutoff' : string}, ignore_index = True) 
                else:
                    listOfUnavailableBranchesForCategory.append(j)
                    #st.write(listOfUnavailableBranchesForCategory)
            else:
                listOfUnavailableBranches.append(j)
 
    
        st.write("####", i,":")
        st.text("\n")
        lenOfListOfUnavailableBranches=len(listOfUnavailableBranches)

        lenOfListOfUnavailableBranchesForCategory=len(listOfUnavailableBranchesForCategory)

        joined_list1 = ", ".join(listOfUnavailableBranches)
        joined_list2 = ", ".join(listOfUnavailableBranchesForCategory)
    
        if((lenOfListOfUnavailableBranches)>0):
            if(lenOfListOfUnavailableBranches==1):
               st.write("This college doesn't offer ",joined_list1,"branch")
                
            else:
                st.write("This college doesn't offer ",joined_list1," branches")
        
            listOfUnavailableBranches=[]

        if((lenOfListOfUnavailableBranchesForCategory)>0):
            if(lenOfListOfUnavailableBranchesForCategory==1):
               st.write(joined_list2,"branch is not available for this cateory")
                
            else:
                st.write(joined_list2," branches are not available for this category")
        
            listOfUnavailableBranchesForCategory=[]    
        
        df2=opdfCheckChance.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
            
        if(opdfCheckChance.shape[0]>0):
            st.dataframe(df2)
            #Code for the Line Chart
            for i in range(1):
                opdfCheckChance_copy=opdfCheckChance.copy(deep=True)
                opdfCheckChance_copy['Rank']=opdfCheckChance_copy['Cutoff']-opdfCheckChance_copy['Difference between your rank and Cutoff']
                chart_data=pd.DataFrame(opdfCheckChance_copy[['Cutoff','Rank']])
                if(chart_data.shape[0]>1):
                    st.line_chart(chart_data)
            st.text("\n\n\n")
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
            cetcode=df.iloc[j]['CETCode']
            cutoff=df.iloc[j][category]
            cutoff=int(cutoff)
            if(cutoff!=0):
                if(len(District_List)>0):
                    for k in District_List:
                        if(k in location):
                            outputdframe = outputdframe.append({'Branch' : branch, 'College' : college, 'Location' : location, 'CET Code':cetcode, 'Cutoff' : int(cutoff)}, 
                            ignore_index = True)
                else:
                    outputdframe = outputdframe.append({'Branch' : branch, 'College' : college, 'Location' : location, 'CET Code':cetcode, 'Cutoff' : int(cutoff)}, 
                            ignore_index = True)

    outputdframe=outputdframe.sort_values(['Cutoff'], ascending = True,ignore_index=True) 

    
    df2=outputdframe.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    df2.set_properties(subset=["Branch", "Location"],**{'text-align': 'left'}).hide_index()
   

    
    if(len(Branch_List)>0):
        st.text("\n")
        st.text("\n")
        st.text("                        ")
        st.text("                        ")
        st.write("##### Here is your Option Entry / Preference List:")
        st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.text("\n")
        st.dataframe(df2)



st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

button=st.sidebar.button("Generate Option Entry / Preference List")
if(button==True):
    generateOptionEntry()

st.text("\n")
st.text("\n")
st.text("Note: The predictions made in this app are purely based on KCET 2020 - Second Extended\nRound Cutoff Data.")
st.text("\n")
st.text("Made with ♥ by Vishnu Sastry H K & Sheetal Neeraj")
st.text("For any queries, drop in an email to us at hkvsastry3300@gmail.com")
st.text("\n")
st.text("\n")
st.write("[Click Here](https://drive.google.com/file/d/1Dz4ujeNT7z4cWF90UJznM84OFK-CgXxN/view?usp=sharing)for more information about colleges")
st.sidebar.text("\n")
st.sidebar.text("Branch Codes for Reference:")


st.sidebar.image(image, use_column_width=True)
st.sidebar.write("To view the entire list: [Click here](https://drive.google.com/file/d/1M6dvmJ5RlltWAMMCMg30C4sqbY6VNRv5/view?usp=sharing)")
