from brownie import FundMe, MockV3Aggregator, network, config
from scripts.utils import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    print(f"Deploying FundMe contract to {account}")
    # if we are on persistent network like Rinkeby, use the associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(price_feed_address,
                            {"from": account},
                            publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"FundMe contract deployed at {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
