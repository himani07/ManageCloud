# Manage Cloud Machines

The project allows users to create clusters, create machines in a cluster, add tags to the machine when creating them,
delete machines and clusters and perform operations like start, stop, reboot on a group of machines using tags.

### Prerequisites
 You should have these installed in your system

```
Git
```
## Getting Started
clone this project using below command:
```
git clone https://github.com/himani07/ManageCloud.git
```
go to project directory
```
cd ManageCloud
``


### Installing
Install project dependencies
```
pip install virtualenv
```
```
virtualenv venv
```
```
cd venv
```
```
pip install python
```
```
pip install -r requirements.txt
```
create tables using this command:
```
python create_table.py
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

To run the tests, use this command
```
pytest
```
### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```
## Code Coverage
To measure the code coverage of your tests, use the coverage command to run pytest instead of running it directly.
```
coverage run -m pytest
```
You can either view a simple coverage report in the terminal using this command:
```
coverage report
```
###or
You can generate a HTML report which allows you to see which lines were covered in each file using this command:
```
coverage html
```
## Deployment

If you want to deploy this on aws using elastic beanstalk follow below steps:
*You will have to Setup 'awsebcli' on your Machine
```
pip install awsebcli
```
```
cd projectdir
```
```
eb init <yourappname> -p <python version> (i.e.python-3.6) <aws-region>
```
```
eb create <yourappenvironment>
```
You can access you app using below command once the processing is complete without errors:
```
eb open
```

## Built With

* [python]() - Programming language
* [flask]() - The web framework used
* [sqlite]() - Relational Database

## Author

**Himani Jain**

