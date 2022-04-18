from brownie import FundMe
from scripts.utils import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Funding {entrance_fee} to {fund_me.address}")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print(f"Withdrawing {fund_me.address}")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
