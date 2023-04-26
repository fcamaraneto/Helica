# https://blog.streamlit.io/introducing-multipage-apps/

import streamlit as st
from PIL import Image # create page icon
import streamlit.components.v1 as components

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SETTINGS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
icon=Image.open('aau_icon.png')
st.set_page_config(page_title="CABOTioN", layout="centered", page_icon=icon)

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


#with st.sidebar.container():
#    image = Image.open('eu_logo.jpg')
#st.image(image)

# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Additional information:",
    ("Work Packages",
     "Upcoming HVDC Projects",
     "Other"))

st.sidebar.image('aau_logo.png', width=150)
st.sidebar.image('ist_logo.png', width=150)
st.sidebar.image('energinet_logo.png', width=200)
st.sidebar.image('orsted_logo.png', width=130)
st.sidebar.image('pscad_logo2.png', width=180)
# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#st.markdown("# CABOTioN Project")
#st.sidebar.markdown("# CABOTioN ")
# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#st.header('This is a header')
#st.title('This is a title')


st.header("CABOTioN Project")

#st.markdown('### Summary')
st.markdown('A sustainable energy network must comply with the usage of offshore wind farms and the sharing of surplus '
            'renewable energy without a dangerous carbon footprint. Amongst the possible technologies to foster the '
            'energy transition one way is to rely on HVDC transmission resorting to submarine cables for energy '
            'transfer. However, field measurements show the lack of confidence in simulation results with regard to '
            'the voltage and current profiles on the core, sheath or armour. A proper representation of the magnetic '
            'behaviour of the armour and the impact of the sea and seabed for an overall assessment of the transient '
            'behaviour remain a challenge.')

st.markdown('### Project description')
st.markdown('The EU-funded CABOTioN project fosters the deployment of offshore interconnections and energy islands '
            'in Europe, by addressing the challenge of modelling high voltage direct current (HVDC) submarine cables. '
            'As HVDC submarine cables are quite complex, the project proposes the design of an innovative '
            'special-purpose tool to compute cable parameters, to allow a straightforward and systematic '
            'implementation as a reliable digital twin. This will increase the confidence of evaluations, '
            'by avoiding simplifications due to the lack of accurate models for the assessment of transient and '
            'steady-state behaviour involving offshore energy transmission. CABOTioN will contribute to the '
            'development of cost-effective green projects by helping to find new and more economical ways of '
            'building HVDC offshore transmission networks.')

st.markdown('### Objectives')
st.markdown('The overall objective of CABOTioN is the development of an innovative approach for identification of '
            'per-unit-length parameters of submarine DC cables and a straightforward interface with simulation tools. '
            'The applicant will resort to up-to-date formulations to design a special-purpose tool to compute '
            'electrical parameters considerably faster than the Finite Element Method without a significant '
            'loss of accuracy. Therefore, evaluations will be conducted to assess the enhancements achieved with '
            'a more accurate model and compared with the common practice and measurements.')
st.markdown("""
    - Develop a computational tool for parameter computation of power cables
    - Investigate special cable design configurations not addressed
    - Verification of ...
    """)



st.markdown("""
    ### Supervision
    - Prof. Filipe Faria da Silva (Aalborg University)
    - Prof. Claus Leth Bak (Aalborg University)         
    - Profa. Maria Teresa Correia de Barros (Instituto Superior Técnico / Lisbon University) 
    - Prof. Antonio Carlos Siqueira de Lima (Federal University of Rio de Janeiro)
    """)

st.markdown("""
    ### Grant
    This project has received funding from the European Union’s Horizon 2020 research and innovation programme 
    under the Marie Skłodowska-Curie grant agreement No 101031088 ([CORDIS](https://cordis.europa.eu/project/id/101031088))”.     
    """)

st.markdown('<a href="/02_MoM-SO.py" target="_self">Next page</a>', unsafe_allow_html=True)


# - Marie-Curie Postdoctoral Fellowship
#     - HORIZON 2020: EU-funded research project
#     - Project description at [CORDIS database](https://cordis.europa.eu/project/id/101031088)
#     - Grant agreement: 101031088
#     - Duration: September 2021 - August 2023
