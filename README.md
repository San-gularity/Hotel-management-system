## Django Hotel Management System API

### Description:

The "Django Hotel Management System API" is a comprehensive solution that allows users to manage room bookings and retrieve relevant information using secure custom API endpoints. The application provides a robust and optimized system for hotel administrators to efficiently handle room availability, category-specific bookings, and guest details.

The project follows clean coding practices and optimal design patterns to ensure maintainability and extensibility. The database schema is carefully designed to cater to the requirements of the hotel management system, allowing for efficient retrieval of data using SQL queries.

The API provides three main endpoints to fulfill the specified requirements:

1. Book Room API: A secure POST request endpoint that allows users to book a room for a specific category within a given date range. The API validates and stores the booking details securely in the database.

2. Room Availability API: This endpoint provides information about the number of available rooms for each category during a specific date range. The API leverages SQL queries to efficiently retrieve and display the results, allowing hotel administrators to manage room availability effectively.

3. Category Availability API: This endpoint returns the number of available rooms for a specific category within a given date range. The API utilizes optimized SQL queries to retrieve the relevant information from the database, empowering administrators with accurate data for decision-making.

To ensure security, the project implements a custom authentication mechanism rather than relying on Django's built-in mechanisms. This ensures that only authorized users can access the APIs and perform the necessary operations.

The GitHub repository for the Django Hotel Management System API provides a detailed README file, explaining the project setup, API documentation, and guidelines for customization. The repository demonstrates the effective use of Django, SQL queries, and secure API development, making it a valuable resource for building similar hotel management systems.
