import streamlit as st
from PIL import Image # create page icon

import pandas as pd
import numpy as np
#import scipy.io as spio
import scipy.special as spios
import plotly.express as px

import plotly.graph_objects as go

print= st.markdown

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

#st.sidebar.markdown("HELICA Cable Rating module complies with IEC 60287 and IEC 60949 ... ")


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     INPUT DATA
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
st.title("Interface")
#st.markdown('The Cable Rating module ... ')
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
tab1, tab2, tab3 = st.tabs(["🖥️ GUI 1", "🖥️ GUI 2", "🖥️ GUI 3"])


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  INTERFACE 1
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab1:
    layer3c = ['Conductor', 'Tape', 'Conductor Screen', 'Insulation', 'Insulation Screen', 'Water blocking', 'Swelling tape', '', '', '']
    layer3s = ['Conductor', 'Sheath Screen', 'Bedding', 'Swelling tape', 'Insulation', 'Insulation Screen', 'Water blocking']
    layer3a = ['Binding', 'Bedding', 'Conductor', 'Tape', 'Conductor', 'Cover', 'Cover']

    conductors = ['', 'Copper', 'Lead', 'Steel', 'Aluminum']
    materials = ['', 'Polyethylene', 'XLPE', 'Polypropylene', 'PVC']

    conductors_core = ['Copper', 'Lead', 'Steel', 'Aluminum']
    materials_core = ['', 'Polyethylene', 'Polyethylene', 'XLPE', 'Polyethylene', 'Polyethylene', 'Polypropylene', '', '', '', '', '', '', '']
    conductors_sheath = ['Lead', 'Copper', 'Steel', 'Aluminum']
    materials_sheath = ['Polyethylene', 'Polyethylene', 'Polyethylene', 'Polyethylene', 'Polypropylene', '', '', '', '', '', '', '', '']
    conductors_armour = ['Steel', 'Steel', '', '', '']
    materials_armour = ['Polyethylene', 'Polypropylene', 'Polypropylene', 'Polypropylene', '', '', '', '', '', '', '', '', '']

    cols3 = [.7, 1.25, 1, .9, .9]

    core_mm = [30., 30.5, 32.5, 48.5, 50.3, 52.5, 9999., 9999., 9999., 9999., 9999., 9999.]
    sheath_mm = [57.1, 62.1, 9999., 9999., 9999., 9999., 9999.]
    armour_mm = [134.9, 135.3, 137.3, 149.3, 9999., 9999., 9999., 9999., 9999.]


    '**CONDUCTOR**'
    col1, col2, col3, col4, col5  = st.columns(cols3)
    with col1:
        '**DESIGN**'
        nn3 = st.number_input('Layers----', value=6, min_value=1, max_value=10, step=1)
        layer = ['' for i in range(0, nn3)]
        material = ['' for i in range(0, nn3)]
        rho = ['' for i in range(0, nn3)]
        text = ['' for i in range(0, nn3)]
        with col2:
            '**LAYER**'
        with col3:
            '**MATERIAL**'
        with col4:
            '**DIAMETER**'
        with col5:
            '**THERMAL RESIST.**'

        for k in range(0, nn3):
            with col2:
                layer[k] = st.selectbox('Layer ' + str(k + 1), layer3c, index=k)
            with col3:
                if layer[k] == 'Conductor':
                    text[k] = st.selectbox(str(layer[k]) + ' Material', conductors_core, index=k)
                else:
                    text[k] = st.selectbox(str(layer[k]) + ' Material', materials_core, index=k)
            with col4:
                Dcore = st.number_input('D' + str(k+1) + ' ('+str(layer[k])+')', value=core_mm[k], min_value=.001, step=1., format="%.1f")
            with col5:
                rho[k] = st.number_input('T'+str(k+1)+ ' [K.m/W]', value=1., min_value=0.001, step=1., format="%.1f")

    ''
    ''
    '**SHEATH**'
    col1, col2, col3, col4, col5 = st.columns(cols3)
    with col1:
        '**DESIGN**'
        nn4 = st.number_input('Layers-----', value=2, min_value=1, max_value=10, step=1)
        material = ['' for i in range(0, nn4)]
        rho = ['' for i in range(0, nn4)]
        text = ['' for i in range(0, nn4)]
        with col2:
            '**LAYER**'
        with col3:
            '**MATERIAL**'
        with col4:
            '**DIAMETER**'
        with col5:
            '**THERMAL RESIST.**'

        for k in range(0, nn4):
            with col2:
                layer[k] = st.selectbox('Layer ' + str(nn3 + k + 1), layer3s, index=k)
            with col3:
                if layer[k] == 'Conductor':
                    text[k] = st.selectbox('Material (Layer ' + str(nn3 + k + 1) + ')', conductors_sheath, index=k)
                else:
                    text[k] = st.selectbox('Material (Layer ' + str(nn3 + k + 1) + ')', materials_sheath, index=k)
            with col4:
                Dsheath = st.number_input('D' + str(nn3 + k + 1), value=sheath_mm[k], min_value=.001, step=1., format="%.1f")
            with col5:
                rho[k] = st.number_input('T' + str(nn3 + k + 1) + ' [K.m/W]', value=1., min_value=0.001, step=1.,
                                         format="%.1f")


    ''
    ''
    '**ARMOUR**'
    col1, col2, col3, col4, col5 = st.columns(cols3)
    with col1:
        '**DESIGN**'
        nn5 = st.number_input('Layers-a', value=4, min_value=1, max_value=20, step=1)
        material = ['' for i in range(0, nn5)]
        rho = ['' for i in range(0, nn5)]
        text = ['' for i in range(0, nn5)]
        lay_a = ['' for i in range(0, nn5)]
        with col2:
            '**LAYER**'
        with col3:
            '**MATERIAL**'
        with col4:
            '**DIAMETER**'
        with col5:
            '**THERMAL RESIST.**'

        for k in range(0, nn5):
            with col2:
                lay_a[k] = st.selectbox('Layer ' + str(nn3 + nn4 + k + 1), layer3a, index=k)
            with col3:
                if lay_a[k] == 'Conductor':
                    text[k] = st.selectbox('Material (Layer ' + str(nn3 + nn4 + k + 1) + ')', conductors_armour, index=k)
                else:
                    text[k] = st.selectbox('Material (Layer ' + str(nn3 + nn4 + k + 1) + ')', materials)#, index=k)
            with col4:
                Darmour = st.number_input('D' + str(nn3 + nn4 + k + 1), value=armour_mm[k], min_value=.001, step=1., format="%.1f")
            with col5:
                rho[k] = st.number_input('T' + str(nn3 + nn4 + k + 1) + ' [K.m/W]', value=1., min_value=0.001, step=1.,
                                         format="%.1f")



    ''
    ''
    print(lay_a)
    print(material)
    print(rho)
    print(text)
    ''






#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  INTERFACE 2
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab2:
    ''

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  INTERFACE 3
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab3:
    ''
