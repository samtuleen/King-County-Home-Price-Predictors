# imports:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


from statsmodels.formula.api import ols
import statsmodels.api as sm
import scipy.stats as stats




def model(features_lst, df, target_var):
    """
    features_lst is a list of strings of the variables to use as features from the df
    df is the dataframe to retrieve the features from 
    target_var is the string of the target variable
    """    
    df_model = df[features_lst]
    target = target_var
    features_lstcopy = features_lst.copy()
    features_lstcopy.remove(target)
    x_vals = features_lstcopy
    x_formula = '+'.join(x_vals)
    formula = target + '~' + x_formula

    model = ols(formula=formula, data=df_model).fit()
    
    print(model.summary())
 
    return model


def model_diagnosis(model, x, x_name, y):
    """
    returns a subplot of the model's distributions (QQPlot, histogram, and a scatter plot of the homoscedasticity
    model is the model variable (model's name)
    x is the object of the feature 
    x_name is the feature's variable
    y is the object of the target variable
    """ 
    
    residuals = model.resid
    
    fig = plt.figure()
    fig, axes = plt.subplots(nrows = 1, ncols = 3, sharex=False, sharey = False, figsize=(65,20), squeeze=False)
    
    fig.text(s="Summary of Model Diagnosis", x=.40, y=1.15, fontsize=40)
    fig.text(s="r-Squared: {r}".format(r=round(model.rsquared, 2)), x=.40, y=1.05, fontsize=30)
    fig.text(s="p-value: {p}".format(p= model.f_pvalue), x=.53, y=1.05, fontsize=30)
    
    fig.text(s='Residuals Histogram', x=.45, y=.93, fontsize=55)
    
    sm.graphics.qqplot(residuals, dist=stats.norm, line='45', fit=True, ax=axes[0][0])    
    plt.show;
    
    fig.text(s='QQ Plot', x=.20, y=.93, fontsize=45)
    
    axes[0][1].hist(residuals)
    plt.show;
    
    sns.residplot(x, y, ax=axes[0][2])
 
    fig.text(s='Residuals vs {x}'.format(x=x_name), x=.73, y=.93, fontsize=40)
    plt.tight_layout;
    plt.show;


def normality_assumption(model):
    """
    plots normality assumption
    model is the model's variable
    """ 
    # plot normality assumption
    fig, ax = plt.subplots(figsize = (15, 10))
    figure = sm.graphics.qqplot(model.resid, dist=stats.norm, line='45', fit=True, ax = ax);
    ax.set_title('QQ-Plot of Residuals', fontsize = 25)
    return plt.show()


def homoscedasticity(model, df):
    """
    plots homoscedasticity assumption
    model is model's variable
    df is the dataframe containing the features
    """ 
    fig, ax = plt.subplots(figsize = (15, 10))
    plt.scatter(model.predict(), model.resid)
    sns.set(font_scale = 1)
    fig.suptitle('Model Predictions VS. Residuals Scatter Plot', fontsize = 25)\
    plt.xlabel('Model Predictions', fontsize = 18)
    plt.ylabel('Model Residuals', fontsize = 18)
    ax.tick_params(labelsize=10)
    plt.plot(model.predict(), [0 for i in range(len(df))], color = 'red')
    return plt.show()

def heatmap_multi(x_features, df):
    """
    Creates a heatmap to show multicollinearity of all the x features in a model
    x_features (list):  A list of strings of the column names of the x features
    df:  the dataframe where the features are located
    Returns the plotted heatmap
    """
    
    df_x_feats = df.loc[:, x_features]

    x_corrs = df_x_feats.corr()

    mask = np.triu(np.ones_like(x_corrs, dtype=np.bool))
    f, ax = plt.subplots(figsize = (18, 16))
    sns.heatmap(x_corrs, mask = mask, vmax = 0.3, 
            center = 0, square = True, linewidths = 0.5, 
            cbar_kws = {'shrink': 0.5})
    ax.tick_params(axis='both', which='major', labelsize=20, labelrotation = 45)
    ax.set_title('Feature Multicollinearity Heat Map', fontsize = 30)
    
    return plt.show()

