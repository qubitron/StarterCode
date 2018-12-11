# Python Flask app on Azure Web App for Containers

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux.

For more information, please see the [Python on App Service quickstart](https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python).

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Tutorial

## 1. Setting Up The Project

1. Clone the reponsitory
```bash
git clone https://github.com/jeffreymew/StarterCode.git
cd StarterCode
```

2. Create and activate a virtual environment

In Bash
```bash
python3 -m venv venv
source venv/bin/activate
```

In Powershell
```Powershell
py -3 -m venv env
env\scripts\activate
```

3. Install requirements.txt
```bash
pip install -r requirements.txt
```

4. Import and open the project folder into VS Code
```bash
code .
```

## 2. Running The Code Locally

1. Build the react.js front-end.
```bash
cd static
npm install
npm run build
```

2. Create the PostgreSQL database
```bash
cd ..
python manage.py create_db
```

3. Start the Flask server
```bash
python manage.py runserver
```

4. Check ```localhost:5000``` in your browser to view the web application.

## 3. Deploying The Code To Azure

1. Go to the extensions tab on VS Code

2. Install the recommended extensions that show up (App Service Extension, Python Extension)

3. Reload the window and navigate to the Azure tab on the left

4. Access Azure services through (1) Guest Mode, (2) Creating a free Azure account or (3) signing into Azure with an existing account

5. Create an App Service instance with the parameters of a linux system with a Python runtime

6. Create a PostgreSQL database with Azure Database for Postgres and connect it to the App Service instance

7. Navigate to the Azure portal for the Azure Database for Postgres instance and allow incoming connections to the instance for everyone 

8. Navigate to the Azure portal for the App service instance that was just created, and under the "Application Settings" tab and uneder the "Runtime" section, set the "startup file" parameter to be "startup.txt"

9. Again under the "Application Settings" tab and under the "Application Settings" section, add a new environment variable for the Postgres 

10. Deploy the code to your newly created App Service instance
