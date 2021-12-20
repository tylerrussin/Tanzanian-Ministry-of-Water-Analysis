# Imports from 3rd party libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc

# Imports from this application
from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            # Tanzanian Ministry of Water Dataset Analysis

            ### Initial Data Exploration

            **Numeric Features**
            - amount_tsh - Total static head (amount water available to waterpoint)
            - date_recorded - The date the row was entered
            - gps_height - Altitude of the well
            - longitude - GPS coordinate
            - latitude - GPS coordinate
            - num_private -
            - region_code - Geographic location (coded)
            - district_code - Geographic location (coded)
            - population - Population around the well
            - construction_year - Year the waterpoint was constructed


            **Categorical Features**
            - funder - Who funded the well
            - installer - Organization that installed the well
            - wpt_name - Name of the waterpoint if there is one
            - basin - Geographic water basin
            - subvillage - Geographic location
            - region - Geographic location
            - lga - Geographic location
            - ward - Geographic location
            - public_meeting - True/False
            - recorded_by - Group entering this row of data
            - scheme_management - Who operates the waterpoint
            - scheme_name - Who operates the waterpoint
            - permit - If the waterpoint is permitted
            - extraction_type - The kind of extraction the waterpoint uses
            - extraction_type_group - The kind of extraction the waterpoint uses
            - extraction_type_class - The kind of extraction the waterpoint uses
            - management - How the waterpoint is managed
            - management_group - How the waterpoint is managed
            - payment - What the water costs
            - payment_type - What the water costs
            - water_quality - The quality of the water
            - quality_group - The quality of the water
            - quantity - The quantity of water
            - quantity_group - The quantity of water
            - source - The source of the water
            - source_type - The source of the water
            - source_class - The source of the water
            - waterpoint_type - The kind of waterpoint
            - waterpoint_type_group - The kind of waterpoint


            **Target**

            - status_group - If the waterpump is functional/ non-functional/ functional needs repair

            **Shape of Dataframe**

            (59400, 41)

            ### Dimensionality Reduction

            The current shape of the dataset is 41 features. To have the best performing model; our goal is to remove all the features that do not have any correlation with predicting a waterpipe's functioning status. 

            **Remove Duplicate Features**

            Many features have roughly the same values an example found in our dataset is waterpoint_type and waterpoint_type_group. We find that the difference between these features is a few outliers and the occasional change in value names. In the case of waterpoint; waterpoint_type has 6103 values that are named "communal standpipe multiple" where waterpoint_type_group is more general classifying those values to "communal standpipe". This pattern of data redundancy is seen in the bulk of the dataset. Below are the features removed due to duplication.

            'extraction_type', 'extraction_type_group', 'waterpoint_type_group', 'source', 'source_type', 'quantity_group', 'water_quality', 'payment_type', 'management', 'region', 'district_code', 'num_private', 'wpt_name', 'ward', 'recorded_by'

            **Initial Nan Removal**

            In the initial search for Nan values, we found high percentages of missing values ranging from 10-70%. These features were high dimensional categorical columns and for our analysis found it best to simply drop them rather than drop rows or worry about imputing. Below are the dropped features

            'funder', 'installer', 'subvillage', 'scheme_management', 'permit', 'public_meeting', 'scheme_name'

            **Hidden Nan Values**

            In the desirable features, we had left there were still a lot of missing values labeled in certain ways. For numerical features, missing values were labeled as 0 and for categorical missing features were labeled as 'unknown'. These values were replaced with Nans

            - amount_tsh - 41,639 observations are labeled as zero. zero could be a mix of water pumps that actually don't have water or unkown (highlyinbalanced)
            - date_recorded - seems fine
            - gps_height - 20438 ovservations are labled as zero (highly inbalanced)
            - longitude - 1812 observatoins labed as zero (highly invalanced)
            - latitude - 1812 obersations labed as -2.000000e-08 (highly inbalacned)
            - basin - no missing values (categorical 9 cats)
            - region_code - no missing values 
            - lga - no missing values (categorical 125 cats)
            - population - 21381 obsevations labeld as 0 (pretty highly inbalanced)
            - public_meeting - 3334 observations Nan (categorical 2 cats)
            - permit - 3056 observations Nan (categorical 2 cats)
            - construction_year - 20709 labed as 0 (higly inbalanced)
            - extraction_type_class - 6430 labeld as other (categorical 7 cats)
            - managment_group - 943 labeld as other, 561 labeled as unknown (categorical 5 cats)
            - payment - 1054 labeled as other, 8157 labeld as unknown (categorical 7 cats)
            - quality_group - 1876 labeld as unknown (categorical 6 cats)
            - quantity - 789 labeled as unknown (categorical 5 cats)
            - source_class - 278 labeld as unknown (categorical 3 cats)
            - waterpoint_type - 6380 labeld as other (categorical 7 cats)
            - status_group - no missing values

            ![missingno](./assets/missingno.png "missingno")

            ### Encoding missing values

            For encoding missing values we adopted two strategies dependent on if the feature consisted of numeric data or categorical data.

            **Numeric Data**

            When imputing numeric data we used KNNImputer which works off the Kmean-Nearest-Neighbor algorithm of statistically imputing values based on their mean proximity in vector space. All default parameters were used except for the test of different values for n_neighbors. Experiments were done with values at 2, 5, and 10. Ultimately settling for n_neighbors=5

            **Categorical Data**

            For imputing categorical data a pipeline of specialized LabelEncodeing (to handle Nan values) and IterativeImputing was utilized. The multivariant imputer uses other surrounding features to attempt to fill in the missing value for a given feature. The approach is rather experimental but effective in our analysis

            ### Feature Engineering

            For this study, we engineered two new features.

            **Sin and Cosine with DateTime**

            For the day and month features derived from the 'date_recorded' feature we wanted the model to acknowledge the cyclical nature of days in a month and months in a year (how day 30 of the month is positionally close to day one and how month 12 is positionally close to month 1 in a year)

            Our approach for doing this was the mapping of our features onto sin and cosine waves which was found to be effective. 

            ![sincos](./assets/sincos.png "sincos")

            **Years in Service**

            In our dataset we had two features; construction year and date recorded. by merging these two features into one by calculating the length of years a given waterpipe has been in service we reduced dimensionality and made a relatively rich feature. The years in service ultimately ranked 5th in the top most important features to our model's predictive abilities.

            **Top Features based on statistical importance**

            For this, we use SKbest along with f_regression to generate a list of statistically important features before we go into modeling. The features are ranked as follows.

            'extraction_type_class', 'payment', 'quantity', 'waterpoint_type',  'years_in_service'

            ### Creating a Baseline

            For the initial baseline we normalized the value counts of the status group feature(target) we found the results to be as follows:

            - functional 0.543081
            - non functional 0.384242
            - functional needs repair 0.072677

            Given this, if we were to always assume a water pump is functional we would be right 54% of the time

            **Splitting Data**

            For the modeling with this dataset, we split our data into three sections. First, a reserved 13,000 rows are given to our test data subset to which the target values we do not have access. Then a 75-25% percent split was done to create our training and validation data subsets. The split ratio was picked based on the ratio of the test dataset

            ### Hyper parameter tuning and cross-validation

            The process used for finding the best performing model was using random search along with cross-validation to tune each of our models and the one with the best accuracy would be used for further analysis. All modeling and search were done with sklearn's prebuilt packages.

            **The models**

            **Decision Tree**

            Tuned Decision Tree Parameters: 

            {'splitter': 'best', 'min_samples_leaf': 3, 'max_leaf_nodes': None, 'max_features': None, 'max_depth': 21, 'criterion': 'entropy'}

            The best score is 0.7624469693152618

            **Random Forest**

            Tuned Random Forest Parameters:

            {'warm_start': False, 'n_jobs': 2, 'n_estimators': 31, 'max_samples': None, 'max_features': 'sqrt', 'criterion': 'entropy'}

            The best score is 0.8004041613493289

            **Logistic Regression**

            Tuned Logistic Regression Parameters: 

            {'penalty': 'l2'}

            The best score is 0.594702581369248

            **ada_boost**

            Tuned Logistic Regression Parameters:

            {'n_estimators': 11, 'learning_rate': 1.5, 'algorithm': 'SAMME.R'}

            The best score is 0.6995735129068462

            **Gradient Boost**

            Tuned Gradient Boost Parameters:

            {'n_estimators': 150, 'learning_rate': 0.5}

            The best score is 0.7760718294051626

            All testing was generated through a pipeline built from the data processing techniques described above. We found Random Forest Classifier with tuned parameters of  {'warm_start': False, 'n_jobs': 2, 'n_estimators': 31, 'max_samples': None, 'max_features': 'sqrt', 'criterion': 'entropy'} to have done the best in scoring accuracy.

            **Further Tuning with Random Forest**

            After some additional tuning, the highest achieved score of the random forest model was 0.804 which is 0.001 more than the initial score of 0.800404. The final parameters for this tuning were warm_start=False, n_jobs=2, n_estimators=200, max_samples=None, max_features='sqrt', criterion='entropy'

            **Feature Importances**

            The top 5 important features found when predicting waterpipe functionality were GPS Height, Longitude, Latitude, Quantity, and Years in Service. These are the features used in our modified model in this demo web app. Also, the feature engineering of years in service provided to be important to the model's predictive abilities.

            ![featureimportance](./assets/featureimportance.png "featureimportance")

            **Confussion Matrix and Random Foresset**

            We found when it came to precision and recall the model performed okay but when looking at false classification percentages we see the model did struggle significantly with classifying water pipes as 'functional needs repair' and overall did poorly by predicting false positives.

            ![confussionmatrix](./assets/confussionmatrix.png "confussionmatrix")

            **ROC curve and Area Under the Curve Score**

            The Random Forest Model received a score of: 0.89

            ![roc](./assets/roc.png "roc")



            """
        ),
    ],
)

layout = dbc.Row([column1])