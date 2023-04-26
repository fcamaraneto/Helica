import streamlit as st
from PIL import Image # create page icon

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SETTINGS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#icon=Image.open('comsol.png')
icon=Image.open('aau_icon.png')
st.set_page_config(page_title="CABOTioN: FEM Modeling", layout="centered", page_icon=icon)

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
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
#                                     FEM
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
st.markdown("# Finite Element Modeling (FEM)")
#st.sidebar.markdown("# FEM ")

st.markdown('Finite element modeling (FEM) comprises a class of numerical methods employed to solve partial '
            'differential equations and plays an important role in the numerical simulation of real systems. '
            'It is widely used to evaluate the behavior of devices and systems before they are built, since it '
            'provides approximate solutions without significant loss of accuracy. It also helps to provide '
            'fundamental insights for real problems through the power of computation and visualization,'
            ' making it one of the most important areas of engineering today. In a few words, it is a reliable '
            'evaluation environment because it is able to handle complex geometries that occur in real life.')

st.markdown('The goal is to establish a model that will serve as the reference framework for validation of the '
            'proposed formulation for calculating the electrical parameters to be developed in this research.')


st.markdown("""### Reference Framework""")

st.markdown('A PhD thesis conducted at Aalborg University investigated the COBRAcable Interconnector with the aim '
            'of proposing a novel control philosophy to allow point-to-point (PtP) HVDC links in operation to be '
            'upgraded to a multi-terminal transmission system -x-x-x-x-\cite{phd_roni}-x-x-x-x-. However, in the '
            'studies performed,an underground model was used, which was the only one available in the cable parameter '
            'routines embeded in EMT-type software and no sensitivity analysis was performed in terms of cable '
            'parameter variability on the achieved results. With this in mind, COBRAcable is the right framework '
            'as a starting point for the CABOTioN project.')

st.markdown('COBRAcable Interconnector is a 325 km submarine HVDC link between Denmark and the Netherlands '
            'and was built to provide a high level of security of electricity supply to both countries, see '
            'Fig. \ref{fig:cobracable}. Due to the extensive deployment of renewable power generation, the '
            'interconnection will provide an opportunity to share surplus renewable energy in both countries and '
            'also promote a pathway for connecting future offshore wind farms in the North Sea. '
            'In addition, COBRAcable is expected to be part of a future interconnected offshore grid between the '
            'countries bordering the North Sea.')

st.markdown('The HVDC submarine cable initially considered for numerical modeling is the cable used '
            'in COBRAcable and COMSOL software will be tool employed ')

image = Image.open('cobracable_scheme.png')
st.image(image, caption='COBRAcable Interconnector [ref]')
# [COBRAcable](https://en.energinet.dk/Infrastructure-Projects/Projektliste/COBRAcable)

