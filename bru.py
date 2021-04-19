#! /usr/bin/env python3

import sys
import argparse
import requests

def checkApiSuccess (response):
    if response.status_code != 200:
        print ("Could not fetch the latest data of billyrocket. He is simply to fast")
        sys.exit (1)

def printDump (response, outFormat='text'):
    if outFormat == 'text':
        for data in response:
            print (data + ':', response [data]['value'], response [data]['unit'])
    else:
        print (response)

def printValueUnit (response, outFormat='text'):
    if outFormat == 'text':
        print (str (response ['value']), response ['unit'])
    else:
        print (response)

def billyrocketDistance (data):
    return data ['distance']

def billyrocketSpeed (data):
    return data ['speed']

def billyrocketUntilUniverseEnd (data):
    return data ['remaining']


if __name__ == "__main__":
    argParser = argparse.ArgumentParser (description='Get statistics about Billyrocket from the command line')
    argParser.add_argument ('-d', '--distance',
                                     help='Print how far Billyrocket has travelled so far',
                                     action='store_true')
    argParser.add_argument ('-s', '--speed',
                                     help='Print the current speed of Billyrocket',
                                     action='store_true')
    argParser.add_argument ('-r', '--remaining',
                                     help='Print the time until Billyrocket reaches the border of the universe',
                                     action='store_true')
    argParser.add_argument ('-t', '--dump',
                                     help="Dump all available information",
                                     action='store_true')
    argParser.add_argument ('-f', '--format',
                            help='The format to print in',
                            nargs=1,
                            choices=['text', 'json'],
                            default='text')

    # Stop if no arguments
    if len (sys.argv) == 1:
        argParser.print_help ()
        sys.exit (1)

    # Create dict from arguments
    args = vars (argParser.parse_args ())

    billyrocketData = requests.get ("https://billyrocket.dgren.dev/api")
    checkApiSuccess (billyrocketData)
    billyrocketJson = billyrocketData.json ()

    if args ['distance']:
        printValueUnit (billyrocketDistance (billyrocketJson), outFormat=args ['format'])
    if args ['speed']:
        printValueUnit (billyrocketSpeed (billyrocketJson), outFormat=args ['format'])
    if args ['remaining']:
        printValueUnit (billyrocketUntilUniverseEnd (billyrocketJson), outFormat=args ['format'])
    if args ['dump']:
        printDump (billyrocketJson, outFormat=args ['format'])
