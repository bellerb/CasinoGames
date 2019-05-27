"""
 * @file cardGames.py
 * @authors Ben Bellerose
 * @date May 27 2019
 * @modified May 27 2019
 * @modifiedby BB
 * @brief class full of gambling book keeping functions
 */
 """
import pandas as pd

class book():
    """Input: none
       Function: loads player accounts
       Output: dataframe with all player accounts"""
    def loadAccounts():
        accounts = pd.read_csv('data/accounts.csv')
        return accounts

    """Input: name - string containing the players name
              score - float containing the players initial starting score
              accounts - dataframe containing all current player accounts
       Function: creates a new player account
       Output: dataframe with all player accounts"""
    def newAccount(name,score,accounts):
        player = {'Name':name,'Score':score}
        accounts = accounts.append(player,ignore_index=True)
        return accounts

    """Input: accounts - dataframe containing all current player accounts
       Function: saves player accounts current scores
       Output:boolean stating outcome of function"""
    def saveScores(accounts):
        result = True
        try:
            pd.DataFrame(accounts).to_csv('data/accounts.csv',index=False)
        except:
            result = False
        return result

    """Input: players - list containing current players stats
              accounts - dataframe containing all current player accounts
       Function: updates player account dicionary to current stats
       Output:dataframe with all player accounts updated"""
    def updateScores(players,accounts):
        for player in players:
            for account in accounts.iterrows():
                print(account)
                print(player['Name'])
                if account['Name'] == player['Name']:
                    account['Score'] == player['Score']
                    break
        return accounts

    """Input: player - dictionary containing player name and score
       Function: place a bet for individual player
       Output: list of dictionaries containing player name and hand"""
    def makeBet(player,**arg):
        while True:
            if 'bet' in arg:
                bet = arg['bet']
            else:
                bet = input("\n{}'s turn how much do you want to bet? (Funds:{})\n".format(player['Name'],player['Score']))
            try:
                if float(bet) <= float(player['Score']):
                    bet = float(bet)
                    player['Score'] = player['Score'] - bet
                    break
                else:
                    if 'bet' in arg:
                        bet = float(player['Score'])
                        player['Score'] = player['Score'] - bet
                        break
                    else:
                        print('Desired bet to big select smaller amount')
            except:
                print('Invalid entry bet must be a number')
        return [player,bet]
