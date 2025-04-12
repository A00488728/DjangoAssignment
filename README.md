# How to run the project
clone the repo
repo link
https://github.com/A00488728/DjangoAssignment.git

Open the root directory
Go to hotel_project directory
Run the following command from the command prompt
python manage.py runserver

# How to access the hosted APIs
When the APIs are hosted, the links created are 
http://127.0.0.1:8000/api/hotels/

# How to test the API
Send a POST request using the data 
{
        "name": "Grand Beach Resort",
        "address": "456 Beach Road",
        "city": "California",
        "stars": 5
    }

It should give you a 201 created response

Send a GET request and the reponse date will be like
{
        "id": 1,
        "name": "Grand Beach Resort",
        "address": "456 Beach Road",
        "city": "California",
        "stars": 5
    }

It will generate the id automatically.
