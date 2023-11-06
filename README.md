# Holiday Planner API

## How to run the project

### docker

navigate to the correct folder within a terminal/command line (the folder with the dockerfile in)

make sure docker is installed

run:

`docker build -t holiday_planner_app .`

run:

`docker run -p 8000:8000 holiday_planner_app`

and then visit http://127.0.0.1:8000/api/schema/swagger-ui/

## A brief description of my thought process

This is the first project that I have created using django and django rest framework, so there was a lot to learn. I decided to include a swagger ui using drf_spectacular because this is how I'm used to interacting with api endpoints. I like that swagger gives you a list of all endpoints and allows them to be easily used. (If you have the code running locally, then you can access the swagger like this: http://127.0.0.1:8000/api/schema/swagger-ui/)

### trips

I wanted to add all CRUD functions for a database, however, I was unable to get UPDATE to work with the nested model serializer. I realise that I could have made my life a lot easier if I had had one database table instead of two that are joined by a foreign key. However, I felt that in a real project it is important to think about how to model the database most effectively, and so this seemed like the best way to model the database tables, even if it caused me difficulties.

### weather and other endpoints

I wanted to create an endpoint called locations with a query parameter called search. I was intending to use a third party api that would return a city, the country and the latitude and longitude (https://open-meteo.com/en/docs/geocoding-api), however, I didn't have the time to implement this.

Because the third party weather api only returns a forecast for the next 14 days, I thought it would be interesting functionality to get the weather data for that time in the previous year. I thought that data could be labled as "estimate = true" so that the front-end could clearly commuicate to the user that this is not the forecast, but instead the weather from the previous year. The only downside to this additional functionality is that the free version of the third party weather api actually only returns data 3 months before today's date. This means that the weather data that is returned is actually null when looking at last year's weather data. However, if this were a real-world api, then I would imagine I would have access to the commercial api, which has weather data reaching back over a year.

## limitations

- No tests!

  - I ran out of time.
  - I would have tested the following:
    - unit tests for the logic within the weather section. For example, the function that extracts the lat long from the string, or the function that puts the date back by one year.
    - integration tests - would have been good to have a test sql lite DB to test the CRUD functions on the database calls
    - end-to-end - I would have mocked the call to the third party API for the weather endpoint, and then tested whether I would have received the correct output
    - I would have done "happy path" testing as well as "unhappy path" testing, and I would have have written specific tests to check known edge-cases.

- no security/log in
- The update function does not work for trips/id
- There is no error handling - for example if the third party api fails or anything else breaks
- There is no checking or cleaning of input data
- All the inputs for the weather endpoint are strings, rather than an array or dates, which means the swagger cannot check if the input data is correct
- When returning the trips from the database, I am not filtering based on user ID, so therefore all trips would be returned for everyone - not ideal!
- maybe creating a model and serializer for the weather endpoint, rather than just returning a dictionary (which could change)
- the query parameters for the third party weather api (e.g. temperature_2m_max) could be created as variables so that they can't accidentally be changed in some places and not others

## known bugs

- The update function does not work for trips/id
- several warnings when starting the server

## wishlist

- for the limitations and bugs to be resolved
- a location search endpoint
