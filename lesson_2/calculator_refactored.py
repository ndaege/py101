import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

with open('lesson_2/calc_config.json', 'r') as config_file:
    data = json.load(config_file)
    
def get_param_and_lang(parameter, lang):
    return data.get(parameter).get(lang)


user_input = "y"
while user_input != "n":
    prompt("What language would you like to use? (en)")
    prompt("Cuál es el idioma que prefiere usar? (es)")
    lang = input("en/es\n")
    
    prompt(get_param_and_lang("welcome", lang))

    prompt(get_param_and_lang("first_number", lang))
    number1 = input()

    while invalid_number(number1):
        prompt(get_param_and_lang("num_invalid", lang))
        number1 = input()

    prompt(get_param_and_lang("second_number", lang))
    number2 = input()

    while invalid_number(number2):
        prompt(get_param_and_lang("num_invalid", lang))
        number2 = input()

    prompt(get_param_and_lang("operation", lang))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(get_param_and_lang("invalid_choice", lang))
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    prompt(f"The result is {output}")
    print()
    prompt(get_param_and_lang("continue", lang))
    user_input = input().lower()