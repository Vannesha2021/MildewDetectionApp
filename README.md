# Dataset Content
The dataset contains a total of 2104 images of leaves taken from cherry trees in the Farmy & Foods plantations. The leafs in the inages are either infected with powdered mildew or healthy leaves. 

# Business Requirements
As a Data Analyst student from Code Institute, I was asked to develop an ML system that can instantly, using a leaf image, detect if a tree is healthy or has powdery mildew for an agricultural company. Their cherry plantations were showing powdery mildew, a fungal disease affecting a wide range of plants. They needed this ML system because they were spending too much time manually inspecting each tree.

1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

2 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.

# Hypothesis and how to validate?

I suspect that powdery mildew infected leaves typically has whiteish spots on leaves differentiating them from uninfected leaves.
An average image study can help evaluate its rationale for mapping the business requirements to Data Visualizations and Machine Learning tasks. The client needed a dashboard to help solve their problem. A succesful project outcome would be a study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew and also the capability to predict if a cherry leaf is healthy or contains powdery mildew.

# Business Requirement 1: Data Visualization

- I will display the "mean" and "standard deviation" images for powdery-mildew contained
and healthy leaves.

- I will display the difference between an average powdery mildew-contained leaf and an average healthy leaf.

- I will display an image montage for either healthy or a powdery-mildew leaf.

# Business Requirement 2: Classification

- We want to predict if a given leaf has powdery-mildew or not.

- We want to build a binary classifier and generate reports.


# ML Business Case

Powdery Mildew Clf

- I want a ML model to predict if a leaf is infected with powdery mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.

- Our ideal outcome is provide the employees a faster and reliable diagnostic if a given leaf is infected or not with powdery mildew.

- The model success metrics are accuracy of 65% or above on the test set.

- The model output is defined as a flag, indicating if the leaf has powedery mildew or not and the associated probability of being infected or not. The planation employees pick leaves from the plantations and upload the picture to the App. This is a real-time prediction (not a batch prediction). 

- The data suggests a binary classifier, indicating whether a particular cherry leaf is healthy or contains powdery mildew.The input is a cherry leaf image and the output is a prediction of whether the cherry leaf is healthy or contains powdery mildew. The performance goal of the predictions with the client was a degree of 97% accuracy. Using this application, the client will be able to avoid compromising the quality of products it produces for the market.

- Heuristics: Currently, the process to check if the tree is infected with powdery midew is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

- The training data to fit the model come from Kaggle Website. This dataset contains about 4 thousand images. We have extracted a subset of 4208 images from this dataset and saved it to kaggle dataset directory for quicker model training.
Train data - target: healthy or not; features: all images. The client provided the data through Kaggle under an NDA (non-disclosure agreement), therefore the data should only be shared with professionals that are officially involved in the project.

# Breakdown of Epics and User Stories

1) Information gathering and data collection.
2) Data visualization, cleaning, and preparation.
3) Model training, optimization and validation.
4) Dashboard planning, designing, and development.
5) Dashboard deployment and release.


# Dashboard Design (Streamlit App User Interface)

## Page 1: Quick Project Summary

**General Information**

- Mildew is a fungal disease that is affecting the cherry plantations at Farmy & Foods. A powdery mildew is a fungus that attacks plants, causing a white, dusty coating on leaves, stems, and flowers.
- A random set of leaves was collected and examined by raw eyes. Visual criteria are used to detect powdery mildew.
- Powdery mildew may cause leaves to turn completely yellow, die, and fall off, which may expose fruit to sunburn. On some plants, powdery mildew may cause leaves to twist, buckle, or otherwise be deformed.

**Project Dataset**

- The available dataset contains 4208 images taken from the cherry tress in the Farmy & Foods planatations.

- Link to further information

**Business requirements**

1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

2 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.


## Page 2: Cells Visualizer

This will answer business requirement 1:
- Checkbox 1 - Difference between average and variability image
- Checkbox 2 - Differences between average powdered mildew and healthy leaves
- Checkbox 3 - Image Montage


## Page 3: Malaria Detector

Business requirement 2 information

 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.

- Link to download a set of healthy and mildew infected leaf images for live prediction.

- Create a user interface with a file uploader widget. The user should upload multiple leaf images. It will display the image and a prediction statement, indicating if the tree is infected or not with powdery mildew and the probability associated with this statement.
- Table with the image name and prediction results.
- Download button to download table.


## Page 4: Project Hypothesis and Validation
I suspect mildew infected leaves has cloudy residue on the leaf, typically the colour of the leaf, that can differentiate, from a healthy leaf.
An Image Montage, shows that typically a infected leaf has white powder across or spotted the leaf.
Average Image, Variability Image and Difference between averages studies didn't reveal any clear pattern to differentiate one to another.

## Page 5: ML Performance Metrics
Label Frequencies for Train, Validation and Test Sets
Model History - Accuracy and Losses
Model evaluation result


**Unfixed bugs**

None


**Main Data Analysis and Machine Learning Libraries**

numpy - NumPy was used for working with arrays in this project.

pandas -  PANDAS was used for cleaning, transforming and visualizing from data and data manipulation.

matplotlib - This was used for data visualisation.

seaborn - This was used to plt the graphs

plotly - This was used create static, animated, and interactive visualisations in this project.

streamlit - This was used to design and pan the dashboard.

scikit-learn - This was used to implement machine learning models and statistical modelling.

tensorflow-cpu - In order to train and evaluate the convolutional neural network, I used TensorFlow to clean the dataset and divide it into the required number of subsets.

keras - This was used to build machine learning models and define the neural network in this project.

Heroku - Cloud Hosting platform

**Deployment**

This app was deployed using Heroku. The first tep was to create an app with Heroku, the I linked my repo to the app in Heroku and clicked "Deploy", this project was deployed a manually.

**Credits**

- Code Institute
- Gyan Shashwat, machine learning analytics developer at Code Institute.
- niel_ci from the Slack Platform