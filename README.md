# Application Overview

This application implements a minimax algorithm to solve decision-making problems in a game environment. The minimax algorithm evaluates possible moves to minimize the potential loss in a worst-case scenario, making it a fundamental approach in game theory and AI.

# Modifications from Baseline Code

1. alpha-beta枝切りの導入＋動的計画法の導入＋探索深さ制限を導入
   1. 21.0737s
2. 動的計画法の導入＋探索深さ制限を導入
   1. 173.9249
3. alpha-beta枝切りの導入＋探索深さ制限を導入
   1. 53.1646
4. 探索深さ制限を導入
   1. これだけ導入するだけでは速度改善にはならず、計測不能

# 考察

初手ではどこに打ってもそれほど結果は変わらないので、探索深さ制限を書て程浅くする。

