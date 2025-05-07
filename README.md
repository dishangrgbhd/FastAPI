#Practicing deploying AI into production using FASTAPIs 

#UPDATE 1:
  The **main.py** is essentially a JSON CRUD API and I have also made files for system testing and functional testing using FastAPI.

  
#UPDATE 2:
  For returning structured responses(i.e json), I first made a simple ML model which i can send data through the API endpoint for prediction and obtain the output. Funneling the output as a json response. That   is the **sentiment_api.py** file and the requests as well as the responses are written in the **struct_senti.py file**. Also used @asynccontextmanager and initialized the function with lifespan, by doing this model is loaded at server startup ready to infer before the users start sending requests.

#UPDATE 3:
  I made **secure_model.py** and **mainforsecuremodel.py** files where I implemented authentication logic i.e how to secure APIs with key-based authentication and also managing request rates with custom rate limiting which prevents the APIs from being abused.
