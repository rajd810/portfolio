pipeline {
    agent any
    stages {
        stage("Clone Git Repository") {
            steps {
                git(
                    url: "https://github.com/rajd810/own_portfolio.git",
                    branch: "main",
                    changelog: true,
                    poll: true
                )
            }
        }
        stage("Printing Sample Message") {
            steps {
                echo "Hello, Starting CI CD pipeline- Push"
            }
        }
        stage("Running container") {
            steps {
                echo "Creating container"
                sh "docker build -t portfolio:0.1 ."
            }
        }
    }
}