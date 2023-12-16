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
        stage('run python') {
            steps {
                script {
                    sh 'python3 1.py'
                }
            }
        }
    }
}
