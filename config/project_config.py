==================================================

Capstone 05 - IoT Equipment Reliability

Project Configuration

Owner: M5 - DataOps Engineer

==================================================

Unity Catalog Configuration

CATALOG = "your_catalog_name"
SCHEMA = "bronze"

Bronze Table Names

BRONZE_TABLES = {
"sensor_events": "bronze_sensor_events",
"status_cdc": "bronze_status_cdc",
"secondary_events": "bronze_secondary_events",
"plant_reference": "bronze_plant_id",
"machine_reference": "bronze_machine_id"
}

Source Volume Configuration

SOURCE_VOLUME = "/Volumes/your_catalog_name/your_schema/your_volume"

Auto Loader Configuration

SCHEMA_LOCATION = SOURCE_VOLUME + "/schema"
CHECKPOINT_LOCATION = SOURCE_VOLUME + "/checkpoint"

Ingestion Metadata Columns

SOURCE_FILE_COLUMN = "_source_file"
INGESTION_TIMESTAMP_COLUMN = "_ingest_ts"
