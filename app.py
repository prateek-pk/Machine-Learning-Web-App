import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

data=pd.read_csv('mushrooms.csv')
print(data.describe())

def main():
    st.title('Binary Classisfication Web Appwebweb🍄')
    st.sidebar.title('Alter Properties🍄')
    st.markdown('Are your mushrooms edible or poisonous🍄')
    st.sidebar.markdown('Are your mushrooms edible or poisonous🍄')

    @st.cache(persist=True)
    def load_data():
        data = pd.read_csv('mushrooms.csv')
        label=LabelEncoder()
        for col in data.columns:
            data[col]=label.fit_transform(data[col])
        return data

    @st.cache(persist=True)
    def split(df):
        y=df['class']
        x=df.drop(['class'], axis=1)
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3, random_state=0)
        return x_train,x_test,y_train,y_test

    

    df = load_data()
    x_train,x_test,y_train,y_test=split(df)

    if st.sidebar.checkbox('Show raw data',False):
        st.subheader('Mushroom Data set (Classification)')
        st.write(df)

if __name__ == '__main__':
    main()
