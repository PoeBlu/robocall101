#! /usr/bin/python3
# rootVIII
# robocall 101
from argparse import ArgumentParser
from os import environ
from sys import exit, stdout
try:
    from twilio.rest import Client
except ImportError as err:
    stdout.write('Unable to import Twilio module, exiting...\n')
    exit(1)


class TwilComm(object):
    def __init__(self):
        try:
            self.from_ = environ['TWILIO_NUMBER']
            self.client = Client(
                environ['TWILIO_ACCOUNT_SID'],
                environ['TWILIO_AUTH_TOKEN']
            )
        except KeyError as key_err:
            self.exit_on_error(key_err)
        self.url = 'https://www.restwords.com/'

    @staticmethod
    def exit_on_error(e):
        stdout.write(type(e).__name__ + ': ' + str(e) + '\n')
        exit(1)


class Call(TwilComm):
    def __init__(self):
        super(TwilComm, self).__init__()
        self.url += 'api/post_json'

    def make_call(self):
        pass


class Text(TwilComm):
    def __init__(self):
        super(TwilComm, self).__init__()

    def send_text(self):
        pass


class ArnoldsHavingABadDay(TwilComm):
    def __init__(self):
        super(TwilComm, self).__init__()
        self.url += 'static/arnold.mp3'

    def arnold_call(self):
        pass


class Arguments:
    def __init__(self):
        description = 'Robocall and Robotext via the command line.\n'
        self.parser = ArgumentParser(description=description)
        self.parser.add_argument(
            '-n', '--number', required=True, help='Outgoing phone number')
        self.parser.add_argument(
            '-c', '--call', help='Robocall - enter text to be spoken')
        self.parser.add_argument(
            '-t', '--text', help='Text - enter text to send as SMS')
        self.parser.add_argument(
            '-a', '--arnold', action='store_true', help='ArnoldsHavingABadDay')

    @classmethod
    def help_menu(cls):
        return """

            REQUIRED:
            -n <outgoing number>               -| Target phone number

            PICK ONE:
            -c/--call <text/string here>       -| Robocall on thy fly
            -t/--text <text/string here>       -| Send an SMS
            -a/--arnold                        -| Call with Arnold recording

        """

    def get_args(self):
        return self.parser.parse_args()


if __name__ == '__main__':
    args = Arguments().get_args()
    if args.call:
        Call().make_call()
    elif args.text:
        Text().send_text()
    elif args.arnold:
        ArnoldsHavingABadDay().arnold_call()
    else:
        print(Arguments.help_menu())
