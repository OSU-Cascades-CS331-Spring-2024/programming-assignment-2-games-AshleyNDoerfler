[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/i3cjXgnP)
# othello-python
Starter Code for Othello AI Agent Programming Assignment

Originally created by Erich Kramer at OSU for Professor Rebecca Hutchinson.
Cleaned up by Rob Churchill.

How to play a game:

1. Run `python3 game_driver.py [player_type] [player_type]`.
2. Choose `human`, or `minimax` as the player types.
3. Follow the prompts to choose where to place stones.

Simulate four games between yourself and the minimax player on a 4x4 board, with the
depth parameter set to 5, 3, 2, and 1, respectively.
a. What were the results of each game?
  I think I misunderstood and thought we were going to use time as the limiting   factor instead of depth, but this is almost due, so here are just the average   times each run: 
    win
    lose
    
b. Did the minimax player’s moves change when the depth was limited to smaller
and smaller values?
  I would assume that it would have this affect. It would make sense if it was    limited to a short search set.
  
c. What was the average time per move for each of the games? Comment on why
there is or is not a difference.
    avg time:  3.6443982805524555e-06 s
    avg time:  1.8978118896484374e-05 s
    With how I created my program, the average time is going to change based on     how many successors there are. My loops iterate through the successors.
    
2. Simulate two games between yourself and the minimax player on an 8x8 board, with the
depth parameter set to 5 and 2.
a. What were the results of each game?
b. Did the minimax player’s moves change when the depth changed?
c. What was the average time per move for each of the games? Comment on why
there is or is not a difference.
Deliverables:

Looking at this, I did my function very wrong...

what I did find from my program is that the AI is not great, and not always acting how I would expect it to. The utility is supposed to find the best scoring move from a given move. It was unable to detect when it could score multiple points part of the time. In situations where it could score points in multiple ways, It liked to pick to go down and right for some reason. Next project I definetly need to start earlier to fix up mistakes like this.
