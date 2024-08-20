## TODO Project API Endpoints

**Endpoints:**

* `/api/todos/:id/`
* `/api/todos/`

**Methods:**

* **GET `{{URL}}/api/todos/`**
    * Retrieves a list of all TODOs.
* **GET `{{URL}}/api/todos/:id/`**
    * Retrieves a single TODO with the specified ID.
* **POST `{{URL}}/api/todos/`**
    * Creates a new TODO.
* **PUT `{{URL}}/api/todos/:id/`**
    * Updates the entire TODO with the specified ID.
* **PATCH `{{URL}}/api/todos/:id/`**
    * Partially updates the TODO with the specified ID.
* **DELETE `{{URL}}/api/todos/:id/`**
    * Deletes the TODO with the specified ID.

**Additional Notes:**

* The `:id` parameter in the endpoints represents the unique identifier of a TODO.
* Refer to the official documentation for detailed request/response structures and error handling.

**Usage Example:**

```bash
# Get all TODOs
curl -X GET {{URL}}/api/todos/

# Get a single TODO
curl -X GET {{URL}}/api/todos/123

# Create a new TODO
curl -X POST {{URL}}/api/todos/ -d '{"title": "New TODO", "description": "This is a new TODO"}'

# Update an entire TODO
curl -X PUT {{URL}}/api/todos/123 -d '{"title": "Updated Title", "description": "Updated Description"}'

# Partially update a TODO
curl -X PATCH {{URL}}/api/todos/123 -d '{"title": "Updated Title"}'

# Delete a TODO
curl -X DELETE {{URL}}/api/todos/123
```

## TODO Item Model
The Todo model represents a TODO item with the following attributes and constraints:

* title: A CharField with a maximum length of 255 characters. This field is required.
* description: A TextField for a detailed description of the TODO item. This field is required.
* completed: A BooleanField indicating whether the TODO item is completed. Defaults to False.
* created_at: A DateTimeField that automatically records the date and time when the TODO item is created. This field is automatically set when the TODO item is created.
* due_date: A DateTimeField for the due date of the TODO item. This field is optional (can be null or left blank).
* priority: An IntegerField with choices representing the priority of the TODO item. The choices are:
    * 0 for Low
    * 1 for Medium
    * 2 for High The default value is 0 (Low).


## Constraints
* title: Must be a string with a maximum length of 255 characters.
* description: Must be a text string.
* completed: Must be a boolean value (True or False).
* created_at: Automatically set to the current date and time when the TODO item is created.
* due_date: Can be null or left blank.
* priority: Must be an integer value corresponding to one of the defined choices (Low, Medium, High). The default is Low.
