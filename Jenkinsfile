pipeline {
  agent any
  stages {
    stage('pytest') {
      steps {
        catchError() {
          withPythonEnv('three') {
            pysh 'pip install pyyaml pytest pytest-runner'
            pysh 'python setup.py build'
            pysh 'python setup.py install'
            pysh 'pip install -e . || true'
            pysh 'pip install -e .'
            pysh 'export YML_PATH=$WORKSPACE/yml/'
            pysh 'pytest --junitxml=docs/reports/pytest-$BUILD_NUMBER.xml || true'
            junit(allowEmptyResults: true, keepLongStdio: true, testResults: 'docs/reports/*.xml')
          }
        }
      }
    }
    stage('coverage') {
      steps {
        catchError() {
          withPythonEnv('three') {
            pysh 'pip install pyyaml pytest pytest-runner coverage'
            pysh 'python setup.py build'
            pysh 'python setup.py install'
            pysh 'pip install -e . || true'
            pysh 'pip install -e .'
            pysh 'export YML_PATH=$WORKSPACE/yml/'
            pysh 'coverage run setup.py test'
            pysh 'coverage xml'
            junit(testResults: 'docs/reports/*xml', allowEmptyResults: true, keepLongStdio: true)
          }
        }
      }
    }
  }
}
