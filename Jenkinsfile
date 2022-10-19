node() {

    def secrets = [
        [path: 'kv/jenkins/github', engineVersion: 2, secretValues: [
        [envVar: 'PRIVATE_TOKEN', vaultKey: 'private-token'],
        [envVar: 'PUBLIC_TOKEN', vaultKey: 'public-token'],
        [envVar: 'API_KEY', vaultKey: 'api-key']]],
    ]

    def configuration = [vaultUrl: 'http://128.199.26.225:8200',  vaultCredentialId: 'vault-approle', engineVersion: 2]

    properties([
        parameters([
            string(name: 'docker_repo', defaultValue: 'YOUR-SERVICE-NAME', description: 'Docker Image Name'),
            string(name: 'docker_server', defaultValue: 'localhost:5000', description: 'Docker Registry URL'),
        ])
    ])

    stage('Vault') {
          withVault([configuration: configuration, vaultSecrets: secrets]) {
            sh "pwd"
            sh "ls"
            sh "echo ${env.PRIVATE_TOKEN}"
            sh "echo ${env.PUBLIC_TOKEN}"
            sh "echo ${env.API_KEY}"
        }  
      }

    stage('Checkout') {
            cleanWs()
            checkout scm
            commit_hash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
            env.commit_id = sh(script: 'echo ' + env.docker_repo + '_' + commit_hash + '_' + env.BRANCH_NAME, returnStdout: true).trim()
            echo "${env.commit_id}"
    }

    stage('docker-build') {
            sh '''
                # docker build -f <location-of-docker-file> -t <tag-of-docker-image> <context-for-docker-image>
                docker build -f build/Dockerfile -t $docker_server/$docker_repo:$commit_id .
                '''
    }

    stage('docker-push') {
        sh '''
                docker push $docker_server/$docker_repo:$commit_id
                '''
    }
    stage('ArchiveArtifacts') {
        sh("echo ${commit_id} > commit_id.txt")
                archiveArtifacts 'commit_id.txt'
                currentBuild.description = "${commit_id}"
    }
}