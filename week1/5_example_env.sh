# Create the envorinments for 5_*example.py
conda create --name cshsweek1 --clone cshs
conda activate cshsweek1
conda install -c vpython vpython -y
python -m ipykernel install --user --name cshsweek1 --display-name "cshsweek1"
jupyter notebook
conda install -c conda-forge pyautogui -y
conda install -c anaconda flask -y
pip install freegames
conda install -c plotly plotly -y
conda install scikit-image -y
