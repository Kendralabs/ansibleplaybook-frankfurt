import yaml

with open('.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
