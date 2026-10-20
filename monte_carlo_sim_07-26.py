# World Cup Monte Carlo Simulator
# Elo ratings taken from World Football Elo Ratings
# 7/14/2026
import random
spa_elo = 2232
eng_elo = 2097
arg_elo = 2177


def expected_win_1(team_1, team_2):
  difference = float(((team_2 - team_1) / 400))
  probability = float(1 / (1 + (10 ** difference)))
  return probability

arg_eng = expected_win_1(arg_elo, eng_elo)
eng_arg = expected_win_1(eng_elo, arg_elo)
arg_spa = expected_win_1(arg_elo, spa_elo)
spa_arg = expected_win_1(spa_elo, arg_elo)
eng_spa = expected_win_1(eng_elo, spa_elo)
spa_eng = expected_win_1(spa_elo, eng_elo)

arg_eng = f'{arg_eng:.3f}'
arg_spa = f'{arg_spa:.3f}'
eng_spa = f'{eng_spa:.3f}'





def monte_carlo(n):
  arg_count = 0
  eng_count = 0
  spa_count = 0
  for x in range(n):
    r = random.random()
    if r <= 0.613:
        r = random.random()
        if r <= 0.422:
          arg_count += 1
        else:
          spa_count += 1
    else:
        r = random.random()
        if r <= 0.315:
          eng_count += 1
        else:
          spa_count += 1
  spa_prob = float(spa_count / n)
  arg_prob = float(arg_count / n)
  eng_prob = float(eng_count / n)
  return spa_prob, arg_prob, eng_prob

tuple_main = monte_carlo(10000)
spain, argentina, england = map(str, tuple_main)
print(f"Spain probability {spain}, Argentina probability {argentina}, England probability {england}")




