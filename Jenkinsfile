pipeline {
  agent any

  environment {
    GIT_USERNAME = credentials('git-user')
    GIT_TOKEN = credentials('git-token')
  }

  stages {
    stage('Checkout') {
      steps { git url: 'https://github.com/you/docker-image-builder.git', branch: 'main' }
    }

    stage('Setup Python') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }

    stage('Fetch Files') {
      steps {
        sh '. venv/bin/activate && python3 scripts/fetch_files.py'
      }
    }

    stage('Generate Dockerfile') {
      steps {
        sh '. venv/bin/activate && python3 scripts/generate_dockerfile.py'
      }
    }

    stage('Build via Buildah') {
      steps {
        sh 'buildah bud -t custom-image .'
      }
    }
  }

  post {
    success { echo '✅ Buildah image built successfully.' }
    failure { echo '❌ Image build failed.' }
  }
}
