
import yaml
def load_yaml(yml_file):
    with open(yml_file,"r") as f:
        load_json =yaml.load(f.read(),Loader=yaml.Loader)
    return load_json