# Jenkins Pipeline Python


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
		
