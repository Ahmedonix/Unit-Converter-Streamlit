import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()
st.title('Ahmedonix Unit Converter')
categories = {'Length': ["m", "cm", "mm", "km", "in", "ft", "yd", "mi"],
              'Mass': ["kg", "g", "mg", "t", "lb", "oz"],
              'Time': ["s", "min", "h", "d", "yr"],
              'Temperature': ["K", "C", "F"],
              'Volume': ["L", "mL", "cm^3", "m^3", "in^3", "ft^3", "yd^3", "gal", "qt", "pt", "cup", "fl oz"]
              }

#Create a dropdown
category = st.selectbox('Select a category', list(categories.keys()))
#Create a dropwon for the units
from_unit = st.selectbox('From', categories[category])
to_unit = st.selectbox('To', categories[category])

#Create a text input for the value
value = st.number_input('Enter a value', min_value=0.0, step=0.1)

#Convert the value
if st.button('Convert'):
    try:
        #Special Case for temperature
        if category == 'Temperature':
            if from_unit == 'C' and to_unit == 'F':
                result = (value * 9/5) + 32
            elif from_unit == 'F' and to_unit == 'C':
                result = (value - 32) * 5/9
            elif from_unit == 'C' and to_unit == 'K':
                result = value + 273.15
            elif from_unit == 'K' and to_unit == 'C':
                result = value - 273.15
            elif from_unit == 'F' and to_unit == 'K':
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == 'K' and to_unit == 'F':
                result = (value - 273.15) * 9/5 + 32 
            else:
                result = value
        else:
            #general coversion for all non-temperature units using pint
            result = (value * ureg(from_unit)).to(to_unit).magnitude

        #display the result in green box
        st.success(f'{value} {from_unit} is {result} {to_unit}')
    except Exception as e:
        #display the error in red box
        st.error(f"Error: {e}")