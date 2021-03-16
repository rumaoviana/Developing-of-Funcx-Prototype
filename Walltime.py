from funcx.sdk.client import FuncXClient
fxc = FuncXClient()
def funcx_test():
    while True:
        print("Viana")
func_uuid = fxc.register_function(funcx_test)
tutorial_endpoint = '70d29c21-66c3-4ba8-98fc-91490b522699' # Public tutorial endpoint
res = fxc.run(endpoint_id=tutorial_endpoint, function_id=func_uuid)
funcx_test()

