import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image # import images
import matplotlib.pylab as plt

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                    SETTINGS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
icon=Image.open('aau_icon.png')
st.set_page_config(page_title="CABOTioN: Black-Box Modeling", layout="wide", page_icon=icon)

#-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SIDEBAR
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                #background-image: url(https://iili.io/gfPxyv.png);
                #background-image: url(https://iili.io/gKGast.png);
                background-image: url(https://iili.io/gq211a.png);
                background-repeat: no-repeat;
                padding-top: 10px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                #content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()

st.sidebar.image('aau_logo.png', width=150)
st.sidebar.image('ist_logo.png', width=150)
st.sidebar.image('energinet_logo.png', width=200)
st.sidebar.image('orsted_logo.png', width=130)
st.sidebar.image('pscad_logo2.png', width=180)

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     TITLE
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

st.title('Network Equivalent Circuit (Black-Box)')
#st.title('This is a title')
#st.header('This is a header')
#st.subheader('This is a subheader')

#st.markdown("# Time-Domain Solver")
st.markdown('Consider the electrical network in Fig. ???  (quantities given in units [ohms], [H], [F]). We wish '
            'to calculate a black box model of the equivalent with respect to terminals 1 and 2 when only '
            'the frequency response at the terminals are known.')

st.markdown('[ref] Matrix Fitting Toolbox for rational modeling from Y-parameter and'
            'S-parameter data '
            '([user manual](https://www.sintef.no/projectweb/vectorfitting/downloads/matrix-fitting-toolbox/))')

#st.caption('This is a string that explains something above.')

image = Image.open('fdne.png')
st.image(image, caption='Electric circuit [ref]', width=550)

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
# EXPANDER
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

with st.expander('Kron Reduction'):
     st.write("""
         Brief explanation on Kron reduction:  .... .
     """)
     st.image('kron1.png')
     st.image('kron2.png')

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
# GET INPUT DATA
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

st.subheader('Define the circuit parameters')
st.caption('Acceptable notation: 1e3 or 1e3.')


# Component values
#st.markdown('Parameter values:')

col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1,1,1,1,1])

with col1:
    st.write("")
    R1 = st.number_input('R1 (ohms)', format= "%f", value=1., step=1., min_value=1.e-12)
    L1 = st.number_input('L1 (mH)', format= "%f", value=1., step=1., min_value=1.e-12)
    C1 = st.number_input('C1 (uF)', format= "%f",  value=1., step=1., min_value=1.e-12)
    L1 = L1*1.e-3
    C1 = C1*1.e-6

with col2:
    st.write("")
    R2 = st.number_input('R2 (ohms)', format= "%f", value=5., step=1., min_value=1.e-12)
    L2 = st.number_input('L2 (mH)', format= "%f", value=5., step=1., min_value=1.e-12)
    L2 = L2*1.e-3

with col3:
    st.write("")
    R3 = st.number_input('R3 (ohms)', format= "%f", value=1., step=1., min_value=1.e-12)
    C3 = st.number_input('C3 (uF)', format= "%f", value=1., step=1., min_value=1.e-12)
    C3 = C3*1.e-6

with col4:
    st.write("")
    R4 = st.number_input('R4 (ohms)', format= "%f", value=1.e-3, step=1., min_value=1.e-12)
    L4 = st.number_input('L4 (mH)', format= "%f", value=1., step=1., min_value=1.e-12)
    L4 = L4*1.e-3

with col5:
    st.write("")
    L5 = st.number_input('L5 (mH)', format= "%f", value=20., step=1., min_value=1.e-12)
    L5 = L5*1.e-3

with col6:
    st.write("")
    R6 = st.number_input('R6 (ohms)', format= "%f", value=10., step=1., min_value=1.e-12)
    C6 = st.number_input('C6 (uF)', format= "%f", value=10., step=1., min_value=1.e-12)
    C6 = C6*1.e-6

with col7:
    st.write("")
    R7 = st.number_input('R7 (ohms)', format= "%f", value=1., step=1., min_value=1.e-12)
    C7 = st.number_input('C7 (uF)', format= "%f", value=2., step=1., min_value=1.e-12)
    C7 = C7*1.e-6

st.subheader('Select the frequency range')

freq = st.slider("Note: 10^", -2., 10., (1.0, 6.0), 1.,
                  format= "%i")
#st.write('Values:', fminx)
freq1 = freq[0]
freq2 = freq[1]



#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
# SOLVER CODE
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

# Make some shortcuts
zeros = np.zeros
pi = np.pi
inverse = np.linalg.inv

Ns=501; # Number of frequency samples
Nc=2; # Size of Y (after reduction)
bigY=zeros((Ns,Nc,Nc), dtype=complex)
Y=zeros((4,4), dtype=complex);

f=np.logspace(1,5,Ns)
s=2*pi*1j*f;

f = np.logspace(freq1, freq2, Ns)
s = 2 * pi * 1j * f;
#s = [f[i] * 2 * pi * 1j for i in range(0, Ns)]

for k in range(0, Ns):
    sk = s[k];
    y1 = 1 / (R1 + sk * L1 + 1 / (sk * C1));
    y2 = 1 / (R2 + sk * L2);
    y3 = 1 / (R3 + 1 / (sk * C3));
    y4 = 1 / (R4 + sk * L4);
    y5 = 1 / (sk * L5);
    y6 = 1 / (R6 + 1 / (sk * C6));
    y7 = 1 / (R7 + 1 / (sk * C7));

    Y[0, 0] = y1 + y3;
    Y[1, 1] = y4;
    Y[2, 2] = y3 + y4 + y5 + y6;
    Y[3, 3] = y1 + y2 + y6 + y7;

    Y[0, 2] = -y3;
    Y[0, 3] = -y1;
    Y[1, 2] = -y4;
    Y[2, 0] = -y3;
    Y[2, 1] = -y4;
    Y[2, 3] = -y6;
    Y[3, 0] = -y1;
    Y[3, 2] = -y6;

    # Eliminating nodes 3 and 4
    dum1 = np.dot(inverse(Y[2:4, 2:4]), Y[2:4, 0:2])
    dum2 = np.dot(Y[0:2, 2:4], dum1)
    Yred = Y[0:2, 0:2] - dum2
    bigY[k, :, :] = Yred

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
# DATAFRAME: STORAGE OF BIGY
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

n = bigY.shape[1]
nf = bigY.shape[0]
nc = np.sum(np.arange(n+1))

data = np.zeros((nf, nc), dtype=complex)

nm = 0

for i in range(n):
    for j in range(n):
        if j >= i:
            data[:, nm] = np.absolute(bigY[:, i, j])
            nm=nm+1

# defining index
idx = f

# defining column headers
columns = []

for i in range(1, n+1):
    for j in range(1, n+1):
        if j >= i:
            col= 'Y'+ str(i)+ str(j)
            columns.append(col)

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
# PLOT
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

st.subheader('Frequency response')

df2 = pd.DataFrame(data, index = idx, columns = columns)

fig = px.line(np.absolute(df2), log_x=True, log_y=True)
fig.update_xaxes(title_text="Frequency (Hz)")
fig.update_yaxes(title_text="Admittance (S)")
fig.update_layout(legend_title="Matrix Element")
st.plotly_chart(fig, use_container_width=False)

#fig = np.absolute(df2).plot(logx=True, logy=True, title='Reduced Network (FDNE)')
