pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/RoshiniShanmugam/test-automation-analytics-framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Automation Tests') {
            steps {
                bat 'python -m robot -d results tests/LoginTests.robot'
            }
        }

        stage('Run Pandas Analytics') {
            steps {
                bat 'python analytics/analyze_results.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'results/*', allowEmptyArchive: true
        }
    }
}