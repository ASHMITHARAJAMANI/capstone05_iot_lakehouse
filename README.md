Capstone 05 – IoT Equipment Reliability and Predictive Maintenance

1. Project Overview

This project aims to build an end-to-end data engineering solution using Azure Databricks to process IoT sensor data and support equipment reliability and predictive maintenance.

The main objective is to reduce unplanned equipment downtime by ingesting, processing and analyzing sensor readings, equipment status changes and maintenance-related events.

2. Project Objectives

- Ingest IoT sensor data from ADLS Gen2.
- Load reference entities from Azure SQL Database or approved CSV extracts.
- Implement the Medallion Architecture (Bronze, Silver and Gold).
- Maintain data quality and source lineage.
- Identify abnormal sensor readings.
- Calculate equipment availability and maintenance downtime.
- Build reliable and restart-safe data pipelines.

3. Technologies Used

- Azure Databricks
- Azure Data Lake Storage Gen2 (ADLS)
- Azure SQL Database
- PySpark
- Python
- Delta Lake
- Unity Catalog
- Databricks Auto Loader
- Databricks Workflows
- Git and GitHub

4. Team Members and Responsibilities

Member| Role| Responsibility
M1| Technical Lead| Architecture, Unity Catalog and design
M2| Ingestion Engineer| Auto Loader and Bronze ingestion
M3| Quality Engineer| Data profiling and quality checks
M4| Analytics Engineer| Data dictionary and KPI definitions
M5| DataOps Engineer| GitHub, testing, monitoring and documentation

5. Repository Structure

capstone05-iot-lakehouse/
│
├── README.md
├── .gitignore
│
├── .github/
│   └── pull_request_template.md
│
├── config/
│   └── project_config.py
│
├── notebooks/
│   ├── 00_setup/
│   │   └── 01_uc_setup
│   ├── 01_bronze/
│   │   └── 01_ingest_bronze
│   └── 02_profiling/
│       └── 01_source_profile
│
├── tests/
│   └── test_bronze_contract
│
└── docs/
    ├── brs.md
    ├── hld.md
    ├── lld.md
    ├── erd.md
    ├── source_to_target.md
    ├── source_qa_summary.md
    ├── data_dictionary.md
    ├── kpi_definitions.md
    ├── decision_log.md
    └── raid_log.md

6. Day 1 Execution Order

Execute the notebooks in the following order:

1. "notebooks/00_setup/01_uc_setup"
   
   - Create Unity Catalog schemas.
   - Configure landing and checkpoint volumes.

2. "notebooks/01_bronze/01_ingest_bronze"
   
   - Load source files using Databricks Auto Loader.
   - Add source file metadata and ingestion timestamps.
   - Populate Bronze Delta tables.

3. "tests/test_bronze_contract"
   
   - Validate Bronze record counts.
   - Check required columns.
   - Validate source lineage.
   - Verify duplicate preservation.
   - Perform ingestion replay tests.

4. "notebooks/02_profiling/01_source_profile"
   
   - Profile source data.
   - Analyze missing values, duplicates and extreme values.
   - Validate key coverage.

7. Git Branching Strategy

Branch| Purpose
main| Stable project code
feature/m1-design-uc-setup| M1 development
feature/m2-bronze-autoloader| M2 development
feature/m3-source-profiling| M3 development
feature/m4-data-dictionary| M4 development
feature/m5-repo-tests| M5 development

All changes must be submitted through Pull Requests and reviewed before merging.

8. Data Architecture

The project follows the Medallion Architecture:

- Bronze: Raw source data with lineage metadata.
- Silver: Cleaned and validated data.
- Gold: Business-ready facts, dimensions and KPI datasets.

9. DataOps Responsibilities

- Maintain GitHub repository and folder structure.
- Establish branch naming conventions.
- Maintain Pull Request templates and review checklists.
- Develop automated Bronze contract tests.
- Validate ingestion completeness and restart safety.
- Maintain decision logs and RAID logs.
- Support reliable project delivery.

10. Important Guidelines

- Do not modify original source files.
- Do not clean or deduplicate Bronze data.
- Never commit CSV files or credentials to GitHub.
- Use shared configuration instead of hard-coded paths.
- Document technical decisions and known limitations.
- Perform testing before submitting Pull Requests.

11. Project Status

Current Phase: Day 1 – Discovery, Architecture and Ingestion.

Project Status: In Progress.

12. Expected Day 1 Outcome

- GitHub repository established.
- Project folder structure created.
- Branch naming rules documented.
- Pull Request checklist configured.
- Bronze contract tests implemented.
- Decision log and RAID log maintained.
- Five Bronze tables validated.
- First ingestion micro-batch demonstrated.
