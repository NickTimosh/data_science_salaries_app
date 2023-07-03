import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title='DS Salaries',
                   page_icon=':💵:'
                   , layout='wide'
)

# ---- Read CSV ----
@st.cache_resource
def get_data():
    df = pd.read_csv('ds_salaries.csv')
    return df

df = get_data()

# Add [job_category]
job_categories = ['Data Science', 'Data Analytics', 'Data Engineering', 'Machine Learning', 'Managerial', 'Research Scientist']

data_science = 'Data Scientist|NLP|Computer Vision Engineer|Applied Scientist'
data_analyst = 'Analyst|Analytics|Data Specialist|BI Developer'
data_engineer = 'Data Engineer|ETL|Architect|Infrastructure'
ml_engineer = 'Machine Learning|ML|Big Data|AI'
manager = 'Manager|Head|Director|Lead|Principal|Staff'
research_scientist = 'Research Scientist|Research Engineer'

conditions = [
    (df['job_title'].str.contains(data_science)),
    (df['job_title'].str.contains(data_analyst)),
    (df['job_title'].str.contains(data_engineer)),
    (df['job_title'].str.contains(ml_engineer)),
    (df['job_title'].str.contains(manager)),
    (df['job_title'].str.contains(research_scientist))
]

df['job_category'] = np.select(conditions,
                               job_categories,
                               default='Other')

# Update [experience_level]
df['experience_level'] =df['experience_level'].str.replace('SE', 'Senior Executive')
df['experience_level'] =df['experience_level'].str.replace('MI', 'Intermediate')
df['experience_level'] =df['experience_level'].str.replace('EX', 'Executive director')
df['experience_level'] =df['experience_level'].str.replace('EN', 'Entry level')

# Update [employment_type]
df['employment_type'] = df['employment_type'].str.replace('FT', 'Full time')
df['employment_type'] = df['employment_type'].str.replace('CT', 'Contract')
df['employment_type'] = df['employment_type'].str.replace('FL', 'Freelancer')
df['employment_type'] = df['employment_type'].str.replace('PT', 'Part Time')

# ---- SIDEBAR ----

st.sidebar.header('Filters')

year = st.sidebar.radio(
    'Year',
    options=df['work_year'].unique()
)

location = st.sidebar.selectbox(
    'Country',
    options=df['company_location'].unique()
)

ex_level = st.sidebar.multiselect(
    'Experience Level:',
    options=df['experience_level'].unique(),
    default=df['experience_level'].unique()
)

emp_type = st.sidebar.multiselect(
    'Employment Type:',
    options=df['employment_type'].unique(),
    default=df['employment_type'].unique()
)


df_selection = df.query(
    'work_year == @year & experience_level == @ex_level & employment_type == @emp_type & company_location == @location'
)

# ---- Dashboard Title ----

st.title('Data Science Salaries 2023')
# st.write('Salaries of Different Data Science Fields in the Data Science Domain')

# ---- KPI`s Section ----
st.markdown('##')
cnt_jobs = df_selection['salary_in_usd'].count()
avg_salary_kpi = int(df_selection['salary_in_usd'].mean())

col_1, col_2, col_3 = st.columns(3)
with col_1:
    st.metric(label = '🌍 Country:', value = location)
with col_2:
    st.metric(label = '👷‍♂️ Jobs in Dataset:', value = f'{cnt_jobs:,}')
with col_3:
    st.metric(label = '💵 Average Salary:', value = f'US $ {avg_salary_kpi:,}')

st.markdown('---')

# ---- Bar Chart View ----

# Calculate the average salary per job category
avg_salary = df_selection.groupby('job_category')['salary_in_usd'].mean().reset_index()

chart = alt.Chart(avg_salary).mark_bar().encode(
    x=alt.X('job_category:N', sort='-y', axis=alt.Axis(title=None, labelAngle=0)),
    y=alt.Y('salary_in_usd:Q', axis=alt.Axis(title=None, ticks=False, labels=False, grid=False)),
    tooltip=['job_category:N', alt.Tooltip('salary_in_usd:Q', format='$,.0f')],
)

text = chart.mark_text(
    align='center',
    baseline='bottom',
    dy=-10,  # Adjust this value to control the vertical position of the data values
    color='white',  # Set the color of the data values to white
    fontSize=12  # Adjust this value to change the font size of the data values
).encode(
    text=alt.Text('salary_in_usd:Q', format='$,.0f')
)

chart = chart + text

chart = chart.properties(
    width=600,
    height=350,
    view={"stroke": None}  # Remove the padding around the chart
)

st.altair_chart(chart, use_container_width=True)
st.markdown('---')
