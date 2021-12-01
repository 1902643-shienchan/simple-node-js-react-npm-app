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
			steps {
				sh 'python unit_test.py'
                    }
                }
        }
        post {
                success {
                        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }
        }
}

