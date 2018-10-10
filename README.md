# Tau Beta Pi Website
Our stack is using an nginx http server that reverse proxies to a Django backend, which communicates with a MySQL database.  

## Setting up for Local Development
In order to set up docker containers for local development, the following steps should be followed. If a step doesn't make sense or if you don't know where to locate a required file, feel free to ask.
1. Git clone the repo.
2. Run `make build` to set up the initial Docker images.
3. Run `make run-dev` to bring up Docker containers for the backend, database, and nginx.
4. Run `make init_db` with a relevant `init.sql` file (made with `mysqldump`).
5. Run `make collect_static` to collect static files into STATIC_ROOT.
6. Optionally, move any desired media files into the media folder (tests, resumes, etc.). 

## Contributing
Check out the `backend` folder

## Folder organization
```
├── backend             # folder that has all Django code and configuration
├── docker-compose.yml  # configures how the Docker images interact
├── Makefile            # contains useful sitewide commands
├── media               # folder that contains all media files
├── nginx               
    └── dev.conf        # configures the nginx HTTP engine on dev
    └── prod.conf       # configures the nginx HTTP engine on prod
└── setup.tar.gz        # tar with initial database config and empty media files
```

## Makefile Commands
- `make build`
    - builds the Docker images (`backend` and `nginx`)
- `make run-dev`
    - runs the Docker images with Docker Compose using configurations for a dev environment
- `make run-prod`
    - runs the Docker images with Docker Compose using configurations for a prod environment
- `make restart`
    - restarts the backend container
- `make shell`
    - interactively runs the `./manage.py shell` command in the `backend` container
- `make clean_db`
    - wipes the whole database.  please run with caution
- `make collect_static`
    - runs the `./manage.py collectstatic` command.  Don't worry about it if you don't get it
- `make init_db`
    - wipes the whole database and initializes it with the `init_db.sql` in the root
- `make untar_setup`
    - untars the `setup.tar.gz`
- `make init`
    - initializes the database and the media files necessary to run the server
- `make backup_db`
    - backs up the database
- `make install_package pkg=$PACKAGE_NAME`
    - installs a package into the `backend` container and adds it to the requirements file

