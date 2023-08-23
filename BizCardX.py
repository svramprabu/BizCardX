import streamlit as st 
# from io import StringIO
import easyocr
from PIL import Image
import re
import pandas as pd 
import sqlite3

conn = sqlite3.connect('bizcard_database.db')
cursor = conn.cursor()
# cursor.execute('DROP table IF EXISTS bizcard_details')

st.title("Extracting Business Card Data with OCR")
st.toast('Loading Your data into db!', icon='😍')

def upload_n_x_data(uploaded_file):
    
    st.sidebar.image(Image.open(uploaded_file))
    IMAGE_PATH = uploaded_file.getvalue() 
    reader = easyocr.Reader(['en'])
    result = reader.readtext(IMAGE_PATH,paragraph="False")
    
    data_from_card=[]
    for key in range(len(result)):
        data_from_card.append(result[key][1])
        # break
    return data_from_card 

uploaded_file = st.file_uploader("Choose the Business card image file")

if uploaded_file is not None:
 
    details_in_card = upload_n_x_data(uploaded_file)
    # details_in_card
    
    string_of_details=""
    for x in details_in_card:
        string_of_details=string_of_details+' '+x
    # string_of_details
    
    details_dict={'email':['none'],'contact_no':['none'],'address':['none'],'website':['none'],'name':['none'],'designation':['none'],'company_name':['none']}
    
    for each_detail in details_in_card:
        if re.findall("\w*@\w*.com",each_detail):
            details_dict['email']=re.findall("\w*@\w*.com",each_detail)
        if re.findall("\d{3}-\d{3}-\d{4}",each_detail):        
            details_dict['contact_no']=[' '.join(map(str, (re.findall("\+*\d{3}-\d{3}-\d{4}",each_detail))))]
        if re.search("\d+ [\d\w ,;]+",each_detail):
            details_dict['address']=re.findall("\d+ [\d\w ,;]+",each_detail)
        if re.search("[w|W]{3}[. ]\w+[. ]*com",each_detail):
            details_dict['website']=re.findall("[w|W]{3}[. ]\w+[. ]*com",each_detail)
   

    details_dict['name']=st.sidebar.text_input('name details in card',value=f"{string_of_details}",key = "name",help="please check the content and make corrections if any")             
    details_dict['designation']=st.sidebar.text_input('designation details in card',value=f"{string_of_details}",key = "designation",help="please check the content and make corrections if any")             
    details_dict['company_name']=st.sidebar.text_input('company details in card',value=f"{string_of_details}",key = "company_name",help="please check the content and make corrections if any")             
    details_dict['email']=st.sidebar.text_input('email details in card',value=f"{details_dict['email'][0]}",key = "email",help="please check the content and make corrections if any")             
    details_dict['contact_no']=st.sidebar.text_input('contact_no details in card',value=f"{details_dict['contact_no'][0]}",key = "contact_no",help="please check the content and make corrections if any")             
    details_dict['address']=st.sidebar.text_input('address details in card',value=f"{details_dict['address'][0]}",key = "address",help="please check the content and make corrections if any")             
    details_dict['website']=st.sidebar.text_input('website details in card',value=f"{details_dict['website'][0]}",key = "website",help="please check the content and make corrections if any")             

    df = pd.DataFrame(details_dict,index=[0])
    st.write("you may also edit details from below table")
    edited_df = st.experimental_data_editor(df)   
    
if st.button("Click to details into SQLite db"):    
    
    # cursor.execute('DROP table bizcard_details if exists')
    # conn.commit()
    sql = 'create table if not exists ' + 'bizcard_details' + ' (email TEXT PRIMARY KEY, contact_no TEXT, address TEXT, website TEXT, name TEXT, designation TEXT, company_name TEXT)'
    cursor.execute(sql)
    
    insert_query = '''
    INSERT OR REPLACE INTO bizcard_details (email, contact_no, address , website , name , designation , company_name )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    val=tuple(edited_df.loc[0])
    cursor.execute(insert_query,val)
    conn.commit()

    df = pd.read_sql_query('SELECT * FROM bizcard_details', conn)
    conn.close()
    df

else:
    st.write("")

