# Hydration Tracker App (FastAPI + Flask)

Keep track of your daily water intake and maintain a healthy lifestyle with the Hydration Tracker App. This application combines the power of FastAPI and Flask to provide users with a seamless experience in monitoring their hydration levels.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Frontend](#frontend)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- User registration and profile management.
- Real-time water consumption tracking.
- Personalized daily hydration goal calculation.
- Historical data visualization for progress monitoring.

## Screenshots

_Insert screenshots or GIFs showcasing the app's UI and features._

## Getting Started

### Prerequisites

- Python 3.10 or later
- Docker (for running the MongoDB instance and the API instance)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/hydration-tracker.git
cd hydration-tracker
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Set up the MongoDB database using Docker:

```bash
docker run -d -p 27017:27017 --name hydration-db mongo:latest
```

4. Configure the app settings in config.py with MongoDB address

```bash
MONGODB_URI = __.__.__.__
```

### USAGE

Start the FastAPI & Flask directly:
```bash
uvicorn app:api
```

Or run it on a Docker Container:
```bash
docker build -t drink_tracker_app .
docker run -d -p 8000:8000 drink_tracker_app
```

### API Documentation
Detailed API documentation and usage instructions can be found in http://localhost:8000/docs#

### Frontend
The Flask-based frontend provides an intuitive user interface to interact with the hydration tracker. Navigate to http://localhost:8000/app after starting the app.

### License
This project is licensed under the MIT License.

### Acknowledgements

* Built using FastAPI and Flask.
* MongoDB Docker container powered by MongoDB Official Image.