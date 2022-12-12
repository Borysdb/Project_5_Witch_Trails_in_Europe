import warnings
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import figure
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
from PIL import Image
warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")
from bokeh.plotting import figure
import plotly.graph_objects as go

#Adding main picture
st.markdown("<h1 style='text-align: center; color: white;'>Witch Trails in Europe between 1300-1850</h1>", unsafe_allow_html=True)
st.markdown("")

image = Image.open(r'C:\Users\borys\IronHack\Streamlit_Python\Graphics\burning.jpg')
im1, im2, im3 = st.columns([2.2,6,1])
with im1:
        st.write("")
with im2:
        st.image(image, caption='Medieval "camping" traditions on a painting')
with im3:
        st.write("")

#Small summary about our subjecy
st.markdown("<h3 style='text-align: center; color: yellow;'>Witchcraft - is a person's collaboration with the devil by the use of magic</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: yellow;'>(as defined by Christian theologians since the 13th century)</h3>", unsafe_allow_html=True)
st.markdown("")
"Witch trials in the early modern period saw that between 1400 to 1782, around 40,000 to 60,000 were killed due to suspicion that they were practicing witchcraft, with some other sources estimating that a total of 100,000 deaths occurred at its maximum for a similar period."
"Prosecutions for the practice of witchcraft would only reach a highpoint from 1560 to 1630 during the Counter-Reformation and the European wars of religion, with some regions burning those who were convicted at the stake, of whom roughly 80% were women, and most often, they were over the age of 40."
"https://en.wikipedia.org/wiki/Witch_trials_in_the_early_modern_period"

#Funny button showing Snow on screen when pressed :)
st.markdown("")
button1 = st.button("Shall we start?")
if button1:
    st.snow()
st.markdown("")


st.markdown("")
st.subheader("Based on received data, we will try to take a deeper look into victims of Witchcraft Prosecution")
st.markdown("#### Content worth mentioning")
st.markdown("🌍 Part of Europe --- 🇪🇺 Country --- 📆 Century --- ⚖ Number of Tried people --- ☠ Number of Deaths")  
st.markdown("")
st.markdown("Original data-> 10941 rows, 12 columns of data")
st.markdown("After cleaning-> 7056 rows, 10 columns of data + 1 new created ('Part of Europe')")
st.markdown("Clean data for map visualisation-> 4142 rows, 2 columns of data")
st.markdown("")


st.write("#### Below is a sample of clean data we are working on:")
data_map = pd.read_csv(r'C:\Users\borys\IronHack\Streamlit_Python\data_map.csv')
st.write(data_map)

data = pd.read_csv(r'C:\Users\borys\IronHack\Streamlit_Python\witch_clean.csv')


#Creation of sidebar
st.sidebar.write("### 🔥🔥 Welcome! 🔥🔥")
st.sidebar.write("")
makes=['Part of Europe','Country']
make_choice = st.sidebar.selectbox('Please select data you would like to visualise:', makes)
st.sidebar.write("")
makes2=['Centuries','Decades']
make_choice2 = st.sidebar.selectbox('Please select time range you are interested in:', makes2)


#Map visualisation

st.subheader("Cleaned map of Trials")
st.markdown("")

data_map2 = pd.read_csv(r'C:\Users\borys\IronHack\Streamlit_Python\data_map2.csv')
map_df = pd.DataFrame.from_dict(data_map2)

st.markdown("")


m1, m2 = st.columns([5,3])

with m1:
        st.map(map_df)
with m2:
        st.write('Number of Trialed and Deaths per Country')
        st.write(data.groupby('Country')[['Tried','Deaths']].sum())

st.markdown("")


#Main Visualisation
st.markdown("<h3 style='text-left: center; color: white;'>Data Visualisation</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
        st.write('Participation in Deaths by Part of Europe')
        tree1= data[["Part of Europe","Deaths"]].groupby(["Part of Europe"],as_index=False).agg("sum")
        fig = px.treemap(
        tree1,
        parents=['Source','Source','Source','Source','Source'],
        names='Part of Europe',
        values='Deaths',)
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        st.plotly_chart(fig, use_container_width=True)

with col2:
        st.write('Participation in Trials by Part of Europe')
        fig = px.sunburst(
        tree1,
        parents=['Source','Source','Source','Source','Source'],
        names='Part of Europe',
        values='Deaths',
        )
        st.plotly_chart(fig, use_container_width=True)

with col3:
        st.write('Number of Trialed and Deaths per Part of Europe')
        st.write(data.groupby('Part of Europe')[['Tried','Deaths']].sum())


col4, col5, col6 = st.columns(3)

with col4:
        st.write('Number of Trialed and Deaths per Part of Europe')
        st.write(data.groupby('Century')[['Tried','Deaths']].sum())
with col5:
        st.write("Number of Tried by Century" )
        BMIC= data[['Century', 'Tried']].groupby(['Century']).agg('sum')
        st.bar_chart(BMIC,use_container_width=True) 
with col6:
        #st.write("Number of Deaths by Century" )
        #BMIC= data[['Century', 'Deaths']].groupby(['Century']).agg('sum')
        #st.bar_chart(BMIC,use_container_width=True)
        fig6 = plt.figure()
        plt.title('Number of Deaths by Century')
        sns.lineplot(x="Century",  y = 'Deaths',data =data).set_title("Number of Deaths by Century")
        st.pyplot(fig6)


#Final question to the User:
st.subheader("I hope you liked my little Demo?")
checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")

if checkbox_one and checkbox_two:
        "Sorry, you can't select both!"
        image = Image.open(r'C:\Users\borys\IronHack\Streamlit_Python\Graphics\choice.jpg')
        st.image(image, width = 600, caption="Choose your destiny")
elif checkbox_one:
        "Great! You have a great taste my friend :)"
        image = Image.open(r'C:\Users\borys\IronHack\Streamlit_Python\Graphics\wand.jpg')
        st.image(image, width = 600, caption="Magic!")
elif checkbox_two:
    value = "No"
    image = Image.open(r'C:\Users\borys\IronHack\Streamlit_Python\Graphics\spanish1.jpg')
    st.image(image, width = 700, caption="Witch! I found a Witch!")