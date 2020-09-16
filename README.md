# chimieAPI
Chimie API with information on chemical elements (Status: Not Complete)

<a><img width= 40% src="https://lh3.googleusercontent.com/Z0OVUc-BQ2m5NdFUj-_3NnoQ8Tar4_Mo8vn1w_0jDSmUi0QpkO4ID5SG56CGY4SgYMpxCJzFCkABhZw6ex0JqPqjNEwQN5tgiwTDuw5WGCildgctqgo1KWKksB9qVyVChtztfo8WZM6tpDcO2MHkj5PRPEgtWIe7RhBD1F8Eh3YYWu0rnq4LtD0k1OGsoY1bFpwf4lS14aHEnWYAgH5wxfzcyOYs_M_R14FmroUCu2UVAkvKaynGXwt8aDrPx6Q2HQEa__opvc6uWyuTGnwtRLSN0y-SPfnRXikhrys6GBM_mtGqlOqds4-ZQ8UxhxVGBJ1wBtW1j6MQvuqSXbaqG-5KvaowNT2WexNBFD6DmwIN9PjD8Gud5j8QpJHNU4mz6f0Srn5QcP49suww9LAyXXsV7-IQjV3PMv5GbWtGO4jKScANcSJm7ZQKVbuglKM4gsN7AtV25wJbaIo_GJxBE3xc427WTTERQiiku6Fi1Tk4BGfb84F-z1OsePu-MQCQj33BCSFLawcuo3NHjoZIAYB2RpqV7aZWETMh6YlP_liofDAhR00KdzBlruOUodUUNik46njdFieoUGKlTEB8m9TkNy2AkmwzUSoN_RP_sy3Tcxc20MdMB9jXH1gUC88kcrnJeAbkfHH3D5KlSVvNaRHAZfu-1VZel2iO-IBK2uweKuOgzM9dYyP1Ab8y=w1450-h930-no?authuser=0"></a>

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
