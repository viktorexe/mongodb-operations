# MongoDB Operations Repository

Professional MongoDB operations toolkit with organized scripts for all common database tasks.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure `.env` file:
```
MONGO_URI=mongodb://localhost:27017/
```

## Complete File Structure

### Aggregation Operations/
- `aggregate_pipeline.py` - Execute custom aggregation pipelines on collections
- `group_by_field.py` - Group documents by a specific field and count occurrences

### Backup and Restore/
- `backup_collection.py` - Backup a single collection to JSON with timestamp
- `backup_database.py` - Backup entire database with all collections to timestamped folder
- `restore_database.py` - Restore database from backup directory

### Collection Management/
- `create_collection.py` - Create a new collection in a database
- `drop_collection.py` - Delete a collection with confirmation prompt
- `get_collection_stats.py` - Display collection statistics (size, count, indexes)
- `list_collections.py` - List all collections in a database
- `rename_collection.py` - Rename an existing collection

### Data Migration/
- `copy_collection.py` - Copy collection from one database to another
- `migrate_database.py` - Migrate entire database with all collections to new database

### Database Management/
- `create_database.py` - Create a new database with initial collection
- `drop_database.py` - Delete a database with confirmation prompt
- `get_database_stats.py` - Display database statistics (size, collections, indexes)
- `list_databases.py` - List all databases on MongoDB server

### Document Operations/
- `count_documents.py` - Count documents matching a query
- `delete_documents.py` - Delete documents matching a query with confirmation
- `find_documents.py` - Find and display documents with optional query and limit
- `insert_document.py` - Insert a single document into collection
- `update_documents.py` - Update multiple documents matching a query

### Download Data/
- `download_database.py` - Export entire database to JSON files in a directory
- `export_collection_csv.py` - Export collection to CSV file
- `export_collection_json.py` - Export collection to JSON file

### Index Management/
- `create_index.py` - Create an index on a field with optional unique constraint
- `drop_index.py` - Delete an index by name
- `list_indexes.py` - List all indexes on a collection

### Monitoring and Stats/
- `check_folder_size.py` - Calculate and display folder size in MB
- `get_server_status.py` - Display MongoDB server status and connection info

### Query Operations/
- `find_one_document.py` - Find and return a single document matching query
- `find_with_projection.py` - Find documents with specific fields only (projection)
- `find_with_sort.py` - Find documents with sorting by field (ascending/descending)

### Upload Data/
- `bulk_upload_documents.py` - Insert multiple documents from JSON array
- `import_csv_to_collection.py` - Import documents from CSV file to collection
- `import_json_to_collection.py` - Import documents from JSON file to collection

### User Management/
- `list_users.py` - List all users and their roles in a database

### Utilities/
- `config.py` - MongoDB connection configuration and helper functions
- `helpers.py` - Utility functions for file operations and size calculations
- `__init__.py` - Package initialization file

## Usage Examples

```bash
# List all databases
python "Database Management/list_databases.py"

# Export collection to JSON
python "Download Data/export_collection_json.py"

# Find documents with query
python "Document Operations/find_documents.py"

# Backup entire database
python "Backup and Restore/backup_database.py"
```

## Features

- 40+ specialized scripts for MongoDB operations
- Clean separation of concerns with organized folders
- Reusable configuration module
- Input validation and confirmations for destructive operations
- Proper error handling
- Timestamped backups
- Support for JSON and CSV formats
- Professional code structure
