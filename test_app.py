import pandas as pd
import plotly.express as px

data = {'Country': ['A', 'B', 'C'], 'Population': [10, 20, 30]}
df = pd.DataFrame(data)

fig = px.pie(df, values='Population', names='Country', title='Population Distribution by Country')
