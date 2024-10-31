from sqlalchemy.exc import IntegrityError, SQLAlchemyError


class BaseService:
    def __init__(self, crud_class):
        self.crud = crud_class

    def create(self, database, data):
        """Create new record."""
        try:
            return self.crud.create(database, data)
        except IntegrityError as e:
            database.rollback()
            raise ValueError(f"Error: {e.args}")

    def get_all(self, database):
        """Retrieve all records."""
        try:
            return self.crud.get_all(database)
        except SQLAlchemyError as e:
            print(f"Error: {e.args}")
            return []

    def get_by_id(self, database, object_id):
        """Retrieve a record by its ID."""
        try:
            record = self.crud.get(database, object_id)
            if not record:
                raise ValueError(f"{record} not found.")
            return record
        except SQLAlchemyError as e:
            raise ValueError(f"Error: {e.args}")

    def update(self, database, object_id, data):
        """Update an existing record."""
        try:
            record = self.get_by_id(database, object_id)
            if not record:
                raise ValueError(f"Record {object_id} does not exist.")
            return self.crud.update(database, object_id, data)
        except IntegrityError as e:
            database.rollback()
            raise ValueError(f"Error updating record: {e}")

    def delete(self, database, record_id):
        """Delete a record by its ID."""
        try:
            record = self.crud.get(database, record_id)
            if not record:
                raise ValueError(f"Record {record_id} does not exist.")
            return self.crud.delete(database, record_id)
        except IntegrityError as e:
            database.rollback()
            raise ValueError(f"Error deleting record: {e}")
