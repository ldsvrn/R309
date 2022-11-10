#!/usr/bin/env python3

import multiprocess
import threads
import pool
import argparse
import logging
import time
import statistics

logging.basicConfig(level=logging.INFO)


def main(nb: int) -> None:
    logging.info(f"Lancement de {nb} test avec les threads...")
    threads_times = []
    for i in range(nb):
        logging.info(f"Test n°{i+1}...")
        start = time.perf_counter()
        threads.main()
        threads_times.append(time.perf_counter() - start)

    logging.info(f"Lancement de {nb} test avec les process...")
    process_times = []
    for i in range(nb):
        logging.info(f"Test n°{i+1}...")
        start = time.perf_counter()
        multiprocess.main()
        process_times.append(time.perf_counter() - start)

    logging.info(f"Lancement de {nb} test avec la pool...")
    pool_times = []
    for i in range(nb):
        logging.info(f"Test n°{i+1}...")
        start = time.perf_counter()
        pool.main()
        pool_times.append(time.perf_counter() - start)
    
    print(f"Temps moyen pour les threads: {round(statistics.fmean(threads_times), 3)}s")
    if nb > 1:
        print(f"Variance pour les threads: {round(statistics.variance(threads_times), 3)}s")
    print("")
    
    print(f"Temps moyen pour les multiprocessing: {round(statistics.fmean(process_times), 3)}s")
    if nb > 1:
        print(f"Variance pour les multiprocessing: {round(statistics.variance(process_times), 3)}s")
    print("")

    print(f"Temps moyen pour la pool: {round(statistics.fmean(pool_times), 3)}s")
    if nb > 1:
        print(f"Variance pour la pool: {round(statistics.variance(pool_times), 3)}s")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--nb", help="nombre de tests (par défaut: 10)")
    args = parser.parse_args()
    if args.nb:
        main(int(args.nb))
    else:
        main(10)
