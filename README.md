# Demoqa Nemshilov

## Quick start:

* clone [this](https://github.com/alexc0re/demoqa_nemshilov.git) repo to your local drive

  ```
  git clone https://github.com/alexc0re/demoqa_nemshilov.git
  ```
* Navigate to project folder 
  ```
  cd demoqa_nemshilov
  ```
* install dependencies

  ```
  pip install -r requirements.txt
  ```
* install playwright browser
  ```
  playwright install
  ```

#### Create .env file with valid creds
- allready done 


#### *Run all tests for login page*

  ```
    pytest -k test_login
  ```
#### Test api flow:

  ```
  pytest -k api_flow
  ```