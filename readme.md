### Blackjack Strategy Calculator

##### This is a project to distract me from revision, designed to perform Monte Carlo simulations of blackjack games, allowing for card-counting strategies. 

##### The aim is for optimal strategies and likelihood of winning estimates to be calculated for every possible hand, given:

- The player's current hand 
- Dealer's current hand
- Other players' hands 
- Active state of deck based on previous hands


##### Therefore, for now, betting functionality is not required; we only wish to estimate the likelihood of winning a hand along any branch of the game tree.

##### Presently, initial simplifications (such as ignoring splits, insurance) are made. 

##### Opting for elegant object-oriented design of the game mechanics, over performance, although that may be changed later on.