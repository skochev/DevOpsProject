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
                bat 'start/min web_app.py'
            }
        }
    }
}
