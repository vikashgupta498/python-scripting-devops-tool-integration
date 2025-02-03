import os
import subprocess

# DevOps Mega Project - Automates CI/CD, Infra, Monitoring, and Security

def run_command(command):
    """Runs a shell command and prints output"""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(stdout.decode())
    else:
        print(stderr.decode())

# 1. Setup CI/CD using Jenkins Pipeline
def setup_jenkins():
    print("Setting up Jenkins...")
    run_command("docker run -d -p 8080:8080 --name jenkins jenkins/jenkins:lts")

# 2. Containerization with Docker
def setup_docker():
    print("Building Docker image...")
    run_command("docker build -t myapp:latest .")
    run_command("docker run -d -p 5000:5000 myapp")

# 3. Deploy with Kubernetes
def setup_k8s():
    print("Applying Kubernetes deployment...")
    run_command("kubectl apply -f k8s/deployment.yaml")

# 4. Infrastructure as Code (Terraform & Ansible)
def setup_infra():
    print("Applying Terraform configuration...")
    run_command("terraform init && terraform apply -auto-approve")
    print("Running Ansible playbook...")
    run_command("ansible-playbook ansible/setup.yml")

# 5. Monitoring with Prometheus & Grafana
def setup_monitoring():
    print("Deploying Prometheus & Grafana...")
    run_command("docker-compose -f monitoring/docker-compose.yml up -d")

# 6. Security & Compliance with HashiCorp Vault
def setup_security():
    print("Starting HashiCorp Vault...")
    run_command("docker run -d --name vault -p 8200:8200 vault")

if __name__ == "__main__":
    print("Starting DevOps Mega Project...")
    setup_jenkins()
    setup_docker()
    setup_k8s()
    setup_infra()
    setup_monitoring()
    setup_security()
    print("DevOps environment setup complete! 🚀")
