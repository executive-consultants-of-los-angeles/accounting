pipeline {
  agent any
  stages {
    stage('pytest') {
      steps {
        catchError() {
          sh '''source /mnt/pg/home/jenkins/.py3/bin/activate
pip install pyyaml
pip install -e .
pytest --junitxml=docs/reports/pytest-$BUILD_NUMBER.xml'''
          junit(allowEmptyResults: true, keepLongStdio: true, testResults: 'docs/reports/*.xml')
        }
        
      }
    }
    stage('nosetests') {
      steps {
        sh '''source /mnt/pg/home/jenkins/.py3/bin/activate
pip install pyyaml
pip install -e .
nosetests --with-xunit --xunit-file=docs/reports/nose-$BUILD_NUMBER.xml'''
        junit(testResults: 'docs/reports/*xml', allowEmptyResults: true, keepLongStdio: true)
      }
    }
  }
}