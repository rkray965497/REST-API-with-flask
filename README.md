# REST API with Flask

A simple RESTful API built with [Flask](https://flask.palletsprojects.com/) for demonstration, learning, or starter project purposes.

## Features

- Basic CRUD (Create, Read, Update, Delete) operations
- Lightweight and easily extensible architecture
- Follows RESTful principles
- JSON-based request and response handling
- Clean and modular codebase for maintainability

## Tech Stack

- **Python** (main language)
- [**Flask**](https://flask.palletsprojects.com/) web framework

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/rkray965497/REST-API-with-flask.git
   cd REST-API-with-flask
   ```

2. **Create a virtual environment (optional, but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   ```bash
   flask run
   ```
   Or, if you have an `app.py`:
   ```bash
   python app.py
   ```

2. **Visit the API:**
   - By default, the API will run on `http://localhost:5000/`
   - Use tools such as [Postman](https://www.postman.com/) or `curl` to access endpoints

## Example Endpoints

- `GET /items` - List all items
- `GET /items/<id>` - Get an item by ID
- `POST /items` - Create a new item (expects JSON body)
- `PUT /items/<id>` - Update an existing item by ID
- `DELETE /items/<id>` - Delete an item by ID

## Project Structure

```
.
├── app.py
├── requirements.txt
├── README.md
└── ...
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

---

> _Made with Flask for simplicity and learning._
