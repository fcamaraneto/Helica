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
st.title("HELICA Current Rating")
st.markdown('The Cable Rating module ... ')
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
tab1, tab2, tab3 = st.tabs(["🖥️ Cable Data", "📊 Cable Rating", "🗂️ Export Results"])

with tab1:
    cable2 = st.selectbox("Select Cable Type",
                       options=["Single Core (stranded sheath)", "Single Core (tubular sheath)",
                                "Three Core", "Pipe Type"])


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  1- Single Core (stranded sheath)
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    if cable2 == "Single Core (stranded sheath)":
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

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.write("")
            radius1 = st.number_input('R1 [mm]', format="%f", value=1.5, step=.1, min_value=.001)
            radius3 = st.number_input('R3 [mm]', format="%f", value=2.75, step=.1, min_value=.001)
        with col2:
            st.write("")
            radius5 = st.number_input('R5 [mm]', format="%f", value=4.0, step=.1, min_value=.001)
            radius6 = st.number_input('R6 [mm]', format="%f", value=4.2, step=.1, min_value=.001)
        with col3:
            st.write("")
            rs = st.number_input('Rsheath [mm]', format="%f", value=0.2, step=.1, min_value=.001)
            ra = st.number_input('Rarmour [mm]', format="%f", value=0.2, step=.1, min_value=.001)

        outs = radius3
        outer = radius5
        ns = 40
        na = 60
        theta = 360/na
        theta_s = 360/ns

        xs = [radius3 * np.cos(i*(theta_s*np.pi/180)) for i in range(0, ns)]
        ys = [radius3 * np.sin(i*(theta_s*np.pi/180)) for i in range(0, ns)]
        xa = [radius5 * np.cos(i*(theta*np.pi/180)) for i in range(0, na)]
        ya = [radius5 * np.sin(i*(theta*np.pi/180)) for i in range(0, na)]

        # PLOT conductors
        fig = go.Figure()
        # core
        fig.add_shape(type="circle", xref="x", yref="y",
                      x0=-radius1, y0=-radius1, x1=radius1, y1=radius1,
                      line_color="LightSeaGreen", fillcolor="PaleTurquoise");
        # sheath
        for i in range(ns):
            fig.add_shape(type="circle",
                          x0= xs[i]-rs, y0= ys[i]-rs, x1= xs[i]+rs, y1= ys[i]+rs,
                          line_color="LightSeaGreen")
        fig.add_shape(type="circle",
                      x0=-outs + rs, y0=-outs + rs, x1=outs - rs, y1=outs - rs,
                      line_color="LightSeaGreen");
        fig.add_shape(type="circle",
                      x0=-outs - rs, y0=-outs - rs, x1=outs + rs, y1=outs + rs,
                      line_color="LightSeaGreen")
        # armour
        for i in range(na):
            fig.add_shape(type="circle",
                          x0= xa[i]-ra, y0= ya[i]-ra, x1= xa[i]+ra, y1= ya[i]+ra,
                          line_color="LightSeaGreen")
        fig.add_shape(type="circle",
                      x0= -radius5-ra, y0= -radius5-ra, x1= radius5+ra, y1= radius5+ra,
                      line_color="LightSeaGreen");
        fig.add_shape(type="circle",
                      x0= -radius5+ra, y0= -radius5+ra, x1= radius5-ra, y1= radius5-ra,
                      line_color="LightSeaGreen");
        # jacket/server
        fig.add_shape(type="circle",
                      x0= -radius6-ra, y0= -radius6-ra, x1= radius6+ra, y1= radius6+ra,
                      line_color="LightSeaGreen");


        fig.update_layout(width=450, height=450)
        fig.update_xaxes(range=[-5, 5])
        fig.update_yaxes(range=[-5, 5])
        fig.update_xaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black',
                         gridcolor='white')
        fig.update_yaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black',
                         gridcolor='white')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig)

        'To do -- choice on the number of sheath/armour conductors.'

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#  2- Single Core (tubular sheath)
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    if cable2 == "Single Core (tubular sheath)":

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

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.write("")
            radius1 = st.number_input('R1 [mm]', format="%f", value=1.5, step=.1, min_value=.001)
            radius2 = st.number_input('R2 [mm]', format="%f", value=99., step=.1, min_value=.001)
            radius3 = st.number_input('R3 [mm]', format="%f", value=2.75, step=.1, min_value=.001)
        with col2:
            st.write("")
            radius4 = st.number_input('R4 [mm]', format="%f", value=99., step=.1, min_value=.001)
            radius5 = st.number_input('R5 [mm]', format="%f", value=4.0, step=.1, min_value=.001)
            radius6 = st.number_input('R6 [mm]', format="%f", value=4.2, step=.1, min_value=.001)
        with col3:
            st.write("")
            rc = st.number_input('Rcore [mm]', format="%f", value=99., step=.1, min_value=.001)
            rs = st.number_input('Rsheath [mm]', format="%f", value=0.2, step=.1, min_value=.001)
            ra = st.number_input('Rarmour [mm]', format="%f", value=0.2, step=.1, min_value=.001)


        outer = 4
        n = 60
        theta = 360 / n

        x = [outer * np.cos(i * (theta * np.pi / 180)) for i in range(0, n)]
        y = [outer * np.sin(i * (theta * np.pi / 180)) for i in range(0, n)]

        # PLOT conductors
        fig = go.Figure()

        for i in range(n):
            fig.add_shape(type="circle", x0=x[i] - ra, y0=y[i] - ra, x1=x[i] + ra, y1=y[i] + ra,
                          line_color="LightSeaGreen")

        fig.add_shape(type="circle", x0= -radius6-ra, y0= -radius6-ra, x1= radius6+ra, y1= radius6+ra,
                      line_color="LightSeaGreen");
        fig.add_shape(type="circle", x0=-radius5-ra, y0=-radius5-ra, x1=radius5+ra, y1=outer+ra,
                      line_color="LightSeaGreen");
        fig.add_shape(type="circle", x0=-radius5+ra, y0=-radius5+ra, x1=radius5-ra, y1=outer-ra,
                      line_color="LightSeaGreen");

        fig.add_shape(type="circle", x0=-3, y0=-3, x1=3, y1=3, line_color="LightSeaGreen");
        fig.add_shape(type="circle", x0=-3.2, y0=-3.2, x1=3.2, y1=3.2, line_color="LightSeaGreen")
        fig.add_shape(type="circle", xref="x", yref="y", fillcolor="PaleTurquoise", x0=-1.5, y0=-1.5, x1=1.5, y1=1.5,
                      line_color="LightSeaGreen");

        fig.update_layout(width=450, height=450)
        fig.update_xaxes(range=[-5, 5], zeroline=False)
        fig.update_yaxes(range=[-5, 5])
        fig.update_xaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black',
                         gridcolor='white')
        fig.update_yaxes(visible=False, mirror=True, ticks='outside', showline=True, linecolor='black',
                         gridcolor='white')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig)
# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    if cable2 == "Three Core":
        ''
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    if cable2 == "Pipe Type":
        ''




    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        ''
    with col2:
        ''









    with col3:
        ''

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



