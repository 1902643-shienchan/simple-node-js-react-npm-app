pipeline {
   agent any
   stages {
       stage('build') {
           steps {
               sh 'pip install -U pip3'
               sh 'pip3 install -U Werkzeug'
           sh 'pip3 install bandit'
           sh 'pip3 install safety'
           sh 'pip3 install Flask-Testing'
           }
       }
     stage('test') {
         agent {
             docker {
                 image 'python:3.9.7-alpine3.13'
             }
         }
           steps {
               sh 'pip3 install Flask-Testing'
               sh 'pip3 install -r requirements.txt --ignore-installed'
           sh 'python functionaltest.py'
           sh 'pytest unit_test.py'
           sh 'pytest security_req_unit_test.py'
           }
       }
       stage ("Python Bandit Security Scan"){
        steps{
           sh "bandit -r Bluedit"
        }
     }
     stage ("Dependency Check with Python Safety"){
        steps{
           sh "safety check --ignore=40291"
        }
     }

   stage ("OWASP Dependency Check"){
     steps{
        dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
     }

  }
   }
  post{
     success{
        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
     }
  }
}

