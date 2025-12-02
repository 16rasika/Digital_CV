
import streamlit as st
#from st_functions import st_button,load_css
from PIL import Image
from pathlib import Path


############ ---- GENERAL SETTINGS ---#########################
st.set_page_config(
   page_title="Digital CV | Rasika Kulkarni",
   #page_icon="👋",
)


#---- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
css_file = current_dir / "style.css"
#resume_file = current_dir / "digital_cv" / "CV.pdf"
#profile_pic = current_dir /  "profile-pic.png"


####################
#st.write("# Welcome to my profile! 👋")
st.markdown("<h2 style='text-align: center; color: black;'>Welcome to my Profile!👋 </h2>", unsafe_allow_html=True)

#st.write("""
# Rasika Kulkarni, Data Scientist
#""")
image= Image.open('resume_photo.jpg')

st.image(image, width=200)

st.markdown("<h1 style='text-align: center; color: grey;'>Rasika Kulkarni, Data Scientist</h1>", unsafe_allow_html=True)

st.write("E-MAIL: 16rasika@gmail.com")

st.markdown('## Summary',unsafe_allow_html=True)

st.info("""
- Junior Data Analyst
- Tech Enthusiast, Machine Learning , Python
- Electronics Engineer 
- Stong Analytical skills
- Strong verbal and written communication skills
- Strong teaching skills in both langauges English as well as Deutsch         
- Experienced Educator
""")

st.markdown(''' ## Education 

"Data Science':  'WBS CODING SCHOOL  Berlin', '03/2023 - 07/2023',

"B.Tech in Elect and Tele ": "Marathwada Institute of Technology, India", '08/2002 -06/2005'
            
''')     

st.markdown(''' ## Work Experience   


' Data Analytics Teacher' : 'Redi Digital School of Integration - Feb 2025 - Present',
            
' Data Literacy Tutor' :    'Redi Digital School of Integration - Feb 2025-Present',
            
' English Teacher':         'Learn Studio Barbarossa',           'Feb 2022- July 2022',
            
' German Teacher' :         'Pratibha Junior College, Pune University,India', 'Aug 2013- Mar 2016',
            
'Electronics Teacher' :     'Pratibha Junior College, Pune University,India', 'Aug 2013- Mar 2016'

'Technical Translator':      'Freelancer Project - Mar 2010 Nov 2013'             

            
''')

st.markdown('''## Skills   ''')
  
