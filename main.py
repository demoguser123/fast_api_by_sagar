from fastapi import FastAPI # importing fast api.

app = FastAPI() # creating our application here can be anything instead of app. and we will make multiple endpoint here which will be connected to below @app.get

"""
here below, we are basically telling our fast api is whenever any "get" request will come to the url of "/" this. run the below function which is here is "home".

"/" is the home address of our server

"here in the return we are returning a dictionary. and fastapi will automatically convert thing dictionary in the json before sending as a response.
"""

@app.get("/") # here we are creating a root with decorator
def home():
    return {"message": "my first api is working."}


    """
    will run the file with the command "uvicorn main:app --reload here reload means everytime we don't have to again close and open the web-browser after doing any change it will automatically run it.
    """