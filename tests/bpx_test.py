# Add the API_KEY and API_SECRET in line 12 before running this code

# import pytest
# from bpx.bpx import BpxClient

# chains = ["Bitcoin"]
# symbols = ['SOL_USDC']

# @pytest.fixture
# def client_obj():
#     bpx_client = BpxClient()
#     bpx_client.init("", "") # Parameters[API_KEY,API_SECRET]
#     return bpx_client

# def test_deposit_address(client_obj):
#     for chain in chains:
#         client_obj.depositAddress(chain=chain)

# def test_order_history(client_obj):
#     for symbol in symbols:
#         client_obj.orderHistoryQuery(symbol,10,0) # Parameters[SYMBOL,LIMIT,OFFSET]

# # TODO: Add tests for all methods
