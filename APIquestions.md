# API Call Questions and Answers
### **What is an API call (answer in your own words)?**
An API is an Application Programming Interface. An API call allows you to “call on” a certain invoke URL (like a Client URL or CURL) to use that certain software application within your programming. This way, you can access data or functionality from that software, kind of like asking a service to perform a task or give information back.


### **What is an example we discussed to create an API call locally?**
In this lecture, the example we discussed to create an API call locally was using a Python web framework called FastAPI, as well as the FastAPI GitHub repository. You can install it within your virtual environment using pip install. Then you can create a Python script and run it within your terminal, which starts the server and creates the API call locally. 


### **What is an example we discussed to create an API call on the cloud?**
The example we discussed in this lecture to create an API call on the cloud was using AWS. We created a Lambda function. We then invoked a test. Then we added a trigger. We chose to use API Gateway. 


### **What is the difference between FastAPI and creating API from AWS Gateway?**
When you create an API on FastAPI, it is more programming intensive and the creation is more manual. This gives you full control but also means more setup. Comparatively, when you create an API on AWS Gateway, it is almost more automatic and you just need to know how to configure and apply the software. 


### **In your own words after watching the video, what are the main steps to create an API call on AWS Gateway?**
When creating API from AWS Gateway, you first have 3 API type options : HTTP API, WebSocket API, and REST API. In our example in the lecture, we chose to use REST API, which helps provide complete control over the API request. We also made the security open, allowing others who look at the program to invoke the API as well on their own computers. The API was then added to the Lambda function we created, allowing it to be invoked in the code or on the test. Then we had to get the URL out of the API so that it can be used more efficiently. To do this, we went to the API within the triggers list, which then takes us to API Gateway. Here, we tested it using the POST method, which actually sends a payload to the API. Once the test of the Request Body works, you know that the API is doing what it is supposed to do. Then you can go back to requests and assign an API key. 


### **Professionally in the industry, how does developers ship product from one team to another? What's the usage of API here?**
The best way to ship product is by associating it with a custom Usage Plan that you create, to control the cost structure for the user. Then you can add associated stages and API keys. Once you deploy it, you can use the URL to access it on the internet. If you make the key required, a user just has to add their key to the Header. These usage plans, API keys, and stages are then used to control access and monitor usage once it’s deployed. This way, other teams can integrate or build on top of them without needing to understand the internal logic.