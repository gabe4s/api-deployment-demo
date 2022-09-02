pipeline {
    agent any
    stages {
        stage('Clone Repo') { 
            steps { 
                script{
                checkout scm
                }
            }
        }
        stage('Docker Build') { 
            steps { 
                script{
                 app = docker.build("api-deployment-demo")
                }
            }
        }
        stage('Docker Push') {
            steps {
                docker.withRegistry("https://804011101642.dkr.ecr.us-east-2.amazonaws.com/api-deployment-demo", "ecr:us-east-2:aws-cred") {
                    dockerImage.push()
                }
            }
        }
    }
}