# AI FAQ Chatbot

An AI-powered FAQ chatbot built with FastAPI, SQLAlchemy, and PostgreSQL.  
It stores frequently asked questions in a PostgreSQL database, generates answers using a language model, and serves them through a REST API.

---

## Project Description

This project provides a simple yet powerful chatbot API to answer user questions. It first checks the database for existing answers and generates new ones if needed. It uses PostgreSQL with a custom schema to manage FAQs and Alembic for database migrations.

---

## Features

- Store and retrieve FAQs from a PostgreSQL database with a dedicated schema.
- Generate answers dynamically via an integrated language model.
- RESTful API built with FastAPI.
- Database schema managed with Alembic migrations.



