import streamlit as st
import pickle

model = pickle.load(open(r"C:\Users\megha\Downloads\flight_rf.pkl", "rb"))

Journey_Date = st.date_input("Select Journey date")
departureTime = st.time_input("Select departure time")

arrivalTime = st.time_input("Select arrival time")

Total_stops = st.number_input("Select number of stops")

sources = ["Delhi", "Kolkata", "Mumbai", "Chennai"]
selectedSource = st.selectbox("Select source", sources)

destinations = ["Cochin", "Delhi", "New_Delhi", "Hyderabad", "Kolkata"]
selectedDestination = st.selectbox("Select destination", destinations)

airlines = [
    "Jet_Airways",
    "IndiGo",
    "Air_India",
    "Multiple_carriers",
    "SpiceJet",
    "Vistara",
    "GoAir",
    "Multiple_carriers_Premium_economy",
    "Jet_Airways_Business",
    "Vistara_Premium_economy",
    "Trujet",
]
selectedAirline = st.selectbox("Select an Airline", airlines)


def predict():
    Journey_day = Journey_Date.day
    Journey_month = Journey_Date.month
    Dep_hour = departureTime.hour
    Dep_min = departureTime.minute
    Arrival_hour = arrivalTime.hour
    Arrival_min = arrivalTime.minute
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)
    Air_India = 1 if selectedAirline == "Air_India" else 0
    GoAir = 1 if selectedAirline == "GoAir" else 0
    IndiGo = 1 if selectedAirline == "IndiGo" else 0
    Jet_Airways = 1 if selectedAirline == "Jet_Airways" else 0
    Jet_Airways_Business = 1 if selectedAirline == "Jet_Airways_Business" else 0
    Multiple_carriers = 1 if selectedAirline == "Multiple_carriers" else 0
    Multiple_carriers_Premium_economy = (
        1 if selectedAirline == "Multiple_carriers_Premium_economy" else 0
    )
    SpiceJet = 1 if selectedAirline == "SpiceJet" else 0
    Trujet = 1 if selectedAirline == "Trujet" else 0
    Vistara = 1 if selectedAirline == "Vistara" else 0
    Vistara_Premium_economy = 1 if selectedAirline == "Vistara_Premium_economy" else 0
    s_Chennai = 1 if selectedSource == "Chennai" else 0
    s_Delhi = 1 if selectedSource == "Delhi" else 0
    s_Kolkata = 1 if selectedSource == "Kolkata" else 0
    s_Mumbai = 1 if selectedSource == "Mumbai" else 0
    d_Cochin = 1 if selectedDestination == "Cochin" else 0
    d_Delhi = 1 if selectedDestination == "Delhi" else 0
    d_Hyderabad = 1 if selectedDestination == "Hyderabad" else 0
    d_Kolkata = 1 if selectedDestination == "Kolkata" else 0
    d_New_Delhi = 1 if selectedDestination == "New_Delhi" else 0
    prediction = model.predict(
        [
            [
                Total_stops,
                Journey_day,
                Journey_month,
                Dep_hour,
                Dep_min,
                Arrival_hour,
                Arrival_min,
                dur_hour,
                dur_min,
                Air_India,
                GoAir,
                IndiGo,
                Jet_Airways,
                Jet_Airways_Business,
                Multiple_carriers,
                Multiple_carriers_Premium_economy,
                SpiceJet,
                Trujet,
                Vistara,
                Vistara_Premium_economy,
                s_Chennai,
                s_Delhi,
                s_Kolkata,
                s_Mumbai,
                d_Cochin,
                d_Delhi,
                d_Hyderabad,
                d_Kolkata,
                d_New_Delhi,
            ]
        ]
    )
    return prediction


st.write(predict()[0])
