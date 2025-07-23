pipeline {
    agent any

    tools {
        python 'python'
    }

    options {
        timestamps()
        skipDefaultCheckout(false)
        buildDiscarder(logRotator(numToKeepStr : '10'))
    }

    environment {
        DJANGO_SETTINGS_MODULE = 'micro_ec.ecom.settings'
    }

    triggers {
        githubpush()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python manage.py test'
            }
        }

        stage('Deploy or Rollback') {
            steps {
                scripts {
                    def result = currentBuild.result ?: 'SUCCESS'

                    if (result == 'SUCCESS') {
                        echo 'test passed. going to deployed'
                        bat 'echo deploying application...'
                        
                        bat '''
                        if not exist C:\\deployments\\micro_ecommerce mkdir C:\\deployments\\micro_ecommerce
                        robocopy . C:\\deployments\\micro_ecommerce /E /MIR /XD .git __pycache__ .venv env
                        cd C:\\deployments\\micro_ecommerce
                        python manage.py makemigrations
                        python manage.py migrate
                        start "python manage.py runserver"
                        '''
                    } else {
                        echo 'test failed. rolling back'
                        bat '''
                        git reset --hard HEAD~1
                        git push origin HEAD --force
                        '''
                    }                
                }
            }
        }
    }

    post {
        sucess {
            echo 'build complete'
        }
        failure {
            echo 'build failed'
        }

        always {
            echo 'clening worksapce'
        }
    }
}