from typing import Any, Dict, List

import streamlit as st
import snowflake.connector
import plotly.figure_factory as ff
import numpy as np
import altair as alt
import pages import utils


from streamlit_prophet.lib.utils.load import load_config, load_image

# Load config
config, instructions, readme = load_config(
   "config_streamlit.toml", "config_instructions.toml", "config_readme.toml"
)

# Initialization
dates: Dict[Any, Any] = dict()
report: List[Dict[str, Any]] = []
   

# CONSUMER REQUEST Main Page
# MainPageLogo
# st.image(load_image("Darkpoolwhite.png"), use_column_width=True)
# Main Page Header

st.title("Provider Admin")

def app():
    st.markdown("## Provider Admin")
