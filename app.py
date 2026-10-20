# the Applicatiob frontend here Using Streamlit
import streamlit as st
import pandas as pd
import requests


st.set_page_config(page_title="House Price Prediction", page_icon=":house:", layout="wide")

st.title("House Price Prediction")

st.write("This application predicts the price of a house based on its features.")

#but some values requires selection like the house title, town, state

house_title = st.selectbox("Select House  Title",['Detached Duplex', 'Terraced Duplexes', 'Semi Detached Duplex',
 'Detached Bungalow', 'Block of Flats', 'Semi Detached Bungalow',
 'Terraced Bungalow'] )

town = st.selectbox("Select Town", [
	'Mabushi', 'Katampe', 'Lekki', 'Ajah', 'Epe', 'Lokogoma District', 'Oredo',
	'Victoria Island (VI)', 'Mowe Ofada', 'Ikeja', 'Ikoyi', 'Magodo', 'Kaura',
	'Galadimawa', 'Gwarinpa', 'Abeokuta North', 'Lugbe District', 'Ibeju Lekki',
	'Yaba', 'Sango Ota', 'Ifako-Ijaiye', 'Agege', 'Ikorodu', 'Jahi', 'Ibadan',
	'Orozo', 'Ifo', 'Owerri North', 'Guzape District', 'Idu Industrial',
	'Owerri Municipal', 'Isheri North', 'Utako', 'Port Harcourt', 'Kuje', 'Isheri',
	'Life Camp', 'Ipaja', 'Ado-Odo/Ota', 'Dape', 'Mushin', 'Ejigbo', 'Isolo',
	'Ojodu', 'Gaduwa', 'Enugu', 'Dakwo', 'Asokoro District', 'Alimosho', 'Sagamu',
	'Chikun', 'Egbeda', 'Wuye', 'Kubwa', 'Shomolu', 'Ogudu', 'Owerri West', 'Ibafo',
	'Surulere', 'Obio-Akpor', 'Ayobo', 'Apo', 'Mowe Town', 'Ibadan South-West',
	'Wuse 2', 'Durumi', 'Simawa', 'Arepo', 'Ikotun', 'Oluyole', 'Maitama District',
	'Maryland', 'Ido', 'Karsana', 'Wuse', 'Ilorin West', 'Kurudu', 'Karmo',
	'Abeokuta South', 'KM 46', 'Gbagada', 'Idimu', 'Kaduna South', 'Magboro',
	'Gudu', 'Kukwaba', 'Mbora (Nbora)', 'Obafemi Owode', 'Jabi', 'Karu', 'Ojo',
	'Garki', 'Aba', 'Ogijo', 'Asaba', 'Uyo', 'Kosofe', 'Oyigbo', 'Karshi', 'Osogbo',
	'Kado', 'Ilupeju', 'Afijio', 'Ketu', 'Ado-Ekiti', 'Ibadan North', 'Egor',
	'Nyanya', 'Ibarapa North', 'Kyami', 'Ojota', 'Dutse', 'Nasarawa', 'Calabar',
	'Kaduna North', 'Eleme', 'Kafe', 'Oshodi', 'Dakibiyu', 'Amuwo Odofin', 'Ijede',
	'Bwari', 'Dekina', 'Jos South', 'Agbara-Igbesa', 'Ijaiye', 'Kagini',
	'Ohaji/Egbema', 'Mpape', 'Apapa', 'Lagos Island', 'Gwagwalada', 'Ijoko',
	'Diplomatic Zones', 'Akure', 'Ethiope West', 'Badagry', 'Kano', 'Ede South',
	'Ilorin South', 'Oke-Aro', 'Oke-Odo', 'Ikot Ekpene', 'Kusada', 'Akinyele',
	'Kabusa', 'Dei-Dei', 'Eket', 'Egbe', 'Udu', 'Ibadan North-East', 'Danja',
	'Yewa South', 'Warri', 'Duboyi', 'Jikwoyi', 'Oyo West', 'Agbara',
	'Ovia North-East', 'Yenagoa', 'Central Business District', 'Guzamala',
	'Lokoja', 'Jos North', 'Orile', 'Wumba', 'Ibadan North-West',
	'Eko Atlantic City', 'Imota', 'Ikwerre', 'Keffi', 'Ilorin East', 'Uvwie',
	'Umuahia', 'Ijesha', 'Okene', 'Aniocha South', 'Ijebu Ode', 'Okpe',
	'Ughelli South', 'Ewekoro', 'Nassarawa', 'Mararaba', 'Uhunmwonde',
	'Ughelli North', 'Ibeju', 'Abraka', 'Paikoro', 'Ikpoba Okha',
])

state = st.selectbox("Select State", [
	'Abuja', 'Lagos', 'Edo', 'Ogun', 'Oyo', 'Imo', 'Anambara', 'Rivers', 'Enugu',
	'Kaduna', 'Kwara', 'Nasarawa', 'Abia', 'Delta', 'Akwa Ibom', 'Osun', 'Ekiti',
	'Cross River', 'Kogi', 'Plateau', 'Kano', 'Katsina', 'Bayelsa', 'Borno', 'Niger',
])



bedrooms = st.number_input("Enter Number of Bedrooms", min_value=1, max_value=10, value=3)
toilets = st.number_input("Enter Number of Toilets", min_value=1, max_value=10, value=2)
bathrooms = st.number_input("Enter Number of Bathrooms", min_value=1, max_value=10, value=2)
parking_space = st.number_input("Enter Number of Parking Spaces", min_value=0, max_value=10, value=1)

if st.button("Predict Price"):
    # Prepare the data to send to the API
    data = {
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "toilets": toilets,
        "parking_space": parking_space,
        "title": house_title,
        "town": town,
        "state": state,
        
    }

    try:
        # Send a POST request to the FastAPI endpoint
        response = requests.post("https://house-price-5nj2.onrender.com/predict", json=data)
    except requests.RequestException as e:
        st.error(f"Error occurred while making the API request: {e}")

    if response.status_code == 200:
        result = response.json()
        predicted_price = result.get("predicted_price")
        st.success(f"The predicted price of the house is: #{predicted_price:,.2f}")
