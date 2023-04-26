import streamlit as st
from PIL import Image # create page icon

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SETTINGS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
icon=Image.open('aau_icon.png')
st.set_page_config(page_title="CABOTioN: MoM-SO", layout="centered", page_icon=icon)
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(‘img_file.jpg’);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 50px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "CABOTioN Project";
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

# BACKGROUND IMAGE
#Option 1:Add a Background Image from a URL
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
#add_bg_from_url()

#Option 2: Add a Background Image from Your Computer
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
#add_bg_from_local('blue_bg.png')



#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                     SIDEBAR
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#add_logo()
#st.sidebar.markdown("# MoM-SO")

add_selectbox = st.sidebar.selectbox(
    "MoM-SO", ("Overview", "MoM-SO Formulation", "Examples"))

st.sidebar.image('aau_logo.png', width=150)
st.sidebar.image('ist_logo.png', width=150)
st.sidebar.image('energinet_logo.png', width=200)
st.sidebar.image('orsted_logo.png', width=130)
st.sidebar.image('pscad_logo2.png', width=180)

#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                      INTRODUCTION
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

st.title("MoM-SO: Method of Moments with Surface Operator")

"""
    The Method of Moments (MoM) is a numerical technique to solve integral equations 
    encountered in a vast number of electromagnetic problems. Recently, it was enhanced
    featuring the Surface Operator (SO) concept, thus the so-called MoM-SO formulation,
    introduced to account for ... ? 
        
    The MoM-SO was initially employed for micro-strip modeling [ref. Zutter] and its 
    versatility was later employed for power cable modeling [ref. Patel]. 
    MoM-SO showed to be a very accurate approach to tackle complex configurations encountered
    in power cables with a higher computational efficiency when compared with 
    FEM-based modeling.  
"""




#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                 METHOD OF MOMENTS
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

st.subheader("""Method of Moments (MoM)""")

"""    
MoM-SO computes $R(\omega)$ and $L(\omega)$ by taking as unknown the longitudinal component
of the electric field on the surface of each conductor.
In a compact notation, the electric field $E$ is related to the equivalent surface current $J$
"""

st.latex(r'''
        \begin{gather}
            \mathbf{J} = \mathbf{Y}~\mathbf{E} 
        \end{gather}
    ''')

"""
where $\mathbf{Y}$ is a diagonal matrix describing the surface admittance operator used to replace each  
conductor by an equivalent surface current.
A truncated Fourier series expansion of order $N_p$ allows to collect the Fourier coefficients 
$E_n$ and $J_n$ into two column vectors that are related by the surface admittance operator matrix $\mathbf{Y}$. 
"""

st.latex(r'''
        \begin{gather}
            \mathbf{E} = [E_{-Np} ~\cdots~ E_{0} ~\cdots~ E_{-Np}] \\
            \mathbf{J} = [J_{-Np} ~\cdots~ J_{0} ~\cdots~ J_{-Np}] 
        \end{gather}
    ''')

st.latex(r'''
	\begin{equation}
		\mathbf{Y} =
		\begin{bmatrix}
			Y_{-N_p} &          &       &         &    \\[6pt]
			         &  \ddots  &       &         &    \\[6pt]
			         &          &  Y_0  &         &    \\[6pt]
			         &          &       & \ddots  &    \\[6pt]
			         &          &       &         & Y_{N_p}
		\end{bmatrix}
	\end{equation}
''')
#"""
#The size of vectors $E$ and $J$ defines the total number of basis functions used to discretize the problem.
#"""

#with st.expander('MoM'):
#    ''


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                             SURFACE ADMITTANCE OPERATOR
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

st.subheader("""Surface Admittance Operator""")

"""
    Let a cable consisting up a round conductor surrounded by an insulating medium. 
    The surface admittance operator aims at replacing the metallic conductor by an equivalent 
    current source on the conductor’s boundary. 
    In order to accomplish this, the medium is homogenized by replacing the conductor with 
    the surrounding medium seeking to maintain unchanged the fields outside the conductor.
"""

st.image('mom_2.png', width=700,
         caption='Figure 1 - Equivalence theorem to a solid round conductor')

