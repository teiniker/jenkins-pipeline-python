pipeline 
{
    agent any 
    
    stages 
    {
        stage('analyze') 
        {
            steps 
            {
                echo 'Analysis stage: Analyze the source code using pylint' 
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip3 install -r requirements.txt'
                sh 'pylint multimeter/*.py'
                sh 'deactivate'
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
    }
}
