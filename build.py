#!/usr/bin/env python
import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help='Docker build mode [base, local]')
args = parser.parse_args()

if args.mode == 'base':
    try:
        # pipenv lock으로 requirements.txt 생성
        subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)
        # docker builder
        subprocess.call('docker build -t eb-docker:base -f Dockerfile.base .', shell=True)
    finally:
        os.remove('requirements.txt')

elif args.mode == 'local':
    subprocess.call('docker build -t eb-docker:local -f Dockerfile.local .', shell=True)

elif args.mode == 'dev':
    subprocess.call('docker build -t eb-docker:dev -f Dockerfile.dev .', shell=True)

else:
    while True:
        user_input = input('Select mode:\n1: base\n2: local\n3: production\nChoice: ')
        if user_input == '1':
            subprocess.call('./build.py -m base', shell=True)
            break
        elif user_input == '2':
            subprocess.call('./build.py -m local', shell=True)
            break
        elif user_input == '3':
            subprocess.call('docker build -t eb-docker:production -f Dockerfile.production .', shell=True)
            break
        else:
            print('1~3번 중에서 다시 입력 해 주세요')