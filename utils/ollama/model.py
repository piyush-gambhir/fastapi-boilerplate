# model_management.py
import ollama

def list_models():
    return ollama.list()

def show_model(model_name):
    return ollama.show(model_name)

def create_model(custom_model_name, base_model_name, system_prompt):
    # ollama >= 0.4 replaced the `modelfile` string with structured fields
    return ollama.create(
        model=custom_model_name, from_=base_model_name, system=system_prompt
    )

def copy_model(source_model, destination_model):
    return ollama.copy(source_model, destination_model)

def delete_model(model_name):
    return ollama.delete(model_name)

def pull_model(model_name):
    return ollama.pull(model_name)

def push_model(model_name):
    return ollama.push(model_name)

def check_running_models():
    return ollama.ps()
