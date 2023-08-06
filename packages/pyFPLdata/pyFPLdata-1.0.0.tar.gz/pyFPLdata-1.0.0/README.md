# Introduction

This data contains a large variety of information on players and their
  current attributes on Fantasy Premier League
  <https://fantasy.premierleague.com/>. In particular, it contains a
  `next_gw_points` (next gameweek points) value for each player
  given their attributes in the current week. Rows represent player-gameweeks,
  i.e. for each player there is a row for each gameweek. This
  makes the data suitable for modelling a player's next gameweek points, given
  attributes such as form, total points, and cost at the current gameweek.
  
  This data, therefore, is in the **ideal format** to create Fantasy Premier League bots (for example that use an ML algorithm and a linear programming solver) to return the best possible team to pick for each gameweek (and therefore the transfers to make), thereby fully automating the decision making process in Fantasy Premier League. This single-function package simply supplies the required data for such a task.

# Usage

```
from pyFPLdata import FPLdata
FPLdata()
``` 