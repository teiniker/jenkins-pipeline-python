pipeline 
{
    agent any 

    environment 
    {
        PATH = "$PATH:/var/lib/jenkins/.local/bin"
    }

    stages 
    {
        stage('setup-env') 
        {
            steps 
            {
                echo 'Setup stage: Install dependencies in a virtual environment'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }
        stage('analyze') 
        {
            steps 
            {
                echo 'Analysis stage: Analyze the source code using pylint' 
                sh 'pylint multimeter/multimeter.py --output-format=json:pylint-report.json'
            }
        }
        stage('test') 
        {
            steps 
            {
                echo 'Test stage: run the test cases' 
               	sh 'python3 multimeter/multimeter_test.py'
            }
        }
        stage('teardown-env') 
        {
            steps 
            {
                echo 'Teardown stage: Remove virtual environment'
                //sh 'deactivate'
            }
        }    
    }
}
