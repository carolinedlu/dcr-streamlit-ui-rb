# Consumer Admin Main Page

from typing import Any, Dict, List

import streamlit as st
import snowflake.connector
import plotly.figure_factory as ff
import numpy as np
import altair as alt


from streamlit_prophet.lib.utils.load import load_config, load_image

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
   

# CONSUMER ADMIN Main Page
# MainPageLogo
# st.image(load_image("Darkpoolwhite.png"), use_column_width=True)
# Main Page Header

st.title("Consumer Admin")
