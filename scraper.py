import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(page_title="Web scraper",page_icon='🎇',layout='wide')


st.markdown("<h1 style='text-align: center'>Web Scraper</h1>",unsafe_allow_html=True)

with st.form('Search'):
    
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button('Search')

placeholder = st.empty()

if keyword:  
    page = requests.get(f'https://unsplash.com/s/photos/{keyword}')
    st.write('Page hit with status code: '+str(page.status_code))
    soup = BeautifulSoup(page.content,'lxml')
    rows = soup.find_all("div",class_="ripi6")
    print(len(rows))
    col1,col2 = placeholder.columns(2)
    for index,row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img",class_="tB6UZ a5VGX")
            lst = img['srcset'].split("?")
            anchor = figures[i].find("a",class_="rEAWd")
            print(anchor["href"])
            if i == 0:
                col1.image(lst[0])
                btn = col1.button("Download",key=str(index)+str(i))
                if btn:
                    print("Button has pressed"+str(anchor["href"]))
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
            else:
                col2.image(lst[0])
                btn = col2.button("Download",key=str(index)+str(i))
                if btn:
                    print("Button has pressed"+str(anchor["href"]))
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])



