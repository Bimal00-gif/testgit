pipeline {
    agent any 
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage ('hello'){
            steps{
                sh 'unit_test.py'
            }
        }  
    }
}
