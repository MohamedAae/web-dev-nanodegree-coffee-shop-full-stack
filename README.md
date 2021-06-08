# **Coffee Shop Full Stack**
 **A virtual coffee shop** offers caffeine drinks. It helps baristas to view the details of drinks added by the managers. This project is a part of my udacity web development Nanodegree.v

 The project adheres to the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) and follows *common best practices* including, using clear function and variables names.


## Getting Started
___
### **Techincal Stack**
The projects needs **`Python3`**, **`pip`**, **`node`**, and **`npm`** to run.

### *Backend Dependencies /*
The project requires Python >= **3.7**, it is recommended to set up a virtual environment for your project, this [guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) will help you set it up.

&mdash; **Key Dependencies**
- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQLite database.
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) handles cross-origin requests from our frontend server.

&mdash; **Running backend server**

From within the `backend` directory first, ensure you are working using your created virtual environment.

install dependencies by naviging to the /backend directory and running:
```
pip install -r requirements.txt
```

To run the server, execute:
```bash
export FLASK_APP=api.py;
export FLASK_ENV=development;
flask run;
```

### *Frontend Dependencies /*
This project depends on Nodejs, Ionic and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

&mdash; **Installing Ionic Cli**

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI is in the Ionic Framework Docs.

&mdash; **Installing dependencies**

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```
&mdash; **Configure Environment Variables**

onic uses a configuration file to manage environment variables. These variables ship with the transpiled software and should not include secrets.

Open `./src/environments/environments.ts` and ensure each variable reflects the system you stood up for the backend.

&mdash; **Running Your Frontend in Dev Mode**

Ionic ships with a useful development server which detects changes and transpiles as you work. The application is then accessible through the browser on a localhost port. To run the development server, cd into the frontend directory and run:
```
ionic serve
```

## Auth0
___
## *Test Credentials* &mdash;
```
AUTH0_DOMAIN = 'udacitycf-fsnd.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'udacity-coffee-shop'
```

## *Barista JWT* &mdash;
### Permissions Available
- `get:drinks-detail`
### Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmeWxaWUNuZXJmZ0ZTVmJPV3VHRCJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHljZi1mc25kLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDU2YTlhNjc5NGIxZTAwNmIwNzRmNjMiLCJhdWQiOiJ1ZGFjaXR5LWNvZmZlZS1zaG9wIiwiaWF0IjoxNjE2Mjk0MzgxLCJleHAiOjE2MTYzMDE1ODEsImF6cCI6IkMxOG92NkhTaXl4d3BNdEI3ZmFBNWNlM0ZlTkY1eWQ2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.c7wlfogSoenQvmpgW6UNppdOqnItTcinH-OuCqp81q2HEY8Ztv0vA-vkvdjFwhhUcdryqgZggxqxFx9QjMAEtueAgjGaoM5AJytvFb7g0etWxoWerHzp01yq3W55wUXa1xRYQKBpgLmsa46niMsAlvhDftvwueSdLo38CNA7tdU909n2Y6DFDOw25AmDknlU2NugWap_X_yOLehU9jiTIQltL-l24o2wc1Q4VXxR-_EtraIoUmbneZjb8JzbvYrpAiEEr9jnZP_z1Si6Fk_mfM9Jo3kRQfCEQ_y93aEqwy_uM3t_z84Jean95uiIQ32hCf135IMHSBY_3X5asBsuPQ
```

## *Manager JWT* &mdash;
### Permissions Available
- `get:drinks-detail`
- `post:drinks`
- `patch:drinks`
- `delete:drinks`
### Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZmeWxaWUNuZXJmZ0ZTVmJPV3VHRCJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHljZi1mc25kLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDU2YTlkODNhZDU3YTAwNjkxZjg0MTgiLCJhdWQiOiJ1ZGFjaXR5LWNvZmZlZS1zaG9wIiwiaWF0IjoxNjE2Mjk0NTA2LCJleHAiOjE2MTYzMDE3MDYsImF6cCI6IkMxOG92NkhTaXl4d3BNdEI3ZmFBNWNlM0ZlTkY1eWQ2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.L0hXchv4LjsgiEAmjX5iwubJ23cUSCTtOA6NrFwKgTXpCT9k-PYTwyuRgcFeMHR0trTBmdYiPMd5N0Y1VK4mkq20DGRqCo1AC4c6Ww-AFatghD8Hy03DgTvRcq4IxRv9wFklmghWzZQ9KqXl4ABAXWpsOivyB5n1lcFPqhTgR20ehEWa2iw1X11kr1DdMIKgMplE9vYiWiYRf32oCUlenVO792k3hX-ccZEUbPBYGNw05qR-qok9NHrSVYEHAVeWtIdAPRrbFjbbFvi4fH4-BtmrvphYwddut1Q_yC1urSvWYU4taZx4BjZVwN6wmJlZrlK7k763LqcljD9AyF8LTg
```

## References
___
- [Auth0 Docs](https://auth0.com/docs/quickstart/backend/python/01-authorization)
- [Basic Flask Auth Github](https://github.com/udacity/FSND/blob/master/BasicFlaskAuth)
