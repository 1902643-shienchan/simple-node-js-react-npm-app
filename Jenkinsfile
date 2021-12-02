pipeline {
	agent any
	stages {
       stage('OWASP DependencyCheck') {
            steps {
                dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Lab6-Prac'
            }
            post {
                success {
                    dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }
	        }
        }
		stage('Testing') {
			agent {
                docker {
                    image 'python:3.8.0'
                }
            }
			steps {
				sh 'pip install -r requirements.txt'
				sh 'pytest unit_test.py/'
			}
		}
	}
	post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}
