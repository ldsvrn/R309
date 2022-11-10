#!/usr/bin/python3

import sys


def printfile(file):
    try:
        with open(file, 'r') as f:
            for l in f:
                print(l.rstrip("\n\r"))  # pour virer les CRLF
    except FileNotFoundError:
        print("Erreur: Le fichier spécifié n'existe pas")
    except PermissionError:
        print("Erreur: Vous n'avez pas la permission de lire ce fichier")
    except IOError:
        print("Erreur: Impossible de lire le fichier")
    finally:
        print("Fin du programme")
    # FileExistsError


if __name__ == "__main__":
    try:
        sys.exit(printfile(sys.argv[1]))
    except IndexError as err:
        print("Erreur: Aucun fichier en argument")
        sys.exit(22) # EINVAL 	22 	It is displayed if there is an invalid argument.
        # raise Exception("Aucun fichier en argument!") from err # err cause cette exception
