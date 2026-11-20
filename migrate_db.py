
from sqlalchemy import inspect, text
from app.database import engine

inspector = inspect(engine)
existing_columns = [column["name"] for column in inspector.get_columns("feedback")]

with engine.begin() as connection:

    if "email" not in existing_columns:
        connection.execute(text(
            "ALTER TABLE feedback ADD COLUMN email VARCHAR"
        ))

    if "confidence_score" not in existing_columns:
        connection.execute(text(
            "ALTER TABLE feedback ADD COLUMN confidence_score FLOAT"
        ))

    if "updated_at" not in existing_columns:
        connection.execute(text(
            "ALTER TABLE feedback ADD COLUMN updated_at DATETIME"
        ))

    connection.execute(text(
        "UPDATE feedback SET updated_at = CURRENT_TIMESTAMP WHERE updated_at IS NULL"
    ))

print("Database migration completed successfully!")
