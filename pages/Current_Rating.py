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


with tab1:
    cable2 = st.selectbox("Select Cable Type",
                       options=["Single Core", "Three Core", "Pipe Type"])

    col1, col2, col3 = st.columns([1, 18, 1])
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

        fig = go.Figure()

        ra = 0.2
        outer = 4
        n = 60
        theta = 360 / n

        x = [outer * np.cos(i * (theta * np.pi / 180)) for i in range(0, n)]
        y = [outer * np.sin(i * (theta * np.pi / 180)) for i in range(0, n)]

        # Add circles

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

        fig.add_shape(type="circle",
                      x0=-3, y0=-3, x1=3, y1=3,
                      line_color="LightSeaGreen");

        fig.add_shape(type="circle",
                      x0=-3.2, y0=-3.2, x1=3.2, y1=3.2,
                      line_color="LightSeaGreen")

        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      fillcolor="PaleTurquoise",
                      x0=-1.5, y0=-1.5, x1=1.5, y1=1.5,
                      line_color="LightSeaGreen");

        fig.update_layout(width=400, height=400.0)
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


    ### Cross-section
    #fig2 = px.line(df2, log_x=True, log_y=True)
    #fig2.update_xaxes(title_text="Frequency (Hz)")
    #fig2.update_yaxes(title_text="Resistance (Ω)")
    #fig2.update_layout(legend_title="R (Ω)")
    #fig2.update_xaxes(exponentformat="SI")
    #fig2.update_yaxes(exponentformat="e")  # "SI"



        




    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  PAG 2 -- CABLE PARAMETERS
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab2:

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')    







with tab3:
    st.subheader('Interfacing with circuit solvers')
    st.markdown(' Interfacing with circuit solvers contains matlab scripts which demonstrate'
            ' how to interface rational function-based models with time domain circuit solvers '
            'via a Norton equivalent. The procedure is shown for models representing '
            'Y-parameters, Z-parameters, S-parameters, and general transfer functions that '
            'do not interact with the circuit.')

    col = st.selectbox("Select Software:",
                       options=["PSCAD", "EMTP", "PowerFactory", "ATP"])

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




