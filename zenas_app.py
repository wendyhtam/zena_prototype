import streamlit
import pandas
import snowflake.connector

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# Retrieve catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
df = pandas.dataframe(my_catalog)

streamlit.title('Zena\'s Amazing Athleisure Catalog')
streamlit.write(df)
#streamlit.selectbox('Pick a sweatsuit color or style:', 
