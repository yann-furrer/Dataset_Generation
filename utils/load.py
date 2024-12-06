import json, yaml
#Load rules from JSON file

def load_rules(rules_int) -> dict:
    file_path = "./config/rules_config.json" if rules_int == 1 else "./config/inverted_rules_config.json"
    
    with open(file_path, 'r') as rules_file:
        return json.load(rules_file)
    
#Load config from YAML file
def load_yaml_config() -> dict:
    with open('./config/dataset_config.yaml', 'r') as config_file:
        return yaml.load(config_file, Loader=yaml.FullLoader)
    
