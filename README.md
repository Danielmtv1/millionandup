# Challenge Million And UP.
#### "Welcome to the Real Estate API designed to provide detailed information about properties in the United States.
"

![N|Solid](https://blog.pronus.io/images/python/fastapi_logo.svg)


## Features
The API offers a set of services to manage information related to properties, property owners, property images, and property history. Below are the key services available:

### 1. Create Property Building

This service allows you to add new properties to the database. Details of the building, such as location, and other relevant features, can be specified using this function.

### 2. Add Image from Property

With this service, you can attach images to a specific property. This is useful for visually showcasing relevant and attractive details of each property.

### 3. Change Price

This service enables you to update the price of an existing property. You can adjust prices according to market conditions or any changes in property valuation.

### CRUD for Main Entities

In addition to the mentioned services, the API includes CRUD (Create, Read, Update, Delete) operations for the main entities:

- Property Owner
- Property Image
- Property Trace

These CRUDs provide standard functionalities to efficiently manage property owners, images, and property history.
## Technology Stack

Our real estate API leverages a robust technology stack to ensure high performance, scalability, and efficient data management. Here are the key components:

- **MongoDB:** A NoSQL database that provides flexibility and scalability for handling diverse real estate data.

- **FastAPI:** A cutting-edge web framework for API development in Python 3.6+. Known for its speed, simplicity, and adherence to Python type hints for improved code quality.

- **Gunicorn:** A Python WSGI HTTP Server designed for UNIX systems, ensuring reliable and efficient handling of web requests.

- **Uvicorn:** The lightning-fast ASGI server that powers our API, delivering exceptional performance and responsiveness.

- **Pydantic:** Empowering data parsing through Python type annotations, Pydantic ensures robust input validation and serialization.

- **Python:** The core programming language driving our API, known for its versatility and extensive ecosystem, making it an ideal choice for a wide range of applications.

- **Poetry:** Serving as our dependency management and packaging tool, Poetry streamlines the development process for Python projects, enhancing project organization and dependency resolution.

This technology stack collectively forms the foundation of our real estate API, delivering a seamless and powerful experience for users and developers alike.


## Installation

To install, you need to clone the repository.Run the following command to set up and start the local server:

```sh
make api
```

This command automates the necessary setup processes and launches the local server. 

To run the test suite, use the following command:
```sh
make test
```
## Explore API Endpoints with Swagger

After initializing the API, you can explore and test the endpoints using Swagger. Simply navigate to the following URL in your web browser:

[Swagger Documentation](http://127.0.0.1:8000/docs)

This interactive documentation provides a user-friendly interface to understand and test the various API endpoints. Feel free to experiment with different parameters and make requests directly from Swagger.

### Search Endpoint
Search for items based on specific criteria. 
Only one field should be specified, while others should be left null.

## License

MIT

**Free Software**

[//]: # ()

  