('Programming', '`Python`, `SQL`')
('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
('Data Visualization', '`Seaborn`, `Tableu`,`Matplotlib`')
('Data visualization', '`matplotlib`, `seaborn`, `plotly`,')
('Machine Learning', '`scikit-learn`')
('Deep Learning', '`TensorFlow`')
('Model deployment', '`streamlit`')
('Business Intelligence','`Power-BI`','`Tableau`')

 

st.markdown('''## Internship  
            
        'Successfully completed & awarded for my work'   

        'Cognify Technologies Power-BI': 'Dec 2024 - Jan 2025 '
            
        'Oasis Web Development' :        'Oct 2024 - Nov 2024'
            
        'Oasis Data Science':            'Jun 2024 - Jul 2024'            
            
        'Skill Genie Data Science':      'Feb 2024 - Mar 2024'
            
 ''')           

st.markdown ('''## Projects
    "SQL-Projects:",       
    "🏆 Analyzing Motorcycle part sales using Sql quries" 
    "🏆 Exploring Trendy names in Ameriacan Baby name with Sql quries "
             
    "Power-BI Dashboards:",  
    "🏆 Analyzing Job market data"   
    "🏆 HR Analytics " 
    "🏆 Analyzing Customer Churn "
    "🏆 E-commerce Analysis",      
    "🏆 Super-Store"
    "🏆 Net-Flix "
             
    "Recommender System:",
    "🏆 Book Recommendaton system "
    "🏆 Movie Recommendation system"
             
    "Tableau Dashboards: "        
    "🏆 Amazon Prime Dashboard "
    "🏆 British Airways,Tableau"
    "🏆 Heart Disease Dashboard"  
             
    "Machine-Learning: "        
    "🏆 Heart Stroke Prediction- Machine Learning & data analysis "                                                                                                        
    "🏆 Heart disease prediction - Created machine learning algorithm presented with streamlit app"
    "🏆 Breast Cancer-  Machine learning  hands on"   
    "🏆 Customer Segmentation - Unsupervised machine learning " 
    "🏆 Fake News Detection - Predicted with machine learning algorithms"
    "🏆 E-mail Classifier -  Natural Language Processing "
    "🏆 Image Classification - Python & machine learning "
    "🏆 Predictive Modelling for Agriculture, Python,Case-study, Machine Learning"         
                              
    "Data-analysis: "         
    "🏆 Covid-19- Data Analysis using python & python libraries" 
    "🏆 Elecric Vehicle - Data Analysis using python & python libraries"
             
    "Python + Streamlit: "         
    "🏆 BMI Calculator - Prepared app "
    "🏆 Restaurant menu system - Python Hoands on"
    "🏆 Bank Program - Python hands on "
    "🏆 Contact Book - Python hands on"
    "🏆 To-do-list- Python hands on "                                                    
''')
st.markdown('''## Datacamp Cerification
        
        'Acquired new skills through datacamp in the year 2025'
            
        'SQL':      'Sql Fundamentals',
            
        'SQL':      'Associate Data Engineer',

        'Power-BI': 'Data Anlyst in Power-BI',
            
        'Power-BI': 'Power-BI Fundamentals',

        'Snow-flake': 'Snowflake Fundamentals',
            
        'Snow flake': 'Associate Data Engineer',

        'Microsoft Azure ' : 'Microsoft Azure Fundamentals'
            
    ''')    

#st.write("Visit Datacamp","https://www.datacamp.com/portfolio/16rasika-b61fdec4-53d2-40ad-b8ea-f1ca2e63a51f")  
st.link_button("Visit Datacamp","https://www.datacamp.com/portfolio/16rasika-b61fdec4-53d2-40ad-b8ea-f1ca2e63a51f")

st.markdown('''## IBM Cerification 
            
        'Certification & Skills aquired in the year 2024 '   

        'Python for Data Science': 'Sept 2024'
            
        'Data Analysis Using Python': 'Dec 2024'
            
        'Data Science Methodology': ''
            
        'Machine Learning With Python' : 'May 2024'
            
        'Deep Learning Using Tensor Flow': 'April 2024'
            
        'Data Visualization Using Python': 'Sept 2024'
            
    'Reinforment Lerning & Deep Learning Essentials : Dec 2024'            
            
''')

################
st.markdown('''## Certification
            
    'Certificattion & Skills aquired in 2023'       

    'Tensor Flow Python':          'Great Learning, Dec 2023'

    'Tableu Certification':        'Simplilearn, Nov 2023'
        
    'Data Visualisation' :         'Kaggle, Oct 2023'
            
    'Data Cleaning'      :         'Kaggle , Sept 2023'  

    'Data Visualisation in Tableu ': 'Great Learning, Oct 2023'
                          
''')            

st.markdown('''## Forage Job Simulation
            
        'Hands-on through simulations'   

        'Common wealth':    'Data Management skills ',
            
        'Accenture':        'A hypothetical social media client',
            
        'PWC':              'Strengthened Power BI skills ',
            
        'British Airways':  'Scraped and analysed customer review data to uncover findings',
            
        'Tata':             'Data analysis using Power-BI Dashboard'
            
        ''')
st.link_button("Visit Forage","https://www.theforage.com/achievements")
##############################################

st.markdown('''## Interest 
            
        'What I do in free time :'
            - Leaning new technology like hugging face, NLP Libraries
            - Improving my german skills
            - Making dashboard using power-bi
            - making small projects  using stremlit app
    
     ''')

st.write ("## Social Media Links")

st.link_button("Visit LinkedIn","https://www.linkedin.com/in/16rasika/")

st.link_button("Visit Github", "https://github.com/16rasika/")

#st.link_button("Visit Datacamp","https://www.datacamp.com/portfolio/16rasika-b61fdec4-53d2-40ad-b8ea-f1ca2e63a51f")

