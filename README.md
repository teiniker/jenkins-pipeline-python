# Jenkins Pipeline Python

In this example we see a Python project that is built using Jenkins.

* `Jenkinsfile`: The pipeline consists of two stages
    - analyze: Analyze the source code using pylint
    - test: Run the test executable

* `Dockerfile`: Jenkins uses an agent in the form of a Docker container 
    for the build process.


## Jenkins Pipeline (Jenkinsfile)

```yml
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
```

## Docker Agent

The agent is described by the following Dockerfile:

```yml
FROM python:3-alpine

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
```

This Docker image installs dependencies as defined in a `requirements.txt` 
file.


## Jenkins Job Configuration

We need the following settings for a new Jenkins job:

* New Item 
	- Pipeline
    - Description (optional)
    - Build Triggers 
	    - Poll SCM: `H/1 * * * *`
    - Pipeline / Definition: 
      - Pipeleine: Pipeline Script from SCM: 
        - SCM: Git 
        - Repository URL: `https://github.com/teiniker/jenkins-pipeline-python.git` 
        - Branches to build: `*/main` 
      - Script Path: Jenkinsfile


## References

* Python Project Layout
    * [RealPython: Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)
    * [RealPython: Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)

* Jenkins
    * [YouTube: How to Install Jenkins](https://youtu.be/CEyfsQq3QEM)
    * [YouTube: Complete Jenkins Pipeline Tutorial](https://youtu.be/7KCS70sCoK0)

    * [Getting started with Pipeline](https://www.jenkins.io/doc/book/pipeline/getting-started/)

    * [Using a Jenkinsfile](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/)

    * Rafał Leszko. **Continuous Delivery with Docker and Jenkins: Create secure applications by building complete CI/CD pipelines**. Packt Publishing, 2nd Edition 2019.

*Egon Teiniker, 2024-2025, GPL v3.0* 
		
