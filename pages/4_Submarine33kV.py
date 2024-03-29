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



tab1, tab2 = st.tabs(["🖥️ Input Data", "📊 GUI"])

with tab1:

    # shortcuts
    divide = np.divide
    pi = np.pi
    log = np.log
    sqrt = np.sqrt
    print = st.markdown


    col1, col2, col3, col4 = st.columns([.75, .75, 1, 1])
    with col1:
        Ux = st.number_input('Voltage [kV]', format="%.2f", value=30., step=1., min_value=10.)
        U0 = Ux*1e3/sqrt(3)
    with col2:
        freq = st.selectbox("FREQUENCY (Hz)", options=["50 Hz", "60 Hz", "DC"])
        if freq == "50 Hz":
            f = 50
        if freq == "60 Hz":
            f = 60
        if freq == "DC":
            f = 0
        omega = 2*pi*f
    with col3:
        theta = st.number_input('MAXIMUN TEMPERATURE [°C]', format="%.2f", value=90.00, step=1.)
        input1 = theta
    with col4:
        input2 = st.number_input('AMBIENT TEMPERATURE [°C]', format="%.2f", value=20.00, step=1.)

    print('**CONDUCTOR DATA**')
    col1, col2, col3, col4 = st.columns([1, 1.25, 1, 1])
    with col1:
        sx = st.number_input('Axial Separation [mm]', format="%.2f", value=62.1, step=1., min_value=.001)
        s = sx*1e-3
        dcx = st.number_input('Diameter [mm]',format="%.2f", value=30.00, step=1.)
        dc = dcx*1e-3

        insulation_c = st.selectbox('Isulation', options=["XLPE"])
    with col2:
        material_c = st.selectbox('Conductor Material', options=["Copper", "Aluminum"])
        epislon = 2.5

        dc2x = st.number_input('External Diameter (screen) [mm]',format="%.2f", value=32.50, step=1.)
        dc2 = dc2x*1e-3
        tgdelta = st.number_input('Ta𝑛 𝛿',format="%.3f", value=0.004, step=0.001)
    with col3:
        type_c = st.selectbox('Conductor Type', options=["Round stranded compacted"])
        Dix = st.number_input('Outer insulation [mm]',format="%.2f", value=48.50, step=1.)
        Di = Dix * 1e-3
    with col4:''

    print('**SHEATH DATA**')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        xxx = st.number_input('Inner Radius [mm]', format="%.2f", value=62.1, step=1., min_value=.001)
        #s = sx * 1e-3
    with col2:
        xxxx = st.number_input('Outer Radius [mm]', format="%.2f", value=30.00, step=1.)
        #dc = dcx * 1e-3
    with col3:
        material_s = st.selectbox('Sheath  Material', options=["Lead"])#, "Copper", "Aluminum"])



    De = 62.1e-3
    Lcore = 2152e-3


    dc_c = 30.3e-3
    S = 75.5e-3

    # 1 -- Calculation of lay-up factor of the cores
    def flayup(D_e, L_core):
        return sqrt(1 + (pi * 1.29 * D_e / L_core)** 2)

    flayup = flayup(De, Lcore)
    #print(flayup)

    # 2 -- Rac: Calculation of of the conductor Rac at operation temperature
    # - - - DC resistance of conductor - - - - - - - - - - - - - - - - - -
    Rdc20_c = 28.3e-6
    alpha20_c = 3.93e-3
    Rdc_c = Rdc20_c * (1 + alpha20_c * (theta - 20))
    #print(Rdc_c)
    # - - - # Skin effect factor - - -  - - -  - - -  - - -  - - -  - - -
    ks = 1
    xs2 = (8 * pi * f / Rdc_c) * 1e-7
    xs = sqrt(xs2)
    # for 0 < xs <= 2.8:
    ys = divide(xs2 ** 2, 192 + 0.8 * xs2 ** 2)
    #print(xs2)
    #print(ys)
    # - - - Proximity effect factor - - -  - - -  - - -  - - -  - - -  - - -
    kp = 1
    xp2 = (8 * pi * f / Rdc_c) * 1e-7 * kp
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
    Rac = Rdc_c * (1 + 1.5*(ys + yp))
    #print(Rac)


    # 3 -- Calculationn of dielectric losses
    # - - - Capacitance (semi-conducting layers or tapes excluded)
    C_core = divide(epislon, 18 * log(divide(Di, dc2))) * 1e-9
    C = C_core*flayup
    Wd = omega * C * U0 * U0 * tgdelta
    #print(C)
    #print(Wd)


    # 4 -- Loss factor for sheath
    rho20_s = 21.4e-8
    alpha20_s = 4.0e-3
    ds = 52.5e-3

    # Calculation of cross-sectional area of the sheath
    ts = 2.3e-3
    As = pi*ts * (ds+ts)
    #print(As*1e6)
    # Rac_s -- Electrical resistance of the metal sheath at 20°C
    # AC Resistance of the screen at 20oC per unit length of 3-core cable is
    # calculated by taken into consideration the lay-up factor
    Rs20 = flayup * (rho20_s/As)
    #print(rho20_s)
    #print(Rs20*1e4)
    # Operating temperature 𝜃𝑠𝑐 of the screen
    I = 838.3399739336
    T1 = 0.3578707848
    theta_s = theta - (Rac*I**2 + 0.5*Wd)*T1
    #print(theta_s)
    # Lead sheath AC resistance at operating temperature 𝜃𝑠ℎ
    Rs = Rs20 * (1 + alpha20_s * (theta_s - 20))
    #print(Rs*1e4)

    # Calculation of the core reactance
    Dsh = 52.5e-3
    d = Dsh+ts
    #print(d*1e3)
    X1c = 2 * omega * log(divide(2 * s, d)) * 1e-7
    X = flayup*X1c
    #print(X1c*1e5)
    #print(X*1e5)


    # Loss factor "lambda1p" caused by circulating currents on the sheath
    # Note: The impact of armour wires in the conductor losses is taken into consideration with the
    # factor 1.5 in the equation
    lambda1p = divide(Rs, Rac) * divide(1.5, 1 + divide(Rs, X) ** 2)
    #print(lambda1p)
    # Loss factor "lambda1pp" caused by eddy currents on the sheath
    m = (omega/Rs)*1e-7
    lambda0 = 3 * divide(m**2, 1+m**2) * divide(d, 2*s)**2
    print(lambda0)
    #delta1 =




    lambda1pp = 0
    lambda1 = lambda1p #+ lambda1pp




    theta_c = input1
    theta_s = theta_c - 10
    theta_a = input2
    # - - - - - - - - - -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                       RESULTS INDEPENDENT OF THE TEMPERATURE
    # - - - - - - - - - -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -


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


    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    col1, col2 = st.columns(2)


    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    #                     RESULTS DEPENDENT OF THE TEMPERATURE
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -






    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    ##                               ITERATIVE PROCESS
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    # Resistance of sheath at operating temperature




    ## Permissible current rating
    n = 1  # single-core cable
    dtheta = input1-input2
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
    theta_c = theta_s + n * (Wc + Wd/2) * T1 # input1

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

            Rs = Rs20 * (1 + alpha20_s * (theta_s - 20))

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

            delta_I = abs(I - Iguess)
            delta_Ts = abs(theta_s - Ts_guess)
            delta_Tj = abs(theta_j - Tj_guess)

            Iguess = I
            Ts_guess = theta_s
            Tj_guess = theta_j

        else:
            break
            #https://www.tutorialspoint.com/python/python_loop_control.htm#:~:text=The%20continue%20statement%20in%20Python,both%20while%20and%20for%20loops.

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
    col1, col2, col3 = st.columns(3)
    col1.metric("Resistance", value=str(float("{:.4f}".format(1e6*Rac))) + str(' μΩ/m'))
    col2.metric("Capacitance", value=str(float("{:.2f}".format(1e12 * C))) + str(' pF/m'))
    col3.metric("Reactance", value=str(float("{:.2f}".format(1e6 * X))) + str(' μΩ/m'))

    ''
    ''
    ''
    #image1 = Image.open('case0_fig1.jpg')
    #image2 = Image.open('case0_fig2.jpg')
    #image3 = Image.open('cigre_TB880.png')

    #col1, col2, col3 = st.columns([1, 1, 1])
    #with col1:
    #    st.image(image3, caption='Source ', width=200)
    #with col2:
    #    st.image(image1, caption='Case 1 - Underground Cable', width=175)
    #with col3:
    #    ''
    #    ''
    #    st.image(image2, caption='Case 1 - Cross-Section', width=250)



    #col1.metric("DC resistance of core conductor [90°C]",
    #            value=str(float("{:.4f}".format(0 * Rs0))) + str(' mΩ/m'))
    #col2.metric("AC resistance of core conductor [90°C]", value=str(float("{:.4f}".format(0))) + str(' Km/W'))
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -


with tab2:

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