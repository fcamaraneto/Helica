import streamlit as st
import math

def calculate_sigma_hi(OD, t, p_idwp, p_e):
    sigma_hi = (p_idwp - p_e) * (OD**2 + (OD - 2*t)**2) / (OD**2 - (OD - 2*t)**2) - p_e
    return sigma_hi

def calculate_sigma_he(OD, t, p_idwp, p_e):
    sigma_he = (p_idwp - p_e) * 2 * (OD - 2*t)**2 / (OD**2 - (OD - 2*t)**2) - p_e
    return sigma_he

def calculate_sigma_ri(p_idwp):
    sigma_ri = -p_idwp
    return sigma_ri

def calculate_sigma_re(p_e):
    sigma_re = -p_e
    return sigma_re

def calculate_sigma_aec(OD, p_idwp):
    sigma_aec = p_idwp*(OD - 2*t)**2 / (OD**2 - (OD - 2*t)**2)
    return sigma_aec

def calculate_tube_area(OD, t):
    outside_area = math.pi * (OD / 2) ** 2
    inside_area = math.pi * ((OD - 2 * t) / 2) ** 2
    return outside_area - inside_area

pressure_units = {
'MPa': 1,
'bar': 10,
'psi': 0.00689476,
}

length_units = {
'mm': 1,
'in': 25.4,
}

st.title('Pressure and Tube Area Calculator')

# Use Streamlit columns to arrange widgets side by side
col1, col2 = st.columns(2)

# Use Streamlit widgets in the first column to get user input for values
length_unit = col1.selectbox('Choose a length unit:', list(length_units.keys()))
OD = col1.number_input(f'Enter the value of OD [{length_unit}]:')
t = col1.number_input(f'Enter the value of t [{length_unit}]:')
p_i = col1.number_input('Enter the value of p_i:')
p_e = col1.number_input('Enter the value of p_e:')

# Use Streamlit widgets in the second column to get user input for units
pressure_unit_p_i = col2.selectbox('Choose a pressure unit for p_i:', list(pressure_units.keys()))
pressure_unit_p_e = col2.selectbox('Choose a pressure unit for p_e:', list(pressure_units.keys()))

# Convert length values to mm
OD_mm = OD * length_units[length_unit]
t_mm = t * length_units[length_unit]

# Convert pressure values to MPa
p_i_mpa = p_i * pressure_units[pressure_unit_p_i]
p_e_mpa = p_e * pressure_units[pressure_unit_p_e]
p_idwp = p_i_mpa * 1.5

# Call the functions with the user-provided values
sigma_hi = calculate_sigma_hi(OD_mm, t_mm, p_idwp, p_e_mpa)
sigma_he = calculate_sigma_he(OD_mm, t_mm, p_idwp, p_e_mpa)
sigma_ri = calculate_sigma_ri(p_idwp)
sigma_re = calculate_sigma_re(p_e_mpa)

# Display the results using Streamlit widgets
st.write(f'sigma_hi: {sigma_hi}')
st.write(f'sigma_he: {sigma_he}')
st.write(f'sigma_ri: {sigma_ri}')
st.write(f'sigma_re: {sigma_re}')