def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}.")
        completed_models.append(current_design)


def show_complete_models(completed_models):
    print("The following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["iphone case", "robot pendant", "dodecachedron"]
completed_models = []

print_models(unprinted_designs[:], completed_models)  # [:] ENVIA UMA CÓPIA DA LISTA PARA MANTER A ORIGINAL INTACTA.
show_complete_models(completed_models)
