# Dockerimage-tool
Docker Image Builder Tool (with Buildah + Flask UI)

A simple, UI-based tool to dynamically build Docker-compatible container images using Buildah, Git repositories, and YAML-based configuration.

Features

Upload a YAML config file to define Git-to-Docker path mappings

Pull files from multiple Git repositories using secure credentials

Specify custom base image (e.g., python:3.10)

Auto-generate a Dockerfile

Build the image using Buildah

Web interface powered by Flask

CI/CD-ready using Jenkins pipeline

 
📁 Project Structure

docker-image-builder/
├── app.py                      # Flask UI
├── requirements.txt           # Python packages
├── Jenkinsfile                # Jenkins pipeline for automation
├── .gitignore
├── templates/
│   └── index.html             # Web form for input
├── scripts/
│   ├── fetch_files.py         # Fetches Git files using config
│   └── generate_dockerfile.py # Builds Dockerfile dynamically
├── config/                    # Stores uploaded config
├── output/                    # Temp output files


Run Locally
	1.	Clone Repo


git clone https://github.com/yourname/docker-image-builder.git eg: https://github.com/Sacmaha17/Dockerimage-tool.git

cd docker-image-builder
	2.	Install Dependencies

pip install -r requirements.txt
	3.	Start Flask App

python app.py
	4.	Access Web UI

Open browser at: http://localhost:5000