'The surface admittance operator relates the electric field and the equivalent current source ' \
'obtained from Maxwell’s equations on the boundary of the conductor.'

st.latex(r'''
        \begin{gather}
		Y_n  = \frac{2 \pi}{j \omega} 		
		    \left[
		    \frac{k a_p \mathcal{J}^{\prime}_{|n|} (k a_p)}{\mu \mathcal{J}_{|n|} (k a_p)} - 
		    \frac{k_0 a_p \mathcal{J}^{\prime}_{|n|} (k_0 a_p)}{\mu_0 \mathcal{J}_{|n|} (k_0 a_p)}
		    \right]  
		\end{gather}
    	''')

"""where $a_p$ is the conductor radius, $k$ is the wavenumber inside the conductor and $\mu$ corresponds 
to the magnetic permeability. $\mathcal{J}_{|n|}$ is the Bessel function of order $|n|$ and 
$\mathcal{J}^{\prime}_{|n|}$ its derivative. The index "0" corresponds to properties of the 
surrounding medium."""


with st.expander('Extended Formulation'):
#with st.expander('Surface Admittance Operator'):

    'Let a solid conductor surrounded by an insulating medium as shown in Figure 1.1. ' \
    'The conductor has a radius $a_p$, permittivity $ε$, permeability $\mu$ and conductivity $\sigma$. ' \
    'The medium presents permittivity $ε_0$ and permeability $\mu_0$.'

    col1, col2, col3, col4 = st.columns([1,2,2,1])
    with col1:
        ''
    with col2:
        st.image('mom_4.png', width=190,
                 caption='Figure 1.1a - ???  ')
    with col3:
        st.image('mom_5.png', width=200,
                 caption='Figure 1.1b - ???  ')
    with col4:
        ''

    'Exploiting the cylindrical symmetry, the electric field $E$ on the boundary of the conductor can ' \
    'be expressed by truncated Fourier series of order $n$'

    st.latex(r'''
        \begin{gather} \tag{A1}
            E_z (\theta_p) = \sum_{n=-N_p}^{N_p} E_n~e^{j n \theta_p}
        \end{gather}
            ''')

    'The electric field inside the conductor can be obtained through the Helmholtz equation'

    st.latex(r'''
            \begin{gather} \tag{A2}
                \nabla^2 E_z ( \rho_p, \theta_p) + k^2 E_z ( \rho_p, \theta_p) = 0   
            \end{gather}
            ''')
    'where $k = \sqrt{\omega \mu (\omega ε - j \sigma)}$ is the wavenumber inside the conductor. ' \
    'The solution of this equation is given by'

    st.latex(r'''
            \begin{gather} \tag{A3}
                E_z ( \rho_p, \theta_p) = \sum_{n=-N_p}^{N_p} E_{n}
                \frac{ \mathcal{J}_{|n|} (k \rho_p) }{ \mathcal{J}_{|n|} (k a_p) } ~ e^{j n \theta_p}
            \end{gather}
            ''')

    'where $\mathcal{J}_{|n|}$ is the Bessel function of the first kind of order $|n|$ and $k$ is the wavenumber inside ' \
    'the conductor. Likewise, the equivalent current on the conductor’s boundary can also be expanded through a truncated ' \
    'Fourier series yielding'

    st.latex(r'''
            \begin{gather} \tag{A4}
                 J (\theta_p) = \frac{1}{2 \pi a_p} \sum_{n=-N_p}^{N_p} J_n~e^{j n \theta_p} 
            \end{gather}
            ''')

    'wtih $1/2 \pi a_p$ as a normalization factor.'

    'The equivalence theorem allows to relate the longitudinal electric field and the tangential magnetic ' \
    'field on the conductor’s boundary by'

    st.latex(r'''
            \begin{gather} \tag{A5}
                    J (\theta_p) = \frac{1}{j \omega}	
    		        \left[
    		        \frac{1}{\mu} \frac{\partial E_z}{\partial n} - 
    		        \frac{1}{\mu_0} \frac{\partial \tilde{E}_z}{\partial n}
    		        \right]
            \end{gather}
            ''')

    'where $E_z$ and $\~E_z$ are the electric fields evaluated before and after the equivalence theorem ' \
    'has been applied and $\partial/\partial n$ corresponds to its derivative with respect ' \
    'to the unit vector $n$ normal to the conductor’s surface.'

    'Resorting to the Fourier expansion of the equivalent current source and applying the solution for the ' \
    'electric field in eq.(6-x), it is possible to obtain an expression relating the coefficients $J_n$ and ' \
    '$E_n$ '

    st.latex(r'''
            \begin{gather} \tag{A6}
                \frac{1}{2 \pi a_p} \sum_{n=-N_p}^{N_p} J_n~e^{j n \theta_p} = 
                \sum_{n=-N_p}^{N_p} E_{n}
                \left[
                \frac{k}{\mu} \frac{ \mathcal{J}^{\prime}_{|n|} (k a_p) }{ \mathcal{J}_{|n|} (k a_p) } -
                \frac{k_0}{\mu_0} \frac{ \mathcal{J}^{\prime}_{|n|} (k_0 a_p) }{ \mathcal{J}_{|n|} (k a_p) } 
                \right]
                e^{j n \theta_p}
            \end{gather}
            ''')

    'The method of moments is employed to both sides of eq.(7-x) to determine the coefficients that ' \
    'satisfies the given equality. Finally, it can be demonstrated that'

    st.latex(r'''
            \begin{gather} \tag{A7}
                J_{n} = Y_{n} ~ E_{n}   
            \end{gather}
            ''')

    'where'

    st.latex(r'''
            \begin{gather} \tag{A8}
    		Y_n = \frac{2 \pi}{j \omega} 		
    		\left[
    		\frac{k a_p J^{\prime}_{|n|} (k a_p)}{\mu J_{|n|} (k a_p)} - 
    		\frac{k_0 a_p J^{\prime}_{|n|} (k_0 a_p)}{\mu_0 J_{|n|} (k_0 a_p)}
    		\right]
    		\end{gather}
        	''')

    'for $n=-N_p, ... , N_p$. Here, the so-called surface admittance operator $Y_n$ stands for the ' \
    'relationship between the electric field and the current density for a solid conductor.'


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                         ELECTRIC FIELD INTEGRAL EQUATION
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

