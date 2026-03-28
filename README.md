
# Software Development Life Cycle (SDLC) Exercise

- Development
- Operations
- Monitoring

# Pre-requisites
- Ubuntu
- Install NodeJS and NPM
    ```bash
    sudo apt update && sudo apt install nodejs npm
    ```
- Install Python
  ```bash
  sudo apt update && apt install python3
  ```
- Install Docker
    - Follow instructions from here: https://docs.docker.com/engine/install/ubuntu/


# Development

### Clone Repository
```bash
git clone --recurse-submodules https://github.com/dihajum/devops-workshop.git
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
```
