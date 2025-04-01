# Application Overview

This application implements a minimax algorithm to solve decision-making problems in a game environment. The minimax algorithm evaluates possible moves to minimize the potential loss in a worst-case scenario, making it a fundamental approach in game theory and AI.

# Modifications from Baseline Code

1. Introduction of alpha-beta pruning + dynamic programming + depth limit
   1. 21.0737s
2. Introduction of dynamic programming + depth limit
   1. 173.9249s
3. Introduction of alpha-beta pruning + depth limit
   1. 53.1646s
4. Introduction of depth limit only
   1. Introducing this alone did not improve speed and was unmeasurable.

# Explanation of Each Algorithm

## Dynamic Programming

Dynamic programming is a technique where previously computed results are stored (memoized) and reused when the same computation is needed again. In the context of the minimax algorithm, this involves storing the evaluation results of board states that have already been calculated. By avoiding redundant calculations, the processing time can be significantly reduced.

### Example Improvement:
- If the same board state is encountered multiple times during the recursive exploration, the stored result is reused instead of recalculating it.

## Depth Limitation

The minimax algorithm uses depth-first search, which explores all possible moves to the deepest level of the game tree. As the depth increases, the number of nodes to evaluate grows exponentially, making it computationally infeasible. Depth limitation addresses this issue by restricting the depth of the search tree. If the search reaches the predefined depth limit, the algorithm stops further exploration and returns an approximate evaluation of the board state.

### Example Improvement:
- When the depth limit is reached, the algorithm can return a heuristic evaluation of the board instead of continuing to explore deeper levels.

# Considerations

When the board size is 3x3, the processing time does not vary significantly. For this reason, the board size was expanded to 5x5. In this case, the processing time differs greatly depending on the combination of algorithms used.