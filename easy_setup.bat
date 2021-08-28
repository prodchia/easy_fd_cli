git clone https://github.com/Cactus-Network/fd-cli .\temp
xcopy /E /H /Y .\temp\ .\
python -m venv venv
rmdir /s /q temp
pip install -e . --extra-index-url https://pypi.chia.net/simple/ 
call .\venv\Scripts\activate & pip install pyyaml
python setup.py install

