pipeline {
  agent any
  stages {
    stage('pytest') {
      steps {
        sh '''source /mnt/pg/home/jenkins/.py3/bin/activate
pip install pyyaml
pip install -e .
export YML_PATH=$WORKSPACE/yml/
pytest --junitxml=docs/reports/pytest-$BUILD_NUMBER.xml || true'''
        junit(allowEmptyResults: true, keepLongStdio: true, testResults: 'docs/reports/*.xml')
      }
    }
    stage('nosetests') {
      steps {
        sh '''source /mnt/pg/home/jenkins/.py3/bin/activate
pip install pyyaml
pip install -e .
export YML_PATH=$WORKSPACE/yml/
nosetests --with-xunit --xunit-file=docs/reports/nose-$BUILD_NUMBER.xml || true'''
        junit(testResults: 'docs/reports/*xml', allowEmptyResults: true, keepLongStdio: true)
      }
    }
  }
}
