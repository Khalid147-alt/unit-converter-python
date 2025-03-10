import streamlit as st
import time
# title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔄 Unit Converter App</h1>", unsafe_allow_html=True)
st.write("Convert Different Units Easily")
col1, col2 = st.columns([1, 1]) 
# categries with dict
unit_categories = {
    "length": {"Meters": 1,"Kilometers":0.001,"Centimeters":100,"Millimeters":1000,"Miles": 0.000621371},
    "Weight":{"Kilograms":1,"Grams":1000, "Pounds":2.20462,"Ounce":35.274},
    "Temperature":{"Celsius":"C","Fahrenheit":"F","Kelvin":"K"}

}
st.sidebar.title("⚙️ Settings")
category = st.sidebar.selectbox("📌 Select Category", list(unit_categories.keys()))
from_unit = st.sidebar.selectbox("🔄 From Unit", unit_categories[category].keys())
to_unit = st.sidebar.selectbox("✅ To Unit", unit_categories[category].keys())
value = st.sidebar.number_input("✏️ Enter Value", min_value=0.0, step=0.1)



# conversion logic
def convert_units(category, from_unit, to_unit, value):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # No conversion needed if both units are the same
    else:
        # Handle non-temperature conversions
        from_factor = unit_categories[category].get(from_unit, 1)
        to_factor = unit_categories[category].get(to_unit, 1)
        return value * (to_factor / from_factor)  # Apply unit conversion formula



if st.button("🚀 Convert Now"):
    with st.spinner("Converting... 🔄"):
        time.sleep(1)  # Simulates a short delay
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"🎯 Converted Value: {result}")

st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        .stSelectbox, .stNumberInput, .stButton {
            border-radius: 8px;
            border: 2px solid #4CAF50;
            padding: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
