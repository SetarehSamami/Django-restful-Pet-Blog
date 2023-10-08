# PET BLOG APIS WITH DJANGO REST FRAMEWORK
CRUD Pet Blog use PostgresSQL as DataBase and JWT 

## Installation
To run code just create and activate your virtual environment.You can do this by running the command
```
python -m venv env
```
After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```
## Structure
In this RESTful API you can create a post about your Pet and upload your pet image. also you can Comment and Reply a comment.
here are all of the endpoints (URLs) you can use.

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`post/` | GET | READ | Get all posts
`create-post/` | POST | CREATE | Create a new post
`update-post/:id` | PUT | UPDATE | Update a post
`delete-post/:id` | DELETE | DELETE | Delete a post
`category/` | GET | READ | Get all categories
`create-category/` | POST | CREATE | Create a new category
`update-category/:id` | PUT | UPDATE | Update a category
`delete-category/:id` | DELETE | DELETE | Delete a category
`comment/` | GET | READ | Get all comments
`create-comment/` | POST | CREATE | Create a new comment
`update-comment/:id` | PUT | UPDATE | Update a comment
`delete-comment/:id` | DELETE | DELETE | Delete a comment
`answer/` | GET | READ | Get all answers
`create-answer/` | POST | CREATE | Create a new answer
`update-answer/:id` | PUT | UPDATE | Update a answer
`delete-answer/:id` | DELETE | DELETE | Delete a answer
`accounts/users/` | GET | READ | Get all accounts
`accounts/register/` | POST | CREATE | Create a new comment
`accounts/update/:id` | PUT | UPDATE | Update a comment
`accounts/delete/:id` | DELETE | DELETE | Delete a comment

## Use
We can test the API using [swagger](http://127.0.0.1:8000/schema/swagger-ui/), or we can use [Insomnia](https://insomnia.rest/)


First, we have to start up Django's development server.
```
python manage.py runserver
```
Only authenticated users can use the API services, for authenticat enter username and password with POST method and this URL:
```
http://127.0.0.1:8000/accounts/token/
```

 We got two tokens, the access token will be used to authenticated all the requests we need to make:
```
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5Njg0MDcwMCwiaWF0IjoxNjk2NzU0MzAwLCJqdGkiOiI3YWJkNWM4MGViM2E0ZTQyODVkOGQ3NjY1MDljMDNjOCIsInVzZXJfaWQiOjR9.0WUfLuhjTVx63FmnlUQeU70BbYqBunX5CX5e8SQKC0E",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NzU2MTAwLCJpYXQiOjE2OTY3NTQzMDAsImp0aSI6IjYzMTBjZjgwZjg3YTRhMWJiZTk5NWExN2UzZDMxZjc1IiwidXNlcl9pZCI6NH0.MrJjPNznCq72aGeMP2tBg-rbsl8B4VOEtMh7MAJaHRU"
}
```

use access token as header :
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NzU2MTAwLCJpYXQiOjE2OTY3NTQzMDAsImp0aSI6IjYzMTBjZjgwZjg3YTRhMWJiZTk5NWExN2UzZDMxZjc1IiwidXNlcl9pZCI6NH0.MrJjPNznCq72aGeMP2tBg-rbsl8B4VOEtMh7MAJaHRU

```
we can use access token for 30 minutes and after that you can refresh it with refresh Token and POST method and this URL:
```
http://127.0.0.1:8000/accounts/token/refresh/
```

refresh Token is valid for one day after that new Token should be taken.




### The API has some restrictions:
-   The posts are always associated with a creator (user who created it).
-   Only authenticated users may create posts.
-   Only the creator of a post or comment may update or delete it.
-   The API doesn't allow unauthenticated requests.
