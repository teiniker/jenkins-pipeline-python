pipeline 
{
    agent any 

    environment 
    {
        PATH = "$PATH:/var/lib/jenkins/.local/bin"
    }

    stages 
    {
        stage('setup') 
        {
            steps 
            {
                echo 'Setup stage: Install pylint'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('analyze') 
        {
            steps 
            {
                echo 'Analysis stage: Analyze the source code using pylint' 
                sh 'pylint multimeter/*.py'
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
