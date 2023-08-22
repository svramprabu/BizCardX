import streamlit as st 
# from io import StringIO
import easyocr
from PIL import Image
import re

st.title("Extracting Business Card Data with OCR")

def upload_n_x_data():
    uploaded_file = st.file_uploader("Choose a file")
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

details_in_card = upload_n_x_data()
details_in_card

details_dict={}
details_dict['name+designation']=[details_in_card[0].split()]
for each_detail in details_in_card:
    if re.findall("\w*@\w*.com",each_detail):
        details_dict['email']=re.findall("\w*@\w*.com",each_detail)
    if re.findall("\d{3}-\d{3}-\d{4}",each_detail):        
        details_dict['contact_no']=re.findall("\+*\d{3}-\d{3}-\d{4}",each_detail)
    if re.search("\d+ [\d\w ,;]+",each_detail):
    # st.write(re.findall("\d+ [\d\w ,;]+",each_detail))
        details_dict['address']=re.findall("\d+ [\d\w ,;]+",each_detail)
    if re.search("[w|W]{3}[. ]\w+[. ]*com",each_detail):
        details_dict['website']=re.findall("[w|W]{3}[. ]\w+[. ]*com",each_detail)
    


details_dict        


