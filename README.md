# LinkMark

<img width="256" height="256" alt="linkmark-logo" src="https://github.com/user-attachments/assets/1ca9d022-80e2-46f5-a3db-bd9af284227b" />

LinkMark is a simple and efficient web application for bookmarking links. Built with **Flask**, it allows users to save links with a title and a personal note, making it easy to organize and revisit their favorite web pages.

---

## Features

* **User Authentication**: Securely create an account or log in with an existing one.
* **Add Bookmarks**: Easily add new links by providing a title, the URL, and an optional note.
* **Bookmark Management**: View all your saved links on a clean, intuitive home page.
* **Quick Access**: Each bookmark is displayed as a card with the title and creation date.
* **Detailed View**: Click on any bookmark card to see the full URL and your personal note.
* **Delete Functionality**: Remove bookmarks you no longer need with a single click.
* **Logout**: A simple way to end your session.

---

<img width="740" alt="image" src="https://github.com/user-attachments/assets/d142a411-02b8-4912-b584-73a2a4efa29b" />

---

## Technologies Used

* **Backend**: Python, Flask
* **Frontend**: HTML, CSS
* **Database**: SQLite

---

## Installation and Setup

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Steps

1.  **Clone the Repository**:
    ```bash
    git clone [your-repository-url]
    cd [your-project-directory]
    ```

2.  **Create a Virtual Environment** (recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**:
    * **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```
    * **On Windows**:
        ```bash
        venv\Scripts\activate
        ```

4.  **Install Dependencies**:
    * **Using pip**:
        ```bash
        pip install -r requirements.txt
        ```

    * **Using uv**:
        ```bash
        uv sync
        ```

        *Note: If you are using uv, it's recommended to create a `pyproject.toml` file to manage your dependencies instead of `requirements.txt`.*

1.  **Run the Application**:
    ```bash
    flask run
    ```

    *Note:  ```uv run main.py``` command can also be used to run the application* 

The application will now be running on `http://127.0.0.1:5000`.

---

## How to Use

1.  **Landing Page**: When you first visit the site, you'll be on the landing page where you can choose to log in or create a new account.
2.  **Home Page**: After logging in, you'll be redirected to the home page, which displays all your previously saved bookmarks.
3.  **Adding a Link**: Click the **"Add"** button to go to the add page. Fill in the title, link, and note, then click **"Add"**.
4.  **Viewing a Link**: Click on any bookmark card on the home page to view the full details (title, link, and note).
5.  **Deleting a Link**: Use the red **"X"** button on a bookmark card to delete it from your collection.
6.  **Logout**: Click the **"Logout"** button to end your session.

---

## License

This project is licensed under the ISC License.
