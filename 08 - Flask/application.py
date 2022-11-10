# Import the classes `Flask` and `render_template` from 
# the `flask` module, written by someone else.
from flask import Flask, render_template, request, jsonify

# We use Pandas to handle the dataset and sci-kit learn to do t-SNE
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from mpl_toolkits.mplot3d import Axes3D
# import seaborn as sns




# Instantiate a new web application called `app`, 
# with `__name__` representing the current file
app = Flask(__name__) 

# When the user goes to the route `/`, 
# exceute the function immediately below
@app.route("/") 
def hello():
    return "Hello, world!"

# When the user goes to the route `/name`, 
# exceute the function immediately below
# get the 'myname' query string and 
# return a format string with the value
@app.route("/name")
def name():
    name = request.args.get('myname')
    return f"Hello, {name}!"

# Here's a similar example using routes 
# instead of query strings
@app.route('/user/<username>')
def username(username):
    return f"Goodbye, {username}!"


# When the user goes to the route `/tsne`, 
# exceute the function immediately below
# Get the file 'frontend.html' from the templates
# directory and return that
@app.route("/tsne")
def tsne():
    return render_template("frontend.html")

# the penguins dataset will be stored in a Pandas DataFrame
penguinData = pd.DataFrame()

# This is called from the javascript function 
# displayUpdated() in frontend.html.
# It does the following:
#   (1) Load the data (if not already done)
#           and do necessary data wrangling
#   (2) Figure out which variables to use for t-SNE and clustering
#   (3) Run t-SNE on the data's attributes to compute the 2D embedding
#   (5) Return the items as a JSON response that's readable by JavaScript
@app.route("/update-tsne", methods=['POST'])
def updateTsne():
    print('trace:updateTsne')
    

    # (1) Load the dataset (if not already done)
    #   Get a reference to the glboal penguinData data frame 
    #   (this is needed to modify global copy).
    #   If the global penguinData is empty,
    #   read the penguin_size csv into the penguinData DataFrame,
    #   and add an index column with reset_index()
    #   NOTE: I've removed rows with missing values from the csv file
    global penguinData
    if penguinData.empty:
        penguinData = pd.read_csv('penguins_size.csv')
        penguinData = penguinData.reset_index()

    # print('PENGUIN INFO')
    # print(penguinData.head())
    # print(penguinData.info())
    # print(penguinData.shape)
    
    

    # (2) Figure out which variables to use when runnning t-SNE
    #   Get the parameters from the request
    params = request.get_json() 
    features = []
    if params['culmenlengthChecked']:
        features.append('culmen_length_mm')
    if params['culmenDepthChecked']:
        features.append('culmen_depth_mm')
    if params['massChecked']:
        features.append('body_mass_g')
    if params['flipperChecked']:
        features.append('flipper_length_mm')
        
    # Filter data to only  have selected columns.
    # Then, since the attributes are on different scales, 
    # convert each attirbute into z-scores with domain = [-1, 1]
    # (number of standard deviations from the mean) for easier comparability
    filteredPenguinData = penguinData[features].values
    scaledPenguinData = StandardScaler().fit_transform(filteredPenguinData)

        

    # (3) Run t-SNE on the dataset using the selected attributes
    tsne = TSNE(n_components=2, n_iter=1000, random_state=42)
    points = tsne.fit_transform(scaledPenguinData)

    # points is a numpy.ndarray with 2 columns
    # Convert it to a DataFrame and merge
    # it into the penguinData DataFrame
    pointsDF = pd.DataFrame(points, columns=["x","y"])
    results = pd.concat([penguinData, pointsDF], axis=1)
    
    
    # (4) Return the items as a JSON response that's readable by JavaScript
    penguinJson = results.to_json(orient="records")
    return penguinJson