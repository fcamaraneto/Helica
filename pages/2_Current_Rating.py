import streamlit as st
from PIL import Image # create page icon

import pandas as pd
import numpy as np
#import scipy.io as spio
import scipy.special as spios
import plotly.express as px

import plotly.graph_objects as go

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SETTINGS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
icon=Image.open('dnv_logo.jpg')
st.set_page_config(page_title="HELICA Multiphysics", layout="centered", page_icon=icon)

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SIDEBAR
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.postimg.cc/K88r3LRp/dnv-logo.jpg);
                background-repeat: no-repeat;
                margin-left: 20px;
                padding-top: 100px;
                background-position: 1px 1px;
            }
            [data-testid="stSidebarNav"]::before {
              # content: "My Company Name";
              #  margin-left: 2px;
              #  margin-top: 2px;
              #  font-size: 3px;
              #  position: relative;
              #  top: 1px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

url='https://i.postimg.cc/NjhVmdYR/helica-logo.png'

st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] + div {{
                position:relative;
                bottom: 0;
                height:65%;
                background-image: url({url});
                background-size: 40% auto;
                background-repeat: no-repeat;
                background-position-x: center;
                background-position-y: bottom;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# '📊 📉 📈 📧 🗂️ 📂 📈  🖥️🗄️  '

add_logo()
#st.sidebar.image('aau_logo.png', width=150)

st.sidebar.markdown("HELICA Cable Rating module complies with IEC 60287 and IEC 60949 ... ")


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     INPUT DATA
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
st.title("Current Rating")
st.markdown('The Cable Rating module ... ')
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
tab1, tab2, tab3 = st.tabs(["🖥️ Cable Data", "📊 Cable Rating", "🗂️ Export Results"])

with tab1:
    study = st.selectbox("Select Study",
                       options=["Permissible short-circuit current", "Short-circuit temperature"])


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  1- Single Core (stranded sheath)
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    if study == "Permissible short-circuit current":
        #tubular = st.checkbox('Tubular sheath')

        st.write("")
        st.write("")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            '**CONDUCTOR**'
            conductor = st.selectbox("Select Conductor", options=["Copper", "Aluminium"])
            S = st.number_input('Cross-section [mm2]', format="%.2f", value=185.00, step=.1, min_value=.001)
        with col2:
            '**TEMPERATURE**'
            theta_i = st.number_input('Initial Temperature [°C]', format="%.1f", value=40., step=1., min_value=-20.)
            theta_f = st.number_input('Final Temperature [°C]', format="%.1f", value=90., step=1., min_value=-20.)
        with col3:
            '**SHORT-CIRCUIT TIME**'
            t = st.number_input('t [s]',   format="%.2f", value = 1., step=.1, min_value=1.e-6)

        st.write("")
        'Material Properties'
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            A7 = st.number_input('Thermal resistivity [K.m/W]', format="%.1f", value=1., step=.1, min_value=0.)
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                CURRENT RATING - RESULTS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab2:

    K_cu = 226
    K_al = 148
    beta_cu = 234.5
    beta_al = 228
    rho_cu = 1.7241e-8
    rho_al = 2.8264e-8
    theta_i = 40.
    theta_f = 90.

    Iad = (K_cu*S/t) * np.log((theta_f+beta_cu)/(theta_i+beta_cu))

    st.markdown(' ')
    st.markdown(' ')

    #'**SHORT-CIRCUIT CURRENT**'
    col1, col2 = st.columns(2)
    col1.metric('ADIABATIC SHORT-CIRCUIT CURRENT', value= float("{:.1f}".format(Iad)))
    col2.metric('MAXIMUM SHORT-CIRCUIT TEMPERATURE', value=theta_f, delta=str(theta_f-theta_i) + str('°C'))
    #st.text_area(label="Output Data:", value=100.)






#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                CURRENT RATING - OUTPUT
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

with tab3:
    #st.subheader('Interfacing with circuit solvers')
    #st.markdown(' Interfacing with circuit solvers contains matlab scripts which demonstrate'
    #        ' how to interface rational function-based models with time domain circuit solvers '
    #        'via a Norton equivalent. The procedure is shown for models representing '
    #        'Y-parameters, Z-parameters, S-parameters, and general transfer functions that '
    #        'do not interact with the circuit.')

    #col = st.selectbox("Select Software:",
    #                   options=["PSCAD", "EMTP", "PowerFactory", "ATP"])

    import time
    localtime = time.asctime(time.localtime(time.time()))
    dum = time.strftime("Date:%d-%m-%Y  Time:%H:%M:%S", time.localtime())


    st.write("")

    st.download_button(
        label="Download Data",
        data='Universal Cable Constants (UCC) \n\n' + dum,
        file_name='cable_parameters.csv',
        mime='text/csv')

    st.download_button(
        label="Download Report",
        data='Universal Cable Constants (UCC) \n\n' + dum,
        file_name='cable_parameters.txt',
        mime='text/csv')




