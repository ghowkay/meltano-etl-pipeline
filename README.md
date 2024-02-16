# SpaceX Data ETL Pipeline Project using Meltano

This project is an ETL pipeline built using Meltano for extracting data from SpaceX and loading it into a PostgreSQL database. It includes a custom SpaceX connector and is designed to run in a Docker environment, leveraging Docker Compose and virtual environments (venv) for isolation and reproducibility.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose
- Python (with venv)
- Meltano


### Set Up the Environment
1. Clone the repository:
   ```bash
     git clone https://github.com/ghowkay/meltano-etl-pipeline.git
     cd meltano-etl-pipeline

     cd postgres_db && docker-compose up -d  # run postgres db

      meltano run spacex_etl   #run ETL job


### Future enhancements

1. Add CI/CD pipeline to run dbt tests on models for Data Validation.
2. Use environment variables to configure sensitive credentials
3. Optimized the data extraction and loading process for large datasets using incremental loading for example.


## Acknowledgments

- SpaceX API
- Meltano Project
- Contributors and maintainers of this project