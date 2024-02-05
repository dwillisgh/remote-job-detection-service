@Library("cicd-global-library") _

dockerPipeline {
  name = "jobs-remote-job-detection-service"
  buildType = "python"

  major_version = "0"
  minor_version = "0"

  skipSonarScan = false
  
  testCommand = {
      sh("python -m spacy download en_core_web_sm")
      sh("pytest tests --cov --cov-report=xml")
  }
}