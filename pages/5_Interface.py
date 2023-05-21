import streamlit as st
from PIL import Image # create page icon

import pandas as pd
import numpy as np
#import scipy.io as spio
import scipy.special as spios
import plotly.express as px

import plotly.graph_objects as go

# shortcuts
divide = np.divide
pi = np.pi
log = np.log
sqrt = np.sqrt
print = st.markdown

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
                background-image: url(https://i.postimg.cc/wvSYBKsj/DNV-logo-RGB-Small.png);
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
tab1, tab2, tab3 = st.tabs(["🖥️ Cable Design", "🖥️ Material Propoerties", "🖥️ Results"])


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  INTERFACE 1
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab1:

    col1, col2, col3, col4 = st.columns([.75, .75, 1, 1])
    with col1:
        Ux = st.number_input('RATED VOLTAGE [kV]', format="%.1f", value=30., step=10., min_value=0.001)
        U0 = Ux * 1e3 / sqrt(3)
    with col2:
        freq = st.selectbox("FREQUENCY (Hz)", options=["50 Hz", "60 Hz", "DC"])
        if freq == "50 Hz":
            f = 50
        if freq == "60 Hz":
            f = 60
        if freq == "DC":
            f = 0
        omega = 2 * pi * f
    with col3:
        theta = st.number_input('MAXIMUN TEMPERATURE [°C]', format="%.2f", value=90.00, step=1.)
        input1 = theta
    with col4:
        input2 = st.number_input('AMBIENT TEMPERATURE [°C]', format="%.2f", value=20.00, step=1.)
    ''
    ''

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
    materials_armour = ['Polypropylene', 'Polypropylene', 'Polypropylene', '', 'Polypropylene', '', '', '', '', '', '', '', '']


    #'**WIRE DATA**'
    col0, col1, col2, col3, col4 = st.columns([.7, .75, .75, 1, 1])
    with col0:
        '**WIRE DATA**'
    with col1:
        '**CONDUCTOR**'
    with col2:
        '**SHEATH**'
    with col3:
        '**ARMOUR**'
    with col1:
        rc = st.number_input('Rcore [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
    with col2:
        rs = st.number_input('Rsheath [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
        ns = st.number_input('Nsheath [mm]', value=99, step=1, min_value=1)
    with col3:
        ra = st.number_input('Rarmour [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
        na1 = st.number_input('Narmour [mm]', value=99, step=1, min_value=1)
        na2 = st.number_input('Narmour [mm] ', value=99, step=1, min_value=1)

    ''
    ''

    core_mm = [30., 30.5, 32.5, 48.5, 50.3, 52.5, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
    sheath_mm = [57.1, 62.1, 0.001, 0.001, 0.001, 0.001, 0.001]
    armour_mm = [134.9, 135.3, 137.3, 149.3, 155.3, 0.001, 0.001, 0.001, 0.001]

    # cols1 = [.7, 1.3, 1.3, .9, .95]
    cols1 = [.7, 1, 1, 1]
    cols0 = [.5, .7, 1.1, 1, .8]

    #'**DESIGN**'
    col0, col1, col2, col3, col4  = st.columns(cols0)
    with col0:
        '**DESIGN**'
    with col1:
        '**CONDUCTOR**'
        nc = st.number_input('Layers----', value=6, min_value=6, max_value=6, step=1)
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
        #with col5:
        #    '**THERMAL RESIST.**'

        for k in range(0, nc):
            with col2:
                layer_c[k] = st.selectbox('Layer ' + str(k + 1), layer3c, index=k)
            with col3:
                if layer_c[k] == 'Conductor':
                    material_c[k] = st.selectbox(str(layer_c[k]), conductors_core, index=k)
                else:
                    material_c[k] = st.selectbox(str(layer_c[k]), materials_core, index=k)
            with col4:
                D_c[k] = st.number_input('D' + str(k+1) + ' [mm]', value=core_mm[k], min_value=.001, step=1., format="%.1f")
                # + ' ('+str(layer_c[k])+')' + ' [mm]'
            #with col5:
                #rho_c[k] = st.number_input('T'+str(k+1)+ ' [K.m/W]', value=1., min_value=0.001, step=1., format="%.1f")

    ''
    ''
    col0, col1, col2, col3, col4 = st.columns(cols0)
    with col1:
        '**SHEATH**'
        ns = st.number_input('Layers-----', value=2, min_value=2, max_value=2, step=1)
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
        #with col5:
        #    '**THERMAL RESIST.**'

        for k in range(0, ns):
            with col2:
                layer_s[k] = st.selectbox('Layer ' + str(nc + k + 1), layer3s, index=k)
            with col3:
                if layer_s[k] == 'Conductor':
                    material_s[k] = st.selectbox('Material (Layer ' + str(nc + k + 1) + ')', conductors_sheath, index=k)
                else:
                    material_s[k] = st.selectbox('Material (Layer ' + str(nc + k + 1) + ')', materials_sheath, index=k)
            with col4:
                D_s[k] = st.number_input('D' + str(nc + k + 1) + ' [mm]', value=sheath_mm[k], min_value=.001, step=1., format="%.1f")
            #with col5:
                #rho_s[k] = st.number_input('T' + str(nc + k + 1) + ' [K.m/W]', value=1., min_value=0.001, step=1., format="%.1f")


    ''
    ''
    col0, col1, col2, col3, col4 = st.columns(cols0)
    with col1:
        '**ARMOUR**'
        na = st.number_input('Layers-a', value=5, min_value=5, max_value=5, step=1)
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
        #with col5:
        #    '**THERMAL RESIST.**'

        for k in range(0, na):
            with col2:
                layer_a[k] = st.selectbox('Layer ' + str(nc + ns + k + 1), layer3a, index=k)
            with col3:
                if layer_a[k] == 'Conductor':
                    material_a[k] = st.selectbox('Material (Layer ' + str(nc + ns + k + 1) + ')', options=['Steel'])#, index=k)
                else:
                    material_a[k] = st.selectbox('Material (Layer ' + str(nc + ns + k + 1) + ')', materials_armour, index=k)
            with col4:
                D_a[k] = st.number_input('D' + str(nc + ns + k + 1) + ' [mm]', value=armour_mm[k], min_value=.001, step=1., format="%.1f")
            #with col5:
            #    rho_a[k] = st.number_input('T' + str(nc + ns + k + 1) + ' [K.m/W]', value=1., min_value=0.001, step=1., format="%.1f")


    ''
    ''
    dum=D_c+D_s+D_a
    print(dum)
    print(len(dum))
    #print(layer_a)
    #print(material_a)
    #print(rho_a)

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  INTERFACE 2
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab2:

    cols2 = [1, 1, 1, 1.]

    rho_c_in = [0.001, 6., 2.5, 3.5, 2.5, 12.]
    #Thermal resistivity of semiconducting tapes 𝜌𝑠𝑐_𝑡 = 6 K.m/W
    #Thermal resistivity of sc screen 𝜌𝑠𝑐 = 2,5 K.m/W
    #Thermal resistivity of insulation 𝜌𝑖 = 3,5 K.m/W
    #Thermal resistivity of water blocking tapes 𝜌𝑤𝑏 = 12 K.m/W
    rho_s_in = [0.001, 2.5]
    #Thermal resistivity of sc PE sheath 𝜌𝑠𝑐𝑃𝐸 = 2,5 K.m/W
    rho_a_in = [6., 6., 6., 0.001, 6.]
    #Thermal resistivity of fillers and binding tapes 𝜌𝑓𝑖𝑙_𝑏𝑡 = 6 K.m/W
    #Thermal resistivity of outer covering 𝜌𝑇 = 6 K.m/W
    #Thermal resistivity of the soil 𝜌𝑇 = 0.7 K.m/W


    '**CONDUCTOR**'
    col1, col2, col3, col4 = st.columns(cols2)
    with col1:
        '**LAYER**'
    with col2:
        '**MATERIAL**'
    with col3:
        '**THERMAL RESISTIVITY**'

    for k in range(0, nc):
        with col1:
            st.selectbox('Layer ' + str(k + 1), options=[layer_c[k]])
        with col2:
            st.selectbox(str(layer_c[k]), options=[material_c[k]])
            #st.selectbox('Material (Layer ' + str(k + 1) + ')', options=[material_c[k]])
        with col3:
            if layer_c[k]=='Conductor':
                st.number_input('𝜌' + str(k + 1) + ' [K.m/W]', value=rho_c_in[k], min_value=0.00, step=1., format="%.1f", disabled=True)
            else:
                rho_c[k] = st.number_input('𝜌' + str(k + 1) + ' [K.m/W]', value=rho_c_in[k], min_value=0.00, step=1., format="%.1f")

    ''
    ''
    '**SHEATH**'
    col1, col2, col3, col4 = st.columns(cols2)
    with col1:
        '**LAYER**'
    with col2:
        '**MATERIAL**'
    with col3:
        '**THERMAL RESISTIVITY**'

    for k in range(0, ns):
        with col1:
            st.selectbox('Layer ' + str(nc + k + 1), options=[layer_s[k]])
        with col2:
            st.selectbox(str(layer_s[k]), options=[material_s[k]])
            #st.selectbox('Material (Layer ' + str(k + 1) + ')', options=[material_c[k]])
        with col3:
            if layer_s[k]=='Conductor':
                st.number_input('𝜌' + str(nc + k + 1) + ' [K.m/W]', value=rho_s_in[k], min_value=0.00, step=1., format="%.1f", disabled=True)
            else:
                rho_s[k] = st.number_input('𝜌' + str(nc + k + 1) + ' [K.m/W]', value=rho_s_in[k], min_value=0.00, step=1., format="%.1f")

    ''
    ''
    '**ARMOUR**'
    col1, col2, col3, col4 = st.columns(cols2)
    with col1:
        '**LAYER**'
    with col2:
        '**MATERIAL**'
    with col3:
        '**THERMAL RESISTIVITY**'

    for k in range(0, na):
        with col1:
            st.selectbox('Layer ' + str(nc + ns + k + 1), options=[layer_a[k]])
        with col2:
            st.selectbox(str(layer_a[k]), options=[material_a[k]])
        with col3:
            if layer_a[k]=='Conductor':
                st.number_input('𝜌' + str(nc + ns + k + 1) + ' [K.m/W]', value=rho_a_in[k], min_value=0.00, step=1., format="%.1f", disabled=True)
            else:
                rho_a[k] = st.number_input('𝜌' + str(nc + ns + k + 1) + ' [K.m/W]', value=rho_a_in[k], min_value=0.00, step=1., format="%.1f")




#disabled
#label_visibility
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  INTERFACE 3
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab3:
    ''
