# https://blog.streamlit.io/introducing-multipage-apps/

import streamlit as st
from PIL import Image # create page icon
#from streamlit_extras.app_logo import add_logo
import streamlit.components.v1 as components

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SETTINGS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
icon=Image.open('dnv_logo.jpg')
st.set_page_config(page_title="HELICA Multiphysics", layout="centered", page_icon=icon)

#-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SIDEBAR
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

#add_logo("https://i.ibb.co/z6v0zDn/dnv-logo.jpg")



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
add_logo()

#st.sidebar.image('dnv_logo.jpg', width=150)



st.header("Umbilical, cable and flexible pipe analysis")



with st.sidebar.container(): 
    image = Image.open('helica_back.jpg')
st.image(image)

st.markdown('### Consistent, highly efficient and robust stress and fatigue analysis of umbilicals, cables and flexible risers in subsea applications')



# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Module:",
    ("Cross-section",
     "Fatigue",
     "VIV"))
# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -



st.markdown('The Helica software module in Sesam includes technology that represents industry consensus for cross section analysis of umbilicals and flexible risers, including fatigue analysis of section components such as helix wires and steel tubes. Using Helica, subsea engineers can reduce the analysis time to a fraction, as thousands of simulations may be performed in minutes. ')

st.markdown('### Cross-section and fatigue analysis')
st.markdown('Helica is tailor-made software for cross-section analysis of flexible pipes and umbilicals and is validated against high quality stress measurements in a full-scale subsea umbilical.')


st.markdown('### Stresses in dynamic umbilicals and flexible pipes')
st.markdown('Accurate evaluation of local stresses in complex cross-sections, e.g. of subsea umbilicals and flexible pipes, '
            'subjected to extreme and fatigue loading, is a challenge to the industry. Fatigue of cross-section components such '
            'as helix tensile armors and steel tubes is a critical design issue for dynamic umbilicals and flexible pipes.')
st.markdown('The basis for assessment of fatigue damage of such elements is the long-term stress cycle distribution at critical locations on the helix '
            'elements caused by long-term environmental loading on the system. The long-term stress cycle distribution will therefore require '
            'global dynamic time domain analysis followed by a detailed cross-section analysis in a large number of irregular sea states.')
st.markdown('Helica is a vital component in an overall computational consistent and highly efficient fatigue analysis scheme.')


#st.markdown('## Main functionalities:')
st.markdown('### Key features')
st.markdown("""
    - Cross-sectional load sharing analysis
    - Short-term fatigue analysis
    - Long-term fatigue analysis
    - Extreme analysis
    - Load-sharing between elements
    - Calculation of cross-sectional stiffness properties
    - Evaluation of stick/slip behaviour due to interlayer frictional forces
    - Stresses in selected components due to combined bending and tensile loading
    - Assessment of capacity curves for combined bending and tensile loading of the cross section
    - Validation against high quality stress measurements in full-scale tests of umbilicals
    - Compatible with result files (time series) generated by global analysis software such as Orcaflex, Riflex and Flexcom
    """)




Project description at [CORDIS database](https://www.dnv.com/services/umbilical-analysis-and-flexible-pipe-analysis-helica-69553)
