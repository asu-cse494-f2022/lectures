# Flask

* [HTTP (Hypertext Transfer Protocol)](https://developer.mozilla.org/en-US/docs/Web/HTTP#:~:text=Hypertext%20Transfer%20Protocol%20(HTTP)%20is,be%20used%20for%20other%20purposes.) is a protocol for transmitting data that is sent over the internet, such as hypermedia documents (e.g., HTML pages). HTTP was originally designed for communication between web servers and clients (web browsers). 
* The [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) is a JS interface for accessing and manipulating the HTTP pipeline (requests and responses). Fetch is used to do asynchronous calls without having to reload the entire page. 
    * For example, `d3.csv` uses fetch: a CSV file is loaded into the browser and can then be manipulating or visualized without the webpage having to do a page refresh.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a microframework written in Python that makes it easy to get a simple web application up and running. We'll use Flask both to receive HTTP requests (i.e., going to a URL), doing any necessary server side processing, and returning the response to the webpage. Likewise, asynchronous calls using fetch will also be handled on the Flask server.
    * There are several servers out there, including Django, Node.js, and Apache HTTP Server. The way that you've been testing your homeworks using HTTPSimpleServer (or http.server in Python 3) is also a server (a very simplified one that can only handle GET requests).
* Flask follows a [client-server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model): the client opens a connection to make a request and then waits until it receives a response. The response contains a code that indciates the state of the response (success, failure, etc.) as well as the information to be displayed on the web page.

 <!-- as well as this tutorail on combining Flask and Fetch: [link](https://pythonise.com/series/learning-flask/flask-and-fetch-api). -->

## Using Flask

The best place to go for learning about Flask is its website. For example, [quickstart page](https://flask.palletsprojects.com/en/1.1.x/quickstart/) is a good starting point. Flask code is normally stored inside an `application.py` file which is written in Python. 

``` 
    from flask import Flask # import the Flask library

    app = Flask(__name__) # create a new web application called `app`, with __name__ representing the current file

    @app.route("/") # when the user goes to the route `/`, execute the function immediately below
    def hello()
        return "Hello, world!"

``` 

The normal practice is to use "routes" when first receiving requests. A route is the part of the URL that determines the page being requested. 

* The default route for a site is `/`, for example: `https://www.google.com/`.
* There are several routes in the `application.py` file in this directory:
    * `/`: the default route, which prints a "Hello, world!" message as the HTML.
    * `/name`: this route reads the value in a query string called `myname` and prints the result.
        * Example: `http://127.0.0.1:5000/name?myname=Tim`
    * `/user/<username>`: this route reads the username part of the route and prints the result.
        * Example: `http://127.0.0.1:5000/user/Tim`
    * `/tsne`: this route will display an html file `frontend.html`.
    * `/update-tsne`: this route is called via a POST method from `frontend.html` using fetch. 
        * This route loads a dataset (the Penguins dataset) and calculates (or updates) its layout using the t-SNE method and return the data to `frontend.html` in JSON format.
    

To use Flask, you'll need to install it (such as, `pip3 install flask`), as well as any other libraries that are used in the application. In our example, we use the following two libraries:
* [Pandas](https://pandas.pydata.org/) is a data storage and manipulation library for working with tabular data. (Install via `pip3 install Pandas`)
* [scikit-learn](https://scikit-learn.org/) is a machine learning library for Python.

To start a Flask application, run `flask run` (of `python3 -m flask run`) from a terminal window in the directory where the `application.py` file is located. Flask will print out the URL that the server is running on, which is how you access your website. 
* If `flask run` produces errors, try running `export FLASK_APP=application.py` first to make sure it knows to look for the `application.py` file as the web server.
* To have Flask auto-reload when code changes are made, you can also run `export FLASK_ENV=development` before running `flask run`.

Note: Flask will create some auxiliary files and folders, such as `__pycache__`. It's a good idea to add these to your `.gitignore` so they are not included in your repository.

## Penguins and t-SNE

This example web application uses a page `frontend.html` to display the penguins dataset using t-SNE. t-SNE, is a dimensionality reduction technique that embeds each item in the dataset (ie, each penguin) into a 2D layout based on the high-dimensional similarity of the items.

* The [penguins dataset](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data) is available here. It is an alternative to popular datasets like [Iris](https://archive.ics.uci.edu/ml/datasets/iris), [Wine](https://archive.ics.uci.edu/ml/datasets/wine), and [Automobiles](https://archive.ics.uci.edu/ml/datasets/automobile) which are used to introduce poeple to statistics and machine learning concepts. 
* The specific file is `penguin_size.csv`, which is a slightly simplified data file from the original dataset. It contains the following attributes.
    * `species`: penguin species (Chinstrap, Adelie, Gentoo)
    * `culmen_length_mm`: the length of the culmen in mm (the upper ridge of the bird's beak)
    * `culmen_depth`: the depth of the culmen in mm
    * `flipper_length_mm`: flipper length in mm
    * `body_mass_g`: the body mass in grams
    * `island`: the name of the island (Dream, Torgersen, Biscoe) in the Palmer Archipelego in Antartica
    * `sex`: penguin sex
* As a preprocessing step, I removed penguins with `NA` values. There are 334 penguins in the dataset that we will visualize.

We will use the `species` attribute to color the items in the display. The four ordered attributes (`culmen length`, `culmen depth`, `body mass`, and `flipper length`) will be used to calculate the similarity between each pair of penguins in the dataset. t-SNE will take this 4-dimensional similarity and compute a 2D layout, where penguins closer together are generally "more similar."

By clicking on one of the checkboxes on the page, we use fetch to recompute the similarities server-side and send updated layout information back to the frontend. Using `d3.join`, the penguins x/y positions are transitioned based on the updated layout information.