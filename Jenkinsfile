pipeline {
  agent any
  stages {
    stage('Clone repository') {
      steps {
        git 'https://github.com/Bimal00-gif/testgit.git'
      }
    }
    
    stage('Run Python code') {
      steps {
        sh 'python unit_test.py'
      }
    }
  }
}

 