st.subheader("""Electric Field Integral Equation""")

"""The electric field integral equation (EFIE) allows one to obtain the equivalent current source 
from the electric field through the following matrix relation
"""
st.latex(r'''
        \begin{gather}
            \mathbf{E} = j \omega \mu_0 ~ \mathbf{G} \mathbf{J} + 
            \mathbf{U} [ \mathbf{R}(\omega) + j \omega \mathbf{L}(\omega) ] \mathbf{I}
        \end{gather}
        ''')

'in which $\mathbf{G}$ corresponds to the discretized Green’s function matrix, $\mathbf{R}$ and $\mathbf{L}$ are the real and imaginary parts of ' \
'the series impedance matrix and $\mathbf{I}$ is the conduction current.' \


with st.expander('Green’s Function'):

    """A second relationship can be established between electric field and current source quantities 
    through the electric field integral equation (EFIE)"""

    st.latex(r'''
        \begin{gather} \tag{B1}
            E_z(\theta_p) = -j \omega A_z(r_p) - \frac {\partial V_p}{\partial z}
        \end{gather}
        ''')
        #E_z(\theta_p) = -j \omega A_z(r_p) - \frac {\partial V_p}{\partial z}

    """ where $V_p$ is the scalar potential and $A_z(r_p)$ is the z-component of the magnetic vector potential 
    that accounts for the field generated by the equivalent current on the contour $c_p$ of p-th conductor 
    given by"""

    st.latex(r'''
            \begin{gather} \tag{B2}
                A_z (r) = -\mu_0 \int_{0}^{2\pi} J(\theta_p)~ G(r, r_p(a_p,\theta_p))~ a_p~ d\theta_p
            \end{gather}
        ''')
        # A_z (r) = -\mu_0 \int_{0}^{2\pi} J_q(\theta_q)~ G(r_p(a_p,\theta_p), r_q(a_q,\theta_q))~ a_q~ d\theta_q

    'where $G(r,r_p)$ is the Green’s function'
    st.latex(r'''
            \begin{gather} \tag{B3}
                G(r,r_p) = \frac{1}{2 \pi} \ln|r-r_p|
            \end{gather}
    ''')

    """
    As defined by the Telegrapher’s equation, the voltage drop term $\partial V_p/ \partial z$ can be substituted 
    by the per-unit-length (p.u.l.) series impedance matrix $Z$ times the vector of impressed current $I$, yielding
    """

    st.latex(r'''
            \begin{gather} \tag{B4}
                E_z(\theta_p) = j \omega \mu_0 \int_{0}^{2\pi} J(\theta_p)~ G(r, r_q(a_p,\theta_p))~ 
                a_p~ d\theta_p + [R(\omega) + j \omega L(\omega)] I
            \end{gather}
            ''')
            #E_z(\theta_p) = j \omega \mu_0 \int_{0}^{2\pi} J_p(\theta_p)~ G(r, r_q(a_p,\theta_p))~ a_p~ d\theta_p + Z I

    """
    wiht $G(r,r_p)$ expressing the relation between an observation point $r$ and the position 
    vector $r_p$ on the p-th conductor’s surface. also known as Green’s function.
    
    As the equivalent current source $J(θ_p)$ in the integrand is a unknown variable, this equation
    can not be evaluated analytically. In order to solve it, the method of moments is employed for 
    discretization into a set of linear equations which requires a prior calculation of matrix $G$.
    """


