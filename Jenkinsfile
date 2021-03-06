
node ('docker') {

    def imagename = "hub.bccvl.org.au/jenkins/firefox:latest"
    def img = docker.image(imagename)
    def config = "test_env_sh_${env.BRANCH_NAME}"

    // fetch source
    stage('Checkout') {
        // clean git clone, but don't fail in case it doesn't exist yet
        sh(script: 'git clean -x -d -f -f -e "eggs"', returnStatus: true)
        checkout scm
    }

    // build image
    stage('Prepare') {

        docker.withRegistry('https://hub.bccvl.org.au', 'hub.bccvl.org.au') {
            img.pull()
        }

    }

    // publish image to registry
    stage('Test') {
        // get env file from settings
        withCredentials([file(credentialsId: config, variable: 'TEST_ENV')]) {
            img.inside() {
                // TODO: does this require git?
                withVirtualenv('python3') {
                    sh '. ${VIRTUALENV}/bin/activate; pip install -r requirements.txt'
                    def result= sh(
                        script: '. "${TEST_ENV}"; . ${VIRTUALENV}/bin/activate; xvfb-run --server-args="-screen 0 1280x800x8" pybot robot',
                        returnStatus: true)
                }
            }
        }

        sh 'ls -l'
        // capture robot result
        step([
             $class: 'RobotPublisher',
             outputPath: '',
             outputFileName: 'output.xml',
             disableArchiveOutput: false,
             reportFileName: 'report.html',
             logFileName: 'log.html',
             otherFiles: 'selenium-screenshot-*.png',
             passThreshold: 90,
             unstableThreshold: 100,
             onlyCritical: false,
             enableCache: false
        ])

    }
}
