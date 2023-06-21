pipeline 
{
    agent any 

    environment 
    {
        PATH = "$PATH:/var/lib/jenkins/.local/bin:/usr/bin"
    }

    stages 
    {
        stage('setup-env') 
        {
            steps 
            {
                echo 'Setup stage: Install dependencies in a virtual environment'
                //sh 'pip3 install -r requirements.txt'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('analyze') 
        {
            steps 
            {
                echo 'Analysis stage: Analyze the source code using pylint' 
                sh 'pylint multimeter/multimeter.py'
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
                sh 'deactivate'
            }
        }    
    }
}