#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                               SERIES IMPEDANCE
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

st.subheader("""Computation of Series Impedance""")

"""
The p.u.l. parameters can be obtained by combining the two relationships relating the electrical 
field $E$ and the surface current source $J$, yielding
"""
# surface admittance operator $Y_n$ and the electric field integral equation $E$ in their discretized form.

st.latex(r'''
            \begin{gather}
                \mathbf{R}(j \omega) + j \omega \mathbf{L}(j \omega) = 
                [\mathbf{U}^T (\mathbf{1} - j \omega \mu_0 ~ \mathbf{Y} \mathbf{G})^{-1} ~ \mathbf{Y} \mathbf{U}]^{-1}
            \end{gather}
        ''')




with st.expander('Numerical Formulation'):

    'The p.u.l. parameters can be computed by combining the surface admittance operator $Y_n$ ' \
    'and the electric field integral equation $E$ in their discretized form.'

    st.latex(r'''
            \begin{gather} \tag{C1}
                J = Y E \\
                E = j \omega \mu_0 ~ G J +  U Z I
            \end{gather}
        ''')

    'Multiplying eq.(11-x) by $Y_n$ on both sides a rearranging like terms '

    st.latex(r'''
        \begin{gather} \tag{C2}
            J = (1 - j \omega \mu_0 ~ Y G)^{-1} ~ Y U Z I
        \end{gather}
            ''')

    'where $1$ is the identity matrix. Resorting to the relation $I=U^T J$ between the equivalent and ' \
    'conduction currents, the left multiplication of eq.(12-x) leads to'

    st.latex(r'''
        \begin{gather} \tag{C3}
            I = [U^T (1 - j \omega \mu_0 ~ Y G)^{-1} ~ Y U Z] I
        \end{gather}
            ''')

    'To ensure the validity of eq.(13-x), the term inside brackets must be equal to the identity matrix, ' \
    'yielding '

    st.latex(r'''
            \begin{gather} \tag{C4}
                Z = [U^T (1 - j \omega \mu_0 ~ Y_n G)^{-1} ~ Y U]^{-1}
            \end{gather}
        ''')

    'where the real and imaginary parts of eq.(13-x) correspond to the resistance and reactance matrices.'



#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                               MATRIX G
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

st.subheader("""Computation of G Matrix""")

"""
Considering the general case given by P solid conductors, the magnetic potential vector $A$ 
can be expanded using the superposition principle to account for the contribution for all conductors
"""

st.latex(r'''
            \begin{gather}
                A_z(r) = \sum_{q = 1} ^ {P} A_q(r)
            \end{gather}
        ''')

"""
resulting the EFIE in the following form  
"""


