import streamlit as st 
# from io import StringIO
import easyocr
from PIL import Image
import re
import pandas as pd 

st.title("Extracting Business Card Data with OCR")

def upload_n_x_data(uploaded_file):
    # st.image(uploaded_file)
    # IMAGE_PATH = r'C:\Users\SVR\Documents\GitHub\BizCardX\card_uploads\1.png'
    st.image(Image.open(uploaded_file))
    IMAGE_PATH = uploaded_file.getvalue() 
    # if uploaded_file is not None:
        # To read file as bytes:
    reader = easyocr.Reader(['en'])
    # result = reader.readtext(IMAGE_PATH,paragraph="True")
    result = reader.readtext(IMAGE_PATH,paragraph="False")
    # result
    data_from_card=[]
    for key in range(len(result)):
        data_from_card.append(result[key][1])
        # break
    return data_from_card 
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
 
    details_in_card = upload_n_x_data(uploaded_file)
    details_in_card
    string_of_details=""
    for x in details_in_card:
        string_of_details=string_of_details+' '+x
    # string_of_details
    details_dict={'email':['none'],'contact_no':['none'],'address':['none'],'website':['none'],'name':['none'],'designation':['none'],'company_name':['none']}
    k=0
    # details_dict['name+designation']=[details_in_card[0].split()]
    for each_detail in details_in_card:
        if re.findall("\w*@\w*.com",each_detail):
            details_dict['email']=re.findall("\w*@\w*.com",each_detail)
        if re.findall("\d{3}-\d{3}-\d{4}",each_detail):        
            details_dict['contact_no']=[' '.join(map(str, (re.findall("\+*\d{3}-\d{3}-\d{4}",each_detail))))]
        if re.search("\d+ [\d\w ,;]+",each_detail):
        # st.write(re.findall("\d+ [\d\w ,;]+",each_detail))
            details_dict['address']=re.findall("\d+ [\d\w ,;]+",each_detail)
        if re.search("[w|W]{3}[. ]\w+[. ]*com",each_detail):
            details_dict['website']=re.findall("[w|W]{3}[. ]\w+[. ]*com",each_detail)
    #     else: 
    #         details_dict[f'other{k}']=each_detail
    #         k+=1

    # for each_detail in range(len(details_in_card)):
        # drop_input = st.selectbox('what input is this?',['name','designation','company_name'],key = f'{each_detail}123')
    details_dict['name']=st.text_input('name details in card',value=f"{string_of_details}",key = "name",help="please check the content and make corrections if any")             
    details_dict['designation']=st.text_input('designation details in card',value=f"{string_of_details}",key = "designation",help="please check the content and make corrections if any")             
    details_dict['company_name']=st.text_input('company details in card',value=f"{string_of_details}",key = "company_name",help="please check the content and make corrections if any")             
        # st.write("\n")
        # st.write("\n")
        # st.write("\n")
        # break

    # drop_input = st.selectbox('what input is this?',['name','designation','company_name'],key = f'{each_detail}123')

    # details_dict[f'{drop_input}']= st.text_input('details in card',value=f"{details_dict[f'{drop_input}']}",key = f"{each_detail}143",help="please check the content and make corrections if any")

    details_dict  

    df = pd.DataFrame.from_dict(details_dict)
    edited_df = st.experimental_data_editor(df)   

    import sqlite3

    # Connect to the database
    conn = sqlite3.connect('bizcard_database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # edited_df.to_sql('bizcard_details', conn, if_exists='append', index=False)
    edited_df.to_sql('bizcard_details', conn, if_exists='replace', index=False)
    # insert_query = '''
    # INSERT INTO bizcard_details (name, age, email)
    # VALUES (?, ?, ?)
    # '''

    df = pd.read_sql_query('SELECT * FROM bizcard_details', conn)
    conn.close()
    df

