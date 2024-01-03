import pandas as pd
import plotly.express as px
base='light'
backgroundColor ='white'
st.write("HELLO")
data = {'Country': ['A', 'B', 'C'], 'Population': [10, 20, 30]}
df = pd.DataFrame(data)

fig = px.pie(df, values='Population', names='Country', title='Population Distribution by Country')
