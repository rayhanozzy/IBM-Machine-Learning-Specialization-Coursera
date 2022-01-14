import streamlit as st
import pandas as pd
import numpy as np

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Dataframe','Chart')
)

if option == 'Home' or option == '':
    st.write("""# Halaman Utama""")
elif option == 'Dataframe':
    st.write("""## Dataframe""")

    df = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-03-12/board_games.csv")
    df.head(10)
elif option == 'Chart':
    st.write("""## Draw Charts""")

    chart_data = pd.DataFrame(
        np.random.randn(30,2),
        columns = ['a','b']
    )

    st.line_chart(chart_data)

    chart_data
