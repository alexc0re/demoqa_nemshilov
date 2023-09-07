# Demoqa Nemshilov

## Quick start:

* clone [this](https://github.com/alexc0re/demoqa_nemshilov.git) repo to your local drive

  ```
  git clone https://github.com/alexc0re/demoqa_nemshilov.git
  ```
* install dependencies

  ```
  pip install -r requirements.txt
  ```
* Add env variables
  ```
  export BOOK_LOGIN=alexnemsh
  export BOOK_PASSWORD=6e8h4VSn4v#Z%bd
  ```

* *Run all tests for login page*

  ```
    pytest -k test_login
  ```
* *Test api flow:*

  ```
  pytest -k test_api_flow
  ```