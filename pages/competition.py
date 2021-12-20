# Imports from 3rd party libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc

# Imports from this application
from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
                    
            ## DataDriven Competition

            **Tanzanian Ministry of Water Dataset**

            DataDriven is a platform for data scientists to compete in analyzing and making predictions around datasets.

            ### The Problem

            Provided is a dataset created from Taarifa and the Tanzanian Ministry of Water. The dataset has 40 features, is relatively uncleaned, and has a high percentage of missing values. Roughly 13,000 scientists have participated in solving this problem.

            ### Scoring

            Models are ranked based on the accuracy score they receive on a test dataset that is only applied to the model at the time of submission.

            ### Our results

            Our model was tested and published on December 18th, 2021, and received an accuracy score of **0.8036** which ranked us **2818** out of **12798** competitors.

            The Competition can be found [here](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/) on data driven

            ### Reflection

            Given more time several optimizations and testing could be done to further improve our accuracy score.

            **In-depth analysis on all data**

            We could continue with a much more in-depth look into the features in the dataset and find more innovative ways to fill missing values and engineer new features.

            **Tuning data to each model**

            relatively little time was given to the comparison of different models. If we were to go back we would tune the data in very targeted ways to each model. For example, we spent time creating a Sin and Cosine based day feature to represent the circular nature of the data (wanted to show that day 30 of the month is positionally close to day 1 of the month). However, in practice, that kind of feature is only useful for a model such as logistic regression and not a random forest classifier like the one we used. This is because the random forest classifier looks at each feature independently. In this case, the circular feature creation was not worth the strength loss from splitting the feature into two.

            **Hyperparameter tuning**

            Random search cross-validation with 10 folds was done to tune our random forest model to best work with this specific dataset. Given the case, that data was analyzed with more depth and tuned to each model the hyperparameter tuning process would have been more in-depth since it would have been the final decider in which model would be used for the competition submission.

            **Conclusion**

            For this first competition and our given timeframe, a well-optimized model was created that is more than useful for solving the problem of predicting if a given waterpipe will be functional or not.

            """
        ),
    ],
)

# ![pairplot](./assets/pairplot.png "pairplot")

layout = dbc.Row([column1])