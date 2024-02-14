import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Assuming the NelsonSiegel class is defined elsewhere and imported here
from nelson_siegel import NelsonSiegelSvensson

# Streamlit UI
st.title("Interactive Nelson-Siegel Yield Curve Model")

# Slider for parameters
beta0 = st.slider("Beta0", min_value=-0.10, max_value=0.10, value=0.045, step=0.005)
beta1 = st.slider("Beta1", min_value=-0.10, max_value=0.10, value=-0.015, step=0.005)
beta2 = st.slider("Beta2", min_value=-0.1, max_value=0.1, value=-0.005, step=0.005)
beta3 = st.slider("Beta3", min_value=-0.1, max_value=0.1, value=0.0, step=0.005)
tau1 = st.slider("Tau1", min_value=0.5, max_value=20.0, value=1.0, step=0.01)
tau2 = st.slider("Tau2", min_value=0.5, max_value=20.0, value=2.0, step=0.01)
n_max = 30 * 12  # Maximum maturity in months (30 years)

# Button to plot the curve

# Create an instance of NelsonSiegel with the selected parameters
obj = NelsonSiegelSvensson([beta0, beta1, beta2, tau1, beta3, tau2], n_max)

# Assuming your plot_curve method generates and shows a plot directly
obj.plot_curve()



# streamlit run C:\Users\Sébastien\Documents\Nelson_siegel\app.py
# streamlit run \Users\sebastiencaron\Desktop\Fixed-Income\Cours 4 Nelson_siegel\app.py
# streamlit run app.py