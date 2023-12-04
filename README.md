## Setup environment
conda create --name main-ds python=3.9
conda activate main-ds
pip install seaborn
pip install pandas
pip install matplotlib
pip install jupyter
pip install streamlit

## Run steamlit app
streamlit run dashboard.py