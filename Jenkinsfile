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
                sh 'echo $PATH'
                sh 'pylint src/*.py'
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
