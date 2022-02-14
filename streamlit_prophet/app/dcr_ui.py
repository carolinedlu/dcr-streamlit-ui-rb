from typing import Any, Dict, List

import streamlit as st
import snowflake.connector
import plotly.figure_factory as ff
import numpy as np
import altair as alt


from streamlit_prophet.lib.utils.load import load_config, load_image


# Page config
# favicon=st.image(load_image("Darkpoolwhite.png"))
st.set_page_config(page_title="snowdcr",page_icon="❄️")

# Load config
config, instructions, readme = load_config(
   "config_streamlit.toml", "config_instructions.toml", "config_readme.toml"
)

# Initialization
dates: Dict[Any, Any] = dict()
report: List[Dict[str, Any]] = []
   




# Sidebar
sideb = st.sidebar
sideb.image(load_image("DCRLogoGray.png"),use_column_width=True)
sideb.header ("Account Login")
sideb.text_input('Snowflake Account', value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None)
sideb.text_input('User Name', value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None)
sideb.text_input('Password', value="", max_chars=None, key=None, type="password", help=None, autocomplete=None, on_change=None, placeholder=None)
sideb.button("Submit", key='login', help=None, on_click=None, args=None, kwargs=None)

# Sidebar choose page 
sideb.header ("Configuration Navigation")
persona = sideb.selectbox("", ('Consumer Request','Consumer Admin','Provider Admin'))
if persona == 'Consumer Request':
      sideb.write('You are viewing the Consumer Request page.')
      
      # Consumer Request Page
      st.title("Consumer Request")
      st.header("Privacy Budget as of today")
      privbudget = "10"
      st.text("Current Privacy Budget: "+ privbudget)
      
      # Connect to Consumer Account
      def init_connection():
         return snowflake.connector.connect(**st.secrets["snowcat"])
      conn = init_connection()
      
      # Load Templates into frame
      def run_query(query):
         with conn.cursor() as cur:
            cur.execute(query)
            # Return a Pandas DataFrame containing all of the results.
            df = cur.fetch_pandas_all()
            option = st.selectbox('Select your template', df)
            #st.dataframe(df)
            
            if option:
               run_query2("select table1.value from table(split_to_table('consumer.pets|consumer.zip|provider1.status|provider1.age_band','|')) as table1;")
               
def run_query2(query_text):
   with conn.cursor() as cur:
    cur.execute(query_text)            
    # Return a Pandas DataFrame containing all of the results.
    df = cur.fetch_pandas_all()
    option2 = st.multiselect('Select dimensions', df)
    st.button("Submit", key='submitquery', help=None, on_click=None, args=None, kwargs=None)
      
run_query("select template_name from DCR_DEMO_APP.CLEANROOM.TEMPLATES;")

   

      
      
      
      
      
      
      
      
      
      
      
      
if persona == 'Consumer Admin':
sideb.write('You are viewing the Consumer Admin page.')

# Consumer Request Page
st.title("Consumer Admin")
st.header("Under Construction")

if persona == 'Provider Admin':
sideb.write('You are viewing the Provider Admin page.')

# Consumer Request Page
st.title("Provider Admin")
st.header("Under Construction")
   




   
