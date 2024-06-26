##https://docs.streamlit.io/library/api-reference/data/st.dataframe
#importing libraries
from numpy import double
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

#Assigning page title as Titanic Dashboard and favicon
st.set_page_config(page_title="Titanic Dashboard",page_icon="🚢",layout="wide")
st.sidebar.success("Select a demo above.")
#taking input from function
df = pd.read_csv(r"C:\Users\ASUS\Documents\train.csv")

#Assigning page title as Titanic Dashboard
st.title("🚢 Titanic Data Analysis Dashboard")
st.markdown("##")

#making 
#Passenger belonging to Embarked % (Pie Chart
pie_chart = px.pie(names = df["Embarked"].unique(),values=df.groupby("Embarked")["Embarked"].count(),hole=0.5)
#Box plot Based on Pclass vs age
box_plot = px.box(df, y="Age",x="Pclass")
#Survival Histogram based on Pclass
group_plot = px.histogram(df, x="Survived", color="Pclass",barmode='group') 

#making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)

#showing data in left col
#Number of Fist class Passenger Survived
#Number of Second class Passenger Survived
#Number of Second class Passenger Survived
with left_column:
    st.subheader(f" Fist class Passenger Deaths: {len(df.loc[(df['Pclass'] == 1) & (df['Survived'] == 0)])}")
    st.subheader(f"Second class Passenger Deaths: {len(df.loc[(df['Pclass'] == 2) & (df['Survived'] == 0)])}")
    st.subheader(f"Third class Passenger Deaths: {len(df.loc[(df['Pclass'] == 3) & (df['Survived'] == 0)])}")
    
#showing data in middle col
#Number of Fist class Passenger Deaths
#Number of Second class Passenger Deaths
#Number of Third class Passenger Deaths

with middle_column:
    st.subheader(f"Fist class Passenger Survived : {len(df.loc[(df['Pclass'] == 1) & (df['Survived'] == 1)])}")
    st.subheader(f"Second class Passenger Survived: {len(df.loc[(df['Pclass'] == 2) & (df['Survived'] == 1)])}")
    st.subheader(f"Third class Passenger Survived: {len(df.loc[(df['Pclass'] == 3) & (df['Survived'] == 1)])}")

#showing data in right col
#Average Fare Value
#Average Fare Tax 
#Average Luggage Charges Value

with right_column:
    st.subheader(f"Average Fare Value: {int(df['Fare'].mean())}")
    st.subheader(f"Average Fare Tax : {int(df['Fare_Tax'].mean())}")
    st.subheader(f"Average Luggage Charges Value: {int(df['Luggage Charges'].mean())}")
    
    
st.markdown('---')

#making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)

#assigning heading to each columns
with left_column:
    st.subheader("Passenger belonging to Embarked % (Pie Chart)")
with middle_column:
    st.subheader("Survival Histogram based on Pclass")
with right_column:
    st.subheader("Box plot Based on Pclass vs age")

st.markdown("---")
# ploting Passenger belonging to Embarked % (Pie Chart)
left_column.plotly_chart(pie_chart,use_container_width=True)

# ploting Survival Histogram based on Pclass
right_column.plotly_chart(box_plot,use_container_width=True)

#Box plot Based on Pclass vs age
middle_column.plotly_chart(group_plot,use_container_width=True)


#MakingLine plot for Fare_Tax,Luggage Charges,Food Charges
plot = px.histogram(df, x="SibSp",color="Sex",barmode='group')
#Making Survival Histogram Based on Sex
group_plot1 = px.histogram(df, x="Survived", color="Sex",barmode='group') 
#Making Survival Rate %(Pie Chart)
pie_chart1 = px.pie(names = df["Survived"].unique(),values=df.groupby("Survived")["Survived"].count(),hole=0.5)


#making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)

#assigning heading to each columns
with left_column:
    st.subheader("Histogram of Sibsp")
with middle_column:
    st.subheader("Survival Histogram Based on Sex")
with right_column:
    st.subheader(" Survival Rate %(Pie Chart)")


st.markdown("---")
#Ploting Line plot for Fare_Tax,Luggage Charges,Food Charges
left_column.plotly_chart(plot,use_container_width=True)

#Making Survival Rate %(Pie Chart)
middle_column.plotly_chart(group_plot1,use_container_width=True)

#Making Survival Rate %(Pie Chart)
right_column.plotly_chart(pie_chart1,use_container_width=True)



group_plot1 = px.histogram(df, x='Sex', y= 'Survived', color='Pclass',barmode='group' )
group_plot2 = px.histogram(df, x='Sex', y= 'Survived', color='Pclass',barmode='stack' )

left_column, middle_column, right_column = st.columns(3)
#ploting Histogram of Sibsp
with left_column:
    st.subheader("Survival Histogram Based on Sex and Pclass")

with middle_column:
    st.subheader("Survival Histogram Stack Based on Sex and Pclass")


left_column.plotly_chart(group_plot1,use_container_width=True)

middle_column.plotly_chart(group_plot2,use_container_width=True)

st.markdown("---")
st.subheader("Survival Histogram based on Pclass")

pclass = st.selectbox("Select PClass", (1, 2, 3), placeholder="Select PClass...")
df1=df.loc[df['Pclass']== pclass, ['Survived', 'Pclass']]

group_plot = px.histogram(df1, x="Pclass", color="Survived",barmode='group') 

st.plotly_chart(group_plot)

st.markdown("---")
st.subheader("pivot table")
table = pd.pivot_table(data=df,index='Sex', aggfunc={'Age':np.mean,'Fare':np.mean,'Parch':np.mean,'SibSp':np.mean,'Survived':np.sum})
st.dataframe(table)
