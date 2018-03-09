"""A script to run projecteuler problems and checks results and run-times."""

__author__ = 'Ezio Melotti'

import re
import sys
import csv
import json
import glob
import time
import argparse
import importlib


def list_problems():
    """List all the problems that have a problemN.py file."""
    files = glob.glob('euler*.py')
    problems = [re.search('euler(\d+).py', f).group(1) for f in files]
    for problem in sorted(problems, key=int):
        print('{:>3s} {}'.format(problem, problems_info[problem][0]))
    return problems


def load_problems_info():
    """Load from a csv the number, description, and solution of the problems."""
    problems_info = {}
    with open('problems.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            num, desc, res = row
            problems_info[num] = (desc, res)
    return problems_info


def run_problem(num):
    """Run a single problem and return the result and the run-time."""
    modname = 'euler{}'.format(num)
    try:
        mod = importlib.import_module(modname)
    except ImportError:
        sys.exit('Unable to find/import {!r}.'.format(modname))
    func = getattr(mod, 'problem')
    start = time.perf_counter()
    res = func()
    end = time.perf_counter()
    t = end - start
    return res, t


def print_problem_results(problem, save=False):
    """Print the result and run-time of a problem."""
    print('Problem {}: {}'.format(problem, problems_info[problem][0]))
    res, t = run_problem(problem)
    print('  Solved in {:.3f}s, result: {!r}'.format(t, res))
    expected = problems_info[problem][1]
    try:
        expected = int(expected)
    except ValueError:
        pass  # the value is missing or not an int, keep the original value
    if expected and res != expected:
        print('  The result is wrong, expected: {!r}'.format(expected))
    print_time_diff(problem, t)
    if save:
        save_time(problem, t)


def print_time_diff(problem, time):
    """Print the difference between the current and last saved run-time."""
    try:
        with open('times.json') as f:
            times = json.load(f)
    except FileNotFoundError:
        print('  Unable to find times.json to compare results.')
        return
    if problem not in times:
        print('  No time found in times.json for problem {}.'.format(problem))
        return
    old_time = times[problem]
    diff = time / old_time
    res = 'slower' if diff >= 1 else 'faster'
    print('  The new solution is {:.2f}x {} '
          'than the previous one.'.format(diff, res))


def save_time(problem, time):
    """Save the run-time in a json file."""
    try:
        with open('times.json') as f:
            times = json.load(f)
    except FileNotFoundError:
        with open('times.json', 'w') as f:
            json.dump({problem: time}, f)
        print('  times.json has been created.')
    else:
        times[problem] = time
        with open('times.json', 'w') as f:
            json.dump(times, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", help="the problem number", nargs='?')
    parser.add_argument("--list", help="list the available problems",
                        action="store_true")
    parser.add_argument("--all", help="run all the available problems",
                        action="store_true")
    parser.add_argument("--save", help="save the run-time of the problem",
                        action="store_true")
    args = parser.parse_args()
    problems_info = load_problems_info()
    if args.list:
        list_problems()
    elif args.problem:
        print_problem_results(args.problem, args.save)
    elif args.all:
        for problem in list_problems():
            print_problem_results(str(problem), args.save)
    else:
        parser.print_help()
