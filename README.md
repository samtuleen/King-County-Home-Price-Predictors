# King County Home Price Analysis

The aim of this analysis is to build a linear regression model that can predict which home improvement projects positively affect house prices with the greatest accuracy possible. The results can inform home owners interested in selling their homes about the most profitable improvements to consider for adding value to their home and thus increasing sale prices.

## This Repository

### Repository Directory

```
├── README.md:  Main README explaining the project
├── [data](data)
│       ├── [processed](data/processed):  Contains cleaned data
│       ├── [raw](data/raw): Contains original pre processed data
│       └── [README](data/README)
├── [Images](Images): Contains image files
│   
├── [notebooks](notebooks): Folder contains notebooks
│       ├── [exploratory](notebooks/exploratory):  Contains EDA notebooks
│       ├── [reports](notebooks/reports): Contains polished notebook
│       │     └── [final_analysis.ipynb](reports/final_analysis.ipynb):  Final analysis and modeling
│       └── [README](notebooks/README)
├── [references](references):  Folder contains references
│   ├── [figures](references/figures):  Contains saved figures from analysis
│   ├── [instructions.md](references/instructions.md):  Contains project instructions
│   ├── [King_County_Home_Sales_Data_Dictionary.pdf](references/King_County_Home_Sales_Data_Dictionary.pdf): Data dictionary
│   └── [README](references/README)
├── [src](src)
│   ├── [modeling](src/modeling):  Contains functions used for modeling    
│   │   └── [modeling_functions.py](src/modeling/modeling_functions.py):  Functions used for modeling
│   └── [__init__.py](src/__init__.py)
│   
└── [linreg-env.yml](linreg-env.yml)
    

```

### Quick Links

1. [Final Analysis Notebook](notebooks/reports/final_notebook.ipynb)
2. [Presentation Slides](reports/presentation.pdf)

### Setup Instructions

This project's environment is linreg-env.yml

## Business Understanding

This analysis is based on the King County Housing Data Set which contains information about the size, location, condition, and other features of houses in King County. The aim of this project is to develop a regression model than can predict which home features positively affect house prices with the greatest accuracy possible. The model and examination is focused on single family homes and what are some of the many factors that contribute to real estate sales prices. The results can inform home owners interested in selling their homes about the most profitable improvements to consider for adding value to their home and thus increasing sale prices.

## Data Understanding

This analysis is based on the King County Housing Data Set which contains information about the size, location, condition, and other features of houses in King County.


## Data Preparation

I've merged and cleaned the provided data sets based on variable I've concluded would be good features in the model. I've dropped a number of columns: some contained outliers, others offered no value to the data (such as an 'Address' column.) I've filtered the data to reflect only those from 2018 till 2020, residential properties, and those under 4500 sqft. I did so to narrow down to single family homes only.

## Modeling

The features of my final model include total square footage of living space, bathroom counts, deck square footage, building grade and township.

## Summary of Model:
**Target: Sales Price**
After filtering the data to be relevant to first time home buyers(narrowed down size and price range), we can visualise the distribution of sales prices in King County over the last 3 years:

## Evaluation

The model does have some limitations: given that some of the variables needed to be log and sqrt-transformed to satisfy regression assumptions, any new data used with this model would need to undergo similar processing. In addition, considering regional differences in housing prices, this model's applicability to data from other counties may be limited. And lastly, since outliers were removed, the model may not accurately predict extreme values.

## Conclusion

1- Total living square footage is a major factor in the price of a home. The larger the home, the pricier. On this note, should a homeowner wish to increase the price of their home before selling by adding to it's living space, converting the garage to an additional bedroom is a highly profitable choice.

2- The grade of a house has the greatest effect on it's value. A surefire way to instantly add value to a home is to upgrade the construction using the highest quality materials.

3 - Location, location, and again, location. The location of a home, be it determined by zip code or township, is a great predictor of the price of a home. If a well built, high quality home is contructed in a bad area, most likely the home owner will have a difficult time sell or will have to comprimise on it's sale price. On the flip side, a run down home in a highly sought after area usually doesn't lose too much value since many people are willing to make the purchase with the intent of fixing it up.

4 - Enclosed porches and decks add to the value of a home. Home owners appreciate having the ability to enjoy the outdoors while maintaining a slight sense of seclusion.

5- The number of bathrooms factors into the high sale price of the house. The more bathrooms, the more valuable.
