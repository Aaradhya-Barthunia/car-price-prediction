import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Import the individual Python files
import home
import data
import plots
import predict
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_squared_log_error
def app(car_df):
    st.header('Visualised Data')
    # Remove deprecation warning.
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Subheader for scatter plot.
    st.subheader('Scatter Plot')
    
    # Choosing x-axis values for scatter plots."Select the x-axis values:",  ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
    features_list = st.multiselect("Select the x-axis values:",  ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))


    # Create scatter plots.
    for feature in features_list:
        st.subheader(f"Scatter plot between {feature} and price")
        plt.figure(figsize = (12, 6))
        sns.scatterplot(x = feature, y = 'price', data = car_df)
        st.pyplot()
    # Add a multiselect widget to allow the user to select multiple visualisation.
    # Add a subheader in the sidebar with label "Visualisation Selector"
    st.subheader('Visualisation Selector')
    
    # Add a multiselect in the sidebar with label 'Select the charts or plots:'
    # and pass the remaining 3 plot types as a tuple i.e. ('Histogram', 'Box Plot', 'Correlation Heatmap').
    # Store the current value of this widget in a variable 'plot_types'.
    plot_types = st.multiselect('Select the charts or plots:', ('Histogram', 'Box Plot', 'Correlation Heatmap'))

    # Display box plot using the 'matplotlib.pyplot' module and the 'st.pyplot()' function.
    if 'Histogram' in plot_types:
        st.subheader("Histogram")
        columns = st.selectbox("Select the column to create its histogram",
                                      ('carwidth', 'enginesize', 'horsepower'))
        # Note: Histogram is generally created for continuous values not for discrete values.
        plt.figure(figsize = (5, 5))
        plt.title('Histogram')
        plt.hist(car_df[columns], bins = 'sturges')
        st.pyplot()
    # Create box plot using the 'seaborn' module and the 'st.pyplot()' function.
    if 'Box Plot' in plot_types:
        st.subheader("Box Plot")
        columns = st.selectbox("Select the column to create its box plot",
                                      ('carwidth', 'enginesize', 'horsepower'))
        sns.boxplot(car_df[columns])
        st.pyplot()
    # Display correlation heatmap using the 'seaborn' module and the 'st.pyplot()' function.
    if 'Correlation Heatmap' in plot_types:
        st.subheader("Correlation Heatmap")
        plt.figure(figsize = (8, 5))
        ax = sns.heatmap(car_df.corr(), annot = True) # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim() # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5) # Increasing the bottom and decreasing the bottom margins respectively.
        st.pyplot()