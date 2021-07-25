import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
from streamlit.elements import button


st.title('北海道の労働統計指標一覧')
st.write('●道内の産業別平均賃金')

# if st.checkbox('参考資料を表示する'):
#     image = Image.open('tenga.jpg')
#     st.image(image, caption='北海道の労働市場の移り変わり')

option = st.selectbox(
        '募集人数を選んでください',
         list(range(1,11))
         )
'募集人数は',option,'人です。'

year = st.slider('何年後の人件費をみたい？',0,50,5)
'人件費',year*200000*option,'円です。'

left_column, right_column = st.beta_columns(2)

button = left_column.button('右カラムに表示する')

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

expander1 = st.beta_expander('標準報酬月額とは・・・')
expander1.write('標準放銃月額とは、一言で言うと月の平均賃金のこと。')