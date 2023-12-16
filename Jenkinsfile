pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/skochev/DevOpsProject.git'
            }
        }
        stage('run backend server') {
            steps {
                bat 'start/min RestAPI/rest_app.py'
            }
        }
        stage('run frontend server') {
            steps {
                bat 'start/min web_app.py'
            }
        }
        stage('run backend testing') {
            steps {
                bat 'start/min Testing/backend_testing.py'
            }
        }
        stage('run frontend testing') {
            steps {
                bat 'start/min Testing/frontend_testing.py'
            }
        }
        stage('run combined testing') {
            steps {
                bat 'start/min Testing/combined_testing.py'
            }
        }
        stage('run clean environment') {
            steps {
                bat 'start/min RestAPI/clean_environment.py'
            }
        }
    }
}
