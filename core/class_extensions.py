import os , sys, re
# Ajouter le dossier racine (project/) au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from business_rules.variables import  numeric_rule_variable, string_rule_variable, boolean_rule_variable, rule_variable

def get_nested_value_from_path(data, path):
    """
    retourne la valeur d'un chemin par rapport à un dataset fournit en paramètre
    path ressemble à cela : test.objet[0].objet2.objet3
    """
    tokens = re.findall(r'\w+|\[\d+\]', path)
    current = data
    for token in tokens:
        if token.startswith('[') and token.endswith(']'):
            index = int(token[1:-1])
            current = current[index]
        else:
            current = current[token]
    return current

def add_methods_to_class(cls, method_names, paths, types):
    
    for name, path, typ in zip(method_names, paths, types):
        # On utilise une fermeture pour capturer le chemin
        def method_factory(path):
            def method(self):
                return get_nested_value_from_path(self.data, path)
            return method
        
        method = method_factory(path)

        # Application du décorateur approprié
        if typ == 'integer'or typ == 'date':
            method = numeric_rule_variable(method)
        elif typ == 'string':
            method = string_rule_variable(method)
        elif typ == 'boolean':
            method = boolean_rule_variable(method)
        elif typ in ['array', 'object']:
            method = rule_variable(method)
        else:
            #pass
            raise ValueError(f"Type inconnu : {typ}")

        # Ajout de la méthode à la classe
        setattr(cls, name, method)

# Votre classe VariablesProduit
# class BaseVariables:
#     pass

# class VariablesProduit(BaseVariables):
#     def __init__(self, data):
#         self.data = data

# # Ajout des méthodes à la classe
# add_methods_to_class(VariablesProduit, array_of_field_name, path_config, array_of_type)

# # Données d'exemple


# # Création d'une instance de VariablesProduit
# variables_produit = VariablesProduit(dataset_sample)

# # Accès à la méthode 'prix'
# valeur_prix = variables_produit.nomPieceJointe_1()
# print(f"Le prix est : {valeur_prix}")