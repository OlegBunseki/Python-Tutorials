import argparse

# https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--name', default=None, type=str, help='Show output')    

    args = parser.parse_args()

    if args.name is None:
        print('None Value')
    else:
        print(args.name)