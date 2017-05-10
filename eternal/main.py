import sys
import argparse
import datetime


def calculate(year, month, day):
    """
    Calculates day of the week (0-Monday, 1-Tuesday)
    :param year:
    :param month:
    :param day:
    :return:
    """

    try:
        return datetime.date(year, month, day).weekday()
    except:
        return None


def main(args):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--year',
                            type=int,
                            required=True,
                            help='Year')
        parser.add_argument('--month',
                            type=int,
                            required=True,
                            help='Month')
        parser.add_argument('--day',
                            type=int,
                            required=True,
                            help='Day')
        parsed_args = parser.parse_args(args)
        weekday = calculate(parsed_args.year, parsed_args.month, parsed_args.day)
    except:
        return 1

    if weekday is None:
        return 1
    else:
        print("Weekday {}".format(weekday))
        return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
