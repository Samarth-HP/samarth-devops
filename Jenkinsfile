node() {
    try {
        parameters {
            string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')

            text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

            booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

            choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')

            password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
        }
        stage('Checkout') {
                cleanWs()
                checkout scm
                echo sh(script: 'env|sort', returnStdout: true)
                commit_hash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                env.commit_id = sh(script: 'echo ' + 'esamwad-backend' + '_' + commit_hash + '_' + env.BUILD_NUMBER, returnStdout: true).trim()
                echo "${env.commit_id}"
        }

        stage('docker-build') {
                sh '''

                   docker build -f Dockerfile -t $docker_server/$docker_repo:$commit_id
                   '''
        }

        stage('docker-push') {
            sh '''
                  docker push $docker_server/$docker_repo:$commit_id
                  docker rmi -f $docker_server/$docker_repo:$commit_id
                  '''
        }
        stage('ArchiveArtifacts') {
            sh("echo ${commit_id} > commit_id.txt")
                    archiveArtifacts 'commit_id.txt'
                    currentBuild.description = "${commit_id}"
        }
    }
    catch (err) {
        currentBuild.result = 'FAILURE'
        throw err
    }
}
