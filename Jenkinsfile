pipeline {
    agent {
        docker {
            image 'python:3.7.2'
            args '--add-host=dev.fiscalnote.com:34.193.229.138 --add-host=staging.fiscalnote.com:34.234.18.56'
        }
    }
    stages {
        stage('build') {
            steps {
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('test') {
            steps {
                sh '''
                bash
                . venv/bin/activate
                pytest -m debug --browser chrome-remote
                '''
            }
        }
    }
}