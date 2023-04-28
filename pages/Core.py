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


st.title("HELICA Current Rating")
#st.sidebar.markdown("# ... ")

st.markdown('The Cable Rating Module ... ')

@st.experimental_memo
def get_data():
    return pd.DataFrame(np.random.randn(30, 3), columns=["Single_Core", "b", "c"])

tab1, tab2, tab3 = st.tabs(["🖥️ Cable Data", "📊 Cable Rating", "🗂️ Export Results"])


    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        ''
    with col2:
        #if cable == "Single Core":
        #    image = Image.open('single_core0.png')
        #    st.image(image, caption='Cross Section', width=250)
        #if cable == "Three Core":
        #    image = Image.open('three_core0.png')
        #    st.image(image, caption='Cross Section', width=250)
        #if cable == "Pipe Type":
        #    image = Image.open('pipe_type0.png')
        #    st.image(image, caption='Cross Section', width=250)
     
    with st.expander('INTRUCTIONS'):
        # with st.expander('Surface Admittance Operator'):

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

    with tab1:
    cable2 = st.selectbox("Select Cable Type",
                       options=["Single Core", "Three Core", "Pipe Type"])

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("")
        radius1 = st.number_input('R1 [mm]', format="%f", value=10., step=1., min_value=.001)
        radius2 = st.number_input('R2 [mm]', format="%f", value=20., step=1., min_value=.001)
        radius3 = st.number_input('R3 [mm]', format="%f", value=25., step=1., min_value=.001)

    with col2:
        st.write("")
        radius4 = st.number_input('R4 [mm]', format="%f", value=30., step=1., min_value=.001)
        radius5 = st.number_input('R5 [mm]', format="%f", value=40., step=1., min_value=.001)
        radius6 = st.number_input('R6 [mm]', format="%f", value=50., step=1., min_value=.001)

    with col3:
        st.write("")
        rc = st.number_input('Rcore [mm]', format="%f", value=1., step=1., min_value=.001)
        rs = st.number_input('Rsheath [mm]', format="%f", value=1., step=1., min_value=.001)
        ra = st.number_input('Rarmour [mm]', format="%f", value=1., step=1., min_value=.001)
        
        
        outc = 1.1 + 1.e-5
        outs = 2.75
        outer = 4

        rc = 0.1
        rs = 0.2
        ra = 0.3


        n = 40
        ns = 40
        theta = 360 / n
        theta_s = 360 / ns


        if outc == rc:
            nc=1
        else:
            layers=int(np.floor(outc/rc- np.floor(0.5*outc/rc)))
            nc= np.zeros(layers)
            nc=[1] + [(i*6) for i in range(1, layers+1)]
            theta_c = [0] + [(360/nc[i]) for i in range(1, layers+1)]
            R1c = [2*rc*i for i in range(0, layers+1)]


        xc= np.zeros(sum(nc),dtype='float32')
        yc= np.zeros(sum(nc),dtype='float32')

        for k in range(0, layers+1):

            a = sum(nc[0:k])
            b = sum(nc[0:k + 1]) 

            xc[a:b] = [R1c[k] * np.cos(i*(theta_c[k]*np.pi/180)) for i in range(1, nc[k]+1)]
            yc[a:b] = [R1c[k] * np.sin(i*(theta_c[k]*np.pi/180)) for i in range(1, nc[k]+1)]


        x = [outer * np.cos(i * (theta * np.pi / 180)) for i in range(0, n)]
        y = [outer * np.sin(i * (theta * np.pi / 180)) for i in range(0, n)]

        xs = [outs * np.cos(i * (theta_s * np.pi / 180)) for i in range(0, ns)]
        ys = [outs * np.sin(i * (theta_s * np.pi / 180)) for i in range(0, ns)]


        # PLOT circles
        fig = go.Figure()

        #fig.add_shape(type="circle",
        #              xref="x", yref="y", fillcolor="PaleTurquoise",
        #              x0=-1.5, y0=-1.5, x1=1.5, y1=1.5,
        #              line_color="LightSeaGreen");

        # CORE
        for i in range(len(xc)):
            fig.add_shape(type="circle",
                          x0=xc[i] - rc, y0=yc[i] - rc, x1=xc[i] + rc, y1=yc[i] + rc,
                          line_color="LightSeaGreen")

        fig.add_shape(type="circle",
            x0=-outc-2*rc, y0=-outc-2*rc, x1=outc+2*rc, y1=outc+2*rc,
            line_color="LightSeaGreen");


        # SHEATH
        for i in range(ns):
            fig.add_shape(type="circle",
            x0=xs[i] - rs, y0=ys[i] - rs, x1=xs[i] + rs, y1=ys[i] + rs,
            line_color="LightSeaGreen")

        fig.add_shape(type="circle",
            x0=-outs+rs, y0=-outs+rs, x1=outs-rs, y1=outs-rs,
            line_color="LightSeaGreen");

        fig.add_shape(type="circle",
            x0=-outs-rs, y0=-outs-rs, x1=outs+rs, y1=outs+rs,
            line_color="LightSeaGreen")

        # ARMOUT
        for i in range(n):
            fig.add_shape(type="circle",
            x0=x[i] - ra, y0=y[i] - ra, x1=x[i] + ra, y1=y[i] + ra,
            line_color="LightSeaGreen")

        fig.add_shape(type="circle",
                      x0=-outer - 2 * ra, y0=-outer - 2 * ra, x1=outer + 2 * ra, y1=outer + 2 * ra,
                      line_color="LightSeaGreen");

        fig.add_shape(type="circle",
            x0=-outer - 1 * ra, y0=-outer - 1 * ra, x1=outer + 1 * ra, y1=outer + 1 * ra,
            line_color="LightSeaGreen");

        fig.add_shape(type="circle",
            x0=-outer + 1 * ra, y0=-outer + 1 * ra, x1=outer - 1 * ra, y1=outer - 1 * ra,
            line_color="LightSeaGreen");




        fig.update_layout(width=450, height=450)
        fig.update_xaxes(range=[-5, 5], zeroline=False)
        fig.update_yaxes(range=[-5, 5])

        fig.update_xaxes(visible= False,mirror=True, ticks='outside', showline=True, linecolor='black', gridcolor='white')
        fig.update_yaxes(visible= False,mirror=True, ticks='outside', showline=True, linecolor='black', gridcolor='white')

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)')

        fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
        )
        
        st.plotly_chart(fig)


    with col3:
        ''






        




    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  PAG 2 -- CABLE PARAMETERS
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab2:

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')    







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



