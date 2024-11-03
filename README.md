## PerplexityAI MDT Model

This repository contains a FastAPI application that uses a Transformer model to answer patient questions in a simulated multidisciplinary team (MDT) setting.

### Requirements
- Python 3.8+
- Install dependencies with `pip install -r requirements.txt`.

### Running the Application
- To run the app, execute:
  ```bash
  ./run.sh
  ```
- Access the API at `http://localhost:8000`.

### API Endpoints
- `POST /answer`: Takes JSON with `question` and `context` fields and returns an answer and confidence level.
