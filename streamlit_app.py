import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
from datetime import datetime, date
    

df = pd.read_csv('cleaned_df.csv')
data = df.copy()

# Setting page configuration
st.set_page_config(page_title="Aviation flights fare", page_icon="✈️", layout='wide')


model = joblib.load('aviation_model.p')    
sc = StandardScaler()

    # Inputs 
col1, col2 = st.columns((5,5))
with col1:
        airline_pred = st.selectbox("Airline Carrier", list(df['Airline'].unique()))
        airline_pred = {'IndiGo':3, 'Air India':1, 'Jet Airways':4, 'SpiceJet':8,
                'Multiple carriers':6, 'GoAir':2, 'Vistara':10, 'Air Asia':0,
                'Vistara Premium economy':11, 'Jet Airways Business':5,
                'Multiple carriers Premium economy':7, 'Trujet':9}.get(airline_pred, airline_pred)
        
        source_pred= st.selectbox("Departure City", list(df['Source'].unique()))    
        source_pred = {'Banglore':0, 'Kolkata':3, 'Delhi':2, 'Chennai':1, 'Mumbai':4}.get(source_pred, source_pred)
        
        destination_pred = st.selectbox("Arrival City", list(df['Source'].unique())) 
        destination_pred = {'New Delhi':5, 'Banglore':0, 'Cochin':1, 'Kolkata':4,
                    'Delhi':2, 'Hyderabad':3}.get(destination_pred, destination_pred)
        
        stops_pred= int(st.selectbox("Stops", options= df['Total_Stops'].unique()))
        
        duration_pred_scaled = sc.fit_transform([[int(st.number_input("Flight Duration (in minutes)",
                                                                    min_value=0, step=10))]])
    
        
    
with col2:
                
        add_info_pred= st.selectbox("Additional Services", list(df['Additional_Info'].unique()))
        add_info_pred = {'No info':7, 'In-flight meal not included':5, 'No check-in baggage included':6,
                    '1 Short layover':1, '1 Long layover':0, 'Change airports':4,
                    'Business class':3, 'Red-eye flight':8, '2 Long layover':2}.get(add_info_pred, add_info_pred)

        # day_pred= int(st.selectbox("Day", options= df['Day'].unique()))
        # month_pred= int(st.selectbox("Month", options= df['Month'].unique()))

        # Date Selection
        today = date.today()
        min_date = today + pd.DateOffset(days=1)
        max_date = today + pd.DateOffset(months=6)
        selected_date = st.date_input('Select a date', min_value=min_date, max_value=max_date, value=min_date)

        st.write(' ')
        st.write(' ')
        st.write('for Departure Hour, If the minutes more than 30, Please increase the hour by 1')
        
        dep_hour = int(st.number_input("Departure Hour (24 format)",min_value=0))

# Submit Button
if st.button("Submit 👇"):
        #input_data = np.array([[duration_pred_scaled[0][0], stops_pred, selected_date.day, selected_date.month, 
                                #dep_hour_pred_scaled[0][0], airline_pred, source_pred,
                                  #destination_pred, add_info_pred]])

        #input_data = np.array([[airline_pred,source_pred,destination_pred,add_info_pred,duration_pred_scaled,stops_pred, selected_date.day, selected_date.month,dep_hour]])
        st.write(input_data[0])
        Price = model.predict([[airline_pred,source_pred,destination_pred,add_info_pred,duration_pred_scaled,stops_pred, selected_date.day, selected_date.month,dep_hour]])
        # Display the price as a metric
        st.metric("Ticket Price", int(Price))
