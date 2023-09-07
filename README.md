# Demoqa Nemshilov

## Quick start:

* clone [this](https://git.tmlab.io/qa/autotest) repo to your local drive

  ```
  git clone git@git.tmlab.io:qa/autotest.git 
  cd autotest
  git switch -c main
  ```
* install dependencies

  ```
  pip install -r requirements.txt
  ```
* **Run all tests for login page**

  ```
    pytest -k test_login
  ```
* **Test single registration internal  offer:**

  ```
  pytest -k test_registration_internal_offer
 