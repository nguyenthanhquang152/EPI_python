from functools import reduce
from itertools import combinations, permutations, product


def cal_avg(n_tries):

    ref_stats = [0.03, 0.07, 0.3, 0.6]
    ref_points = [50, 20, 10, 0]

    point_stat_zip = dict(zip(ref_points, ref_stats))

    stats_tbl = {50: 0, 20: 0, 10: 0, 0: 0}

    sample = [ref_points] * n_tries
    combos = product(*sample)
    for combo in combos:
        sort_combo = sorted(combo)

        combo = map(lambda x: point_stat_zip[x], combo)
        stat = reduce((lambda x, y: x * y), combo)
        stats_tbl[sort_combo[-1]] += stat

    # print(reduce((lambda x, y: x + y), stats_tbl.values()))
    results = reduce((lambda x, y: x + y), [key * value for key, value in stats_tbl.items()])
    return results


def optimized_cal_avg(n_tries):

    ref_stats = [0.03, 0.07, 0.3, 0.6]
    ref_points = [50, 20, 10, 0]

    stats_tbl = {50: 0, 20: 0, 10: 0, 0: 0}
    for i in range(4):
        big_stats = sum(ref_stats[i:]) ** n_tries
        small_stats = sum(ref_stats[i+1:]) ** n_tries
        diff_stats = big_stats - small_stats
        stats_tbl[ref_points[i]] = diff_stats

    # print(reduce((lambda x, y: x + y), stats_tbl.values()))
    results = reduce((lambda x, y: x + y), [key * value for key, value in stats_tbl.items()])
    return results


for n in range(1, 10):
    print(f"{n} attempt {cal_avg(n)} vs {optimized_cal_avg(n)}")





