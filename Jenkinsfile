pipeline {
  agent { label 'jenkins-agent-python' }

  stages {
    stage('Build') {
      steps {
        // code review
        sh ' python setup.py install\
         && pylint --rcfile=./pylint.conf ./apps/*'
        // remove the existed image if necessray
        sh '[ -z $(docker images -q $IMAGE_NAME:${BRANCH_NAME#*/}) ] || docker rmi $IMAGE_NAME:${BRANCH_NAME#*/}'
        // build from source
        sh 'docker build . -t $IMAGE_NAME:${BRANCH_NAME#*/}'
        // clean up
        sh 'docker image prune -f --filter label=stage=build'
      }
    }

    stage('Push') {
      parallel {
        stage('Local') {
          when { branch 'develop' }
          steps {
            // TODO: using local registry mirror
            withCredentials([usernamePassword(credentialsId: 'registry', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
              sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin $REGISTRY_URL'
              sh 'docker push $IMAGE_NAME:$BRANCH_NAME'
            }
          }
        }

        stage('Central') {
          when { branch 'master' }
          steps {
            withCredentials([usernamePassword(credentialsId: 'registry', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
              sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin $REGISTRY_URL'
              sh 'docker tag $IMAGE_NAME:$BRANCH_NAME $IMAGE_NAME:$IMAGE_TAG'
              sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
              sh 'docker rmi $IMAGE_NAME:$IMAGE_TAG'
            }
          }
        }
      }
    }

    stage('Pre-deploy') {
      when { branch 'develop' }

      steps {
        node(label: 'UAT') {
          withCredentials([usernamePassword(credentialsId: 'container', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
            sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin registry.cn-shenzhen.aliyuncs.com'
          }

          // remove the existed container
          sh '[ -z $(docker ps -q -f name=$APP_NAME) ] || docker stop $APP_NAME'
          sh '[ -z $(docker ps -aq -f name=$APP_NAME) ] || docker rm $APP_NAME'
          // remove the existed image
          sh '[ -z $(docker images -q $IMAGE_NAME:$BRANCH_NAME) ] || docker rmi $IMAGE_NAME:$BRANCH_NAME'
          // pull the latest image
          sh 'docker pull $IMAGE_NAME:$BRANCH_NAME'
          // bring up the new container
          sh 'docker-compose -f $ROOT_PATH/$UAT_COMPOSE_FILE -p $UAT_COMPOSE_PROJECT up -d'
          //TODO: replaced by automation test suites
          echo 'Now it is time to running all test suites...'
        }
      }
    }

    stage('Test') {
      when {branch 'develop'}

      steps {
        node(label: 'UAT') {
          //smoke test

          sh 'docker-compose -f $ROOT_PATH/$BEACON_COMPOSE_FILE -p $BEACON_COMPOSE_PROJECT restart beacon'
        }
      }
    }

    stage('Verify') {
      when { branch 'develop' }

      steps {
        node(label: 'UAT') {
          input 'Does the testing environment look ok?'
        }
      }
    }

  }
  post {
    success {
      dingTalk (
        robot: 'c033b95b-41ee-4caa-88b5-e27bfa68cf5f',
        type: 'LINK',
        title: '构建通知 - Ayes Hemnes',
        text: ['构建成功！'],
        messageUrl: 'https://ci.diannei-ai.com/blue/organizations/jenkins/pipelines',
        picUrl: 'http://static-contents.oss-cn-shenzhen.aliyuncs.com/misc/passed.png'
      )
    }

    failure {
      dingTalk (
        robot: 'c033b95b-41ee-4caa-88b5-e27bfa68cf5f',
        type: 'LINK',
        title: '构建通知 - Ayes Hemnes',
        text: ['构建失败，请及时查看问题原因！'],
        messageUrl: 'https://ci.diannei-ai.com/blue/organizations/jenkins/pipelines',
        picUrl: 'http://static-contents.oss-cn-shenzhen.aliyuncs.com/misc/failed.png'
      )
    }
  }

  environment {

    APP_NAME = 'hemnes'
    IMAGE_NAME = 'registry.cn-shenzhen.aliyuncs.com/dntech/hemnes'
    IMAGE_TAG = 'latest'
    REGISTRY_URL = 'registry.cn-shenzhen.aliyuncs.com'

    ROOT_PATH = '/home/dntech'
    UAT_COMPOSE_FILE = 'uat.yml'
    UAT_COMPOSE_PROJECT = 'uat'
    BEACON_COMPOSE_FILE = 'beacon.yml'
    BEACON_COMPOSE_PROJECT = 'beacon'
  }
}
