import json
import os
import re
from enum import Enum

class Crime(str,Enum):
    BLACKLIST_PLAYER = 1
    GRAYLIST_PLAYER = 2
    SUS_MANAGER = 3

dict_path = "death.note"

def handle_response(message:str) -> str:
    if message.startswith("condemn:\n"):
        return condemn_subject(message[9:])
    return judge(message)

def read_dic() -> {str,str}:
    if os.path.isfile(dict_path):
        with open('death.note') as f:
            return json.load(f)
    else:
        return {}

def save_json(dict:{str,str}):
    with open('death.note', 'w') as fp:
        json.dump(dict, fp)

def condemn_subject(message:str) -> str:
    dict = read_dic()
    subjects = message.split("\n")
    for subject in subjects:
        print(subject)
        if subject.lower().startswith("blacklist:"):
            dict[subject[10:]] = Crime.BLACKLIST_PLAYER
        if subject.lower().startswith("graylist:"):
            dict[subject[9:]] = Crime.GRAYLIST_PLAYER
        if subject.lower().startswith("manager:"):
            dict[subject[8:]] = Crime.SUS_MANAGER
    print(dict)
    save_json(dict)
    return "another criminal off the streets!"
        
def extract_players(message:str):
    return re.findall(r"[^[\s:,;()-]+#[0-9]*",message)
    
def judge(message:str) -> str:
    ret = ""
    players = extract_players(message)
    dict = read_dic()
    for player in players:
        if player in dict:
            match(dict[player]):
                case Crime.BLACKLIST_PLAYER:
                    ret += f"{player} has committed unforgivable crimes\n"
                case Crime.GRAYLIST_PLAYER:
                    ret += f"{player} is redeemable\n"
                case Crime.SUS_MANAGER:
                    ret += f"{player} managed a blacklisted team\n"
    return ret