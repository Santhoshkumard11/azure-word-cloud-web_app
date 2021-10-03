## Word Cloud Web App  📑💨
This is a simple project to demonstrate the power of Azure

### Services Used
- #### Azure Functions (HTTP Trigger, Timer Trigger) 
- #### Azure CosmosDB
- #### Azure Blob Storage

#### Fill in the inputs to see your name on the word cloud

#### https://word-cloud-web-app.azurewebsites.net/api/web_app_home

#### Azure Functions 

- #### HTTP Trigger
    - displays homepage where we enter the inputs
    - send a post request from homepage to another Azure Functions which add the item to Cosmos DB

- #### Timer Trigger
    - triggers an Azure Function to get all the data from cosmos DB and generate a word cloud and updated the image in blob storage