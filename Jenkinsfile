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
                #sh 'pylint src/'
            }
        }
        stage('test') 
        {
            steps 
            {
                echo 'Test stage: run the test cases' 
               	sh 'python3 src/multimeter_test.py'
            }
        }
    }
}
