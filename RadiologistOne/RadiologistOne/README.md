## Getting Started

In the root directory of the project...

1. Install node modules `yarn install` or `npm install`.
2. Install Python dependencies `yarn install-requirements` or `npm install-requirements`
2. Start development server `yarn start` or `npm start`.

## Next Steps


### Sample Data

Replace the sample data stored in /server/sampleData.py.
Replace the default images stored in /src/images.



### Adding a New Page

1. Create a file in `/src/views` with your Vue Template.
2. Add a route for your page to `/src/router/index.js`.
3. Add a button to the navigation bar in `/src/components/TheNavBar.vue`.


### Deployment

If you selected Azure App Service when creating your project, follow these steps:

1. Press `Ctrl + Shift + P` in Windows/Linux or `Shift ⇧ + Command ⌘ + P` in Mac and type/select `Web Template Studio: Deploy App` to start deploying your app.
2. After your project is built, click on "server" in the pop up on the top middle section of your screen, and then click "Deploy" on the window pop up.
3. Once the deployment is done, click "Browse website" in the notification window on the lower right corner to check out your newly deployed app.

If you did not select Azure App Service and want to create a new Azure App Service web app, follow these steps:

1. Press `Ctrl + Shift + P` in Windows/Linux or `Shift ⇧ + Command ⌘ + P` in Mac and type/select `Azure App Service: Create New Web App...` to create a new web app.
   - Select your subscription
   - Enter your web app name
   - Select Linux as your OS
   - Select Node.js 10.14 for a Node/Express application, Python 3.7 for a Flask application
2. Once the creation is done, click "Deploy" in the notification window on the lower right corner.
   - Click "Browse" on the top middle section of your screen and select the server folder within your project
   - Click "Yes" in the notification window on the lower right corner (build prompt)
   - Click "Deploy" on the window pop up
   - Click "Yes" in the notification window on the lower right corner again
3. Once the deployment is done, click "Browse website" in the notification window on the lower right corner to check out your newly deployed app.

Consider adding authentication and securing back-end API's by following [Azure App Service Security](https://docs.microsoft.com/en-us/azure/app-service/overview-security).

Full documentation for deployment to Azure App Service can be found here: [Deployment Docs](https://github.com/Microsoft/WebTemplateStudio/blob/dev/docs/deployment.md).


### Cosmos Database

**Do Not share the keys stored in the .env file publicly.**
The Cosmos database will take approximately 5 minutes to deploy. Upon completion of deployment,
a notification will appear in VS Code and your connection string will be automatically added in
the .env file. The schema and operations for the Cosmos database are defined in `/server` folder.
Additional documentation can be found here: [Cosmos Docs](https://github.com/Microsoft/WebTemplateStudio/blob/dev/docs/services/azure-cosmos.md).

## File Structure

The front-end is based on [Vue CLI](https://cli.vuejs.org/).

The back-end is based on [Flask](https://github.com/pallets/flask).

The front-end is served on http://localhost:3000/ and the back-end on http://localhost:3001/.

```
.
├── server/ - Flask server that provides API routes and serves front-end
│ ├── sql/ - Handles all interactions with the cosmos database
│ ├── constants.py - Defines the constants for the endpoints and port
│ ├── sampleData.py - Contains all sample text data for generate pages
│ └── server.py - Configures Port and HTTP Server and provides API routes
├── src - Vue front-end
│   ├── assets/                     - Default images
│   ├── components/                 - Common Vue components shared between different views
│   ├── router/                     - Vue routes
│   ├── views/                      - The main pages displayed
│   ├── constants.js                - Contains constants for error messages and endpoints
│   ├── App.vue                     - Base Vue template
│   └── main.js                     - Root Vue Component
└── README.md
```

## Additional Documentation


- Vue - https://vuejs.org/v2/guide/
- Vue Router - https://router.vuejs.org/

- Bootstrap CSS - https://getbootstrap.com/
- Flask - http://flask.pocoo.org/


- Cosmos DB - https://docs.microsoft.com/en-us/azure/cosmos-db/create-sql-api-python

  This project was created using [Microsoft Web Template Studio](https://github.com/Microsoft/WebTemplateStudio).
