pipeline{
  agent any
  environment {
    NEXUS_LOGIN =credentials("NEXUS_LOGIN")
    }
  stages{
    stage("Build"){
      steps{
      sh "cd my_project1"
      sh "sudo docker build -t localhost:8083/pythonapp"
      sh "sudo docker image ls"
     }
    }
    stage("Push"){
      steps{
      sh "sudo docker login localhost:8083 -u ${NEXUS_LOGIN_USR} -p  ${NEXUS_LOGIN_PSW}"
      }
    }
  }
}
