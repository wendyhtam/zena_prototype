import streamlit
import pandas
import snowflake.connector

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# Retrieve catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
df = pandas.DataFrame(my_catalog)
color_list = df[0].values.tolist()

streamlit.title('Zena\'s Amazing Athleisure Catalog')
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
product_caption = "Our warm, comfortable, " + option + " sweatsuit!"
streamlit.write(product_caption)

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()

streamlit.image(
  df2[0],
  width = 400,
  caption = product_caption
)

streamlit.write('Price', df2[1])
streamlit.write('Sizes Available', df2[2])
streamlit.write(df2[3])



