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
                                dependencyCheck additionalArguments: '--format HTML --format XML --suppression suppression.xml', odcInstallation: 'Default'
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

