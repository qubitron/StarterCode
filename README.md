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
npm run install
npm run build
```

2. Select your Python runtime.

Open a python file (.py) from within your VS Code window.

At the bottom right of the VS Code window, click on the "Select Python Evnrionmnt" button to choose your newly created Python virtual environment

![](https://i.imgur.com/y1LShjR.png)

3. Create the SQL database

Open the VS Code terminal by using the keyboard shortcut "Ctrl" + "\`".

```bash
python manage.py create_db
```

4. Start the Flask server
```bash
python manage.py runserver
```

4. Check ```localhost:5000``` in your browser to view the web application.

## 3. Deploying The Code To Azure

1. Go to the extensions tab on VS Code

2. Install the recommended extensions that show up (App Service Extension, Python Extension)

3. Reload the window and navigate to the Azure tab on the left

4. Access Azure services through either (1) clicking on "Sign in to Azure..." to sign in with an existing azure account or (2) clicking "Create a Free Azure Account..." which brings you to the Azure web portal to allow you to create a free account with Azure

![](https://i.imgur.com/HZebZhX.png)

5. Create an App Service instance 

On the Azure tab in VS Code, click the "+" button at the top to create a new App Service instance

![](https://i.imgur.com/HZebZhX.png)

A popup should appear asking for a name for the new web app. Enter a unique name for this new application and then press the "Enter" key. For example, "vs-code-test".

![](https://i.imgur.com/psEAyoa.png)

On the next screen, select "Python 3.7 " as the runtime.

![](https://i.imgur.com/3qW0CpR.png)

A notification should popup on the bottom right of your VS Code window indicating your new App Service instance is being created.

![](https://i.imgur.com/fuOVnfu.png)

Once the instance has been created, a notification will popup on the bottom right of your VS COde window indicating that the creation of the App Service instance was successful.

![](https://i.imgur.com/EZk6SXO.png)

6. Create a PostgreSQL database with Azure Database for Postgres and connect it to the App Service instance.

Install the Azure CLI: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest

Configure your Azure Database for Postgres instance by opening up the file "envvars.py" and filling in the values for the variables: "POSTGRES_SERVER_NAME", "POSTGRES_ADMIN_USER", "POSTGRES_ADMIN_PASSWORD", and "APP_DB_NAME"

POSTGRES_SERVER_NAME represents a unique name for your Postgres server in Azure

POSTGRES_ADMIN_USER represents the username for the admin account to the Postgres server (which will be used to login by the web application)

POSTGRES_ADMIN_PASSWORD represents the password for the admin account (remember to never commit this file to Github). The guidelines for the password are as follows: "A new password for the server admin account. It must contain between 8 and 128 characters. Your password must contain characters from three of the following categories: English uppercase letters, English lowercase letters, numbers (0 through 9), and non-alphanumeric characters (!, $, #, %, etc.)."

APP_DB_NAME represents a name for the database in your Postgres server

Open the terminal window from within VS Code by using the keyboard shortcut "Ctrl + \`".

Run the command:
```bash
python createdb.py
```

7. Connect your Postgres instance to your App Service instance

Navigate back to the Azure tab in VS Code. 

Click on your newly created App Service instance to expand it. 

Right click on the "Application Settings" option in your expanded App Service instance.

![](https://i.imgur.com/mqLqytz.png)

Select "Add New Setting" from the menu options.

In the "Enter new setting key" popup, enter the environment variable name "DATABASE_URL" and press enter to continue

In the "Enter setting value" popup, enter the value of your Postgres connection string to your Azure Database for Postgres instance. The format of the string is as follows: postgres://[USERNAME]@[SERVER_NAME]:[PASSWORD]@[SERVER_NAME].postgres.database.azure.com:5432/postgres

For example: postgres://vs_code_user@vs_code_postgres:password@vs_code_postgres.postgres.database.azure.com:5432/postgres

8. Configure the startup script.

On the Azure tab in VS Code, right click on your App Service instance.

Click "Open in portal". This should open up your browser and redirect you to the configuration page for your App Service instance.

Under the "Application Settings" tab and in the "Runtime" textfield, enter the value "startup.txt" in the field. This way, App Service will run the "startup.txt" file specifically generated for this project.

![](https://i.imgur.com/wKGgMz1.png)

![](https://i.imgur.com/MEqyU2g.png)

9. Deploy the code to your newly created App Service instance

On the Azure tab in VS Code, click on the upload button at the top of the extension pane

![](https://i.imgur.com/FlX1XJL.png)

Select the the name of the App Service instance you created in the previous steps

Select the root folder (the first item on the menu) to deploy

A notification should appear on the bottom right of the VS Code window showing that the deployment to your App Service instance is now in progress

![](https://i.imgur.com/y1LShjR.png)

When the deployment is complete, a notification on the bottom right of the VS Code window will show saying that "Deployment sucessful".

From there, click on the "Browse Website" button from within the notification to view the website live in your browser.
