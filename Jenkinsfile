pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t kubernetes-rollback-app:v1 ./app'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Deployment Verification') {
            steps {
                bat 'kubectl rollout status deployment/rollback-app --timeout=60s'
            }
        }
    }

    post {
        failure {
            bat 'kubectl rollout undo deployment/rollback-app'
        }
    }
}