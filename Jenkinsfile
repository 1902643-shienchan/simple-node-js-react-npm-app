pipeline {
        agent any
        stages {
		stage('Checkout SCM') {
			steps {
				checkout scm
				echo 'Building..'
			}
		}
                stage('OWASP DependencyCheck') {
                        steps {
                                dependencyCheck additionalArguments: '''
                                -o "./" 
                                -s "./"
                                -f "ALL"
				--enableExperimental
                                ''', odcInstallation: 'OWASP-Dependency-Check'
                        }
                }             
                stage('Testing') {
			agent {
				docker {
					image 'python:3.8.12-buster'
					args '-u root'
				}
			}
			steps {
				sh 'apt-get update'
				sh 'apt-get install -y python3-dev default-libmysqlclient-dev build-essential'
                                sh 'pip install -r flask/requirements.txt --ignore-installed'
				sh 'python unit_test.py
                    }
                }
        }
        post {
                success {
                        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }
        }
}

