pipeline {
    agent any
    environment {
            NEXUS_LOGIN=credentials('NEXUS_LOGIN')
    }
    stages {
      stage('build') {
          steps {
              sh "cd project1"
              sh "sudo docker build -t localhost:8083/pythonapp ."  
              sh "docker image ls"
          }
      }
    }
}
