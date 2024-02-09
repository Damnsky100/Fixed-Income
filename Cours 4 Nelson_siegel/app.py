import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Assuming the NelsonSiegel class is defined elsewhere and imported here
from nelson_siegel import NelsonSiegelSvensson

# Streamlit UI
st.title("Interactive Nelson-Siegel Yield Curve Model")

# Slider for parameters
beta0 = st.slider("Beta0", min_value=-0.1, max_value=0.1, value=0.07, step=0.01)
beta1 = st.slider("Beta1", min_value=-0.1, max_value=0.1, value=-0.03, step=0.01)
beta2 = st.slider("Beta2", min_value=-0.1, max_value=0.1, value=0.0, step=0.01)
beta3 = st.slider("Beta3", min_value=-0.1, max_value=0.1, value=0.0, step=0.01)
tau1 = st.slider("Tau1", min_value=0.5, max_value=20.0, value=2.0, step=0.1)
tau2 = st.slider("Tau2", min_value=0.5, max_value=20.0, value=2.0, step=0.1)
n_max = 30 * 12  # Maximum maturity in months (30 years)

# Button to plot the curve

# Create an instance of NelsonSiegel with the selected parameters
obj = NelsonSiegelSvensson([beta0, beta1, beta2, tau1, beta3, tau2], n_max)

# Assuming your plot_curve method generates and shows a plot directly
obj.plot_curve()


# streamlit run C:\Users\Sébastien\Documents\Nelson_siegel\app.py