#!/usr/bin/env python3
# rootVIII
# robocall101 - Robovoice/SMS command-line tool
# pycodestyle/pep8 validated
from argparse import ArgumentParser
from json import loads
from os import environ
from sys import exit, argv
from urllib.request import Request, urlopen
from urllib.error import URLError
try:
    from twilio.rest import Client
except ImportError:
    print('Unable to import Twilio module, exiting.')
    exit(1)


class TwilComm(object):
    def __init__(self):
        self.my_twilio = environ['TWILIO_NUMBER']
        self.client = Client(
            environ['TWILIO_ACCOUNT_SID'], environ['TWILIO_AUTH_TOKEN'])
        self.url = 'https://www.restwords.com/api/post_markup'
        self.message = ''

    @staticmethod
    def exit_on_error(e):
        print(type(e).__name__ + ': ' + str(e))
        exit(1)

    def post(self):
        request = Request(self.url)
        request.add_header('Content-type', 'text/xml; charset="utf-8"')
        rbody = '<?xml version=\"1.0\" encoding=\"utf-8\"?><Response>'
        rbody += '<Pause/><Say>' + self.message + '</Say></Response>'
        request.data = rbody.encode()
        try:
            result = urlopen(request)
        except URLError as e:
            self.exit_on_error(e)
        else:
            self.url = loads(result.read().decode())['url']


class Call(TwilComm):
    def __init__(self, outgoing, message):
        TwilComm.__init__(self)
        self.outgoing = outgoing
        self.message = message

    def make_call(self):
        self.client.calls.create(
            to=self.outgoing, from_=self.my_twilio, url=self.url)


class Text(TwilComm):
    def __init__(self, outgoing, message):
        TwilComm.__init__(self)
        self.outgoing = outgoing
        self.message = message

    def send_text(self):
        self.client.messages.create(
            to=self.outgoing, from_=self.my_twilio, body=self.message)


class ArnoldsHavingABadDay(Call):
    def __init__(self, outgoing):
        Call.__init__(self, outgoing=outgoing, message=None)
        self.url = 'https://blue-platypus-3554.'
        self.url += 'twil.io/assets/arnold.mp3'
        self.outgoing = outgoing


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

            Obtain your Twilio Credentials and Twilio Number.
            Set the following environment variables:

            TWILIO_NUMBER=18885551234
            TWILIO_ACCOUNT_SID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            TWILIO_AUTH_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



            REQUIRED:
            -n <outgoing number>             -| Target phone number

            PICK ONE:
            -c/--call <text/string here>     -| Robocall on thy fly
            -t/--text <text/string here>     -| Send an SMS
            -a/--arnold                      -| Call with Arnold recording

        """

    def get_args(self):
        return self.parser.parse_args()


def main():
    # Print better help menu if no args
    if len(argv) < 2:
        print(Arguments.help_menu())
        exit(1)
    args = Arguments().get_args()
    if not args.number.isnumeric():
        print(Arguments.help_menu())
        exit(1)
    if args.call:
        call = Call(args.number, args.call)
        call.post()
        call.make_call()
    elif args.text:
        text = Text(args.number, args.text)
        text.send_text()
    elif args.arnold:
        ArnoldsHavingABadDay(args.number).make_call()
    else:
        print(Arguments.help_menu())


if __name__ == '__main__':
    main()
