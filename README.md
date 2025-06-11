# Pet Spark
 A fullstack web application built using Svelte and Flask to help pets find loving owners.

# Running
Open two terminals, one for the front end and one for the back end.

## Front End
1. Install npm if you don't have it.
2. Install the following:
    1. vite:  `npm install vite`
    2. svelte-kit:  `npm install svelte-kit`
    3. auth0-spa-js: `npm install @auth0/auth0-spa-js`
3. Run `npm run dev`
4. Site should be hosted at `http://localhost:5173`

## Back End
1. Create andd activate a virtual python environment
	- Tutorial: https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/
2. Install the following:
    1. flask and flask_cors:  `pip install flask flask_cors`
    2. requests:  `pip install requests`
    3. dotenv:  `pip install dotenv`
    4. pymongo:  `pip install pymongo`
3. Run `python app.py`