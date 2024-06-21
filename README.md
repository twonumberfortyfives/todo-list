# Task Management Application

A simple task management application built with Django. The app allows users to create, update, delete, and list tasks and tags.

## Features

- **Home Page**: Displays the main interface of the application.
- **Task Management**:
  - Create new tasks
  - Update existing tasks
  - Delete tasks
  - List all tasks with task count
  - Toggle task status between active and inactive
- **Tag Management**:
  - Create new tags
  - Update existing tags
  - Delete tags
  - List all tags

## Project Structure

- **Templates**: Located in the `templates` directory, including `home.html`, `task_form.html`, `task_delete_confirm.html`, `tags_list.html`, `tags_form.html`, and `tag_delete_confirm.html`.
- **Forms**: Uses `TaskCreationForm` for task creation and update.
- **Models**: Includes `Task` and `Tags` models defined in `website.models`.

## How to Run the Project

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd yourproject
    ```
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```
5. **Run the Server**:
    ```bash
    python manage.py runserver
    ```
6. **Access the Application**: Open your browser and go to `http://localhost:8000`.

## Main Views and Their URLs

### Index View
- **URL**: `/`
- **Description**: Renders the home page.

### Task Views
- **Create Task**: `/create-task/`
- **List Tasks**: `/`
- **Update Task**: `/tasks/<pk>/update`
- **Delete Task**: `/tasks/<pk>/delete`
- **Toggle Task Status**: `/tasks/status/update/<pk>/`

### Tag Views
- **Create Tag**: `/tags/create/`
- **List Tags**: `/tags/`
- **Update Tag**: `/tags/<pk>/update`
- **Delete Tag**: `/tags/<pk>/delete`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
