import requests

url = "http://localhost:8080/analyze"
data = {"text": "This is amazing, I like this."} #positive sentiment
#data = {"text": "This is dissapointing, I didn't like this."} #negative sentiment

# Send post request and pass the sample request data
response = requests.post(url, json=data)

# Print prediction response
print(response.json())

#this is a ml model using logistic regression for practice and simple purpose so it is very volatile so can experience inaccuracies.