# MongoDB Operations Repository

Professional MongoDB operations toolkit with organized scripts for all common database tasks.

## Setup

1. Install dependencies:
```bash
pip install pymongo python-dotenv
```

2. Configure `.env` file:
```
MONGO_URI=mongodb://localhost:27017/
```

## Folder Structure

- **Database Management** - Create, drop, list databases and get stats
- **Collection Management** - Create, drop, rename, list collections and get stats
- **Document Operations** - Insert, find, update, delete, count documents
- **Download Data** - Export collections and databases to JSON/CSV
- **Upload Data** - Import data from JSON/CSV files
- **Backup and Restore** - Backup and restore databases/collections
- **Index Management** - Create, drop, list indexes
- **Query Operations** - Advanced queries with sort, projection
- **Aggregation Operations** - Group by, custom pipelines
- **Data Migration** - Copy/migrate collections and databases
- **User Management** - List and manage users
- **Monitoring and Stats** - Server status, folder size checks
- **Utilities** - Shared configuration and helper functions

## Usage

Navigate to any folder and run the desired script:

```bash
python "Database Management/list_databases.py"
python "Download Data/export_collection_json.py"
python "Document Operations/find_documents.py"
```

## Dependencies

- pymongo
- python-dotenv
- bson

## Features

- Clean separation of concerns
- Reusable configuration module
- Input validation and confirmations
- Proper error handling
- Timestamped backups
- Support for JSON and CSV formats
