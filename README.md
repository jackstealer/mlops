# MLOps Pipeline - Iris Classification API

[![CI Pipeline](https://github.com/jackstealer/mlops/actions/workflows/ci-pipeline.yml/badge.svg)](https://github.com/jackstealer/mlops/actions/workflows/ci-pipeline.yml)
[![Docker Build](https://github.com/jackstealer/mlops/actions/workflows/docker-build.yml/badge.svg)](https://github.com/jackstealer/mlops/actions/workflows/docker-build.yml)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.143-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

A production-ready Machine Learning API built with FastAPI and Docker for predicting Iris flower species.

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Build the image
docker build -t iris-ml-api:v1.0 .

# Run the container
docker run -d -p 8000:8000 --name iris-api iris-ml-api:v1.0

# Or use the PowerShell script
.\run_docker.ps1
```

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python train.py

# Run the API
uvicorn main:app --reload
```

## 📋 Project Structure

```
mlops_pipeline/
├── models/
│   └── iris_random_forest_model.joblib  # Trained model
├── main.py                               # FastAPI application
├── train.py                              # Model training script
├── requirements.txt                      # Python dependencies
├── Dockerfile                            # Docker configuration
├── .dockerignore                         # Docker ignore rules
└── run_docker.ps1                        # Docker run script
```

## 🌐 API Endpoints

Once running, access the API at: `http://localhost:8000`

- **GET /** - Welcome message
- **GET /health** - Health check
- **POST /predict** - Make predictions
- **GET /docs** - Interactive API documentation (Swagger UI)

## 📊 Example Usage

### cURL

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.6,
    "petal_width": 0.5
  }'
```

### Python

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.6,
    "petal_width": 0.5
}

response = requests.post(url, json=data)
print(response.json())
# Output: {"prediction": 0, "class_name": "setosa"}
```

### PowerShell

```powershell
$body = @{
    sepal_length = 5.1
    sepal_width = 3.5
    petal_length = 1.6
    petal_width = 0.5
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/predict" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"
```

## 🧪 Test Cases

**Setosa (Class 0):**

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Versicolor (Class 1):**

```json
{
  "sepal_length": 6.4,
  "sepal_width": 3.2,
  "petal_length": 4.5,
  "petal_width": 1.5
}
```

**Virginica (Class 2):**

```json
{
  "sepal_length": 6.3,
  "sepal_width": 3.3,
  "petal_length": 6.0,
  "petal_width": 2.5
}
```

## 🐳 Docker Commands

```bash
# View running containers
docker ps

# View logs
docker logs iris-api
docker logs -f iris-api  # Follow logs

# Stop container
docker stop iris-api

# Remove container
docker rm iris-api

# Remove image
docker rmi iris-ml-api:v1.0
```

## 📦 Tech Stack

- **Python 3.11** - Programming language
- **scikit-learn** - Machine learning
- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Docker** - Containerization

## 📊 Model Information

- **Algorithm**: Random Forest Classifier (100 trees)
- **Dataset**: Iris dataset (150 samples, 4 features, 3 classes)
- **Accuracy**: 100% on test set
- **Model Size**: ~50 KB

## 🚀 Deployment

### Docker Hub

```bash
docker tag iris-ml-api:v1.0 your-username/iris-ml-api:v1.0
docker login
docker push your-username/iris-ml-api:v1.0
```

### Cloud Platforms

Deploy to:

- AWS (ECS, EKS, App Runner)
- Azure (Container Instances, AKS)
- GCP (Cloud Run, GKE)
- Heroku (Container Registry)

## 🔧 Development

### Requirements

- Python 3.11+
- Docker (optional)
- Git

### Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Train model: `python train.py`
4. Run API: `uvicorn main:app --reload`

## 📝 License

Educational project for MLOps learning.
