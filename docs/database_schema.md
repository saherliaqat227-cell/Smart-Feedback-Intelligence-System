
# Database Schema
## Smart Feedback Intelligence System

This project uses SQLite as its database and SQLAlchemy for database management.

### 1. Users Table

| Column | Data Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| username | String | User name |
| email | String | User email |
| hashed_password | String | Securely stored password |

### 2. Feedback Table

| Column | Data Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| customer_name | String | Customer name |
| feedback_text | Text | Customer feedback |
| sentiment | String | Positive, Negative or Neutral |
| user_id | Integer | Foreign Key referencing Users |
| created_at | DateTime | Feedback creation date and time |

### 3. Relationship

One user can have multiple feedback records.

The `user_id` column in the Feedback table references the `id` column in the Users table.

### 4. Database

Database Name: smart_feedback.db

Database Type: SQLite

ORM: SQLAlchemy
