import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns
import altair as alt
from PIL import Image


st.set_page_config(page_title="Music and Mental Health Dashboard",page_icon=":musical_note:",layout="wide")
st.title("Music and Mental Health Dashboard :headphones::sunflower:")
st.text("Music therapy or MT, is the use of music to improve an individual's stress, mood, and overall mental health")
st.text("MT is also recognized as an evidence-based practice, using music as a catalyst for happy hormones such as oxytocin.")
st.markdown('Data collection was managed by @catherinerasgaitis via a Google Form. Respondents were not restricted by age or location.')

image = Image.open('music image.jpg')
st.image(image, caption='source:google')


df=pd.read_csv("music&mentalheath.csv",nrows=200)
st.dataframe(df)
df.describe()
df.head()
 

st.sidebar.title("please filter here:")
option = st.sidebar.selectbox("Select an option", ("Age", "Hours per day","BPM","While working"))

if option == "Age":
    st.write("You selected Age")
    plt.figure(figsize=(4,3))
    sns.histplot(df['Age'])
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    
elif option == "Hours per day":
    st.write("You selected hours per day")
    plt.figure(figsize=(4,3))
    sns.histplot(df['Hours per day'])
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

elif option== "BPM":
    st.write("You selected BPM")
    plt.figure(figsize=(4,3))
    sns.histplot(df['BPM'])
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


elif option=="While working":
    st.write("You selected while working")
    plt.figure(figsize=(4,3))
    sns.countplot(x=df['While working'])
    st.pyplot()


###frequency

frequency = st.sidebar.selectbox("Select a frequency of the genre", ("classical ","folk","country","EDM","Gospel","Hip hop","jazz","Kpop"))

if frequency == "classical":
    st.write("You selected classical")
    plt.figure(figsize=(4,3))
    sns.countplot(x=df['Frequency [Classical]'])
    plt.xlabel('Classical Music')
    st.pyplot()

elif frequency == "folk":
    st.write("You selected folk")
    plt.figure(figsize=(4,3))
    sns.countplot(x=df['Frequency [Folk]'])
    plt.xlabel('Folk Music')
    st.pyplot()

elif frequency =="country":
    st.write("You selected country")
    plt.figure(figsize=(4,3))
    sns.countplot(x=df['Frequency [Country]'])
    plt.xlabel('Country Music')
    st.pyplot()

elif frequency =="EDM":
    st.write("You selected EDM")
    plt.figure(figsize=(4,3))
    sns.countplot(x=df['Frequency [EDM]'])
    plt.xlabel('EDM Music')
    st.pyplot()

elif frequency =="Gospel":
    st.write("You selected Gospel")
    plt.figure(figsize=(4,3))
    sns.countplot(x=df['Frequency [Gospel]'])
    plt.xlabel('Gospel Music')
    st.pyplot()

elif frequency =="Hip hop":
    st.write("You selected Hip hop")
    plt.figure(figsize=(4,3))
    sns.countplot(x=df['Frequency [Hip hop]'])
    plt.xlabel('Hip Hop Music')
    st.pyplot()

elif frequency =="Jazz":
    st.write("You selected Jazz")
    plt.figure(figsize=(4,3))
    sns.countplot(x=df['Frequency [Jazz]'])
    plt.xlabel('Jazz Music')
    st.pyplot()

elif frequency =="K pop":
    st.write("You selected K-pop")
    plt.figure(figsize=(4,3))
    sns.countplot(x=df['Frequency [K pop]'])
    plt.xlabel('K Pop Music')
    st.pyplot()


###condition
condition= st.sidebar.selectbox("Select a condition", ("OCD","Anxiety","Insomnia","Depression"))
if condition == "OCD":
    st.write("You selected OCD")
    plt.figure(figsize=(4,3))
    sns.barplot(x=df['Fav genre'], y=df['OCD'], hue=df['Music effects'], errwidth=0, palette='coolwarm')
    plt.xticks(rotation=90)
    st.pyplot()

elif condition == "Anxiety":
    st.write("You selected Anxiety")
    plt.figure(figsize=(4,3))
    sns.barplot(x=df['Fav genre'], y=df['Anxiety'], hue=df['Music effects'], errwidth=0, palette='coolwarm')
    plt.xticks(rotation=90)
    st.pyplot()


elif condition == "Insomnia":
    st.write("You selected Insomnia")
    plt.figure(figsize=(4,3))
    sns.barplot(x=df['Fav genre'], y=df['Insomnia'], hue=df['Music effects'], errwidth=0, palette='coolwarm')
    plt.xticks(rotation=90)
    st.pyplot()


