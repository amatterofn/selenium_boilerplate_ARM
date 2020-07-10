pipeline {
    agent {
        docker {
            image 'python:3.7.2'
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
                pytest --browser chrome-remote --html=reports/ui_login.html --log-cli-level INFO
                '''
            }
            post {
                always {
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: false,
                        reportDir: 'reports',
                        reportFiles: 'ui_login.html',
                        reportName: 'Test Results',
                        reportTitles: 'CQ Login Test Results'
                    ])
                }
            }
        }
    }
}