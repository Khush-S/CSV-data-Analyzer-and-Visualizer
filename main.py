import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title of the app
st.title("CSV Data Analyzer and Visualizer")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the CSV file into a pandas DataFrame, only the first 100 rows
    try:
        df = pd.read_csv(uploaded_file, nrows=100)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        df = None
    
    if df is not None:
        # Show basic information about the dataset
        st.write("### Data Preview (First 100 Rows):")
        st.write(df.head())  # Show first 5 rows of the DataFrame
        
        # Show basic stats of the dataset
        st.write("### Data Statistics:")
        st.write(df.describe())  # Statistical summary of the dataset

        # Ensure that there are enough columns to plot
        if len(df.columns) > 1:
            # Select columns for plotting
            columns = df.columns.tolist()
            x_axis = st.selectbox("Select X-axis", columns)
            y_axis = st.selectbox("Select Y-axis", columns)

            # Additional plots based on user choice
            plot_type = st.selectbox("Choose plot type", ["Scatter", "Line", "Bar", "Histogram"])

            if plot_type == "Scatter":
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter plot of {x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            elif plot_type == "Line":
                fig = px.line(df, x=x_axis, y=y_axis, title=f"Line plot of {x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            elif plot_type == "Bar":
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"Bar plot of {x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            elif plot_type == "Histogram":
                fig = px.histogram(df, x=x_axis, title=f"Histogram of {x_axis}")
                st.plotly_chart(fig)
        else:
            st.write("### Not enough columns to create plots.")
else:
    st.write("Please upload a CSV file to begin.")
