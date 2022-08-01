import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('Ronnies healthy Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.text('🍕 Pizza with 4 types of cheese')
streamlit.text('Breakfast Lasagne smotherd in cheese!!')
               
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)



## streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")

##streamlit.write('The user entered ', fruit_choice)
def get_fruityvice_data(this_fuit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
  
try: 
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Error on selection")
  else:
   back_from_function = get_fruityvice_data(fruit_choice)
   streamlit.dataframe(back_from_function)

except URLError as e:
   streamlit.error()
                                                 
                                                 
## debug stop
##streamlit.stop()

def get_fruit_load_list():
    with  my_cnx.cursor() as my_cur
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
  
# add a button
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list
  streamlit.dataframe(my_data_rows)

  ## hier jetzt stop
streamlit.stop()

  
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you add?','Jackfruit')

streamlit.write("thx 4 adding", add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
