import streamlit as st
import pandas as pd
import plotly.graph_objects as go


enrollment_2019 = pd.read_csv("../data/texas/2019/Statewide Totals/Grade/Enrollment Report_Statewide_Grade_2018-2019.csv")
enrollment_2020 = pd.read_csv("../data/texas/2020/Statewide Totals/Grade/Enrollment Report_Statewide_Grade_2019-2020.csv")


enrollment_2019


st.title("Student Enrollment Report")
st.markdown(
"""
This app is for visualizing the High School enrollment for various States and years. 
"""
)

st.markdown("## " + 'Total Enrolled users ')
st.markdown("#### " +"What years would you like to see?")
selected_metrics = st.selectbox(
    label="Choose...", options=['2018-2019','2019-2020']
)
st.markdown("#### " +"What Demographics would you like to view?")
demographics = st.selectbox(
    label="Choose...", options=['Ethnicity','Sex']
)


# Create traces
fig = go.Figure()
if selected_metrics == '2018-2019':
	fig.add_trace(go.Scatter(x=enrollment_2019.GRADE, y=enrollment_2019.ENROLLMENT,
                    mode='lines',
                    name='Enrollment'))

if selected_metrics == '2019-2020':
	fig.add_trace(go.Scatter(x=enrollment_2020.GRADE, y=enrollment_2020.ENROLLMENT,
                    mode='lines',
                    name='Enrollment'))
st.plotly_chart(fig, use_container_width=True)


st.sidebar.title("State-Wise Data")
State_list = st.sidebar.selectbox(
    'state',
    ["Texas", "Alabama"])

st.sidebar.title("Compare With:")
State_list = st.sidebar.selectbox(
    'state',
    ["California", "New York"])


# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0, 12, (1, 4)
)