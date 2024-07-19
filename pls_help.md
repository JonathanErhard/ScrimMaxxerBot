# ScrimMaxxer
The bot has 4 commands:
## pull
by writing "pull", the bot sends a DM, so you don't have to keep spamming the server
## pls help
I guess you figured that one out :3 gj
## condemn
If a message starts with "condemn:", the bot adds the names contained in the message (seperated by a new line) to the death.note file.
To specify how harsh the punishment should be the you can start the name with "blacklist:","greylist:" or "manager:".Example:
```
condemn:
blacklist:WesternSpy#4321
manager:Krissey#1242
```
note, that the bot is not case sensitive, but you have to add the manager in batteletag format, otherwise the bot doesn't work properly :/
## judge
By default the bot searches for battetags contained in the message.
Example:
```
Hello we would like to scrim against you!
our players are:
  IHOLDW#3141
  1RONCL4D#5926
  Cvpids4rrow#5358
  AlreadyTrac3r#9793
  AntlerAntler#2384

please contact C4LYPSO#6264 for the lobby!
```
would check
```
IHOLDW#3141
1RONCL4D#5926
Cvpids4rrow#5358
AlreadyTrac3r#9793
AntlerAntler#2384
C4LYPSO#6264
```
for past misbehaviour.