#E-Commerce (CSC370) Course Revision Tool (B.Sc. CSIT 6th Semester)

A web-based application for revising E-commerce course content, built with FastAPI and Jinja2.

## Features

- Comprehensive coverage of E-commerce concepts
- Interactive unit-by-unit learning
- Detailed explanations for each concept
- Revision questions for self-assessment
- Modern, responsive UI
- Markdown support for rich content

## Course Content

The application covers 7 units:
1. Introduction to E-commerce
2. E-commerce Business Models
3. Electronic Payment Systems
4. Building E-commerce Systems
5. Security in E-Commerce
6. Digital Marketing and Advertising
7. Optimizing E-commerce Systems

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/ecommerce-revision-app.git
cd ecommerce-revision-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

4. Visit http://127.0.0.1:8000 in your browser

## Technology Stack

- FastAPI - Web framework
- Jinja2 - Template engine
- markdown2 - Markdown processing
- Bootstrap - Frontend styling
- Bootstrap Icons - UI icons

## Project Structure

```
ecommerce_revision_app/
├── main.py           # FastAPI application
├── data.py          # Course content
├── requirements.txt  # Dependencies
├── static/          # CSS and static files
└── templates/       # HTML templates
    ├── base.html    # Base template
    ├── index.html   # Homepage
    └── unit.html    # Unit detail page
```

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

MIT License 
