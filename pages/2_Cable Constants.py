import streamlit as st
from PIL import Image # create page icon
#from streamlit_extras.app_logo import add_logo
#import streamlit.components.v1 as components

import pandas as pd
import numpy as np
#import scipy.io as spio
import scipy.special as spios
import plotly.express as px

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


st.title("HELICA cable constants ")
#st.sidebar.markdown("# ... ")

st.markdown('The Universal Cable Constants (UCC) aims at providing a computational tool to allow an '
            'accurate computation of cable parameters and a straightforward interface with EMT-type '
            'software for time-domain simulations.')

#colored_header("🧶 st.line_chart")

#image = Image.open('emtp2.png')
#st.image(image, caption='Cable cross-section')

# Using object notation
#add_selectbox = st.sidebar.selectbox(
#    "Select Cable Type:",
#    ("1) HVDC - Single core",
#     "2) HVAC - Single Core",
#     "3) HVAC - Three Core",
#     "4) HVAC - Pype-type"))

@st.experimental_memo
def get_data():
    return pd.DataFrame(np.random.randn(30, 3), columns=["Single_Core", "b", "c"])

tab1, tab2 = st.tabs(["📊 Cable Parameters", "🗂️ Export Parameters"])


    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #  PAG 2 -- CABLE PARAMETERS
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
with tab1:

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')    

    #nf = st.number_input('Samples', value=500, step=100, min_value=1)
    
    f1 = st.slider("Frequency range (10^ Hz)", -2., 7., (0., 6.0), step=1.)
    freq1 = f1[0]
    freq2 = f1[1]

    #st.write('Values:', np.power(10, freq1), np.power(10, freq2))  # *** FORMATAR NUMERO ***


    

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                   SURFACE OPERATOR
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    #st.line_chart(get_data().query(filter_query))

    # Make some shortcuts
    pi = np.pi
    sqrt = np.sqrt
    zeros = np.zeros
    besselJ = spios.jv
    inverse = np.linalg.inv
    transpose = np.transpose
    conjugate = np.conjugate
    identity = np.identity
    abs = np.absolute
    real = np.real
    imag = np.imag

    x = np.array([0., dd*1e-3])
    y = np.array([0., 0.])
    r = np.array([radius1*1e-3, radius2*1e-3])

    xpq = x[1] - x[0]
    ypq = y[1] - y[0]
    dpq = sqrt(np.power(xpq, 2) + np.power(ypq, 2))

    # Fourier order
    Np = 2
    nc = 2 * Np + 1

    # frequency range
    #nf = 501
    f = np.logspace(freq1, freq2, nf)
    s = 2 * pi * f;

    Y = zeros((nf, nc), dtype=complex)
    Z = zeros((nf, 1), dtype=complex)
    L = zeros(nf)
    R = zeros(nf)

    # CONSTANTS
    mu0 = 4 * pi * 1e-7
    # condutor
    muc = 1
    epc = 1
    sigc = ssg*1e7
    # meio isolante
    mur = 1
    epsr = 1


    def surface(radius, order, omega, mur1, epsr1, mur2, epsr2, sigma):
        mu = 4 * pi * 1e-7
        eps = 8.854e-12

        k = sqrt(omega * mur1 * mu * (omega * eps * epsr1 - 1j * sigma))
        k0 = omega * sqrt(mur2 * mu * eps * epsr2)

        bessel = besselJ(order, k * radius)
        bessel0 = besselJ(order, k0 * radius)

        dbessel = 0.5 * (besselJ(-1 + order, k * radius) - besselJ(1 + order, k * radius))
        dbessel0 = 0.5 * (besselJ(-1 + order, k0 * radius) - besselJ(1 + order, k0 * radius))

        yn = (2 * pi / (1j * omega)) * (
                    (k * radius * dbessel / (mu * mur1 * bessel)) - k0 * radius * dbessel0 / (mu * mur2 * bessel0))

        return (yn)


    for k in range(0, nf):
        omega = s[k]
        for nm in range(-Np, Np+1):
            yn = surface(r[1], nm, omega, 1, 1, 1, 1, sigc)
            Y[k, nm+Np] = yn


    # DATAFRAME: armazenamento de Y de forma mais eficiente para plotagem

    data1 = np.zeros((nf, nc), dtype=complex)

    for i in range(nc):
        data1[:, i] = (Y[:, i])

    idx = f

    # defining column headers
    columns = []
    for i in range(-Np, Np + 1):
        col = 'Y' + str(i)
        columns.append(col)

    df1 = pd.DataFrame(data1, index = idx, columns = columns)



    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #              PARAMETERS COMPUTATION
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    def f45(dpq):
        sol = np.log(dpq) / (2 * pi)
        return (sol)

    def f46(ap, dpq, n2, xpq, ypq):
        sol1 = (-1 / (4 * pi * abs(n2))) * np.power(ap / dpq, abs(n2))
        sol2 = np.power(-(xpq - 1j * ypq) / dpq, n2)
        sol = sol1 * sol2
        return (sol)

    def f50(ap, aq, n2, n, xpq, ypq):
        sol1 = (-pi * np.power(aq, n) / np.power(-ap, n2)) * spios.binom(n - n2 - 1, -n2)
        sol2 = np.power(xpq - 1j * ypq, -n + n2) / (np.power(2 * pi, 2) * n)
        sol = sol1 * sol2
        return (sol)

    def f52(radius):
        sol = np.log(radius) / (2 * pi)
        return (sol)

    def f53(order):
        sol = -1 / (4 * pi * abs(order))
        return (sol)
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    U = zeros((2, 2 * nc), dtype=int)
    U[0,2] = 1
    U[1,7] = 1
    Q = np.array([(1, 0), (0, 1)])
    S = np.array([1, -1])
    U = transpose(U)

    g11 = zeros((nc, nc), dtype=complex)
    g12 = zeros((nc, nc), dtype=complex)
    G = zeros((2 * nc, 2 * nc), dtype=complex)

    g11[0, 0] = f53(-2)
    g11[1, 1] = f53(-1)
    g11[2, 2] = f52(r[0])
    g11[3, 3] = f53(1)
    g11[4, 4] = f53(2)

    g12[0, 2] = f46(r[0], dpq, -2, xpq, ypq)  # [G,-2,0]
    g12[1, 2] = f46(r[0], dpq, -1, xpq, ypq)  # [G,-1,0]
    g12[2, 2] = f45(dpq)                      # [G,0,0]
    g12[3, 2] = f46(r[0], dpq, 1, xpq, ypq)   # [G,1,0]
    g12[4, 2] = f46(r[0], dpq, 2, xpq, ypq)   # [G,2,0]

    # upper off-diagonal block
    g12[0, 3] = f50(r[1], r[1], -2, 1, xpq, ypq)  # [G, -2,1]
    g12[0, 4] = f50(r[1], r[1], -2, 2, xpq, ypq)  # [G, -2,2]
    g12[1, 3] = f50(r[1], r[1], -1, 1, xpq, ypq)  # [G, -1,1]
    g12[1, 4] = f50(r[1], r[1], -1, 2, xpq, ypq)  # [G, -1,2]
    g12[2, 3] = f50(r[1], r[1], 0, 1, xpq, ypq)  # t[G, 0,1]
    g12[2, 4] = f50(r[1], r[1], 0, 2, xpq, ypq)  # [G, 0,2]

    # lower off-diagonal block
    g12[2, 0] = conjugate(f50(r[0], r[1], 0, 2, xpq, ypq))  # [G, 0,-2]
    g12[2, 1] = conjugate(f50(r[0], r[1], 0, 1, xpq, ypq))  # [G, 0,-1]
    g12[3, 0] = conjugate(f50(r[0], r[1], -1, 2, xpq, ypq))  # [G, 1,-2]
    g12[3, 1] = conjugate(f50(r[0], r[1], -1, 1, xpq, ypq))  # [G, 1,-1]
    g12[4, 0] = conjugate(f50(r[0], r[1], -2, 2, xpq, ypq))  # [G, 2,-2]
    g12[4, 1] = conjugate(f50(r[0], r[1], -2, 1, xpq, ypq))  # [G, 2,-1]

    # global G matrix
    G[0:nc, 0:nc] = g11
    G[0:nc, nc:2 * nc] = g12
    G[nc:2 * nc, 0:nc] = transpose(conjugate(g12))   #g12.getH()  # transpose-conjugate
    G[nc:2 * nc, nc:2 * nc] = g11

    for k in range(0, nf):

        omega = s[k]
        dig = (np.array([Y[k, :], Y[k, :]])).flatten()
        Yn = np.diag(dig)

        zz = inverse(transpose(U) @ (inverse(identity(2 * nc) - 1j * omega * mu0 * Yn @ G)) @ Yn @ U)
        z = transpose(S) @ inverse(Q @ inverse(zz) @ transpose(Q)) @ S

        Z[k] = z
        R[k] = real(z)
        L[k] = imag(z) / omega



    # DATAFRAME: armazenamento da bigY de forma mais eficiente para plotagem
    df2 = pd.DataFrame(R, index = idx, columns = ['R'])
    df3 = pd.DataFrame(L, index = idx, columns = ['L'])

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #              PLOT
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    

    st.markdown("""### Resistance""")
    fig2 = px.line(df2, log_x=True, log_y=True)
    fig2.update_xaxes(title_text="Frequency (Hz)")
    fig2.update_yaxes(title_text="Resistance (Ω)")
    fig2.update_layout(legend_title="R (Ω)")
    fig2.update_xaxes(exponentformat="SI")
    fig2.update_yaxes(exponentformat="e") # "SI"
    st.plotly_chart(fig2, use_container_width=False)

    st.markdown("""### Inductance""")
    fig3 = px.line(df3, log_x=True, log_y=False)
    fig3.update_xaxes(title_text="Frequency (Hz)")
    fig3.update_yaxes(title_text="Inductance (H)")
    fig3.update_layout(legend_title="L (H)")
    fig3.update_xaxes(exponentformat="SI")
    fig3.update_yaxes(exponentformat="e") # "SI"
    st.plotly_chart(fig3, use_container_width=False)


with tab2:
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





    #st.dataframe(get_data().query(filter_query))


    #@st.cache
    #def convert_df(df):
    #    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    #    return df.to_csv().encode('utf-8')

    #csv = convert_df(my_large_df)






