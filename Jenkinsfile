pipeline {
    agent any

    environment {
        IMAGE_NAME = "gtdreams/wog4"
        CONTAINER_NAME = "wog4-lesson11_your_service_1"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }

        stage('Update Docker Compose') {
            steps {
                script {
                    sh "sed -i 's|gtdreams/wog4:v1.0|${IMAGE_NAME}:${env.BUILD_ID}|g' docker-compose.yml"
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker-compose up -d"
                }
            }
        }

        stage('Run e2e Tests') {
            steps {
                script {
                    sh '''#!/bin/bash
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    python3 e2e.py
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up - stop and remove the container if it's running
            script {
                sh(script: "docker stop ${CONTAINER_NAME} || true", returnStatus: true)
                sh(script: "docker rm ${CONTAINER_NAME} || true", returnStatus: true)
            }
        }
    }
}
