1. Configuring enviromnent:
    1. install [docker compose](https://docs.docker.com/compose/install/) for your operation system.
    :warning: **At some systems the command can be docker compose, without hyphen.**
    2. Run `docker-compose build`. 

2. Start services
    1. Just run `docker-compose up`.


3. Accessing the UIs:
    1. [Airflow](http://localhost:8080) **username**:airflow and **password**:airflow
    2. [JupyterLab](http://localhost:8888/)
    3. [PgAdmin](http://localhost:8081/browser/) **email**:admin@admin.com and **password**:password.
    3.1. For PgAdmin you will need to create a connection with postgres at first usage. To do this:
    3.1.1. Click on 'Add New Server' button.
    3.1.2. Give a name to the connection and put the follow configuration at **Connection** tab:
    ``` 
        Host name/address:  postgres_clever 
        port:  5432
        Username:  clever 
        Password:  clever 

4. To actually run the pipeline, go to Airflow, click at **clever_main_DAG** and enable it. If after a couple minutes it does not start, manual start the pipeline (click at top right 'play' button).

5. That's it, after a few seconds you should have data at postgres to play with.