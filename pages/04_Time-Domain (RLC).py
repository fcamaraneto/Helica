import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image # import images
import matplotlib.pylab as plt

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SETTINGS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
icon=Image.open('aau_icon.png')
st.set_page_config(page_title="CABOTioN: Time-Domain Solver", layout="wide", page_icon=icon)

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


#-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -


st.markdown("# Time-Domain Solver")
#st.markdown('## Network Equivalent Circuit')

#st.markdown('Consider the electrical network in Fig. ???  (quantities given in units [ohms], [H], [F]). We wish '
#            'to calculate a black box model of the equivalent with respect to terminals 1 and 2 when only '
#            'the frequency response at the terminals are known.')

#st.markdown('[ref] Matrix Fitting Toolbox for rational modeling from Y-parameter and'
#            'S-parameter data '
#            '([user manual](https://www.sintef.no/projectweb/vectorfitting/downloads/matrix-fitting-toolbox/))')

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

# Component values
#st.markdown('Parameter values:')

image = Image.open('RLC.png')
st.image(image, caption='Electric circuit [ref]', width=400)

st.subheader('Define the circuit parameters')
st.caption('Acceptable notation: 1e3 or 1e3.')

col1, col2, col3, col4,col5, col6 = st.columns([.5,.25,.5,.25,.5,2])


with col1:
    st.write("")
    R = st.number_input('R (ohms)', format= "%f", value=100., step=10., min_value=1.e-12)
    L = st.number_input('L (mH)', format= "%f", value=110., step=10., min_value=1.e-12)
    L = L*1.e-3
    C = st.number_input('C (uF)', format= "%f", value=0.25, step=.10, min_value=1.e-12)
    C = C*1.e-6

with col2:
    st.write("")

with col3:
    st.write("")
    vin = st.number_input('Vs (V)', format="%f", value=1., step=1.)
    freq = st.number_input('f (Hz)', format="%f", value=50., step=10.)
    phase = st.number_input('Phase (deg): NOT WORKING', format= "%f", value=0., step=10.,
                            min_value=-360., max_value=360.)
with col4:
    st.write("")

with col5:
    st.write("")
    tmax = st.number_input('tmax (ms)', format= "%f", value=20., step=10.)
    tmax = tmax * 1.e-3
    dt = st.number_input('dt (us)', format= "%f", value=10., step=5.)
    dt = dt*1.e-6
    t1 = st.number_input('t1 (ms): NOT WORKING', format= "%f", value=0., step=1.)
    t1 = t1*1.e-3

with col6:
    st.write("")

#with col6:
#    st.write("")
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

# Make some shortcuts
zeros = np.zeros
pi = np.pi
cos = np.cos
solve = np.linalg.solve

# Time vector
kmax = round(tmax/dt)
t = [i*dt for i in range(0, kmax)]
time = [i*dt*1e3 for i in range(0, kmax)]
nt = len(t)
omega = 1 * 2*pi*freq



# Nodal Admittance Matrix

yR = 1/R
yL = dt/(2*L)
yC = (2*C)/dt

n=3
ynodal = zeros((n+1, n+1))

ynodal[0, 0] = yR
ynodal[1, 1] = yR + yL
ynodal[2, 2] = yL + yC
ynodal[0, 1] = ynodal[1, 0] = -yR
ynodal[1, 2] = ynodal[2, 1] = -yL
ynodal[0, n] = ynodal[n, 0] = 1

# Initialization of other vectors

input = [vin*cos(omega*t[i]) for i in range(0, nt)]
rhs = zeros((n+1), dtype=complex)
x = zeros(n, dtype=complex)
out = zeros((nt, n+1))

v = np.array([input[0], 0, 0, 0, 0, 0])

hisL = zeros(1,dtype=complex)
hisC = zeros(1,dtype=complex)
vL = zeros(1,dtype=complex)
vC = zeros(1,dtype=complex)
iL = zeros(1,dtype=complex)
iC = zeros(1,dtype=complex)

for nm in range(nt):
    hisL = yL * vL + iL
    hisC = yC * vC + iC
    rhs[0] = 0
    rhs[1] = -hisL
    rhs[2] = hisL + hisC
    rhs[3] = input[nm]

    x = solve(ynodal, rhs)

    vL = x[1] - x[2]
    vC = x[2]
    iL = yL * vL + hisL
    iC = yC * vC - hisC

    out[nm] = x.real

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
# PLOT
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

# defining column headers
columns1=(['V1','V2','V3'])
columns2=(['i'])

df1 = pd.DataFrame(out[:,0:3], index = time, columns = columns1)
df2 = pd.DataFrame(-1000*out[:,3], index = time, columns = columns2)

st.subheader('Time-domain response')

#col1, col2, col3 = st.columns([4,4,1])

#with col1:
fig1 = px.line(df1)
fig1.update_xaxes(title_text="Time (ms)")
fig1.update_yaxes(title_text="Voltage (V)")
fig1.update_layout(legend_title="")
st.plotly_chart(fig1, use_container_width=False)
# fig.update_layout(legend_title="Matrix Element")

#with col2:
fig2 = px.line(df2)
fig2.update_xaxes(title_text="Time (ms)")
fig2.update_yaxes(title_text="Current (mA)")
fig2.update_layout(legend_title="")
# fig.update_layout(legend_title="Matrix Element")
st.plotly_chart(fig2, use_container_width=False)

#with col3:
#    st.write("")

