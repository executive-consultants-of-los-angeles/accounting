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
    stage('coverage') {
      steps {
        sh '''source /mnt/pg/home/jenkins/.py3/bin/activate
pip install pyyaml
pip install -e .
export YML_PATH=$WORKSPACE/yml/
coverage run setup.py test
coverage xml
        junit(testResults: 'docs/reports/*xml', allowEmptyResults: true, keepLongStdio: true)
      }
    }
  }
}
