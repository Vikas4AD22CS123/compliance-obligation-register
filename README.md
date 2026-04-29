# Compliance Obligation Register

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

## Testing

### Install Test Dependencies
```bash
pip install pytest
```

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/test_routes.py
```

### Run Single Test
```bash
pytest tests/test_routes.py::TestFlaskApp::test_health_endpoint_success -v
```

### Test Coverage
```bash
pytest --cov=app --cov-report=html
```

## API Endpoints

- `GET /health` - Health check endpoint
- `POST /describe` - Describe compliance text
- `POST /recommend` - Get compliance recommendations
- `POST /generate-report` - Generate compliance report
- `GET /generate-report-stream` - Stream compliance report (SSE)
- `POST /analyse-document` - Analyze document for compliance findings