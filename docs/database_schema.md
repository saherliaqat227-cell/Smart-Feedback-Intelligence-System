# Database Schema
## Smart Feedback Intelligence System

This project uses SQLite as its database and SQLAlchemy as the Object Relational Mapper (ORM) for database management.

## 1. Users Table

The Users table stores registered user information.

| Column | Data Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| username | String | User name |
| email | String | User email |
| hashed_password | String | Securely stored hashed password |

## 2. Feedback Table

The Feedback table stores customer feedback and its sentiment prediction results.

| Column | Data Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| customer_name | String | Customer name |
| email | String | Customer email address |
| feedback_text | Text | Submitted customer feedback |
| sentiment | String | Predicted sentiment: Positive, Negative or Neutral |
| confidence_score | Float | Model prediction confidence score |
| user_id | Integer | Foreign Key referencing Users.id; nullable |
| created_at | DateTime | Feedback creation date and time |
| updated_at | DateTime | Last update date and time |

## 3. Relationship

The Users and Feedback tables have a conceptual one-to-many relationship.

One user can be associated with multiple feedback records.

The `user_id` column in the Feedback table references the `id` column in the Users table.

The `user_id` field is nullable, so a feedback record can also exist without an associated user.

## 4. Database Configuration

- Database Name: `smart_feedback.db`
- Database Type: SQLite
- ORM: SQLAlchemy

## 5. Database Design Purpose

The database is designed to:

- Store registered users securely.
- Store customer feedback information.
- Save predicted sentiment labels.
- Store model confidence scores.
- Maintain feedback creation and update timestamps.
- Connect feedback records with users through a foreign key.

