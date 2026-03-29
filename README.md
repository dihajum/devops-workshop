# Software Development Life Cycle (SDLC) Exercise

Common Roles in SDLC
- Developer
- DevOps
- MLOps
- SRE

---

# Developer Role

## Pre-requisites
- Ubuntu
- Install Git
  ```bash
  sudo apt update && sudo apt install git -y
  ```
- Install NodeJS and NPM
  ```bash
  sudo apt update && sudo apt install nodejs npm -y
  ```
- Install Python
  ```bash
  sudo apt update && apt install python3 -y
  ```
- Install Docker
    - Follow instructions from here: https://docs.docker.com/engine/install/ubuntu/


## Development

### Clone Repository
```bash
git clone https://github.com/dihajum/devops-workshop.git
```

### Install Dependencies
```bash
cd angular-landing-page
npm install
```

### Starting application
```bash
npm run start
```

### Building application
```bash
npm run build
```

### Serving Application
```bash
python3 -m http.server -d dist
```

## Docker

Virtual Machine vs Containers
![Virtual Machines vs Containers](./assets/images/0-VM-vs-Containers.png)

- Container is the technology to build lightweight, standalone, executable package that includes everything needed to run an application
- Docker is an open source tool for packaging, sharing and running container image
- Container image are built from the specification defined in Dockerfile


### Build Container Imge
```bash
docker build -t myapp -f ../dockerfile-raw .
```

### Build Optimized Container Image
```bash
docker build -t myapp-opt -f ../dockerfile-optimized .
```

### Running application from container
```bash
docker run -it --rm -p 80:80 myapp

# Run as a service (Optimized Image)
docker run -d --restart=unless-stopped -p 80:80 --name myapp myapp-opt
```

---

# DevOps Role

Common responsibilities include:
- Infrastructure Management
- Deployment
- Automation
- CI/CD Pipeline Management
- Monitoring / Logging

![DevOps](./assets/images/1-DevOps.png)

Popular DevOps Tools
![Tools](./assets/images/2-DevOps-Tools.png)

## Github Actions

- CI/CD Platform for automating software development workflows
- Built-in to Github
- Workflows are written in YAML file
- Workflow is run in a pre-configured node called runner

Sample github actions workflow file
```yaml
# Triggers Definitions
on:
  push:
    branches:
    - main

# Pipeline Definitions
jobs:
  build:
    runs-on: self-hosted
    steps:
      - name: Clone Repository
        uses: actions/checkout@v6
      - name: Build App Container
        run: |
          cd src
          docker build -t image .

```

---

# MLOps Role

Common responsibilities includes:
- Data preparation and featurization
- Continuous Training
- Model tracking and deployment

![MLOps](./assets/images/3-MlOps.png)

Popular MLOps Tools
![Tools](./assets/images/4-MlOps-Tools.png)
ZenML, Mlflow, AWS Bedrock, Google Agentic Development Kit, Kubeflow, Weights & Biases Weave, Databricks, Azure Machine Learning, Metaflow, ClearML, DataRobot, Apache Airflow


## MlFlow

### Pre-requisites
- Python

### Installing mlflow
```bash
pip install mlflow

# OPTIONAL: If you are facing issue with pip install,
# create virtual environemnt before pip command
python -m venv .venv
source .venv/bin/activate

```

### Starting MLFlow UI
```bash
mlflow ui

# Access UI at http://127.0.0.1:5000
```
