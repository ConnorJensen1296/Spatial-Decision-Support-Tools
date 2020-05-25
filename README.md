# Spatial Decision Support Tools
1) Please download the train.csv file from kaggle linked here https://www.kaggle.com/c/nyc-taxi-trip-duration/data this wasn't able to be uploaded to github due to it exceeding their file size limit. Extract it and place it in the data folder

2) Install the required packages with the following command
pip install -r /path/to/requirements.txt

3) You can generate the centroids.csv file located in the data folder by running through the Clustering notebook but this may take a while

4) Gmaps for jupyter is required if you want to view the centroids of the clusters on an interactive google map in the Jupyter notebook the link to install is here https://jupyter-gmaps.readthedocs.io/en/latest/

5) The Dataset anaysis notebook was used to generate all of the images in the output folder
   The ElbowMethodEvaluation notebook was used to generate the elbow.png file in output this file will take about 15minutes to run if you wish to recreate this image
   
6) The webpage can be accessed by running the app.py file and navigating to http://127.0.0.1:5000/ in your browser
