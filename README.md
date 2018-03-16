# Tau Beta Pi Website
Our stack is using an nginx http server that reverse proxies to a Django backend, which communicates with a MySQL database.  

## Contributing
Check out the `backend` folder

## Folder organization
```
├── backend             # folder that has all Django code and configuration
├── docker-compose.yml  # configures how the Docker images interact
├── Makefile            # contains useful sitewide commands
├── media               # folder that contains all media files
├── nginx               
    └── nginx.conf      # configures the nginx HTTP engine
└── setup.tar.gz        # tar with initial database config and empty media files
```

## Makefile Commands
- `make build`
    - builds the Docker images (`backend` and `nginx`)
- `make run`
    - runs the Docker images with Docker Compose
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

