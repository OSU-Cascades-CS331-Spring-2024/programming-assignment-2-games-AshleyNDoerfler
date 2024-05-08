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

  Depth 5: Human Won
  Depth 3: Human Won
  Depth 2: Human Won
  Depth 1: AI won
    
b. Did the minimax player’s moves change when the depth was limited to smaller
and smaller values?
  I would assume that it would have this affect. It would make sense if it was    limited to a short search set.
  
c. What was the average time per move for each of the games? Comment on why
there is or is not a difference.

    Depth 5: avg time:  2.5272369384765625e-05 s
    Depth 3: avg time:  1.5894571940104168e-05 s
    Depth 2: avg time:  1.5163421630859375e-05 s
    Depth 1: avg time:  3.309249877929688e-05 s
    
2. Simulate two games between yourself and the minimax player on an 8x8 board, with the
depth parameter set to 5 and 2.
a. What were the results of each game?
b. Did the minimax player’s moves change when the depth changed?
c. What was the average time per move for each of the games? Comment on why
there is or is not a difference.
Deliverables:

I think my utility sucks, back to the drawing boards
