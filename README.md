# AI-DIGIT-RECOGNITIONS
A Django-based web application for recognizing handwritten digits using a TensorFlow model.

## Setup
1. Clone the repository: `git clone https://github.com/alanjoseph77/AI-DIGIT-RECOGNITIONS.git`
2. Navigate to the project: `cd AI-DIGIT-RECOGNITIONS/digitreco_project`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt` (create `requirements.txt` with `pip freeze > requirements.txt`)
6. Run migrations: `python manage.py migrate`
7. Start the server: `python manage.py runserver`

## Usage
Upload an image of a handwritten digit (1-9) at `http://127.0.0.1:8000/digitreco/` to get a prediction.

## Deployment
Deployed using [Render/Your Platform].