from typing import Any, Dict, List

import streamlit as st
import snowflake.connector
import plotly.figure_factory as ff
import numpy as np
import altair as alt


from streamlit_prophet.lib.utils.load import load_config, load_image
from multipage import MultiPage
from pages import

# Create an instance of the app 
app = MultiPage()

# Page config
#favicon=st.image(load_image("Darkpoolwhite.png"))
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

# Sidebar choose page 
sideb.header ("Configuration Navigation")
persona = sideb.selectbox("", ('Consumer Analyst','Consumer Admin','Provider Admin'))
if persona == 'Consumer Analyst':
      sideb.write('You are viewing the Consumer Analyst Setup Page.')
else:
      sideb.write('This setup page is under construction.') 

      
if persona == 'Consumer Analyst':
   st.title("Consumer Request")
    
