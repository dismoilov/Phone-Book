## **1. Install Python 3.11 to CentOS of FreePBX**

```bash
sudo yum update -y
sudo yum groupinstall "Development Tools" -y
sudo yum install wget openssl-devel libffi-devel bzip2-devel -y
sudo wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
sudo tar xvf Python-3.11.1.tgz
cd Python-3.11.1
./configure --enable-optimizations
sudo make altinstall
```

Check installation:
```bash
python3.11 --version
```

## **2. Install Libs for sending call recordings to django server**
```bash
pip3.6 install python-dotenv requests
```

## **3. Install Git for clone the project**
```bash
sudo yum install git
```
Check installation:
```bash
git --version
```

## **4. Deploy project to CentOS**

4.1 Clone Repo to server
```bash
git clone https://github.com/Diyorbek-Ismoilov/Phone-Book
cd Phone-Book/
```

4.2.1 First, enable the EPEL repository so that we can get the components we need:
```bash
sudo yum install epel-release
```

4.2.2 With the new repository available, we can install all of the pieces we need in one command:
```bash
sudo yum install python-pip python-devel postgresql-server postgresql-devel postgresql-contrib gcc nginx 
```

4.3 Set Up PostgreSQL for Django
```bash
sudo postgresql-setup initdb
sudo systemctl start postgresql
sudo systemctl restart postgresql
sudo systemctl enable postgresql
```

```bash
sudo su - postgres
psql
```

```SQL
CREATE DATABASE PhoneBook;
CREATE USER PhoneBook WITH PASSWORD '!Qazxsw2';
GRANT ALL PRIVILEGES ON DATABASE PhoneBook TO PhoneBook;
\q
exit
```

4.3 Create a Python Virtual Environment for your Project
```bash
sudo pip3.6 install virtualenv
virtualenv venv
source venv/bin/activate
```

4.4 Install All requirements
```bash
pip3.6 install -r requirements.txt
```

4.5 Create Super User For Django
```bash
cd phonebook
python3.6 manage.py migrate
python3.6 manage.py cretesuperuser
```
**Create User with username `admin` and password `!Qazxsw2`**

4.6 Configure Nginx

4.6.1 Modify the Nginx Configuration File
```bash
sudo nano /etc/nginx/nginx.conf
```
