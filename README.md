## **1. Install Python 3 to CentOS of FreePBX**

```bash
yum install https://centos7.iuscommunity.org/ius-release.rpm
yum install python36u python36u-devel python36u-pip
```

Check installation:
```bash
python3.6 -V
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
