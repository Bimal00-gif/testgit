pipeline {
  agent any
  stages {
    stage('Clone repository') {
      steps {
        git 'https://github.com/Bimal00-gif/testgit.git'
      }
    }
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run Python code') {
      steps {
        sh 'python3 unit_test.py'
      }
    }
  }
}

 
