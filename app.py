import streamlit as st
import sklearn
import joblib
import xgboost

def app():
    st.title("Steel Industry Consumption Energy Prediction")
    st.header("Epsilon Final Project Diploma")
    st.write("This project about prediction of steel energy consumption from DAEWOOSteelCo. Ltd in Gwangyang, SouthKorea")
    
    lagging_reactive_power = st.number_input('lagging_reactive_power')
    leading_reactive_power = st.number_input("leading_reactive_power")
    CO2 = st.selectbox('CO2',['0.00','0.01', '0.02','0.03','0.04', '0.05','0.06', '0.07'])
    lagging_power_factor = st.number_input('lagging_power_factor')
    leading_power_factor = st.number_input("leading_power_factor")
    NSM = st.number_input("NSM", value=0)
    week_status = st.radio('week_status', ['weekday', 'weekend'])
    load_type = st.radio("load_type", ['lightload','mediumload','maximumload'])
    year = st.number_input("Year", value=0)
    month = st.number_input("Month", value=0)
    day = st.number_input("Day", value=0)

    if week_status == 'weekday':
        week_status = 0
    else:
        week_status = 1

    if load_type == 'lightload':
        load_type = 0
    elif load_type == 'mediumload':
        load_type = 1
    else:
        load_type = 2

    raw_data = [lagging_reactive_power, leading_reactive_power, CO2, lagging_power_factor, leading_power_factor, NSM, week_status, load_type, year, month, day]
   
    model = joblib.load('model.h5')
    scaler = joblib.load('scaler.h5')
    predicted_value = round(model.predict(scaler.transform([raw_data]))[0])
    
    button = st.button('predict')

    if button:
        st.markdown(f'{predicted_value} KWh')
        
app()
