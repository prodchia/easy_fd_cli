'''
Created on Aug 20, 2021

@author: prodchia
'''
import os, argparse , configparser
import pathlib, yaml


if __name__== "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--blockchain',default = 'silicoin')
    args = parser.parse_args()
    blockchain = args.blockchain
    
    if blockchain in ['goji','spare']:
        blockchain = blockchain + '-blockchain'
    
    # get config file
    config_file = os.path.join(pathlib.Path(__file__).parent.resolve(), 'config.cfg')
    config=configparser.ConfigParser()
    config.read(config_file)
    
    fingerprint = config['main']['fingerprint']
    
    
    # Set id of NFT plot. It is currently stored in config
    # Launcher ID: can be obtained using "chia plotnft show"
    # Execute above command in Chia, as those values are the original NFT contract details, which do not exist in the forks
    LAUNCHER_HASH = config['main']['launcher_hash']
    print(f" Recovering NFT coins for {blockchain} with {LAUNCHER_HASH}")
    os.environ["LAUNCHER_HASH"] = LAUNCHER_HASH
    
    # Pool contract address: can be obtained using "chia plotnft show"
    # Execute above command in Chia, as those values are the original NFT contract details, which do not exist in the forks
    pool_contract = config['main']['pool_contract']
    os.environ["POOL_CONTRACT_ADDRESS"] = pool_contract

    user = config['main']['user']

    # Set blockchain path.
    if blockchain == 'silicoin':
        FD_CLI_BC_DB_PATH = f"C:\\Users\\{user}\\.{blockchain}\\mainnet\\db\\blockchain_v1_testnet.sqlite"
    else:
        FD_CLI_BC_DB_PATH = f"C:\\Users\\{user}\\.{blockchain}\\mainnet\\db\\blockchain_v1_mainnet.sqlite"

    os.environ['FD_CLI_BC_DB_PATH'] = FD_CLI_BC_DB_PATH
    print(FD_CLI_BC_DB_PATH)
    # Set wallet path.
    # This must be the wallet that is associated with mnemonic from which NFT plot was created. (Usually your hot wallet)
    # Replace <fingerprint> with your wallet fingerprint found at below path or by using "chia wallet show"
    if blockchain == 'silicoin':
        FD_CLI_WT_DB_PATH = f"C:\\Users\\{user}\\.{blockchain}\\mainnet\\wallet\\db\\blockchain_wallet_v1_testnet_{fingerprint}.sqlite"
    else:
        FD_CLI_WT_DB_PATH = f"C:\\Users\\{user}\\.{blockchain}\\mainnet\\wallet\\db\\blockchain_wallet_v1_mainnet_{fingerprint}.sqlite"
    os.environ['FD_CLI_WT_DB_PATH'] = FD_CLI_WT_DB_PATH
    
    certificate = f"C:\\Users\\{user}\\.{blockchain}\\mainnet\\config\\ssl\\full_node\\private_full_node.crt "
    key = f"C:\\Users\\{user}\\.{blockchain}\\mainnet\\config\\ssl\\full_node\\private_full_node.key "

    # read config to get rpc_port
    config_file = f"C:\\Users\\{user}\\.{blockchain}\\mainnet\\config\\config.yaml"
    with open(config_file,'r') as istream:
        data_config = yaml.safe_load(istream)

    port = data_config['full_node']['rpc_port']

    cmd_str = f"""fd-cli nft-recover -l {LAUNCHER_HASH} -p {pool_contract} -nh 127.0.0.1  -np {port} -ct {certificate} -ck {key} """
                
    os.system(cmd_str)
    
    # All coins that were mined +7 days ago WITH NFT PLOT should be spendable soon via wallet.