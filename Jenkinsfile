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
    stage('push') {
        steps {
            sh "sudo docker login localhost:8083 -u ${NEXUS_LOGIN_USR} -p ${NEXUS_LOGIN_PSW}"
        }
    }
    stage('deploy') {
}
}
}
}
