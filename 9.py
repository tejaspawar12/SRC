import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel('gemini-pro')

def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text


Database_Fundamentals = st.selectbox("Select your level in Database fundamentals:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Computer_architecture = st.selectbox("Select your level in computer architecture:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Distributed_Computing_Systems = st.selectbox("Select your level in Distributed Computing Systems:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Cyber_Security = st.selectbox("Select your level in Cyber Security:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])

Networking = st.selectbox("Select your level in Networking:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Software_Development = st.selectbox("Select your level in Software Development:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Programming_Skills = st.selectbox("Select your level in Programming Skills:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
DSA= st.selectbox("Select your level in Data Structure and algorithms:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
OOP = st.selectbox("Select your level in Object Oriented Programming:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])

AI_ML = st.selectbox("Select your level in AI ML:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Data_Science= st.selectbox("Select your level in Data Science:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
O_S = st.selectbox("Select your level in Operating System:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Programming_Language = st.selectbox("Select your prefered Programming Language:", ["C", "C++", "Python", "R", "Java", "Ruby"])
#Logic_Building = st.selectbox("Select your level in Logic Building:", ["C", "C++", "Python", "R", "Java", "Ruby"])
Logic_Building = st.selectbox("Select your level in Logic Building:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Mathematics = st.selectbox("Select your level in Mathematics :", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
 
Intrested_Subject = st.selectbox("Select your intrested subject:", ["Networks", "IOT", "Data Engineer", "Computer Architecture", "Hacking", "Programming", "Cloud Computing", "Software Engineering", "Management", "Parallel Computing", "Other"])
Other1 = st.text_input("mention your interested subject if you selected other otherwise type NA:")

ICA = st.selectbox("Select your intrested Career area:", ["testing", "System developer", "Cloud computing", "Security", "Web Developer", "Application developer", "Security", "Data Scientist", "AI ML Engineer", "Business Process Analyst", "Project Manager", "Product Manager", "OTHER"])
Other2 = st.text_input("mention your interested career area if you selected other OPTION otherwise type NA:")

TOCYWTSI = st.selectbox("Select type of comapny you want to settele in:", ["Service Based", "Product Based", "Cloud Service", "Web services", "Finance", "Testing and maintaince service", "Cloud Computing", "Product Development", "Business Process automtion", "AI ML based", "Sales and Marketing"])
 #Store inputs in a dictionary
user_data = {
       "Database_Fundamentals": Database_Fundamentals,
       "Computer_architecture": Computer_architecture,
       "Distributed_Computing_Systems": Distributed_Computing_Systems,
       "Cyber_Security": Cyber_Security,
       "Software_Development": Software_Development,
       "Programming_Skills": Programming_Skills,
       "DSA" : DSA,
       "OOP" : OOP,

       "AI_ML ": AI_ML,
       "Data_Science" : Data_Science,
       "Operating_System" : O_S,
       "Programming_Language" : Programming_Language,
       "Logic_Building" : Logic_Building ,
       "Mathematics" : Mathematics,
       "Intrested_Subject" : Intrested_Subject,
       "Other1" : Other1,
       "ICA" : ICA,
       "Other2" : Other2,
       "TOCYWTSI" : TOCYWTSI

}


prompt = '''You are an expert proficient in a diverse array of computer engineering domains,
           including Database Fundamentals, Computer Architecture, Distributed Computing 
           Systems, Cybersecurity, Software Development, Programming Skills, AI/ML, Data 
           Science, Data Structures and Algorithms, Object-Oriented Programming, Logic
           Building, Mathematics, Networking, IoT, and more, I possess a comprehensive
           understanding of the intricate facets of technology and its applications.

           Additionally, your expertise extends to various career areas within the 
           computer engineering field, encompassing roles such as Testing, System 
           Development, Cloud Computing, Security, Web Development, Application
           Development, Data Science, AI/ML Engineering, Business Process Analysis,
           Project and Product Management, among others. Furthermore, you possess thorough
          knowledge of companies across diverse sectors, ranging from Service-Based and 
          Product-Based companies to Cloud Services Providers, Financial Institutions, and
          beyond.

         Utilizing your vast expertise, you can provide tailored guidance to individuals
         seeking career advice and also provide roadpmap so that they can get their job
        in the computer engineering domain. By analyzing the user's preferences and 
        background, you can offer a detailed roadmap tailored to their specific career 
        aspirations. This roadmap may include recommendations on skill development, 
        specialization areas, suitable job roles to pursue, and potential companies to 
        target, ensuring a strategic approach towards achieving their desired career goals.

        In essence, you aim to empower individuals with the knowledge and insights
        necessary to navigate the complex landscape of computer engineering careers 
        successfully. Through meticulous analysis and personalized recommendations, 
        you strive to assist individuals in realizing their full potential and securing 
        rewarding opportunities in their preferred job roles within the dynamic tech 
        industry.

        Provide Career roadmap solution using the data collected from user and stored in the 
        user_data array in following way only do not add anything else than below mentioned points
        1) Tell them prefered job role using the data collected data collected in use_data
        2) According to that prefered job role provide them proper and tailourd individual roadmap from start to end what 
        to do so to get thee job in prefered job role and company.
        3) provide them study material related to preferd job role which is available on internet.
        4) provide guidance job searching and guidance'''

#def get_gemini_repsonse(user_data,prompt):
#model=genai.GenerativeModel('gemini-pro')
    #response=model.generate_content(user_data,prompt)
    #return response.text

submit=st.button("Provide me solution")

if submit:
    response= get_gemini_response(prompt)
    st.subheader("The Response is")
    st.write(response)
