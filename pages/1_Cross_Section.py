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

st.sidebar.markdown("HELICA Cable Rating module complies with IEC 60287 and IEC ... ")


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     CROSS-SECTION
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
st.title("HELICA Cross-Section")
st.markdown('The Cable Rating module ... ')
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
tab1, tab2, tab3 = st.tabs(["🖥️ Cable Data", "📊 Cable Rating", "🗂️ Export Results"])

with tab1:
    cable2 = st.selectbox("Select Cable Type",
                       options=["Single Core", "Three Core"])
    #, "Pipe Type"


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  1- Single Core (stranded sheath)
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    if cable2 == "Single Core":
        tubular = st.checkbox('Tubular sheath', key="disabled")

        if tubular == False:

            col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
            with col1:
                st.write("")
                radius1 = st.number_input('R1 [mm]', format="%.2f", value=1.00, step=.1, min_value=.001)
                radius3 = st.number_input('R3 [mm]', format="%.2f", value=3.00, step=.1, min_value=.001)
            with col2:
                st.write("")
                radius5 = st.number_input('R5 [mm]', format="%.2f", value=4.0, step=.1, min_value=.001)
                radius6 = st.number_input('R6 [mm]', format="%.2f", value=4.2, step=.1, min_value=.001)
            with col3:
                st.write("")
                rc = st.number_input('Rcore [mm]',   format="%.2f", value=0.2, step=.1, min_value=.001)
                rs = st.number_input('Rsheath [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
                ra = st.number_input('Rarmour [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
            with col4:
                st.write("")
                ns = st.number_input('Nsheath [mm]',   value=40, step=1, min_value=1)
                na = st.number_input('Narmour [mm]',   value=60, step=1, min_value=1)


            outc = radius1
            theta_s = 360/ns
            theta_a = 360/na
            theta_a = 360 / na

            if (outc == rc):
                layers = 0
                nc = [1]
                theta_c = [0]
                R1c = [0]
            else:
                layers = int(np.floor(((outc + 1.e-5) / rc) - np.floor(0.5 * (outc + 1.e-5) / rc)) - 1)
                nc = np.zeros(layers)
                nc = [1] + [(i * 6) for i in range(1, layers + 1)]
                theta_c = [0] + [(360 / nc[i]) for i in range(1, layers + 1)]
                R1c = [2 * rc * i for i in range(0, layers + 1)]

            xc = np.zeros(sum(nc), dtype='float32')
            yc = np.zeros(sum(nc), dtype='float32')

            for k in range(0, layers + 1):
                a = sum(nc[0:k])
                b = sum(nc[0:k + 1])

                xc[a:b] = [R1c[k] * np.cos(i * (theta_c[k] * np.pi / 180)) for i in range(1, nc[k] + 1)]
                yc[a:b] = [R1c[k] * np.sin(i * (theta_c[k] * np.pi / 180)) for i in range(1, nc[k] + 1)]

            xs = [radius3 * np.cos(i*(theta_s*np.pi/180)) for i in range(0, ns)]
            ys = [radius3 * np.sin(i*(theta_s*np.pi/180)) for i in range(0, ns)]
            xa = [radius5 * np.cos(i*(theta_a*np.pi/180)) for i in range(0, na)]
            ya = [radius5 * np.sin(i*(theta_a*np.pi/180)) for i in range(0, na)]

            #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
            #                      PLOT cross-section (1core)
            #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
            fig = go.Figure()
            shapes = []

            # core
            for i in range(len(xc)):
                shapes.append(dict(type="circle", xref="x", yref="y",
                                   x0=xc[i] - rc, y0=yc[i] - rc, x1=xc[i] + rc, y1=yc[i] + rc,
                                   line_color="LightSeaGreen"))

            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=-max(xc) - rc, y0=-max(xc) - rc, x1=max(xc) + rc, y1=max(xc) + rc,
                               line_color="LightSeaGreen"))
            # sheath
            for i in range(ns):
                shapes.append(dict(type="circle", xref="x", yref="y",
                                    x0= xs[i]-rs, y0= ys[i]-rs, x1= xs[i]+rs, y1= ys[i]+rs,
                                   line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=-radius3+rs, y0=-radius3+rs, x1=radius3-rs, y1=radius3-rs,
                               line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=-radius3-rs, y0=-radius3-rs, x1=radius3+rs, y1=radius3+rs,
                               line_color="LightSeaGreen"))
            # armour
            for i in range(na):
                shapes.append(dict(type="circle", xref="x", yref="y",
                              x0= xa[i]-ra, y0= ya[i]-ra, x1= xa[i]+ra, y1= ya[i]+ra,
                              line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0= -radius5-ra, y0= -radius5-ra, x1= radius5+ra, y1= radius5+ra,
                               line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0= -radius5+ra, y0= -radius5+ra, x1= radius5-ra, y1= radius5-ra,
                               line_color="LightSeaGreen"))
            # jacket/server
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0= -radius6-ra, y0= -radius6-ra, x1= radius6+ra, y1= radius6+ra,
                               line_color="LightSeaGreen"))


            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                ''
            with col2:
                fig.update_layout(width=400, height=400)
                fig.update_xaxes(range=[-radius6*1.2,radius6*1.2])
                fig.update_yaxes(range=[-radius6*1.2, radius6*1.2])
                fig.update_xaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black', gridcolor='white')
                fig.update_yaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black', gridcolor='white')
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
                fig.update_layout(shapes=shapes)
                st.plotly_chart(fig)
            with col3:
                ''

            with st.expander('INTRUCTIONS'):
                'CORE: For R1 > Rcore, the number of subconductors is estimated automatically.'
                'SHEATH: For stranded sheath, specify the sheath outer radius R3 and the sheath conductor radius.'
                'ARMOUR: For stranded armour, specify the armour outer radius R5 and the armour conductor radius.'

                col1, col2, col3 = st.columns([1, 4, 1])
                with col1:
                    ''
                with col2:
                    st.image('cross.png', width=500, caption='Figure 1 - Cross-section parameters')
                with col3:
                    ''
                col1, col2 = st.columns([1, 1])
                with col1:
                    'R1: core outer radius.'
                    'R2: sheath inner radius.'
                    'R3: sheath outer radius.'
                    'R4: armour inner radius.'
                    'R5: armour outer radius.'
                    'R6: "jacket" outer radius.'
                with col2:
                    'Rcore: core conductor radius.'
                    'Rsheath: sheath conductor radius.'
                    'Rarmour: armour conductor radius.'


            'Next enhancements:'
            '1) Double-check the Instructions.'
            '3) Option for choosing the number of sheath conductors.'
            '4) Option for choosing the number of armour conductors.'
            '5) Design a sanity check for R5>R6.'
            '6) Design a sanity check for R1>Rcore. ' \
            'If R1/Rcore is not an integer multiple, should R1 assume the lower or higher ratio?'
            '7) Double-layered armour.'

        else:
            #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
            #  2- Single Core (tubular sheath)
            #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
            #if cable2 == "Single Core (tubular sheath)"

            col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
            with col1:
                st.write("")
                radius1 = st.number_input('R1 [mm]', format="%.2f", value=1.00, step=.1, min_value=.001)
                radius2 = st.number_input('R2 [mm]', format="%.2f", value=2.6, step=.1, min_value=.001)
                radius3 = st.number_input('R3 [mm]', format="%.2f", value=3., step=.1, min_value=.001)
            with col2:
                st.write("")
                radius5 = st.number_input('R5 [mm]', format="%.2f", value=4.0, step=.1, min_value=.001)
                radius6 = st.number_input('R6 [mm]', format="%.2f", value=4.2, step=.1, min_value=.001)
            with col3:
                st.write("")
                rc = st.number_input('Rcore [mm]',   format="%.2f", value=0.2, step=.1, min_value=.001)
                ra = st.number_input('Rarmour [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
            with col4:
                st.write("")
                na = st.number_input('Narmour [mm]',   value=60, step=1, min_value=1)

            outc = radius1
            theta_a = 360/na

            if (outc == rc):
                layers = 0
                nc = [1]
                theta_c = [0]
                R1c = [0]
            else:
                layers = int(np.floor(((outc + 1.e-5) / rc) - np.floor(0.5 * (outc + 1.e-5) / rc)) - 1)
                nc = np.zeros(layers)
                nc = [1] + [(i * 6) for i in range(1, layers + 1)]
                theta_c = [0] + [(360 / nc[i]) for i in range(1, layers + 1)]
                R1c = [2 * rc * i for i in range(0, layers + 1)]

            xc = np.zeros(sum(nc), dtype='float32')
            yc = np.zeros(sum(nc), dtype='float32')

            for k in range(0, layers + 1):
                a = sum(nc[0:k])
                b = sum(nc[0:k+1])

                xc[a:b] = [R1c[k] * np.cos(i * (theta_c[k]*np.pi/180)) for i in range(1, nc[k]+1)]
                yc[a:b] = [R1c[k] * np.sin(i * (theta_c[k]*np.pi/180)) for i in range(1, nc[k]+1)]

            xa = [radius5 * np.cos(i*(theta_a*np.pi/180)) for i in range(0, na)]
            ya = [radius5 * np.sin(i*(theta_a*np.pi/180)) for i in range(0, na)]

            # PLOT conductors
            fig = go.Figure()
            shapes = []

            # core
            for i in range(len(xc)):
                shapes.append(dict(type="circle", xref="x", yref="y",
                                   x0= xc[i]-rc, y0= yc[i]-rc, x1= xc[i]+rc, y1= yc[i]+rc,
                                   line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=-max(xc) - rc, y0=-max(xc) - rc, x1=max(xc) + rc, y1=max(xc) + rc,
                               line_color="LightSeaGreen"))
            # sheath
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0= -radius2, y0= -radius2, x1= radius2, y1= radius2,
                               line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0= -radius3, y0= -radius3, x1= radius3, y1= radius3,
                               line_color="LightSeaGreen"))
            # armour
            for i in range(na):
                shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=xa[i]-ra, y0=ya[i]-ra, x1=xa[i]+ra, y1=ya[i]+ra,
                               line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=-radius5-ra, y0=-radius5-ra, x1=radius5+ra, y1=radius5+ra,
                               line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=-radius5+ra, y0=-radius5+ra, x1=radius5-ra, y1=radius5-ra,
                               line_color="LightSeaGreen"))
            # jacket/server
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0= -radius6-ra, y0= -radius6-ra, x1= radius6+ra, y1= radius6+ra,
                               line_color="LightSeaGreen"))



            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                ''
            with col2:
                fig.update_layout(shapes=shapes)
                fig.update_layout(width=400, height=400)
                fig.update_xaxes(range=[-radius6*1.2,radius6*1.2])
                fig.update_yaxes(range=[-radius6*1.2, radius6*1.2])
                fig.update_xaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black', gridcolor='white')
                fig.update_yaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black', gridcolor='white')
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
                st.plotly_chart(fig)
            with col3:
                ''


            with st.expander('INTRUCTIONS'):
                'CORE: For R1 > Rcore, the number of subconductors is estimated automatically.'
                'SHEATH: For stranded sheath, specify the sheath outer radius R3 and the sheath conductor radius.'
                'ARMOUR: For stranded armour, specify the armour outer radius R5 and the armour conductor radius.'
                col1, col2, col3 = st.columns([1, 4, 1])
                with col1:
                    ''
                with col2:
                    st.image('cross.png', width=500, caption='Figure 1 - Cross-section parameters')
                with col3:
                    ''
                col1, col2 = st.columns([1, 1])
                with col1:
                    'R1: core outer radius.'
                    'R2: sheath inner radius.'
                    'R3: sheath outer radius.'
                    'R4: armour inner radius.'
                    'R5: armour outer radius.'
                    'R6: "jacket" outer radius.'
                with col2:
                    'Rcore: core conductor radius.'
                    'Rsheath: sheath conductor radius.'
                    'Rarmour: armour conductor radius.'

            'Next enhancements:'
            '1) Double-check the Instructions.'
            '2) Option for choosing the number of armour conductors.'
            '3) Design a sanity check for R5>R6.'
            '4) Design a sanity check for R1>Rcore. ' \
            'If R1/Rcore is not an integer multiple, should R1 assume the lower or higher ratio?'
            '5) Double-layered armour.'

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  3- Three Core (stranded sheath)
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    if cable2 == "Three Core":

        col1, col2 = st.columns([1, 1])
        with col1:
            dlayer = st.checkbox('Double-layered armour')
        with col2:
            dlayertubular = st.checkbox('Tubular sheath')

        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            st.write("")
            radius1 = st.number_input('R1 [mm]', format="%.2f", value=1.00, step=.1, min_value=.001)
            radius3 = st.number_input('R3 [mm]', format="%.2f", value=2.75, step=.1, min_value=.001)
        with col2:
            st.write("")
            radius4 = st.number_input('R4 [mm]', format="%.2f", value=3.5, step=.1, min_value=.001)
            # radius5 = st.number_input('R5 [mm]', format="%.2f", value=8.0, step=.1, min_value=.001)
            radius6 = st.number_input('R6 [mm]', format="%.2f", value=8.1, step=.1, min_value=.001)
        with col3:
            st.write("")
            rc = st.number_input('Rcore [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
            rs = st.number_input('Rsheath [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
            ra = st.number_input('Rarmour [mm]', format="%.2f", value=0.2, step=.1, min_value=.001)
        with col4:
            st.write("")
            ns = st.number_input('Nsheath [mm]', value=40, step=1, min_value=1)
            na = st.number_input('Narmour [mm]', value=100, step=1, min_value=1)



        outc = radius1
        theta_s = 360 / ns
        theta_a = 360 / na
        theta_a = 360 / na

        if (outc == rc):
            layers = 0
            nc = [1]
            theta_c = [0]
            R1c = [0]
        else:
            layers = int(np.floor(((outc + 1.e-5) / rc) - np.floor(0.5 * (outc + 1.e-5) / rc)) - 1)
            nc = np.zeros(layers)
            nc = [1] + [(i * 6) for i in range(1, layers + 1)]
            theta_c = [0] + [(360 / nc[i]) for i in range(1, layers + 1)]
            R1c = [2 * rc * i for i in range(0, layers + 1)]

        xc = np.zeros(sum(nc), dtype='float32')
        yc = np.zeros(sum(nc), dtype='float32')

        for k in range(0, layers + 1):
            a = sum(nc[0:k])
            b = sum(nc[0:k + 1])

            xc[a:b] = [R1c[k] * np.cos(i * (theta_c[k] * np.pi / 180)) for i in range(1, nc[k] + 1)]
            yc[a:b] = [R1c[k] * np.sin(i * (theta_c[k] * np.pi / 180)) for i in range(1, nc[k] + 1)]

        xs = [radius3 * np.cos(i * (theta_s * np.pi / 180)) for i in range(0, ns)]
        ys = [radius3 * np.sin(i * (theta_s * np.pi / 180)) for i in range(0, ns)]

        # xa = [Xa * np.cos(i*(theta_a*np.pi/180)) for i in range(0, na)]
        # a = [Ya * np.sin(i*(theta_a*np.pi/180)) for i in range(0, na)]
        Ra = 2 * (radius4 + 2 * ra)  # + 0.1
        xa = [Ra * np.cos(i * (theta_a * np.pi / 180)) for i in range(0, na)]
        ya = [Ra * np.sin(i * (theta_a * np.pi / 180)) for i in range(0, na)]

        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        #                      PLOT cross-section (3core)
        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        fig = go.Figure()
        shapes = []

        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        # CABLE 1
        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        # core
        for i in range(len(xc)):
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0= xc[i]-rc - radius4, y0= yc[i]-rc, x1= xc[i]+rc - radius4, y1= yc[i]+rc,
                               line_color="LightSeaGreen"))


        shapes.append(dict(type="circle", xref="x", yref="y",
                           x0= -max(xc)-rc - radius4, y0= -max(xc)-rc, x1= max(xc)+rc - radius4, y1= max(xc)+rc,
                           line_color="LightSeaGreen"))
        # sheath
        for i in range(ns):
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=xs[i] - rs - radius4, y0=ys[i] - rs, x1=xs[i] + rs - radius4, y1=ys[i] + rs,
                               line_color="LightSeaGreen"))
        shapes.append(dict(type="circle", xref="x", yref="y",
                           x0=-radius3 + rs - radius4, y0=-radius3 + rs, x1=radius3 - rs - radius4, y1=radius3 - rs,
                           line_color="LightSeaGreen"))
        shapes.append(dict(type="circle", xref="x", yref="y",
                           x0=-radius3 - rs - radius4, y0=-radius3 - rs, x1=radius3 + rs - radius4, y1=radius3 + rs,
                           line_color="LightSeaGreen"))
        shapes.append(dict(type="circle", xref="x", yref="y",
                           x0=-radius4 - radius4, y0=-radius4, x1=radius4 - radius4, y1=radius4,
                           line_color="LightSeaGreen"))

        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        # CABLE 2
        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        # core
        for i in range(len(xc)):
            shapes.append(
                dict(type="circle", xref="x", yref="y",
                     x0=xc[i] - rc + radius4, y0=yc[i] - rc, x1=xc[i] + rc + radius4, y1=yc[i] + rc,
                     line_color="LightSeaGreen"))
        shapes.append(
            dict(type="circle", xref="x", yref="y",
                 x0=-max(xc) - rc + radius4, y0=-max(xc) - rc, x1=max(xc) + rc + radius4, y1=max(xc) + rc,
                 line_color="LightSeaGreen"))
        # sheath
        for i in range(ns):
            shapes.append(
                dict(type="circle", xref="x", yref="y",
                     x0=xs[i] - rs + radius4, y0=ys[i] - rs, x1=xs[i] + rs + radius4, y1=ys[i] + rs,
                     line_color="LightSeaGreen"))
        shapes.append(
            dict(type="circle", xref="x", yref="y",
                 x0=-radius3 + rs + radius4, y0=-radius3 + rs, x1=radius3 - rs + radius4, y1=radius3 - rs,
                 line_color="LightSeaGreen"))
        shapes.append(
            dict(type="circle", xref="x", yref="y",
                 x0=-radius3 - rs + radius4, y0=-radius3 - rs, x1=radius3 + rs + radius4, y1=radius3 + rs,
                 line_color="LightSeaGreen"))
        shapes.append(dict(type="circle", xref="x", yref="y",
                           x0=-radius4 + radius4, y0=-radius4, x1=radius4 + radius4, y1=radius4,
                           line_color="LightSeaGreen"))

        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        # CABLE 3
        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        # core
        Yoffset = radius4 + 2 * (radius4 * np.sqrt(3) / 6) + 3 * rs;

        for i in range(len(xc)):
            shapes.append(dict(type="circle", xref="x", yref="y",
                     x0=xc[i] - rc, y0=yc[i] - rc + Yoffset, x1=xc[i] + rc, y1=yc[i] + rc + Yoffset,
                     line_color="LightSeaGreen"))
        shapes.append(
            dict(type="circle", xref="x", yref="y",
                 x0=-max(xc) - rc, y0=-max(xc) - rc + Yoffset, x1=max(xc) + rc, y1=max(xc) + rc + Yoffset,
                 line_color="LightSeaGreen"))
        # sheath
        for i in range(ns):
            shapes.append(
                dict(type="circle", xref="x", yref="y",
                     x0=xs[i] - rs, y0=ys[i] - rs + Yoffset, x1=xs[i] + rs, y1=ys[i] + rs + Yoffset,
                     line_color="LightSeaGreen"))
        shapes.append(
            dict(type="circle", xref="x", yref="y",
                 x0=-radius3 + rs, y0=-radius3 + rs + Yoffset, x1=radius3 - rs, y1=radius3 - rs + Yoffset,
                 line_color="LightSeaGreen"))
        shapes.append(
            dict(type="circle", xref="x", yref="y",
                 x0=-radius3 - rs, y0=-radius3 - rs + Yoffset, x1=radius3 + rs, y1=radius3 + rs + Yoffset,
                 line_color="LightSeaGreen"))
        shapes.append(
            dict(type="circle", xref="x", yref="y",
                 x0=-radius4, y0=-radius4 + Yoffset, x1=radius4, y1=radius4 + Yoffset,
                 line_color="LightSeaGreen"))

        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        # armour
        #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
        Xa = radius4
        Ya = 2 * (radius4 * np.sqrt(3)) / 6

        for i in range(na):
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=xa[i] - ra, y0=ya[i] - ra + Ya, x1=xa[i] + ra, y1=ya[i] + ra + Ya,
                               line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=-Ra + ra, y0=-Ra + ra + Ya, x1=Ra - ra, y1=Ra - ra + Ya,
                               line_color="LightSeaGreen"))
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=-Ra - ra, y0=-Ra - ra + Ya, x1=Ra + ra, y1=Ra + ra + Ya,
                               line_color="LightSeaGreen"))
            # jacket/server
            shapes.append(dict(type="circle", xref="x", yref="y",
                               x0=-radius6 - ra, y0=-radius6 - ra + Ya, x1=radius6 + ra, y1=radius6 + ra + Ya,
                               line_color="LightSeaGreen"))


        col1, col2, col3 = st.columns([1, 9, 1])
        with col1:
            ''
        with col2:
            fig.update_layout(width=600, height=600)
            fig.update_xaxes(range=[-max(xa) * 1.2, max(xa) * 1.2])
            fig.update_yaxes(range=[-max(xa) * 1., max(xa) * 1.5])
            fig.update_xaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black', gridcolor='white')
            fig.update_yaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black', gridcolor='white')
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
            fig.update_layout(shapes=shapes)
            st.plotly_chart(fig)
        with col3:
            ''

        with st.expander('INTRUCTIONS'):
            'CORE: For R1 > Rcore, the number of subconductors is estimated automatically.'
            'SHEATH: For stranded sheath, specify the sheath outer radius R3 and the sheath conductor radius.'
            'ARMOUR: For stranded armour, specify the armour outer radius R5 and the armour conductor radius.'

            col1, col2, col3 = st.columns([1, 4, 1])
            with col1:
                ''
            with col2:
                st.image('cross.png', width=500, caption='Figure 1 - Cross-section parameters')
            with col3:
                ''
            col1, col2 = st.columns([1, 1])
            with col1:
                'R1: core outer radius.'
                'R2: sheath inner radius.'
                'R3: sheath outer radius.'
                'R4: armour inner radius.'
                'R5: armour outer radius.'
                'R6: "jacket" outer radius.'
            with col2:
                'Rcore: core conductor radius.'
                'Rsheath: sheath conductor radius.'
                'Rarmour: armour conductor radius.'

        'Next enhancements:'
        '1) Update the Instructions.'
        '3) Option for choosing the number of sheath conductors.'
        '4) Option for choosing the number of armour conductors.'
        '5) Design a sanity check for R5>R6.'
        '6) Design a sanity check for R1>Rcore. ' \
        'If R1/Rcore is not an integer multiple, should R1 assume the lower or higher ratio?'
        '7) Double-layered armour.'
        '8) Constraint of max Nsheath/Narmour.'
        '9) Verify definition for R5.'


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                CURRENT RATING - RESULTS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -


with tab2:

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')    






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




