# ETL_for_Sales
# Sales Data ETL Pipeline with Apache Airflow

This project implements an ETL (Extract, Transform, Load) pipeline using Apache Airflow to process Sales data from a CSV file, transform and load it into a MySQL database.

## Requirements

- Python 3.x
- Apache Airflow
- Pandas
- SQLAlchemy
- MySQL Server

## Installation

1. Install Apache Airflow following the official documentation: [Apache Airflow Installation Guide](https://airflow.apache.org/docs/apache-airflow/stable/installation.html).

2. Install required Python packages:

```bash
pip install pandas sqlalchemy 
```

3. Set up the MySQL database:

   - Install MySQL Server on your system if not already installed.
   - Create a new database to store the transformed data.
   - Note down the connection details, including the username, password, host, and database name.

## Usage

1. Clone this repository:

```bash
git clone https://github.com/Rekha-Varupula/ETL_for_Sales.git
cd ETL_for_Sales
```

2. Configure Airflow:
   - Open `airflow.cfg` (usually located in the `AIRFLOW_HOME` directory).
   - Set `dags_folder` to the path of the directory containing the DAG definition file (`sales_etl_dag.py`).
   - Configure the Airflow database to initialize and store the DAG metadata:

3. Access the Airflow UI:
   - Open a web browser and go to `http://localhost:8080`.
   - Enable the DAG by toggling the DAG switch in the Airflow UI.

4. Configure the DAG:
   - In the `sales_etl_dag.py` file, set the correct CSV file path in the `extract` function.
   - Set the MySQL database connection string (`db_connection_string`) and table name (`table_name`) in the `load` function.

5. Run the DAG:
   - Once the DAG is enabled in the Airflow UI, it will be scheduled to run daily according to the `schedule_interval` set in the DAG definition.
   - You can manually trigger the DAG to run immediately from the Airflow UI.

## Project Structure

```
sales-etl-pipeline/
|-- dags/
|   |-- sales_etl_dag.py
|-- scripts/
|   |-- extraction.py
|   |-- transformation.py
|   |-- loading.py
|-- data/
|   |-- sales_data.csv
|-- README.md
```

## Contributing

If you would like to contribute to this project or have any suggestions, feel free to submit a pull request or open an issue.
