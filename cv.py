import streamlit as st
import pandas as pd
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


###########################

#Header 

st.write("""
# Rasika Kulkarni, Junior Data Analyst
#### * Resume *
""")
image = Image.open(r"C:\Users\atharv\Desktop\Rasika\Resume\digital_cv\profile_photo\resume_photo.jpg")
st.image(image,width=150)

st.markdown('Summary')
st.info("""
- Junior Data Analyst, Electronics Engineer, Tech Enthusiast, Machine Learning ,Python.
- Stong Analytical skills
- Strong verbal and written communication skills
- Experienced Educator
""")

########## Navigation  ############################################

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Rasika Kulkarni</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Certification">Certification</a>
       </li> 
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
    
def txt4(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
   st.markdown(b)

def txt5(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################

st.markdown('''
## Education
''')

txt("**Data Analyst**, *WBS CODING SCHOOL*, Berlin",  '03/2023 - 07/2023')

txt("**Bachelor of Technology in Electronics and Telecommunication**, *Marathwada Institute of Technology*, India", '08/2002 -06/2005')                                

###############################
st.markdown('''
## Projects 
''')

txt3(" Heart disease prediction",'`Python`, `Steamlit`')
txt3(" Heart disease prediction dashboard using Tableu",'`Tableu`')
txt3(" Recommadaton system",'`Python`,`Steamlit`')
txt3(" Digital resume",'`Python`,`Steamlit`')

##################################

st.markdown('''## Skills ''')    
  
txt3('Programming', '`Python`, `SQL`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data Visualization', '`Seaborn`, `Tableu`,`Matplotlib`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`,')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Model deployment', '`streamlit`')

#################################
st.markdown('''
## Certification
''')

txt3('Tensor Flow','https://olympus.mygreatlearning.com/courses/56698/certificate')
txt3('Tableu Certification','https://certificates.simplicdn.net/share/4648475_1700063318.pdf')
txt3('Data Visualisation in Tableu ','https://olympus.mygreatlearning.com/courses/46844/certificate')
txt3('Data Visualisation','https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.kaggle.com%2Flearn%2Fcertification%2Frasikakul%2Fdata-visualization')
################################################
st.markdown('''
## Social_Media
''')

txt2('Linkedin', 'https://www.linkedin.com/in/16rasika/')
txt2('Github','https://github.com/16rasika')