st.latex(r'''
        \begin{gather}
		\begin{split}
            \sum_{n=-N_p}^{N_p} E_n~e^{j n \theta_p} &= \frac{j \omega \mu_0}{2 \pi} J^{(q)}_{n} 
            \sum_{q=1}^{P} \sum_{n=-N_p}^{N_p} \int_{0}^{2\pi} 
            e^{j n \theta_q} ~ G(r_p(a_p,\theta_p), r_q(a_q,\theta_q))~d\theta_q \\
            &+ \sum_{q=1}^{P} [\mathbf{R}_{pq}(\omega) + j \omega \mathbf{L}_{pq}(\omega)] I_q
		\end{split}
        \end{gather}
        ''')

"""Applying the method of moments to discretize the above equation"""

st.latex(r'''
        \begin{gather}		
            E^{(p)}_{n^{\prime}} &= j \omega \mu_0 \sum_{q=1}^{P} \sum_{n=-N_p}^{N_p}
             G^{(p,q)}_{n^{\prime},n} J^{(q)}_{n}
            + \delta_{n^{\prime},0} \sum_{q=1}^{P} [R_{pq}(\omega) + j \omega L_{pq}(\omega)] I_q
		\end{gather}
        ''')

'for $p=1, ~.~.~.~, P$, where'

st.latex(r'''
        \begin{equation}
        \delta_{n^{\prime},0} =
            \begin{cases}
            1, & when \; n^{\prime} = 0 \\
            0, & when \; n^{\prime} \neq 0 
        \end{cases}
        \end{equation}
        ''')

"""
and $G^{(p,q)}_{n^{\prime},n}$ stands for the $(n^{\prime},n)$ entry fo the $G^{(p,q)}$ matrix.
This matrix describes the contribution of the current on the $qth$ conductor to the field 
on the $pth$ conductor.
The entries of $G^{(p,q)}$ are given by the double integral
"""

st.latex(r'''
        \begin{gather}
		\begin{split}
		    \mathbf{G}^{(p,q)}_{n^{\prime},n} = \frac{1}{(2 \pi)^2} 
            \int_{0}^{2\pi} \int_{0}^{2\pi} 
           G(r_p(\theta_p), r_q(\theta_q))~ e^{j (n \theta_q - n^{\prime} \theta_p)} d\theta_p d\theta_q 
		\end{split}
        \end{gather}
        ''')

"""
'which can be computed analytically.
Using the matrix notation, the EFIE equation can be written in compact form as
"""

st.latex(r'''
        \begin{gather}
            \mathbf{E} = j \omega \mu_0 ~ \mathbf{G} \mathbf{J} 
            + \mathbf{U} [ \mathbf{R}(j \omega) + j \omega \mathbf{L}(j \omega) ] \mathbf{I}
        \end{gather}
        ''')

'where $G$ is the block matrix'

st.latex(r'''
	\begin{equation}
		\mathbf{G} =
		\begin{bmatrix}
			G^{(1,1)}  &  \cdots   &   G^{(1,P)}      \\[6pt]
			\vdots     &  \ddots   &   \vdots         \\[8pt]
			G^{(P,1)}  &  \cdots   &   G^{(P,P)}
		\end{bmatrix}
	\end{equation}
''')


