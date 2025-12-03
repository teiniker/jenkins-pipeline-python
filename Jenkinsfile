pipeline 
{
    agent { dockerfile true }

    stages 
    {
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
               	sh 'python multimeter/multimeter_test.py'
            }
        }
    }
}
