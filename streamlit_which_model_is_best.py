import time
import pandas as pd
from PIL import Image
import streamlit as st
import statsmodels.api as sm

st.set_page_config(layout="wide")
# left-alignment 
st.markdown('''   
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True)
st.title("Which model is the best?")
st.write("By Y.X. Yan, v1.0, 1/1/2023")
col1, col2,col3=st.columns([1.7,0.2,1])
col1.markdown(' ## Four finance models:')

col1.latex(r'''CAPM: R_{IBM} -R_f = \alpha + \beta(R_{mkt}- R_f)''')
col1.latex(r'''FF3: R_{IBM} -R_f = \alpha + \beta_1(R_{mkt}- R_f)+\beta_2SMB+\beta_3HML''')
col1.latex(r'''FFC4: R_{IBM} -R_f = \alpha + \beta_1(R_{mkt}- R_f)+\beta_2SMB+\beta_3HML+\beta_4MOM''')
col1.latex(r'''FF5: R_{IBM} -R_f=\alpha+\beta_1(R_{mkt}- R_f)+\beta_2SMB+\beta_3HML+\beta_4RMW+\beta_5CMA''')

model_name = col3.selectbox('Step 1: select a model',('CAPM', 'FF3', 'FFC4','FF5'))
ticker=col3.selectbox('Step 2: select a stock', ('IBM', 'Walmart', 'Apple'))
with col3.expander(" ooooooo or load your own data set:"):
    data0=col3.file_uploader(" or upload you monthly data downloaded from Yahoo!Finance")

col2.markdown("Step 1 =>")
col2.markdown("    ")
col2.markdown("    ")
col2.markdown("    ")
col2.markdown("Step 2 =>")

path="http://datayyy.com/data_pickle/"
def getStockData(name):
    data = None
    if name == 'IBM':
        infile=path+'ibmMonthly.pkl'
    elif name == 'Walmart':
        infile=path+"wmtMonthly.pkl"
    else:
        infile=path+"aaplMonthly.pkl"
    data=pd.read_pickle(infile)
    return data

def which_model(model_name):
    mkt = None
    if model_name == 'FFC4':
        infile='http://datayyy.com/data_pickle/ffc4monthly.pkl'
    elif model_name == 'FF5':
        infile='http://datayyy.com/data_pickle/ff5monthly.pkl'
    else:
        infile='http://datayyy.com/data_pickle/ff3monthly.pkl'
    mkt=pd.read_pickle(infile)        
    return(mkt)

df=getStockData(ticker)

ans=globals()['data0']   # check the existence of data0
if ans==None:
    col3.write("[Default status: not using an uploaded data]")
else:
    df=pd.read_csv(data0,index_col='Date')
    df= df.set_index(pd.DatetimeIndex(df.index))    
    ticker=data0.name
    col2.write(f"[now using an uploaded data called '{ticker}']")


df['Ret']=df['Adj Close'].pct_change()    # get return 
df=df.dropna()
df2=df["Ret"]

#st.write(f"#### Model: {model_name} is selected")
mkt=which_model(model_name)
final=mkt.merge(df2,left_on=mkt.index,right_on=df2.index)
y=final["Ret"]-final["RF"]
if model_name=="CAPM":
    X=final["MKT_RF"]
elif model_name=="FF3":
    X=final[["MKT_RF","SMB","HML"]]
elif model_name=="FFC4":
    X=final[["MKT_RF","SMB","HML","MOM"]]
elif model_name=="FF5":
    X=final[["Mkt_RF","SMB","HML","RMW","CMA"]]
#st.write(f'OLS summary for the Model of "{model_name}"')
x = sm.add_constant(X)
result= sm.OLS(y, x).fit()

with col1.expander("Model explanations: click here to see and hide"):
    st.write("CAMP: Capital Asset Pricing Model;   FF: Fama-French Model")
    st.write("SMB: Small Minus Bug, HML: High Minus Low; MOM: Momentum factor")
    st.write("FFC: Fama-Frech-Carhat; RMW: Robust Minus Week, CMA: Conservative Minus Aggressive")
    st.write("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html")

with col1.expander("Stock and model selected: click here to see and hide"):
    st.write(f"#### stock: {ticker} is selected")
    st.write(f"#### Model: {model_name} is selected")


with col1.expander("The first 2 obs of stock and market: click here to see and hide"):
    st.write(df.head(2))
    st.write(mkt.head(2))

with col3.expander("Result interpretation: click here to see and hide"):
    st.write("----------------------------------------------------------")
    st.write("Key1: check individual beta's significance")
    st.write("Key2: check the performance of the whole model")
    #st.write("Key3:",st.latex(r'''R^2'''),"and adj",st.latex(r'''R^2'''))
    st.write("Key3: compare adj. R^2 for difference models")
#
with st.expander("Results: click here to see and hide"):
    st.write(f'OLS summary for the Model of "{model_name}"')
    st.write(result.summary())
    
    