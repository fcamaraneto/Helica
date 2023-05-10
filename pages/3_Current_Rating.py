import streamlit as st
from PIL import Image # create page icon
import pandas as pd
import numpy as np

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
                height:60%;
                background-image: url({url});
                background-size: 40% auto;
                background-repeat: no-repeat;
                background-position-x: center;
                background-position-y: bottom;
            }}
        </style>
        """,
        unsafe_allow_html=True)

add_logo()

#st.sidebar.markdown("HELICA Cable Rating module complies with IEC 60287 and IEC 60949 ... ")
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -



tab1, tab2 = st.tabs(["🖥️ Cable Data", "📊 Cable Rating"])

with tab1:

    '**CABLE DESIGN**'
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    with col1:
        study = st.selectbox("CROSS-SECTION", options=["Single Core", "Three Core", "Bipole"])
        #conductor = st.selectbox('CONDUCTOR', options=["Copper", "Aluminium", "Other"])
    with col2:
        layout = st.selectbox("LAYOUT", options=["Trefoil", "Flat"])
        #insulation = st.selectbox('INSULATION', options=["XLPE", "PVC", "Other"])
    with col3:
        installation = st.selectbox("INSTALLATION", options=["Buried", "Layered", "J-Tube", "Floating"])
    with col4:
        freq = st.selectbox("Frequency", options=["50 Hz", "60 Hz", "DC"])


    ''
    ''
    '**CABLE MATERIALS**'
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    with col1:
        conductor1 = st.selectbox('CONDUCTOR', options=["Copper", "Aluminium", "Other"])
        insulation1 = st.selectbox('INSULATION1', options=["XLPE", "PVC", "Other"])
    with col2:
        conductor2 = st.selectbox('SHEATH', options=["Copper", "Aluminium", "Lead", "Other"])
        insulation2 = st.selectbox('INSULATION2', options=["XLPE", "PVC", "Other"])
    with col3:
        conductor3 = st.selectbox('ARMOUR', options=["Steel1", "Steel2", "Other"])
        insulation3 = st.selectbox('INSULATION3', options=["XLPE", "PVC", "Other"])
    with col4:
        ''#insulation4 = st.selectbox('SERVING', options=["Material1", "Material2", "Other"])

    ''
    ''
    '**OPERATING CONDITIONS**'
    col1, col2, col3, col4 = st.columns([1., 1.25, 1.25, 1])
    with col1:
        media = st.selectbox("EXTERNAL MEDIA", options=["Seabed", "Sea", "Soil"])
    with col2:
        maxt = st.number_input('MAX. TEMPERATURE [°C]', format="%.2f", value= 99.00, step=.1, min_value= .001)
    with col3:
        t1 = st.number_input('AMBIENT TEMPERATURE [°C]', format="%.2f", value=20.00, step=.1, min_value=.001)
    with col4:
        ''


    ''
    ''
    '**THERMAL RESISTANCE**'
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        rt1 = st.number_input('SEABED', format="%.2f", value= 99.00, step=.1, min_value= .001)
    with col2:
        rt2 = st.number_input('SEA', format="%.2f", value= 99.00, step=.1, min_value= .001)
        #insulation1 = st.selectbox('INSULATION', options=["XLPE", "PVC", "Other"])
    with col3:
        rt3 = st.number_input('SOIL', format="%.2f", value= 99.00, step=.1, min_value= .001)

with tab2:

    # shortcuts
    divide = np.divide
    pi = np.pi
    log = np.log
    sqrt = np.sqrt

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        input1 = st.number_input('MAX TEMPERATURE', format="%.2f", value=90.00, step=1.)#, min_value=.001)
    with col2:
        input2 = st.number_input('AMBIENT TEMPERATURE', format="%.2f", value=20.00, step=1.)#, min_value=.001)
    with col3: ''
    with col4: ''


    #'**RESULTS INDEPENDENT OF THE TEMPERATURE** '
    #'**ELECTRICAL PARAMETERS** '
    # - - - Capacitance -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    # only consider the dielectric only when the values of the diameters are selected (semi-conducting layers or tapes excluded).
    epislon = 2.5
    dc = (30.3 + 2 * 1.5) * 1e-3
    Di = (33.3 + 2 * 15.5) * 1e-3
    C = divide(epislon, 18 * log(divide(Di, dc))) * 1e-9
    # - - - Reactance -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    S = 75.5e-3
    d = (64.3 + (2 * 1.3) + 0.8) * 1e-3
    f = 50
    omega = 2 * np.pi * f
    X = 2 * omega * np.log(divide(2 * S, d)) * 1e-7




    # - - - Electrical resistance of the metal sheath at 20°C -  -  -  -  -  -  -  -  -  -  -  -
    d = 67.7e-3
    ts = 0.8e-3
    As = np.pi * d * ts
    rho_20 = 2.84e-8
    Rs0 = rho_20 / As
    # - - - Thermal resistance between conductor and sheath -  -  -  -  -  -  -  -  -  -  -  -
    def rho_T1(t1, dc, rhoT):
        out = np.zeros(len(t1))
        for i in range(len(t1)):
            out[i] = divide(rhoT[i], 2 * pi) * log(1 + divide(2 * t1[i], dc[i]))
        return out

    t1 = ([1.5e-3, 15.5e-3, 1.3e-3])
    dc = ([30.3e-3, 33.3e-3, 64.3e-3])
    rhoT = ([2.5, 3.5, 2.5])
    T1 = sum(rho_T1(t1, dc, rhoT))

    # - - - Thermal resistance of the oversheath - - -  - - -  - - -  - - -  - - -  - - -  - - -
    # Warning! Despite the lack of reminder in Section 4.1.4.1 of [4], the T3 value must be increased in the
    # case of three single-core touching cables, with metallic sheath in trefoil formation (Section 4.2.4.3.2 of [4])
    # In this case, the thermal resistance of the serving over the sheath or armour, T3, as
    # calculated by the method given in 4.1.4 shall be multiplied by a factor of 1,6.

    t3 = 3.5e-3
    rhoT35 = 3.5
    Da = 68.5e-3
    rho_T3 = (1.6) * divide(1, 2 * pi) * rhoT35 * log(1 + divide(2 * t3, Da))

    # - - - External thermal resistance - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -
    L = 1e0
    De = 75.5e-3
    rhoT4 = 1.
    u = 2 * L / De
    rho_T4 = divide(1.5, pi) * rhoT4 * (log(2 * u) - 0.630)

    # - - - Dielectric losses

    U = 132e3
    U0 = U / np.sqrt(3)
    tdelta = 0.001
    Wd = omega * C * U0 * U0 * tdelta

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    col1, col2 = st.columns(2)
    #col1.metric("Electrical resistance of the metal sheath at 20°C", value=str(float("{:.4f}".format(1e3 * Rs0))) + str(' mΩ/m'))
    #col1.metric("Thermal resistance of the oversheath (T3)", value=str(float("{:.4f}".format(rho_T3))) + str(' Km/W'))
    #col2.metric("Thermal resistance between conductor and sheath (T1)", value=str(float("{:.4f}".format(T1))) + str(' Km/W'))
    #col2.metric("Thermal resistance of the oversheath (T4)", value=str(float("{:.4f}".format(rho_T4))) + str(' Km/W'))
    #col1.metric("Dielectric losses (Wd)", value=str(float("{:.4f}".format(Wd))) + str(' W/m'))
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -



    #'**RESULTS DEPENDENT OF THE TEMPERATURE** '
    theta_c = input1 #theta_c = 90
    theta_s = theta_c - 10
    theta_a = input2 #theta_a = 20
    # - - - DC resistance of conductor - - - - - - - - - - - - - - - - - -
    R0_c = 28.3e-6
    alpha20_c = 3.93e-3
    Rdc = R0_c * (1 + alpha20_c * (theta_c - 20))

    # - - - # Skin effect factor
    ks = 1
    xs2 = (8 * pi * f / Rdc) * 1e-7
    xs = sqrt(xs2)
    # for 0 < xs <= 2.8:
    ys = divide(xs2 ** 2, 192 + 0.8 * xs2 ** 2)

    # - - - Proximity effect factor
    kp = 1
    dc_c = 30.3e-3

    xp2 = (8 * pi * f / Rdc) * 1e-7 * kp
    xp = sqrt(xp2)

    dum1 = divide(xp2 ** 2, 192 + 0.8 * xp2 ** 2) * divide(dc_c, S) ** 2
    dum2 = 0.312 * divide(dc_c, S) ** 2
    dum3 = divide(1.18, divide(xp2 ** 2, 192 + 0.8 * xp2 ** 2) + 0.27)
    yp = dum1 * (dum2 + dum3)

    # - - - AC resistance of conductor
    Rac = Rdc * (1 + ys + yp)

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    ##                               ITERATIVE PROCESS
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # Resistance of sheath at operating temperature
    Rs0 = 1.669128650e-4
    alpha20_s = 4.03e-3
    Rs = Rs0 * (1 + alpha20_s * (theta_s - 20))

    # Losses caused by circulating currents
    # Since the conductor is not Milliken, eddy-current loss is ignored (λ1” = 0)
    lambda1p = divide(Rs, Rac) * divide(1, 1 + divide(Rs, X) ** 2)
    lambda1pp = 0
    lambda1 = lambda1p + lambda1pp

    ## Permissible current rating
    n = 1  # single-core cable
    dtheta = 70
    # unarmoured: λ2 = 0 and T2 = 0
    lambda2 = 0
    T2 = 0
    T3 = rho_T3
    T4 = rho_T4

    dum21 = dtheta - Wd * (0.5 * T1 + n * (T2 + T3 + T4))
    dum22 = Rac * T1 + n * Rac * (1 + lambda1) * T2 + n * Rac * (1 + lambda1 + lambda2) * (T3 + T4)
    I = sqrt(divide(dum21, dum22))

    # Losses in conductor and sheath
    Wc = Rac * I ** 2
    Ws = lambda1 * Wc

    ## Temperature on cable components
    # Temperature on the oversheath (jacket or external serving)
    theta_j = theta_a + n * (Wc + Ws + Wd) * T4
    theta_s = theta_j + n * (Wc + Ws + Wd) * T3
    theta_c = input1 #theta_s + n * (Wc + Wd / 2) * T1

    errorI = 0.001
    errorT = 0.0001
    Iguess = 10000
    Ts_guess = 780
    Tj_guess = 780

    delta_I = abs(I - Iguess)
    delta_Ts = abs(theta_s - Ts_guess)
    delta_Tj = abs(theta_j - Tj_guess)

    # LOOP
    for ITER in range(1, 10):

        if delta_I > errorI and delta_Ts > errorT and delta_Tj > errorT:

            Rs = Rs0 * (1 + alpha20_s * (theta_s - 20))

            lambda1p = divide(Rs, Rac) * divide(1, 1 + divide(Rs, X) ** 2)
            lambda1 = lambda1p + lambda1pp

            dum21 = dtheta - Wd * (0.5 * T1 + n * (T2 + T3 + T4))
            dum22 = Rac * T1 + n * Rac * (1 + lambda1) * T2 + n * Rac * (1 + lambda1 + lambda2) * (T3 + T4)
            I = sqrt(divide(dum21, dum22))

            Wc = Rac * I ** 2
            Ws = lambda1 * Wc

            theta_j = theta_a + n * (Wc + Ws + Wd) * T4
            theta_s = theta_j + n * (Wc + Ws + Wd) * T3
            theta_c = theta_s + n * (Wc + Wd / 2) * T1

            delta_I = abs(I - Iguess);  # print(delta_I)
            delta_Ts = abs(theta_s - Ts_guess);  # print(delta_Ts)
            delta_Tj = abs(theta_j - Tj_guess);  # print(delta_Tj)

            Iguess = I
            Ts_guess = theta_s
            Tj_guess = theta_j

        else:
            break





    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    ''
    #'**RESULTS DEPENDENT OF THE TEMPERATURE** '
    '**RESULTS** '

    st.metric("Current Rating [A]", value=str(float("{:.4f}".format(I))) + str(' A'))

    col1, col2, col3 = st.columns(3)
    col1.metric("Core Temperature [°C]", value=str(float("{:.1f}".format(input1))) + str(' °C'))
    col2.metric("Sheath Temperature [°C]", value=str(float("{:.1f}".format(theta_s))) + str(' °C'))
    col3.metric("Jacket Temperature [°C]", value=str(float("{:.1f}".format(theta_j))) + str(' °C'))

    st.markdown('Convergence: ' + str(ITER) + ' iterations')

    ''
    ''
    '**ELECTRICAL PARAMETERS** '
    col1, col2 = st.columns(2)
    col1.metric("Capacitance", value=str(float("{:.2f}".format(1e12 * C))) + str(' pF/m'))
    col2.metric("Reactance", value=str(float("{:.2f}".format(1e6 * X))) + str(' μΩ/m'))

    #col1.metric("DC resistance of core conductor [90°C]",
    #            value=str(float("{:.4f}".format(0 * Rs0))) + str(' mΩ/m'))
    #col2.metric("AC resistance of core conductor [90°C]", value=str(float("{:.4f}".format(0))) + str(' Km/W'))
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -







































#st.markdown('Remark: “All current rating calculations shall be performed with a verified current rating calculation tool '
#            'and on the basis of IEC 60287. Where CIGRE TB 880 provides additional guidance compared to '
#            'IEC 60287, this shall be followed. If the TB 880 provides a different interpretation of the IEC '
#            'calculations, it is suggested to follow the TB 880 guidance.”')

#columns = ['Result %d' % i for i in range(3)]
#index = ['Case %d' % i for i in range(int(steps))]

#df = pd.DataFrame(
#    np.random.randn(int(steps), 3),
#    columns=columns, index=index)

#st.table(df)
