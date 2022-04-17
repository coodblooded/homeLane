##  Installation
```
 --> Create a new  virtual ENV
 -->  Install the all the dependencies  pip install -r requirements.txt
 --> Migrate the data python manage.py migrate
 --> Run the server python manage.py runserver
```

## Get the API Key 

```
URL : http://localhost:8000/api-key

Method: GET

Response: 
{
    "status": true,
    "API-KEY": "Sknq9QhV.Vpr2DF0pPK5YBTTDPrZxi7g7fcJcU1Uw"
}

```

## Budget Homes API Key 

```
URL : http://localhost:8000/home/budget/

Method: POST

Add api get param in the header
X-Api-Key : <API KEY>

Payload: 
{
    "minPrice": 122,
    "maxPrice":1234
}


```

##   SQRT Homes API Key 

```
URL : http://localhost:8000/home/sqft/

Method: POST

Add api get param in the header
X-Api-Key : <API KEY>

Payload: 
{
    "minSqft": 122
}


```


##   Year Homes API Key 

```
URL : http://localhost:8000/home/year/

Method: POST

Add api get param in the header
X-Api-Key : <API KEY>

Payload: 
{
    "year": 1992
}


```





