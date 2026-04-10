# Install Python (via winget)
winget install -e --id Python.Python.3.13

# Install Git
winget install -e --id Git.Git

# Clone repo
git clone https://github.com/Ruined-life/Forsaken-Voicelines.git
cd Forsaken-Voicelines

# Install dependencies
pip install -r requirements.txt

# Run app
python main.py
