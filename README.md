# Civilization 5 Civ and Wonder Drafter

## Installation
simply go to your preferred workspace directory and enter the following:
```
git clone https://github.com/synonymous01/civ5_drafter.git
```

## Usage
run this command
```
python wonders.py
```

The program will ask you for the number of players. Enter that then it will ask you the name of each player. Output will be the Wonders and Civilization allocated to each player.

## Why did I make this?
Me and my friends used to play Civilization 5 competitively and one of the biggest issues was the amount of luck one needed to win the game. If they had a good enough Civ, they would automatically win given they handled their production well and easily make every wonder.

## How does the algorithm work?
To combat this, this program gives a set amount of points to each player and balanced the Civilization power (based on the community based tier list) by allocating them wonders that are reserved only for them. They aren't allowed to make somebody else's wonders.
For example, if somebody got a low-tier civ, they will be allocated high-tier wonders to balance the game for them and vice versa
