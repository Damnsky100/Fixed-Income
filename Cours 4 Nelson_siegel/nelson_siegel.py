
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import streamlit as st



class NelsonSiegelSvensson:
    def __init__(self, df, n_max) -> None:
        self.df = df
        self.n_max = n_max  
          
    @staticmethod
    def nelson_siegel(n, tau1, beta0, beta1, beta2, beta3: float = 0, tau2 : float = 0):
        part1 = beta0
        part2 = beta1 * (1 - math.exp(-n / tau1)) / (n / tau1)  # beta1 * (1- math.exp(-n/tau1)) / (n / tau1)
        part3 = beta2 * (((1 - math.exp(-n / tau1)) / (n / tau1)) - math.exp(
            -n / tau1))  # beta2 *(((1- math.exp(-n/tau1)) / (n / tau1))  - math.exp(-n / tau1))
        part4 = beta3 * (((1 - math.exp(-n / tau2)) / (n / tau2)) - math.exp(-n / tau2))
        total = part1 + part2 + part3 + part4

        return [part1, part2, part3, part4, total]

    def get_curve(self, tau1, beta0, beta1, beta2, beta3, tau2, n_range):
        """

        Args:
            tau1 (_type_): _description_
            beta0 (_type_): _description_
            beta1 (_type_): _description_
            beta2 (_type_): _description_
            n_range (_type_): _description_
            
        Output : 1 x n_range
        
        """
        result = np.zeros(n_range-1)
        part1 = np.zeros(n_range-1)
        part2 = np.zeros(n_range-1)
        part3 = np.zeros(n_range-1)
        part4 = np.zeros(n_range - 1)
        for n in range(1, n_range):
            
            n_step = n/12
            part1[n-1], part2[n-1], part3[n-1], part4[n-1], result[n-1] = self.nelson_siegel(n_step, tau1, beta0, beta1, beta2, beta3, tau2)
            
        
        return (part1, part2, part3, part4, result)


    def plot_curve(self):
        beta0, beta1, beta2, tau1, beta3, tau2  = self.df
        
        part1, part2, part3, part4, result = self.get_curve(tau1, beta0, beta1, beta2, beta3, tau2, self.n_max)
        time_steps = np.arange(1, self.n_max) / 12 
        # Plot each curve
        
        
        plt.figure(figsize=(10, 6))  # Create a new figure for each plot
        plt.plot(time_steps, result, label=f'Yield Curve')
        plt.title(f'Nelson-Siegel Yield Curve')
        plt.xlabel('Time (Years)')
        plt.ylabel('Nelson-Siegel Result')
        plt.legend()
        st.pyplot(plt.gcf())
        
        
        plt.figure(figsize=(10, 6))
        plt.plot(time_steps, part1, label = "Equilibrium")
        plt.plot(time_steps, part2, label = "Beta1")
        plt.plot(time_steps, part3, label = "Beta2")
        plt.plot(time_steps, part4, label="Beta3")
        plt.title(f'Décomposition Nelson-Siegel Yield Curve')
        plt.xlabel('Time (Years)')
        plt.ylabel('Nelson-Siegel Result')
        plt.legend()
        st.pyplot(plt.gcf())
