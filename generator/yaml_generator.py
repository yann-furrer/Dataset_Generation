#Faker method to generate nested object

import yaml
# Il faut implémenter les fakerType

# Exemple de données
yaml_data = {
    'datasetName': 'produit',
    'numberOfRecords': 5,
    'fields': []
}

datatest = {
    'price': 18,
    'produit': 'Colleen Lynch',
    'description': {
        'test21': 8,
        'Obj': [2, '2022-05-02', 1656526831, 2, '2020-09-01', 1656805500],
        'test22': 'walteroliver@example.com'
    },
    'quantite': 17,
    'discount': None
}

def flatten_object(obj, level=0, parent_key=''):
    """
    Aplati une structure imbriquée en une liste de champs avec leurs types et niveaux.
    """
    items = []
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            type_name = get_type_name(value)
            items.append({'name': key, 'type': type_name, 'level': level})
            if isinstance(value, (dict, list)):
                items.extend(flatten_object(value, level + 1, parent_key=key))
    
    elif isinstance(obj, list):
        for idx, item in enumerate(obj, start=1):
            type_name = get_type_name(item)
            name = f"{parent_key}_{idx}"  # Inclure l'indice pour différencier les éléments de liste
            items.append({'name': name, 'type': type_name, 'level': level})
            if isinstance(item, (dict, list)):
                items.extend(flatten_object(item, level + 1, parent_key=name))
    print(items)
    return items

def get_type_name(value):
    """
    Détermine le type d'un objet pour la description de schéma.
    """
    if isinstance(value, list):
        return 'array'
    elif value is None:
        return 'null'
    elif isinstance(value, (int, float)):
        return 'number'
    elif isinstance(value, str):
        return 'string'
    elif isinstance(value, dict):
        return 'object'
    elif isinstance(value, bool):
        return 'boolean'
    return type(value).__name__

def build_structure(flat_data):
    """
    Construit une structure hiérarchique à partir d'une liste de champs aplanis.
    """
    root = {'datasetName': 'UserProfiles', 'numberOfRecords': 3, 'fields': []}
    stack = [(root, -1)]  # Stack pour gérer les niveaux hiérarchiques

    for item in flat_data:
        node = {'fieldName': item['name'], 'type': item['type']}
        current_level = item['level']

        # Ajuster le niveau hiérarchique
        while stack and stack[-1][1] >= current_level:
            stack.pop()

        parent_node, _ = stack[-1]
        if 'fields' not in parent_node:
            parent_node['fields'] = []
        parent_node['fields'].append(node)

        stack.append((node, current_level))

    return root

# Exécution
flattened_data = flatten_object(datatest)
structure = build_structure(flattened_data)

# Impression en YAML
print(yaml.dump(structure, sort_keys=False))