elif condition == "Depression":
    st.write("You selected Depression")
    plt.figure(figsize=(4,3))
    sns.barplot(x=df['Fav genre'], y=df['Depression'], hue=df['Music effects'], errwidth=0, palette='coolwarm')
    plt.xticks(rotation=90)
    st.pyplot()
    

###graphs
graph= st.sidebar.selectbox("Select a graph", ("Line plot","heatmap","boxplot","pie chart 1","pie chart 2"))

if graph == "Line plot":
    plt.figure(figsize=(4,3))
    sns.lineplot(x=df['Fav genre'], y=df['Age'], ci=None)
    plt.xticks(rotation=90)
    st.pyplot()

elif graph == "heatmap":
    corr = df.corr()
    sns.set(style="white")
    fig, ax = plt.subplots(figsize=(15,5))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

elif graph == "boxplot":
    plt.figure(figsize=(8,6))
    sns.boxplot(x=df['Fav genre'], y=df['Hours per day'])
    plt.xticks(rotation=90)
    st.pyplot()

elif graph == "pie chart 1":
    def create_pie_chart():
      plt.figure(figsize=(5, 4))
    plt.title('Effects of Music on Mental Health')
    effects = df['Music effects'].value_counts()
    effects.plot(kind='pie', colors=['indianred', 'gold', 'darkblue'], ylabel='')
    st.pyplot()

elif graph == "pie chart 2":
    s_colors = ['lightgreen', 'lightcoral', 'steelblue', 'palevioletred', 'gold', 'darkturquoise']
    services = df['Primary streaming service'].value_counts()
    services.plot(kind='pie', colors = s_colors)
    plt.title('Streaming services by popularity')
    plt.ylabel("")
    st.pyplot()


option=="Primary streaming service"
st.write("You selected Primary streaming service ")
plt.figure(figsize=(4,3))
sns.countplot(x=df['Primary streaming service'],palette="Dark2")
plt.xticks(rotation=75)
st.pyplot()

##using altair
chart = alt.Chart(df).mark_bar().encode(
    alt.X('Age', bin=alt.Bin(step=0.5)),
    y='count()'
).properties(
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)

##using altair
chart = alt.Chart(df).mark_arc().encode(
    color='Primary streaming service',
    theta='values'
).properties(
    width=600,
    height=400
)

chart = alt.Chart(df).mark_bar().encode(x='Age',y='Hours per day')
st.altair_chart(chart, use_container_width=True)
 
##barplots

plt.figure(figsize=(4,3))
sns.barplot(x=df['Fav genre'], y=df['Anxiety'], errwidth=0)
plt.xticks(rotation=90)
st.pyplot()

plt.figure(figsize=(4,3))
sns.barplot(x=df['Fav genre'], y=df['Insomnia'], errwidth=0)
plt.xticks(rotation=90)
st.pyplot()

plt.figure(figsize=(4,3))
sns.barplot(x=df['Fav genre'], y=df['OCD'], errwidth=0)
plt.xticks(rotation=90)
st.pyplot()

plt.figure(figsize=(4,3))
sns.barplot(x=df['Fav genre'], y=df['Depression'], errwidth=0)
plt.xticks(rotation=90)
st.pyplot()

####

plt.figure(figsize=(4,3))
sns.barplot(x=df['Fav genre'], y=df['Age'], hue=df['Music effects'], errwidth=0, palette='coolwarm')
plt.xticks(rotation=90)
st.pyplot()


###subplots
df.dropna(inplace=True)
fig = plt.figure(figsize=(10,5))

plt.suptitle("BPM vs Mental Health")

y = df["Anxiety"]
y2 = df["Depression"]
y3 = df["Insomnia"]
y4 = df["OCD"]
x = df["BPM"]
ax = fig.add_subplot(221)
plt.title('Anxiety')
plt.xticks([])
plt.ylabel('Mental health ranking')
plt.hist2d(x,y, density = True)
st.pyplot()


ax = fig.add_subplot(222)
plt.title('Depression')
plt.xticks([])
plt.hist2d(x,y2, density = True)
st.pyplot()

ax = fig.add_subplot(223)
plt.title('Insomnia')
plt.ylabel('Mental health ranking')
plt.xlabel('BPM')
plt.hist2d(x,y3, density = True)
st.pyplot()

ax = fig.add_subplot(224)
plt.title('OCD')
plt.xlabel('BPM')
plt.hist2d(x,y4, density = True)
st.pyplot()

###
sns.scatterplot(data=df, y="Fav genre", x="Age", alpha = 0.5, marker = "X", color = "sienna")
plt.title('Age distribution by genre')
st.pyplot()
 
 

 

   
 
