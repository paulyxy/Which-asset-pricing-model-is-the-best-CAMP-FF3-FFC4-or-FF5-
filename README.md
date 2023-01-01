# Which asset pricing model is the best?

Model 1:  CAPM (Capital Asset Pricing Model)

         R_IBM -Rf = alpha + beta(Rmkt- Rf)
         
        st.latex(r'''CAPM: R_{IBM} -R_f = \alpha + \beta(R_{mkt}- R_f)''')

Model 2: FF3, Fama-French 3-factor model 

         R_IBM -Rf = alpha + beta1(Rmkt- Rf)+beta2*SMB+beta3*HML
         
      st.latex(r'''FF3: R_{IBM} -R_f = \alpha + \beta_1(R_{mkt}- R_f)+\beta_2SMB+\beta_3HML''')

Model 3:FFC4, Fama-French-Carhart 4-factor model 

         R(IBM) -Rf = alpha + beta1(R(mkt)- Rf)+beta_2*SMB + beta3*HML+ beta4*MOM
         
        st.latex(r'''FFC4: R_{IBM} -R_f = \alpha + \beta_1(R_{mkt}- R_f)+\beta_2SMB+\beta_3HML+\beta_4MOM''')

Model 4: Fama-French 5-factor model

       R(IBM) -Rf=alpha+beta1(R(mkt)- Rf)+beta2*SMB+beta3*HML+beta4*RMW+beta5*CMA
       
       st.latex(r'''FF5: R_{IBM} -R_f=\alpha+\beta_1(R_{mkt}- R_f)+\beta_2SMB+\beta_3HML+\beta_4RMW+\beta_5CMA''')

   SMB: Small Minus Big, i.e.,the difference between returns of portfolio and big portfolios
   
   HML: High Minus  Low, i.e.,the difference between returns of portfolio with high book/market ratio
   
                      and the portfolio with low book/market ratio
                      
                    Book (market) stands for book (market) value of equity

   MOM: Momentum factor: i.e.,the difference between returns of winning and loser portfolios
   
   RMW: Robust Minus Week, i.e.,the difference between returns of robust and week portfolios
   
   CMA: Conservative Minus Aggressive, i.e.,the difference between returns of Conservative and aggressive portfolios

 For more information, please go to Professor French Data Library at
 
     https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

     https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_factors.html

     https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_5_factors_2x3.html

## Data
   stock data 
      http://datayyy.com/data_pickle/ibmMonthly.pkl'

      http://datayyy.com/data_pickle/wmtMonthly.pkl"

      http://datayyy.com/data_pickle/aaplMonthly.pkl"

  Market data 
      http://datayyy.com/data_pickle/ffc4monthly.pkl

      http://datayyy.com/data_pickle/ff5monthly.pkl

      http://datayyy.com/data_pickle/ff3monthly.pkl

## Contribute

   Email me at paulyxy@gmail.com if you find typos in the code 

