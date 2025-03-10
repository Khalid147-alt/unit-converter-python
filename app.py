import streamlit as st

# title
st.title("Unit Converter")
st.write("Convert Different Units Easily")

# ui comp
unit_categories = {
    "length": {"Meters": 1,"Kilometers":0.001,"Centimeters":100,"Millimeters":1000,"Miles": 0.000621371},
    "Weight":{"Kilograms":1,"Grams":1000, "Pounds":2.20462,"Ounce":35.274},
    "Temperature":{"Celsius":"C","Fahrenheit":"F","Kelvin":"K"}

}


# user input
category = st.selectbox("Choose a Category", list(unit_categories.keys()))

# display dropdown
from_unit = st.selectbox("From Unit", list(unit_categories[category].keys()))
to_unit = st.selectbox("To Unit", list(unit_categories[category].keys()))

# user select the source unit and target unit
value = st.number_input("Enter Value",min_value=0.0,format="%.2f")



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

# button
if st.button("Convert"):
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

 