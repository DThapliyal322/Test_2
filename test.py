import os

var = "Hello World"
var_2 = "Deepak"
def setup_custom_logger_gcp_with_service_id(log_name):
    os.environ["key_path"] = "./config/ring_central_dev_serviceaccount.json"
    # Instantiates a client with Service Account
    # logging_client = logging.Client.from_service_account_json(os.environ["key_path"])
    # Selects the log to write to
    # logger = logging_client.logger(log_name)
    # return logger
print(var)