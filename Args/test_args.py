import argparse

# https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-FT', '--defFalseStoreTrue', default=False, action="store_true", help='Show output')    
    parser.add_argument('-FF', '--defFalseStoreFalse', default=False, action="store_false", help='Show output')
    parser.add_argument('-TF', '--defTrueStoreFalse', default=True, action="store_false", help='Show output')
    parser.add_argument('-TT', '--defTrueStoreTrue', default=True, action="store_true", help='Show output')

    args = parser.parse_args()

    FT = args.defFalseStoreTrue
    FF = args.defFalseStoreFalse
    TF = args.defTrueStoreFalse
    TT = args.defTrueStoreTrue

    print('FT', FT)
    print('FF', FF)
    print('TF', TF)
    print('TT', TT)

    # $ python test_args.py
    # FT False
    # FF False
    # TF True
    # TT True

    # $ python test_args.py -FT -FF -TF -TT
    # FT True
    # FF False
    # TF False
    # TT True