with st.expander('Detailed Description'):


    st.latex(r'''
            \begin{gather}
                \mathbf{G}^{(p,q)}_{n^{\prime},n} =
                \begin{bmatrix}
                \\[-6pt]
                    \begin{bmatrix}
                        G^{(1,1)}_{-1,-1} & G^{(1,1)}_{-1,0} & G^{(1,1)}_{-1,1} \\[9pt]
                        G^{(1,1)}_{0,-1} & G^{(1,1)}_{0,0} & G^{(1,1)}_{0,-1} \\[9pt]
                        G^{(1,1)}_{1,-1} & G^{(1,1)}_{1,0} & G^{(1,1)}_{1,1} \\
                    \end{bmatrix}~
                    \begin{bmatrix}   
                        G^{(1,2)}_{-1,-1} & G^{(1,2)}_{-1,0} & G^{(1,2)}_{-1,1} \\[9pt]
                        G^{(1,2)}_{0,-1} & G^{(1,2)}_{0,0} & G^{(1,2)}_{0,-1} \\[9pt]
                        G^{(1,2)}_{1,-1} & G^{(1,2)}_{1,0} & G^{(1,2)}_{1,1} \\
                    \end{bmatrix}\\\\ 
                    \begin{bmatrix} 
                        G^{(2,1)}_{-1,-1} & G^{(2,1)}_{-1,0} & G^{(2,1)}_{-1,1} \\[9pt]
                        G^{(2,1)}_{0,-1} & G^{(2,1)}_{0,0} & G^{(2,1)}_{0,-1} \\[9pt]
                        G^{(2,1)}_{1,-1} & G^{(2,1)}_{1,0} & G^{(2,1)}_{1,1} \\
                    \end{bmatrix}~
                    \begin{bmatrix}
                        G^{(2,2)}_{-1,-1} & G^{(2,2)}_{-1,0} & G^{(2,2)}_{-1,1} \\[9pt]
                        G^{(2,2)}_{0,-1} & G^{(2,2)}_{0,0} & G^{(2,2)}_{0,-1} \\[9pt]
                        G^{(2,2)}_{1,-1} & G^{(2,2)}_{1,0} & G^{(2,2)}_{1,1} \\
                    \end{bmatrix} 
                \end{bmatrix}
            \end{gather}
            ''')












#The $G$ matrix is the discretization of the Green’s function and its entries are given by a
#double integral that can be solved analytically.
''
''
''
''
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#                                   REFERENCES
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
'#### References'
'[Patel2013] U. R. Patel, B. Gustavsen and P. Triverio, "An Equivalent Surface Current Approach for the Computation of the Series Impedance of Power Cables with Inclusion of Skin and Proximity Effects," in IEEE Transactions on Power Delivery, vol. 28, no. 4, pp. 2474-2482, Oct. 2013, doi: 10.1109/TPWRD.2013.2267098.'
'[Patel2014a] U. R. Patel, B. Gustavsen and P. Triverio, "Proximity-Aware Calculation of Cable Series Impedance for Systems of Solid and Hollow Conductors," in IEEE Transactions on Power Delivery, vol. 29, no. 5, pp. 2101-2109, Oct. 2014, doi: 10.1109/TPWRD.2014.2330994.'
'[Patel2014b] U. R. Patel, Master Thesis, "A Surface Admittance Approach For Fast Calculation of the Series Impedance of Cables Including Skin, Proximity, and Ground Return Effects".'
'[Patel2015] U. R. Patel and P. Triverio, "MoM-SO: A Complete Method for Computing the Impedance of Cable Systems Including Skin, Proximity, and Ground Return Effects," in IEEE Transactions on Power Delivery, vol. 30, no. 5, pp. 2110-2118, Oct. 2015, doi: 10.1109/TPWRD.2014.2378594.'
'[Patel2016a] U. R. Patel and P. Triverio, "Accurate Impedance Calculation for Underground and Submarine Power Cables Using MoM-SO and a Multilayer Ground Model," in IEEE Transactions on Power Delivery, vol. 31, no. 3, pp. 1233-1241, June 2016, doi: 10.1109/TPWRD.2015.2469599.'
'[Patel2016b] B. Gustavsen, M. Høyer-Hansen, P. Triverio and U. R. Patel, "Inclusion of Wire Twisting Effects in Cable Impedance Calculations," in IEEE Transactions on Power Delivery, vol. 31, no. 6, pp. 2520-2529, Dec. 2016, doi: 10.1109/TPWRD.2016.2531125.'


#	where $E_z (\theta_p)$ is the electric field on the boundary $c_p$.

#image = Image.open('mom_1.png')
#st.image(image, caption='Figure 1 - Equivalence theorem to a solid round conductor')


#st.write('The unknown function is approximated by a finite series of known '
#        'expansion functions with unknown expansion coefficients.')

#st.write("""
#        Surface operaator concept relates the electric field and the equivalent
#        current sources through the electric field integral equation (EFIE) ...
#
#        ### Overview
#        - Initially employed for micro-strip modeling
#        - Applied for power cable modeling in the early 2010s
#        - Fast and accurate approach to tackle complex configurations
#""")


# As a result, matrix $G$ needs to be calculated
# st.latex(r'''
#    G_{(n\prime,n)} = \frac{1}{(2\pi)^2}
#	''')


