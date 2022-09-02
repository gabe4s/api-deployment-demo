pipeline {
    agent any
    stages {
        stage('Initialize'){
            def dockerHome = tool 'docker'
            env.PATH = "${dockerHome}/bin:${env.PATH}"
        }
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
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}