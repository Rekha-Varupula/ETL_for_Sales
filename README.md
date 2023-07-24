# ETL_for_Sales
# Sales Data ETL Pipeline with Apache Airflow

This project implements an ETL (Extract, Transform, Load) pipeline using Apache Airflow to process Sales data from a CSV file, transform and load it into a MySQL database.

## Requirements

- Python 3.x
- Apache Airflow
- Docker(optional)
- Pandas
- SQLAlchemy
- MySQL Server

## Installation

1. Install Apache Airflow following the official documentation: [Apache Airflow Installation Guide](https://airflow.apache.org/docs/apache-airflow/stable/installation.html).

2. Installed Apache Airflow with Docker, I haven't used Docker specifically.(Only installed for the purpose of Airflow).

3. Install required Python packages:

```bash
pip install pandas sqlalchemy
```

4. Set up the MySQL database:

   - Install MySQL Server on your system if not already installed.
   - Create a new database to store the transformed data.
   - Note down the connection details, including the username, password, host, and database name.

## Usage

1. Clone this repository:

```bash
git clone https://github.com/Rekha-Varupula/ETL_for_Sales.git
cd ETL_for_Sales
```

2. Access the Airflow UI:
   - Open a web browser and go to `http://localhost:8080`.
   - Enable the DAG by toggling the DAG switch in the Airflow UI.

3. Configure the DAG:
   - In the `sales_etl_dag.py` file, set the correct CSV file path in the `extract` function.
   - Set the MySQL database connection string (`db_connection_string`) and table name (`table_name`) in the `load` function.

4. Run the DAG:
   - Once the DAG is enabled in the Airflow UI, it will be scheduled to run daily according to the `schedule_interval` set in the DAG definition.
   - You can manually trigger the DAG to run immediately from the Airflow UI.

5. Extraction.py:
   - Considered a Sales dataset from Kaggle and converted into CSV file.

6. Transformation.py:
   - Filtered the required features of the dataset and dropped all the unnecessary columns.
   - Merged the similar columns into a single column (ADDRESS, CONTACTNAME).
   - Transformed the columns(DATE) that are having multiple formats in a single column and verified if all the data in the columns are homogenous or not.
   - Verified if there are any null values and duplicate values in the dataset.

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
