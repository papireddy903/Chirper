# Create project directory
mkdir -p ~/dev/saas-foundations
cd ~/dev/saas-foundations

# macos/linux: Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# windows: Create and activate a virtual environment
c:\Python312\python.exe -m venv venv
.\venv\Scripts\activate

# Create requirements.txt
echo "Django>=5.0,<5.1" >> requirements.txt
echo "gunicorn" >> requirements.txt

# install requirements
pip install pip --upgrade
pip install -r requirements.txt

# Start the django project
mkdir -p src
cd src
django-admin startproject cfehome .
