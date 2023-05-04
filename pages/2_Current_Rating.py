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
                       options=["Permissible short-circuit current", "Maximum short-circuit temperature"])


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  1 - PERMISSIBLE SHORT-CIRCUIT CURRENT
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    if study == "Permissible short-circuit current":
        #tubular = st.checkbox('Tubular sheath')

        st.write("")
        st.write("")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            '**CONDUCTOR**'
            conductor = st.selectbox("Select Conductor", options=["Copper", "Aluminium"])
            S = st.number_input('Cross-section [mm2]', format="%.2f", value= 185.00, step=.1, min_value= .001)
        with col2:
            '**TEMPERATURE**'
            theta_i = st.number_input('Initial Temperature [°C]', format="%.1f", value= 90., step=1., min_value=-20.)
            theta_f = st.number_input('Final Temperature [°C]', format="%.1f", value= 250., step=1., min_value=-20.)
        with col3:
            '**SHORT-CIRCUIT**'
            t = st.number_input('Short-circuit time [s]', format="%.2f", value=1., step=.1, min_value=1.e-6)
            Icc = st.number_input('Short-circuit current [kA]', format="%.2f", value=20., step=.1, min_value=1.e-6, disabled =True)

        #st.write("")
        #'**MATERIAL PROPERTIES**'
        #col1, col2, col3 = st.columns(3)
        #with col1:
        #    st.number_input('Label A ', format="%.1f", value=0., step=.1, min_value=0.)
        #with col2:
        #    st.number_input('Label B ', format="%.1f", value=0., step=.1, min_value=0.)
        #with col3:
        #    st.number_input('Label C ', format="%.1f", value=0., step=.1, min_value=0.)
            #A7 = st.number_input('Thermal resistivity [K.m/W]', format="%.1f", value=1., step=.1, min_value=0.)

        K_cu = 226
        K_al = 148
        beta_cu = 234.5
        beta_al = 228
        rho_cu = 1.7241e-8
        rho_al = 2.8264e-8

        Iad = K_cu * S * np.sqrt((1 / t) * np.log((theta_f + beta_cu) / (theta_i + beta_cu))) * 0.001

        st.markdown(' ')
        st.markdown(' ')

        col1, col2 = st.columns(2)
        col1.metric('ADIABATIC SHORT-CIRCUIT CURRENT (kA)', value=str(float("{:.2f}".format(Iad))) + str(' kA'))
        col1.metric('(Review) NON-ADIABATIC SHORT-CIRCUIT CURRENT (kA)',
                    value=str(float("{:.1f}".format(Iad / 0.7))) + str(' kA'))
        col2.metric('SHORT-CIRCUIT TEMPERATURE', value=str(float("{:.1f}".format(theta_f))) + str(' °C'),
                    delta=str(theta_f - theta_i) + str('°C'))
        ''
        ''
        '**PARAMETRIC STUDIES**'
        col1, col2, col3, col4 = st.columns([2,2,2,1.5])
        with col1:
            study = st.selectbox("SELECT VARIABLE",
                             options=["Cross-section", "Initial temperature","Final Temperature", "Short-circuit time"])
        with col2:
            min = st.number_input(str.upper(study) + ' [min]', format="%.2f", value=1.00, step=1., min_value=.001)
        with col3:
            max = st.number_input(str.upper(study) + ' [max]', format="%.2f", value=1.00, step=1., min_value=.001)
        with col4:
            steps = st.number_input('Steps', format="%i", value= 5, step=1, min_value=1)



        columns = ['Result %d' % i for i in range(3)]
        index =   ['Case %d' % i for i in range(int(steps))]

        df = pd.DataFrame(
            np.random.randn(int(steps), 3),
            columns=columns, index=index)

        st.table(df)

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  2 - SHORT-CIRCUIT TEMPERATURE
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    if study == "Maximum short-circuit temperature":
        st.write("")
        st.write("")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            '**CONDUCTOR**'
            conductor = st.selectbox("Select Conductor", options=["Copper", "Aluminium"])
            S = st.number_input('Cross-section [mm2]', format="%.2f", value=185.00, step=.1, min_value=.001)
        with col2:
            '**TEMPERATURE**'
            theta_i = st.number_input('Initial Temperature [°C]', format="%.1f", value=90., step=1., min_value=-20.)
            theta_f = st.number_input('Final Temperature [°C]', format="%.1f", value=250., step=1., min_value=-20., disabled =True)
        with col3:
            '**SHORT-CIRCUIT**'
            t = st.number_input('Short-circuit time [s]', format="%.2f", value=1., step=.1, min_value=1.e-6)
            Isc = st.number_input('Short-circuit current [kA]', format="%.2f", value=26.47, step=.1, min_value=1.e-6)

        K_cu = 226
        K_al = 148
        beta_cu = 234.5
        beta_al = 228
        rho_cu = 1.7241e-8
        rho_al = 2.8264e-8

        theta_max = (theta_i+beta_cu) * np.exp( ((1000*Isc)**2)*t/((K_cu*S)**2) )  - beta_cu

        st.markdown(' ')
        st.markdown(' ')

        col1, col2, col3 = st.columns(3)
        col1.metric('SHORT-CIRCUIT TEMPERATURE (°C)', value= str(float("{:.1f}".format(theta_max)))+ str(' °C'),
                    delta= str(float("{:.1f}".format(theta_max-theta_i))) + str('°C'))
        col2.metric('SHORT-CIRCUIT CURRENT (kA)', value= str(float("{:.1f}".format(Isc)))+ str(' kA'))
        col3.metric('SHORT-CIRCUIT TIME (s)', value= str(float("{:.1f}".format(t)))+ str(' s'))




import webbrowser
url = 'https://store.veracity.com/sesam-cloud-compute'
if st.button('Veracity by DNV'):
    webbrowser.open_new_tab(url)




#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                         TAB2 -- CURRENT RATING - RESULTS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab2:

    if study == "Permissible short-circuit current":

        st.markdown(' ')
        st.markdown(' ')

        col1, col2 = st.columns(2)
        col1.metric('ADIABATIC SHORT-CIRCUIT CURRENT (kA)', value= str(float("{:.2f}".format(Iad)))+ str(' kA'))
        col1.metric('NON-ADIABATIC SHORT-CIRCUIT CURRENT (kA)', value= str(float("{:.1f}".format(Iad/0.7)))+ str(' kA'))
        col2.metric('SHORT-CIRCUIT TEMPERATURE', value= str(float("{:.1f}".format(theta_f)))+ str(' °C'),
                    delta= str(theta_f-theta_i) + str('°C'))

    if study == "Maximum short-circuit temperature":
        col1, col2, col3 = st.columns(3)
        col1.metric('SHORT-CIRCUIT TEMPERATURE (°C)', value= str(float("{:.1f}".format(theta_max)))+ str(' °C'),
                    delta= str(float("{:.1f}".format(theta_max-theta_i))) + str('°C'))
        col2.metric('SHORT-CIRCUIT CURRENT (kA)', value= str(float("{:.1f}".format(Isc)))+ str(' kA'))
        col3.metric('SHORT-CIRCUIT TIME (s)', value= str(float("{:.1f}".format(t)))+ str(' s'))





#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                         TAB3 -- CURRENT RATING - OUTPUT
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


