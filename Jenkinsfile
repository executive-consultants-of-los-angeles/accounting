pipeline {
  agent any
  stages {
    stage('pytest') {
      steps {
        sh '$HOME/.py3/pytest --junitxml=docs/reports/$BUILD_NUMBER.xml'
        junit(testResults: 'docs/results/*xml', allowEmptyResults: true, keepLongStdio: true)
      }
    }
    stage('nosetests') {
      steps {
        sh '$HOME/.py3/bin/nosetests --with-xunit --xunit-file=docs/reports/nose-$BUILD_NUMBER.xml'
        junit(testResults: 'docs/reports/*xml', allowEmptyResults: true, keepLongStdio: true)
      }
    }
  }
  environment {
    HOME = '/mnt/pg/home/jenkins'
  }
}