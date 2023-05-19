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
    layer3a = ['Fillers', 'Binding', 'Bedding', 'Conductor', 'Cover', '', '', '']

    conductors = ['', 'Copper', 'Lead', 'Steel', 'Aluminum']
    materials = ['', 'Polyethylene', 'XLPE', 'Polypropylene', 'PVC']

    conductors_core = ['Copper', 'Lead', 'Steel', 'Aluminum']
    materials_core = ['', 'Polyethylene', 'Polyethylene', 'XLPE', 'Polyethylene', 'Polyethylene', 'Polypropylene', '', '', '', '', '', '', '']
    conductors_sheath = ['Lead', 'Copper', 'Steel', 'Aluminum']
    materials_sheath = ['Polyethylene', 'Polyethylene', 'Polyethylene', 'Polyethylene', 'Polypropylene', '', '', '', '', '', '', '', '']
    conductors_armour = ['Steel', 'Steel', '', '', '']
    materials_armour = ['Polypropylene', 'Polyethylene', 'Polypropylene', '', 'Polypropylene', '', '', '', '', '', '', '', '']

    cols3 = [.7, 1.3, 1, .9, .95]

    core_mm = [30., 30.5, 32.5, 48.5, 50.3, 52.5, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
    sheath_mm = [57.1, 62.1, 0.001, 0.001, 0.001, 0.001, 0.001]
    armour_mm = [134.9, 135.3, 137.3, 149.3, 155.3, 0.001, 0.001, 0.001, 0.001]


    '**CONDUCTOR**'
    col1, col2, col3, col4, col5  = st.columns(cols3)
    with col1:
        '**DESIGN**'
        nc = st.number_input('Layers----', value=6, min_value=1, max_value=10, step=1)
        layer_c = ['' for i in range(0, nc)]
        material_c = ['' for i in range(0, nc)]
        D_c = ['' for i in range(0, nc)]
        rho_c = ['' for i in range(0, nc)]
        with col2:
            '**LAYER**'
        with col3:
            '**MATERIAL**'
        with col4:
            '**DIAMETER**'
        with col5:
            '**THERMAL RESIST.**'

        for k in range(0, nc):
            with col2:
                layer_c[k] = st.selectbox('Layer ' + str(k + 1), layer3c, index=k)
            with col3:
                if layer_c[k] == 'Conductor':
                    material_c[k] = st.selectbox(str(layer_c[k]), conductors_core, index=k)
                else:
                    material_c[k] = st.selectbox(str(layer_c[k]), materials_core, index=k)
            with col4:
                D_c = st.number_input('D' + str(k+1) + ' [mm]', value=core_mm[k], min_value=.001, step=1., format="%.1f")
                # + ' ('+str(layer_c[k])+')' + ' [mm]'
            with col5:
                rho_c[k] = st.number_input('T'+str(k+1)+ ' [K.m/W]', value=1., min_value=0.001, step=1., format="%.1f")

    ''
    ''
    '**SHEATH**'
    col1, col2, col3, col4, col5 = st.columns(cols3)
    with col1:
        '**DESIGN**'
        ns = st.number_input('Layers-----', value=2, min_value=1, max_value=10, step=1)
        layer_s = ['' for i in range(0, ns)]
        material_s = ['' for i in range(0, ns)]
        D_s = ['' for i in range(0, ns)]
        rho_s = ['' for i in range(0, ns)]
        with col2:
            '**LAYER**'
        with col3:
            '**MATERIAL**'
        with col4:
            '**DIAMETER**'
        with col5:
            '**THERMAL RESIST.**'

        for k in range(0, ns):
            with col2:
                layer_s[k] = st.selectbox('Layer ' + str(nc + k + 1), layer3s, index=k)
            with col3:
                if layer_s[k] == 'Conductor':
                    material_s[k] = st.selectbox('Material (Layer ' + str(nc + k + 1) + ')', conductors_sheath, index=k)
                else:
                    material_s[k] = st.selectbox('Material (Layer ' + str(nc + k + 1) + ')', materials_sheath, index=k)
            with col4:
                D_s = st.number_input('D' + str(nc + k + 1) + ' [mm]', value=sheath_mm[k], min_value=.001, step=1., format="%.1f")
            with col5:
                rho_s[k] = st.number_input('T' + str(nc + k + 1) + ' [K.m/W]', value=1., min_value=0.001, step=1.,
                                         format="%.1f")


    ''
    ''
    '**ARMOUR**'
    col1, col2, col3, col4, col5 = st.columns(cols3)
    with col1:
        '**DESIGN**'
        na = st.number_input('Layers-a', value=5, min_value=1, max_value=20, step=1)
        layer_a = ['' for i in range(0, na)]
        material_a = ['' for i in range(0, na)]
        D_a = ['' for i in range(0, na)]
        rho_a = ['' for i in range(0, na)]

        with col2:
            '**LAYER**'
        with col3:
            '**MATERIAL**'
        with col4:
            '**DIAMETER**'
        with col5:
            '**THERMAL RESIST.**'

        for k in range(0, na):
            with col2:
                layer_a[k] = st.selectbox('Layer ' + str(nc + ns + k + 1), layer3a, index=k)
            with col3:
                if layer_a[k] == 'Conductor':
                    material_a[k] = st.selectbox('Material (Layer ' + str(nc + ns + k + 1) + ')', options=['Steel'])#, index=k)
                else:
                    material_a[k] = st.selectbox('Material (Layer ' + str(nc + ns + k + 1) + ')', materials_armour, index=k)
            with col4:
                D_a = st.number_input('D' + str(nc + ns + k + 1) + ' [mm]', value=armour_mm[k], min_value=.001, step=1., format="%.1f")
            with col5:
                rho_a[k] = st.number_input('T' + str(nc + ns + k + 1) + ' [K.m/W]', value=1., min_value=0.001, step=1.,
                                         format="%.1f")




    ''
    ''
    #print(layer_a)
    #print(material_a)
    #print(rho_a)
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
