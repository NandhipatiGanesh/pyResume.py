import streamlit as st
import pandas as pd
 

st.set_page_config(
    page_title="Portfolio",
)

# Using object notation
#add_selectbox = st.sidebar.selectbox(
  #  "My Digital Marketing Resume",
 #   ("_","Digital Marketing",)
#)



# Define CSS styles for the left and right columns
left_style = """
    font-family: 'Tangerine';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
    float: left;
    width: 70%;
    padding-right: 30px;
"""

right_style = """
    font-family: 'Tangerine';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
    padding: 20px 0px 0px 0px;
    float: right;
    width: 30%;
"""

# Create the left and right columns
left_column, right_column = st.columns([3, 1])

# Apply the CSS styles to the columns
left_column.markdown(f'<div style="{left_style}">', unsafe_allow_html=True)
right_column.markdown(f'<div style="{right_style}">', unsafe_allow_html=True)

# Add content to the left column

left_column.markdown("<h5 style='text-align: left;'>Name: N.Ganesh Kumar</h5>", unsafe_allow_html=True)
left_column.text("Email:nandhipatiganeshkumar16@gmail.com")
left_column.text("Contact Number:+917569753062")

# Add content to the right column

right_column.markdown("<h5 style='text-align: left;'>Address</h5>", unsafe_allow_html=True)
right_column.text("Vadamalapet\nTirupati District, Andhra Pradesh\nIndia,")



#create table and put under expander
df = pd.DataFrame({
   'Course': ['B.Tech(CSE)', 'Higher Secondary', 'Secondary School'],
  'Institution': ['Sri Venkata Perumal College of Engineering(Autonomous), Puttur', 'Sri Chaitany Junior College, Tirupati', 'Sri Viswa Vani High School, Vadamalapet'],
  'Board/University':['JNTU Ananthapur','Board of Intermediate','Board of Secondary Education'],
  'Year of Completion':['2022','2018','2016'],
  'Percentage/Grade':['62.0','76.0','7.7'],
})






tab1, tab2, tab3 = st.tabs(["**MySelf**", "**My Skills**", "**My Works**"])



with tab1:
    with st.expander("**Career Objective**"):
     st.write( """To achieve a position in an esteemed organization where in I can put my knowledge and skills
        in practice for the development of the organization and give myself a chance to face new challenges& develop an ever learning 
        atmosphere around me.
        """ )  
    
    with st.expander("**Education Details**"):
       st.table(df)
      
    with st.expander("**Personal Details**"):
       
        st.write("• Date of Birth   -16-11-1999")
        st.write("• Gender-Male")
        st.write("• Nationality-Indian")
        st.write("• Languages Known  - English,Telugu, and Tamil,Hindi are Understandable")
        st.write("• Hobbies-Learning New Stratagies and Technologies, Playing Games") 
    
   



with tab2:
   with st.expander("**Programming Languages**"):
    st.write("• **Python**-*intermediate level*")
    st.write("• **C&Java**-*Basics*")   
    
   with st.expander("**Web Technologies**"):
        st.write("• **HTML**-*Very Good*")
        st.write("• **CSS**-*Very Good*")
        st.write("• **Javascript**-*Intermediate*")
        st.write("• **Node js & React Js**-Basic")
   with st.expander("**Non-Technical**"):
       st.write("• **SEO**-*Advanced Level*")
       st.write("• **Social Media Marketing**-*Advanced*")
   with st.expander("**Design&Development**"):
       st.write("• **Wordpress Design**-*Advanced Level*")
       st.write("• **WebDesigning**-*Intermediate*")    
            
        
with tab3: 
   with st.expander("with **Programming Languages**"):
       st.write("""• **Crypto Currency Price Prediction**
                by using \n**Python,Machine Learning**
                *Description*\n The prediction model will describe you whether to invest in the cryptocurrency or not.Here, we choose to minimize the risk for investing i.e. we aim to inverse and analysis of bitcoin prediction
                """)
       st.write("• [**Python Resume like portfolio**](https://nandhipatiganesh-pymyresume-py-resume-53237f.streamlit.app/)-Basic level")
       st.write("more Coming Soon") 
   with st.expander("with **Web Technologies**"):
       st.write("""• [**Resume Builder by using Node.js & React js**](https://github.com/NandhipatiGanesh/MyResumeBuilder) by using npm packages
                Source Code-teken from github
                """)
       st.write("more coming soon")   
   with st.expander("**Design&Development**"):
     st.write("""• [**Freshersway.in**](https://freshersway.in/)-Jobs Portal
              *About* This site for Blogging Well Optimised for SEO,
               Developed by Using Various Techniques""")
     st.write("• [**makesyoushock.com**](https://makesyoushock.com/)-mobile Reviews site")
     st.write("• [**rocketnews.in**](https://rocketnews.in/)-News site")
     st.write("• [**Leadsuccesser.com**](https://leadsuccesser.com/)-not active")
     st.write("• [**mhtjobs.online**](https://mhtjobs.online/)-not active")
  
#add a footer 

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://freshersway.in/" target="_blank">Ganesh Kumar</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)    
  
    

   
