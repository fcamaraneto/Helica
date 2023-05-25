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
tab1, tab2, tab3 = st.tabs(["🖥️ Cable Design", "🖥️ Material Data", "🖥️ Electrical Output"])


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  INTERFACE 1
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab1:

    col0, col1, col2, col3 = st.columns([.75, .75, .9, .75])
    with col0:
        '**SYSTEM DATA**'
    with col1:
        '**RATED VOLTAGE**'
        U_temp = st.number_input('Design Voltage [kV]', format="%.1f", value=30., step=10., min_value=0.001)
        U0 = U_temp * 1e3 / sqrt(3)
    with col2:
        '**TYPE OF SYSTEM**'
        system = st.selectbox("Cable Type", options=["HVAC Three-core", "HVAC Single-Core", "HVDC Single-Core"])
    with col3:
        '**FREQUENCY**'
        if system != 'HVDC Single-Core':
            freq = st.selectbox("System Frequency (Hz)", options=["50 Hz", "60 Hz"])
        else:
            freq = st.selectbox("System Frequency (Hz)", options=["0 Hz - DC"])
        if freq == "50 Hz":
            f = 50
        if freq == "60 Hz":
            f = 60
        if freq == "0 Hz - DC":
            f = 0
        omega = 2 * pi * f
    line = st.write("-" * 34)  # horizontal separator line




    # '**INSTALLATION CONDITIONS**'
    col0, col1, col2, col3 = st.columns([1.25, 1.1, 1, 1.])
    with col0:
        '**OPERATION CONDITIONS**'
    with col1:
        '**INSTALLATION**'
        x1 = st.selectbox("Installation Method", options=["Buried", 'On the Seabed', 'J-Tube'])
        x2 = st.selectbox("External Media", options=["Seabed", "Sea", 'Air', "Soil"])
    with col2:
        '**BURRIAL DEPTH**'
        L_temp = st.number_input('L [m]', format="%.2f", value=1., step=1., min_value=.001)
        L_burrial = L_temp * 1e3
    with col3:
        '**TEMPERATURE**'
        theta_0 = st.number_input('Ambient Temperature [°C]', format="%.1f", value=20., step=.1, min_value=.001)
        theta_1 = st.number_input('Operation Temperature [°C]', format="%.1f", value=90., step=1.)
        theta_2 = st.number_input('Maximum Temperature [°C]', format="%.1f", value=250., step=1.)
    line = st.write("-" * 34)  # horizontal separator line


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


    #'**WIRE DIMENSIONS**'
    col0, col1, col2, col3 = st.columns([1.25, 1, 1, 1])
    with col0:
        '**WIRE DIMENSIONS**'
    with col1:
        '**CONDUCTOR**'
    with col2:
        '**SHEATH**'
    with col3:
        '**ARMOUR**'
    with col1:
        rc = st.number_input('Radius [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
    with col2:
        rs = st.number_input('Radius [mm] ', format="%.2f", value=0.2, step=.1, min_value=.001)
        ns = st.number_input('Wires', value=99, step=1, min_value=1)
    with col3:
        ra = st.number_input('Radius [mm]  ', format="%.2f", value=0.2, step=.1, min_value=.001)
        na1 = st.number_input('Wires (Layer 1)', value=99, step=1, min_value=1)
        na2 = st.number_input('Wires (Layer 2)', value=99, step=1, min_value=1)
    line = st.write("-" * 34)  # horizontal separator line

    core_mm = [30., 30.5, 32.5, 48.5, 50.3, 52.5, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
    sheath_mm = [57.1, 62.1, 0.001, 0.001, 0.001, 0.001, 0.001]
    armour_mm = [134.9, 135.3, 137.3, 149.3, 155.3, 0.001, 0.001, 0.001, 0.001]

    # cols1 = [.7, 1.3, 1.3, .9, .95]
    cols1 = [.7, 1, 1, 1]
    cols0 = [.5, .7, 1.1, 1, .8]

    # DESIGN - CONDUCTOR
    col0, col1, col2, col3, col4  = st.columns(cols0)
    with col0:
        '**DESIGN**'
    with col1:
        '**CONDUCTOR**'
        nc = st.number_input('Layers----', value=6, min_value=1, max_value=16, step=1)
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
    #line = st.write("-" * 34)  # horizontal separator line
    ''
    ''


    # DESIGN - SHEATH
    col0, col1, col2, col3, col4 = st.columns(cols0)
    with col1:
        '**SHEATH**'
        ns = st.number_input('Layers-----', value=2, min_value=1, max_value=12, step=1)
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
    #line = st.write("-" * 34)  # horizontal separator line
    ''
    ''


    # DESIGN - ARMOUR
    col0, col1, col2, col3, col4 = st.columns(cols0)
    with col1:
        '**ARMOUR**'
        na = st.number_input('Layers-a', value=5, min_value=1, max_value=15, step=1)
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
    line = st.write("-" * 34)  # horizontal separator line



    # '**MISCELLANEOUS**'
    col0, col1, col2, col3 = st.columns([1.25, 1.2, 1, 1.])
    with col0:
        '**MISCELLANEOUS**'
    with col1:
        laylength_temp = st.number_input('Lay length [mm]', format="%.0f", value=2152., step=1.)
        laylength = laylength_temp * 1e-3
        #
        ts_temp = st.number_input('Sheath thickness [mm]', format="%.2f", value=2.3, step=.1)
        ts_sheath = ts_temp * 1e-3
    with col2:
        tgdelta = st.number_input('Tan Delta 𝛿 (XLPE)', format="%.5f", value=40e-4, step=1.)
    with col3:
        epsilon = st.number_input('Permittivity εr (XLPE)', format="%.1f", value=2.5, step=.1)
        #input1 = theta
        #theta_2 = st.number_input('Maximum Temperature [°C]', format="%.2f", value=250.00, step=1.)
    line = st.write("-" * 34)  # horizontal separator line


    #dum=D_c+D_s+D_a
    #print(dum)
    #print(len(dum))
    #print(layer_a)
    #print(material_a)
    #print(rho_a)

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  INTERFACE 2
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab2:
    cols2 = [1, 1, 1, 1, 1.]

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

    # '**WIRES**'
    col0, col1, col2, col3, col4 = st.columns(cols2)
    with col0:
        '**WIRES**'
    with col1:
        '**CONDUCTOR**'
        Rdc20_core_in = st.number_input('Rdc at 20°C [10^-3 𝛺/𝑚]', value=0.0283, min_value=1e-8, format="%.4f")
        Rdc20_core = Rdc20_core_in*1e-3
        st.number_input('𝜌 at 20°C [10^-8 𝛺/𝑚]', value=0.00001, min_value=1e-8, format="%.2f")

        𝛼20_core_in = st.number_input('𝛼 at 20°C [10^-3 1/K]', value=3.93, min_value=1e-5, format="%.3f")
        𝛼20_core = 𝛼20_core_in * 1e-3
    with col2:
        '**SHEATH**'
        Rdc20_sheath_in = st.number_input('Rdc at 20°C [10^-3 𝛺/𝑚] ', value=0.0283, min_value=1e-8, format="%.4f")
        Rdc20_sheath = Rdc20_sheath_in*1e-3
        𝜌20_sheath_in = st.number_input('𝜌 at 20°C [10^-8 𝛺.𝑚]', value=21.4, min_value=1e-8, format="%.2f")
        𝜌20_sheath = 𝜌20_sheath_in * 1e-8
        𝛼20_sheath_in = st.number_input('𝛼 at 20°C [10^-3 1/K] ', value=4.00, min_value=1e-5, format="%.3f")
        𝛼20_sheath = 𝛼20_sheath_in * 1e-3
    with col3:
        '**ARMOUR**'
        Rdc20_armour_in = st.number_input('Rdc at 20°C [10^-3 𝛺/𝑚]  ', value=0.0283, min_value=1e-8, format="%.4f")
        Rdc20_armour = Rdc20_armour_in*1e-3
        𝜌20_armour_in = st.number_input('𝜌 at 20°C [10^-8 𝛺.𝑚]', value=13.8, min_value=1e-8, format="%.2f")
        𝜌20_armour = 𝜌20_armour_in * 1e-8
        𝛼20_armour_in = st.number_input('𝛼 at 20°C [10^-3 1/K]  ', value=4.50, min_value=1e-5, format="%.3f")
        𝛼20_armour = 𝛼20_armour_in * 1e-3
    line = st.write("-" * 34)  # horizontal separator line

    #'**CONDUCTOR**'
    col0, col1, col2, col3, col4 = st.columns(cols2)
    with col0:
        '**CONDUCTOR**'
    with col1:
        '**LAYER**'
    with col2:
        '**MATERIAL**'
    with col3:
        '**THERMAL RESIST.**'

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
    line = st.write("-" * 34)  # horizontal separator line


    #'**SHEATH**'
    col0, col1, col2, col3, col4 = st.columns(cols2)
    with col0:
        '**SHEATH**'
    with col1:
        '**LAYER**'
    with col2:
        '**MATERIAL**'
    with col3:
        '**THERMAL RESIST.**'

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
    line = st.write("-" * 34)  # horizontal separator line


    #'**ARMOUR**'
    col0, col1, col2, col3, col4 = st.columns(cols2)
    with col0:
        '**ARMOUR**'
    with col1:
        '**LAYER**'
    with col2:
        '**MATERIAL**'
    with col3:
        '**THERMAL RESIST.**'

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

    line = st.write("-" * 34)  # horizontal separator line



#disabled
#label_visibility
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  INTERFACE 3
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab3:
    '**PROMPT:**'

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  CALCULATIONS
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # Multiplication by 10^ factors
    D_temp = D_c + D_s + D_a
    D = [D_temp[i] * 1e-3 for i in range(0, len(D_temp))]
    print(D_temp)

    dc = D[0]
    s = D[7]
    Di = D[3]
    dc2 = D[2]
    ds =  D[5]
    Dsh = (D[5]+D[6])/2
    print(Dsh)


    # 1 -- Calculation of lay-up factor of the core
    flayup = sqrt(1 + (pi * 1.29 * D[7] / laylength) ** 2)
    #print(flayup)

    # 2 - Rac: Calculation of Rac at operation temperature (conductor)
    # 2.1 - DC resistance of conductor
    Rdc_core = Rdc20_core * (1 + 𝛼20_core * (theta_1 - 20))
    #print(Rdc)
    # 2.2 - Skin effect factor
    ks = 1
    xs2 = (8 * pi * f / Rdc_core) * 1e-7
    xs = sqrt(xs2)
    # for 0 < xs <= 2.8:
    ys = divide(xs2 ** 2, 192 + 0.8 * xs2 ** 2)
    #print(xs2)
    #print(ys)
    # 2.2 - Proximity effect factor
    kp = 1
    xp2 = (8 * pi * f / Rdc_core) * 1e-7 * kp
    xp = sqrt(xp2)
    dum1 = divide(xp2 ** 2, 192 + 0.8 * xp2 ** 2) * divide(dc, s) ** 2
    dum2 = 0.312 * divide(dc, s) ** 2
    dum3 = divide(1.18, divide(xp2 ** 2, 192 + 0.8 * xp2 ** 2) + 0.27)
    yp = dum1 * (dum2 + dum3)
    #print(xp2)
    #print(yp)
    # - - - AC resistance of conductor
    # Note: The impact of armour wires in the conductor losses is taken into consideration
    # with the factor 1.5 in the equation above. See Section 2.5.4 in the guidance chapter.
    Rac_core = Rdc_core * (1 + 1.5*(ys + yp))
    #print(Rac_core)

    # 3 - Calculationn of dielectric losses
    # 3.1 -  Capacitance (semi-conducting layers or tapes excluded)
    C_core = divide(epsilon, 18 * log(divide(Di, dc2))) * 1e-9
    C = C_core * flayup
    Wd = omega * C * U0 * U0 * tgdelta
    #print(C)
    #print(Wd)

    # 4 -- Loss factor for sheath
    #𝜌20_sheath
    #𝛼20_sheath
    # 4.1 - Calculation of cross-sectional area of the sheath
    As = pi * ts_sheath * (ds + ts_sheath)
    #print(As*1e6)
    # Rac20_sheath -- Electrical resistance of the metal sheath at 20°C
    # AC Resistance of the screen at 20oC per unit length of 3-core cable is
    # calculated by taken into consideration the lay-up factor
    Rac20_sheath = flayup * (𝜌20_sheath/As)
    #print(Rac20_sheath*1e4)
    # Operating temperature 𝜃𝑠𝑐 of the screen
    I = 838.3399739336
    T1 = 0.3578707848
    theta_s = theta_1 - (Rac_core * I**2 + 0.5*Wd) * T1
    print(theta_s)
    # Lead sheath AC resistance at operating temperature 𝜃𝑠ℎ
    Rac_sheath = Rac20_sheath * (1 + 𝛼20_sheath * (theta_s - 20))
    print(Rac_sheath*1e4)

    # 4.2 - Calculation of the core reactance
    Dsh = 52.5e-3
    d = Dsh + ts_sheath
    # print(d*1e3)
    X1c = 2 * omega * log(divide(2 * s, d)) * 1e-7
    X = flayup * X1c
    # print(X1c*1e5)
    # print(X*1e5)







    # -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    # horizontal separator line
    st.write("-" * 34)  # horizontal separator line
    '**REPORT (output results)**'
    print('- Lay-up factor: ' + str(flayup))
    print('- Rdc at operating temperature: ' + str(Rdc_core*1e3) + ' m𝛺/m')
    print('- Rac at operating temperature: ' + str(Rac_core*1e3) + ' m𝛺/m')

    print('- Nominal capacitance per phase: ' + str(C*1e9) + ' pF/m')

    print('- Cable losses:')
    print('- Dielectric losses per phase: ' + str(Wd) + ' W/m')






















