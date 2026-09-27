import pandas as pd
import statsmodels.api as sm

def run_regression_model(df)
    
    Multiple linear regression predicting asymmetry changes from WOMAC, Age, and BMI[cite 1].
    
    X = df[['womac_total', 'age', 'bmi']]
    y = df['asymmetry_change']
    
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    
    print(model.summary())
    return model

if __name__ == __main__
    pass