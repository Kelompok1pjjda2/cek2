import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor,ExtraTreesRegressor
from sklearn.model_selection import validation_curve, LeaveOneOut, train_test_split, cross_val_score
from sklearn.model_selection import cross_validate, KFold, cross_val_score, RandomizedSearchCV, GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder 
from matplotlib import pyplot
import pickle
import math

#Baca Data
data = pd.read_excel("./SUMMARY DATA SOURCE.xlsx")

loaded_model = pickle.load(open('./model.sav', 'rb'))

LOGO_IMAGE = "./logo.jpeg"
#Disable Warning
st.set_option('deprecation.showPyplotGlobalUse', False)
#Set Size
sns.set(rc={'figure.figsize':(8,8)})
#Coloring
colors_1 = ['#66b3ff','#99ff99']
colors_2 = ['#66b3ff','#99ff99']
colors_3 = ['#79ff4d','#4d94ff']
colors_4 = ['#ff0000','#ff1aff']
st.markdown(
    f"""
    <div style="text-align: center;">
    <img class="logo-img" src="data:png;base64,{base64.b64encode(open(LOGO_IMAGE, 'rb').read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color: #243A74; font-family:sans-serif'>PROYEKSI PENERIMAAN BEA MASUK</h1>", unsafe_allow_html=True)
menu = st.sidebar.selectbox("Select Menu", ("Dashboard", "Prediksi"))