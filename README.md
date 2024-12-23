# OSINT Search Tool

The OSINT (Open Source Intelligence) Search Tool is a web application for gathering public information from various platforms, including Twitter, Facebook, Google, and Instagram. The tool allows users to search for profiles and retrieve relevant data in an organized manner.

## Features

- Search for usernames across multiple platforms.
- Display user details such as bio, followers, location, and recent posts.
- Concurrent search functionality for faster results.
- Lightweight and easy to set up.

## Technologies Used

- **Python**: Backend development.
- **Flask**: Web framework.
- **BeautifulSoup**: HTML parsing and scraping.
- **Jinja2**: Templating engine.
- **HTML/CSS**: Frontend design.
- **Requests**: API requests to fetch data.

## Prerequisites

- Python 3.11 or later.
- A virtual environment (optional but recommended).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AdilSadqi/osint.git
   cd osint
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create Templates Directory**:
   Ensure the `templates/` directory exists, and include the following files:
   - `index.html`
   - `result.html`

## Running the Application

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Start the Flask application:
   ```bash
   python osint.py
   ```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## File Structure

```
OSINT/
├── osint.py             # Main application file
├── requirements.txt     # Project dependencies
├── templates/           # HTML templates
│   ├── index.html       # Homepage
│   └── result.html      # Results page
├── static/              # Static files (CSS, JS, images)
├── README.md            # Project documentation
└── venv/                # Virtual environment
```

## Example Usage

1. Enter a username in the search bar.
2. Select one or more platforms to search (Twitter, Facebook, Google, Instagram).
3. Click `Search` to view the results.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

Special thanks to the developers of Flask, BeautifulSoup, and Requests for their excellent libraries.

