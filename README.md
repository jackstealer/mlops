# MLOps Pipeline - Iris Classification API

A production-ready Machine Learning API built with FastAPI, scikit-learn, and Docker for predicting Iris flower species.

## 🚀 Features

- **ML Model**: Random Forest Classifier trained on Iris dataset
- **API Framework**: FastAPI with automatic OpenAPI documentation
- **Containerization**: Docker for consistent deployment
- **Production-Ready**: Health checks, validation, error handling

## 📋 Project Structure

```
aiops/
├── mlops_pipeline/
│   ├── models/
│   │   └── iris_random_forest_model.joblib
│   ├── main.py              # FastAPI application
│   ├── train.py             # Model training script
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile           # Docker configuration
│   └── .dockerignore        # Docker ignore rules
├── cse/                     # Virtual environment
└── notes.txt                # Study notes
```

## 🛠️ Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jackstealer/mlops.git
   cd mlops
   ```

2. **Create virtual environment**
   ```bash
   python -m venv cse
   ```

3. **Activate virtual environment**
   - Windows (PowerShell):
     ```powershell
     cse\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     cse\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     source cse/bin/activate
     ```

4. **Install dependencies**
   ```bash
   cd mlops_pipeline
   pip install -r requirements.txt
   ```

5. **Train the model**
   ```bash
   python train.py
   ```

6. **Run the API**
   ```bash
   uvicorn main:app --reload
   ```

### Docker Setup

1. **Build Docker image**
   ```bash
   cd mlops_pipeline
   docker build -t iris-ml-api:v1.0 .
   ```

2. **Run container**
   ```bash
   docker run -d -p 8000:8000 --name iris-api iris-ml-api:v1.0
   ```

   Or use the PowerShell script:
   ```powershell
   .\run_docker.ps1
   ```

## 🌐 API Usage

Once running, the API is available at: `http://localhost:8000`

### Endpoints

- **GET /** - Welcome message
- **GET /health** - Health check
- **POST /predict** - Make predictions

### API Documentation

Interactive documentation available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Example Request

**cURL:**
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

**Python:**
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
```

**Response:**
```json
{
  "prediction": 0,
  "class_name": "setosa"
}
```

## 📊 Model Details

- **Algorithm**: Random Forest Classifier
- **Dataset**: Iris (150 samples, 4 features, 3 classes)
- **Features**:
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- **Classes**:
  - 0: Setosa
  - 1: Versicolor
  - 2: Virginica
- **Accuracy**: 100% on test set

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

## 📦 Dependencies

- **scikit-learn** - Machine learning algorithms
- **joblib** - Model serialization
- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **pydantic** - Data validation

## 🧪 Testing

Test the API with different iris measurements:

**Setosa (expected: 0)**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Versicolor (expected: 1)**
```json
{
  "sepal_length": 6.4,
  "sepal_width": 3.2,
  "petal_length": 4.5,
  "petal_width": 1.5
}
```

**Virginica (expected: 2)**
```json
{
  "sepal_length": 6.3,
  "sepal_width": 3.3,
  "petal_length": 6.0,
  "petal_width": 2.5
}
```

## 🚀 Deployment

### Docker Hub

1. **Tag the image**
   ```bash
   docker tag iris-ml-api:v1.0 your-username/iris-ml-api:v1.0
   ```

2. **Push to Docker Hub**
   ```bash
   docker login
   docker push your-username/iris-ml-api:v1.0
   ```

### Cloud Platforms

- **AWS**: ECS, EKS, App Runner
- **Azure**: Container Instances, AKS
- **GCP**: Cloud Run, GKE
- **Heroku**: Container Registry

## 📚 Learning Resources

This project covers:
- ✅ MLOps fundamentals
- ✅ FastAPI web development
- ✅ Docker containerization
- ✅ REST API design
- ✅ Model serialization
- ✅ Production deployment

## 📝 License

This project is for educational purposes.

## 👤 Author

Study project for MLOps, LLMOps, and AIOps course.

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests!

## 📧 Contact

For questions or feedback, please open an issue on GitHub.
