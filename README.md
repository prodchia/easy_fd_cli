# easy_fd_cli

Easy windows version to install and run  https://github.com/Flora-Network/fd-cli

[1] git clone https://github.com/prodchia/easy_fd_cli.git 
 
[2] cd easy_fd_cli 
 
[3] easy_setup.bat 


[4] Open config.cfg and complete the required information there


Wallet fingerprint found at below path or by using "chia wallet show"

Launcher ID: can be obtained using "chia plotnft show"

Window User is the windows user name under which you are currently working. 


That's it.

Now to recover coins:

[5] get_coins.bat coinname(e.g. flora, dogechia etc.)

I want to mention that I haven't been succesful in recovering NFT rewards for cactus.

If you receive the error "ImportError: DLL load failed while importing blspy: The specified module could not be found", it's likely due to the missing Visual C++ redistributable package used by blspy. You can try to the reinstall blspy. 

[a] Go to the easy_fd_cli directory

[b] call .\venv\Scripts\activate

[c] pip install blspy

If [c] works try to run get_coins.bat. If it doesn't then it probably crashed with some error like c++ not found. You can download and install what it is asking for, and follow the steps from a-c. Hopefully it should work
