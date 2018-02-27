
node ('docker') {

    def imagename = "hub.bccvl.org.au/jenkins/firefox:latest"
    def img

    // fetch source
    stage('Checkout') {
        checkout scm
    }

    // build image
    stage('Prepare') {

        docker.withRegistry('https://hub.bccvl.org.au', 'hub.bccvl.org.au') {
            img = img.pull(imagename)
        }

    }

    // publish image to registry
    stage('Test') {
        # get env file from settings
        withCredentials([string(credentialsId: 'pypi_index_url_prod', variable: 'PYPI_INDEX_URL')]) {
            img.inside() {
                withVirtualenv() {
                    sh '. ${VIRTUALENV}/bin/activate; pip install -r requirements.txt'
                    sh '. ${VIRTUALENV}/bin/activate; xvfb-run --server-args="-screen 0 1280x800x8" pybot robot'
                }
            }
        }

        // capture robot result
        step([
             $class: 'RobotPublisher',
             outputFileName: 'output.xml',
             disableArchiveOutput: false,
             reportFileName: 'report.html',
             logFileName: 'log.html',
             otherFiles: 'selenium-screenshot-*.png',
             passThreshold: 90,
             unstableThreshold: 100,
             onlyCritical: false,
             otherFiles: '',
             enableCache: false
        ])

    }
}
