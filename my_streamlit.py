import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

option = st.sidebar.selectbox(
    'Menu:',
    ('Home','Dataframe','Chart')
)

if option == 'Home' or option == '':
    st.write("""# Homepage""")
    st.markdown("Bienvenue sur la page d'accueil. C'est un de mes projets à l'IBM Machine Learning")

elif option == 'Dataframe':
    st.write("""## Dataframe""")

    df = pd.read_csv("Mall_Customers.csv")
    st.table(df.head(10))
    
    st.markdown("Describing data")
    st.table(df.describe())
    
elif option == 'Chart':
    st.write("""## Draw Charts""")

    chart_data = pd.DataFrame(
        np.random.randn(30,4),
        columns = ['a','b','c']
    )

    st.line_chart(chart_data)

    chart_data
