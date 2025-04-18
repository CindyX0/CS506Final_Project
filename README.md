# CS506Final_Project
Link to Dataset: https://www.icpsr.umich.edu/web/NACDA/studies/37404/variables?start=850&sort=VARLABEL_SORT%20asc&STUDYQ=37404&EXTERNAL_FLAG=1&ARCHIVE=NACDA&rows=50# 

Description of the project.
Conduct exploratory analysis on what factors influence the health(emotional,mental, physical) and satisfaction(including happiness) of relationships between married couples. What factors are strongly correlated with healthier and happier relationships? Are there any patterns we notice in unhealthy relationships when it comes to spouse behavior?
The categories that would be interesting to explore are general relationship health & satisfaction, emotional & mental Health in Relationships, physical health & relationship quality, conflict & unhealthy relationship patterns, external influences on relationships, gender & role dynamics in relationships and predictiong relationship succsess/ struggle

The data is available online for public use , however it needs to be engineered to include variables that are more relevant to the questions being asked and refine into a subset of data that can be easier to workwith.
Modeling Options: Linear/Logistic  Regression, Decion Trees
Visualization: Bar plot, Scatter plot, Heat Maps, line graphs, area graphs, I also want to create an interactive where we can see different facotrs on happiness/satisfaction/ health
Test plan: the conventional 80/20 rule , 20 used to train and 80 used to test. I also want to validate the models create with acccuracy, precision, recall and  f1 scores


#Midterm Report
Video: https://youtu.be/N13AAylApxM 
#1 Understanding Dataset and Variables
I initially started this entire process by trying to understand the data I was given and the variables I was working with. I believe there are around 500 variables, and since this was a survey where participants were asked questions before giving their responses in a quantitative way, I wanted to ensure I had an in-depth understanding of the survey. I went through the codebook and first looked at all the variables and their categorizations. I created a document to organize this information, where I categorized the variables into different themes and noted what each variable represented. The categories that variables can fall under as of now are Mood, Physical Health, Interpersonal Support/Strain, Daily Stressors, Emotion Work, Intimacy, Interactions with Spouse, Personal Control, Satisfaction & Happiness, and Previous Adversity. Some variables can also overlap.
Data Cleaning and Handling Nulls
I started by cleaning the data and obtaining initial information about the dataset, such as the number of rows and columns. There were no "nulls" originally in the dataset, but there was null-adjacent data where, for participant privacy, responses were replaced with "MASKED BY ICPSR," which I converted into null values. I checked that all inputs were numeric; if not, they were set to null. Additionally, I removed unusual inputs that disrupted later functions. I chose not to drop rows with null values because I realized that many of the null cells contained information irrelevant to the columns I was interested in. If I had dropped them, the dataset would have been empty.
Checking for Correlative Relationships
Since I am working with an extensive number of variables, I wanted to see which variables were correlated for exploratory analysis. I assumed these variables would be more important and help me craft questions related to the overall topic of the project. To do this, I created a correlation matrix to visualize linear relationships and a Spearman correlation matrix to detect nonlinear correlations. Initially, the correlation matrix was a bit messy, so I applied a threshold of 0.5, as I was only interested in moderate to high correlations. I exported these correlations for further examination.
Creating Subsets of Data for Preliminary Visualizations
My visualizations for correlated features are not yet complete, nor do they explore as many categories as I would like. Below are the current visualizations and the methods used to create them:
1.Mean of Emotional Self-Rated Health over the past 24 hours vs. Mean Physical Self-Rated Health over the past 24 hours (Bar Chart)

2.Relationship Satisfaction across Different Stress Variables (Stress Friends, Stress Family, Stress Spouse, Stress Work, Stress Finances) – A separate box plot for each variable. I also created a grouped bar chart to present similar information differently. I wanted to experiment with different ways of representing the same data to find the most easily understandable format.

3.Line Graph of Average Relationship Satisfaction by These Behaviors: spouse listens, relationship happiness, feeling like you can confide in a partner, relationship rewarding, and respondent feeling like their spouse loves and cares.

Visualizations I would like to continue working on:
-The impact of adverse childhood experiences on relationship outcomes

-A comparison of physical health in happier vs. less happy relationships

-Specific behaviors correlated with happier vs. less happy couples

There are many more areas to explore since this is an exploratory study.
Predictive Modeling #1
I created a decision tree (random forest regression model) to predict the following metrics: Feelings of Relationship Satisfaction, Relationship Happiness, and Relationship Rewarding. I had to pivot because my model does not handle nulls, so I replaced missing values with the average of the respective column. As stated earlier, I could not drop the nulls because that would leave the dataset empty.
To determine which parameters or "behaviors" to include, I considered:
-A combination of variables representing different behaviors and actions

-Variables that were positively or negatively correlated with the target metrics

-General relationship behaviors that I believed could influence someone's happiness

I adjusted my parameters three times to fine-tune my model. After my initial model, I used R² and MSE to evaluate its performance, yielding scores of 0.93 and 0.09, respectively. The model improved with each iteration. I also performed cross-validation to assess its performance on new data. Surprisingly, despite the strong initial performance, the cross-validation scores for MSE and R² were 0.61 and 0.5, respectively. After tweaking my parameters for the third time, I ended up with an R² of 0.9986 and MSE of 0.0016, which is a strong improvement. However, cross-validation yielded a score of 0.53 for both metrics, along with an improved model MSE.
I attempted another method for selecting features by analyzing feature importance within the forest. I trained a model, selected the top 30 features, and used them as parameters, but this resulted in lower accuracy. I suspected that high-variance features might have been biased or that correlated features misled the model’s weighting.
When I examined feature importance using the features from my original model, the results differed from those of the top 30 features method. The model showed error issues in the code, so I chose to stick with my original approach. In the future, I plan to attend office hours to seek help with the discrepancy between my model’s high performance and lower cross-validation scores, as well as assistance with the top 30 features function.
I also wanted to perform hyperparameter tuning, but my computer takes too long to process it, and it never finished loading. I decided to postpone this step and focus on exploring other models for now.
Visualizing Prediction of Model #1
I plotted the actual values of the target metrics against their predicted values in a scatter plot. Additionally, I created a scatter plot of residuals to visualize model performance.
Predictive Model #2
Initially, I used K-means to cluster the following metrics: Feelings of Relationship Satisfaction, Relationship Happiness, and Relationship Rewarding. However, the results were visually unappealing and difficult to interpret due to the dimensionality of my data. I pivoted and used the elbow method to determine the optimal number of clusters, choosing six clusters. I also applied PCA to reduce the data’s dimensions for better visualization.
I focused only on data where the target metrics were high (ratings of 4 and above on a 1-5 scale). For each cluster, I aimed to identify dominant variables or behaviors. My plan is to analyze how these clusters compare to each other and what insights they provide about relationship dynamics.
To further compare the clusters, I created a bar graph showing how each cluster performed across all target metrics.
Future Work
This round primarily focused on traits and behaviors that lead to successful relationships. However, I definitely plan to explore the inverse—factors that contribute to relationship dissatisfaction.
