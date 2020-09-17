# chimieAPI
Chimie API with information on chemical elements (Status: Database not yet complete)

<a><img width= 40% src="https://www.jorgeweiss.com/static/chimie-desktop.png"></a>

An API for all 118 chemical elements. How many protons does a Silver atom have? What's the melting point of Sodium? Chimie can provide this information and more. As more element data gets added to API, more endpoints will be added to the application including being able to retrieve information for a specific element group. 

The application responds using JSON. If using a web browser to view resources, a JSON viewer browser extension is recommended. 

A potential application that could be used with this API is the creation of an interactive periodic table where the data that makes up the table is provided with the API resource. The way the application is designed, one call to get all elements returns a resource with limited information for each element, speeding the API response time. If a call is made to a particular element endpoint, then the API responds with a more complete resource with all available data on that element. 



## Technology
- Flask for back-end routing
- SQL-Alchemy for Object-Relational-Mapping
- Relational DB using PostgreSQL
- Currently deployed on Heroku

## Base URL and Current Endpoints
#### Get list of all elements
- To get the entire list of elements along with some of their data, follow the base route with "/api/elements" added to URL
  
#### Get details of one element
To get a single element with all info, follow the base route with "/api/elements/[id]" added to the URL where id is the atomic number.  
If axios is being used on clientside JS fil to make requests to API, below is a sample request that could be made:  
Axios request in javascript to get data for helium would look like this:  
`let heliumData = await axios.get('https://chimie-api.herokuapp.com/api/2')`  

Visit [axios repository](https://github.com/axios/axios) for complete documentation on how it can be used to make AJAX calls from the client-side JavaScript file. 


## To-Do
- Fill database with all information
- Create more routes like (get noblegases or nonmetals, get elements with 5 valence electrons, etc);
- Add integration testing for each route

## LIVE APPLICATION:
https://chimie-api.herokuapp.com/
