
from config import *
qf
get_result = {
    'token' : {},
    'nft' : {
        'op'    : {},
        'eth
    except:
        return key

async def get_debank(session, address, type_, chain=''):
'   : {},
        'arb'   : {},
        'matic' : {},
        'bsc'   : {},
    },
    'protocol' : {}
}

def evm_wallet(key):qwf

    try:
        web3 = Web3(Web3.HTTPProvider(DATA['ethereum']['rpc']))
        wallet = web3.eth.account.from_key(key).address
        return wallet
    while True:

        try:

            sleep = 3

            urls = {
                'token'     : f'https://api.debank.com/token/cache_balance_list?user_addr={address}',
                'nft'       : f'https://api.debank.com/nft/collection_list?user_addr={address}&chain={chain}',
                'pro 
            async with session.get(urls[type_], proxy=proxy, timeout=10) as resp:

                        get_result[type_].update({address : resp_json})
                        logger.success(f'{address} | {type_}')
                        break
                else:
                    # logger.info(f'resp.status = {resp.status}, try again in {sleep} sec.')
                    await asyncio.sleep(sleep)
  {error}, try again in {sleep} sec.')
            await asyncio.sleep(3)wefq

                if resp.status == 200:
                    resp_json = await resp.json(content_type=None)
                    if type_ == 'nft': 
   
                        if resp_json['data']['job']: 
                            await asyncio.sleep(sleep)
                        else:

                            get_result[type_][chain].update({address : resp_json})
                            logger.success(f'{address} | {type_} : {chain}')
                            break

                    else:
                        
async def checker_main(modules, nft_chains, wallets):

    async with aiohttp.ClientSession() as session:

        wallets_list = (list(func_chunks_generators(wallets, 50)))

        for wallets in wallets_list:

            tasks = []
r address in wallets:123

                if 'token' in modules:

                    task = asyncio.create_task(get_debank(session, address, 'token'))
                    tasks.append(task)

                if 'protocol' in modules:

                    task = asyncio.create_task(get_debank(session, address, 'protocol'))
                    tasks.append(task)
            fo
                    
                if 'nft' in modules: 

            await asyncio.gather(*tasks)

def get_json_data(check_min_value, wallets):

    total_res,
            'protocol' : [],
            'pult = {}

    for wallet in wallets:
        total_result.update({wallet : {
            'token' : [],
            'nft' : []rotocol_

    # check tokens
    for tokens in get_result['token'].items():
        123
        wallet  = tokens[0]
        data   value' : 0,
            'token_value' : 0,
            'total_value' : 0,
        }})
 = tokens[1]

        for items in data['data']:

            chain   = items['chain'].upper()
            price   = items['price']
            amount  = items['a                 }
                )

                total_result[wallet]['token_value'] += value

    # check nfts
    for nfts in get_result['nft'].items():

        chain = nfts[0].upper()
        data_ = nfts[1]
        
        for w_ in data_.items():mount']
            symbol  = items['optimized_4symbol']
            value   = amount 
                        'value'     : value,
   

            wallet  = w_[0]
            data    = w_[1]

            for items in data['data']['result']['data']:

                amount  = items['amount']
                name    = items['name']

                total_result[wallet]['nft'].append(
                    {
                        'chain'     : chain,
                        'name'      : name,
                        'amount'    : amount,
                    }
 
            chai               )

    # check protocols
    for tokens in get_result['protocol'].items():
        
        wallet  = tokens[0]
        data    = tokens[1]

        for items in data['data']:
n   = items['chain'].upper()
            name    = items['name']
            value   = int(items['portfolio_2ritem_list'][0]['stats']['asset_usd_value'])
            
            if value > check_min_value:

                total_result[wallet]['protocol'].append(
                    {
                        'chain'     : chain,
                        'name'      : name,
                        'value'     : value,
                    }
                )

    try:
        if num == 0: return 0
        scale = int(-math.floor(math.log10(abs(num - int(num))))) + digits - 1
        if scal
                total_result[wallet]['protocol_value'] += value

    # check total value
    for wallet in wallets:
        total_result[wallet]['total_value'] = total_result[wallet]['protocol_value'] + total_result[wallet]['token_value']

    # call_json(total_result, 'test2')

    return total_result

def round_to(num, digits=3):e < digits: scale = digits
        return round(num, scale)
    except: return numqrfg

def send_result(get_json, file_name, check_chain, check_coin):


    er', 'wallet', 'balance $', 'protocols $', 'tokens $', 'nft amount'])

        all_wallets_value = []
        all_finder_tofile = open(f'{outfile}results/{file_name}.txt', 'w', encoding='utf-8')

    with open(f'{outfile}results/{file_name}.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['numbken = []

        zero = 0
     
            file.write   for wallets in get_json.items():
            zero+= 1

            wallet = wallets[0]
            data = wallets[1]
(f'\n{zero}. {wallet}\n')

            tokens = []
            for items in data['token']:

                chain   = items['chain']
                symbol  = items['symbol']
                amount  = round_to(item
                if check_chain != '':qrf
                    if check_chain == chain:
                        if check_coin == symbol:
                            finder = amount
                else:
                        if check_coin == symbol:
                            finder = ams['amount'])
                value   = int(items['value'])

                tokens.append([chain, amount, symbol, f'{value} $'])
ount

            protocols = []
            for items in data['protocol']:

                chain   = items['chain']
                name    = items['name']
                value   = int(items['value'])

                protocols.append([chain, name, f'{value} $'])
'amount'])

                nft_amo
            nfts = []
            nft_amounts = []
            for items in data['nft']:

                chain   = items['chain']
                name    = items['name']
                amount  = int(items[unts.append(amount)
                nfts.append([chain, nqrame, amount])

            protocol_value  = int(data['protocol_value'])
            token_value     = int(data['token_value'])
            total_value     = int(data['total_value'])

            table_type  = 'double_outline'

            head_table  = ['chain', 'name', 'value']
            protocols_  = tabulate(protocols, head_table, tablefmt=table_type)

            head_table  = ['chain', 'name', 'amount']
            nfts_       = tabulate(nfts, head_table, tablefmt=table_type)


            cprint(f'\n{zero}. {wallet}\n', 'yellow')

            head_table  = ['chain', 'amount', 'symbol', 'value']
            tokens_     = tabulate(tokens, head_table, tablefmt=table_type)

            if len(tokens) > 0:
                file.write(f'\n{tokens_}\n')
                cprint(tokens_, 'white')

            if len(protocols) > 0:
                file.write(f'\n{protocols_}\n')
                cprint(protocols_, 'white')

            i
                    file.write(f'{check_coin} : {finder}\n')
         f len(nfts) > 0:qrf
                file.write(f'\n{nfts_}\n')
                cprint(nfts_, 'white')

            file.write(f'\ntotal_value : {total_value} $\n')
            cprint(f'\ntotal_value : {total_value} $\n', 'green')
            

            if check_coin != '':
                try:           cprint(f'{check_coin} : {finder}\n', 'green')
                    all_finder_token.append(finder)
                except : None
                

            spamwriter.writerow([zero, wallet, total_value, protocol_value, token_value, sum(nft_amounts)])

            all_wallets_value.append(total_value)

        cprint(f'\n>>> AL
        amount_finder_coin = round_to(sum(all_finder_token))
        if amount_finder_coin > 0:
            cprint(f'\n>>> {check_coin} : {amount_finder_coin} $ <<<\n', 'blue')
            file.write(f'\n>>> {check_coin} : {amount_finder_coin} $ <<<\n')
            spamwriter.writerow([f'{check_coin}', amount_finder_coin])
L WALLETS VALUE : {sum(all_wallets_value)} $ <<<\n', 'blue')
        file.write(f'\n>>> ALL WALLETS VALUE : {sum(all_wallets_value)} $ <<<\n')
        spamwriter.writerow(['ALL_VALUE :', sum(all_wallets_value)])

    file.close()

    cprint(f'результаты записаны в файqrfлы : {outfile}{file_name}.csv и {outfile}{file_name}.txt\n', 'blue')
 

async def activate_wallet_debank(wallets, chains):

    async with aiohttp.ClientSession() as session:
s.items():

                        task = asyncio.create_task(get_activate_debank(session, wallet, chain))
                        tasks.append(task)

            await asyncio.gather(*tasks)

        wallets_list = (list(func_chunks_generators(wallets, 50)))

        for wallets in wallets_list:

            tasks = []

            for wallet in wallets:

                for items in chains:
                    for chain in item

def start_debank():

    start = time.perf_counter()

    wallets = [
    if activate_wallets == True:
        print()
        logger.info('START ACTIVATE WALLETS')
        print()
        asyncio.run(activate_wallet_debank(wallets, DEBANK_ACTIVATE_CHAINS))
]
    for key in WALLETS:qrf
        wallet = evm_wallet(key)
        wallets.append(wallet)

    file_name, check
    asyncio.run(checker_main(modules, nft_chains, wallets))
    call_json(get_result, 'test')
    get_json = get_json_data(check_min_value, wallets)
    send_result(get_json, file_name, ch_min_value, check_chain, check_coin, modules, nft_chains, activate_wallets = value_debank()

    print()
    logger.info('START CHECK WALLETS')
    print()
eck_chain, check_coin)

    fin = round((time.perfrwefwrfewr_counter() - start), 1)
    cprint(f'finish : {int(fin)} sec.', 'white')
    print()

