import g4f


print(g4f.Provider.Ails.params)  # supported args

'''
try:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "test php"}],
        stream=True,
    )
    for message in response:
        print(message, flush=True, end='')
except:
    print("gpt-3.5-turbo except")


try:
    # normal response
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": "test php"}],
    )  # alterative model setting

    print(response)
except:
    print("g4f.models.gpt_4 except")

try:
    # Set with provider
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.DeepAi,
        messages=[{"role": "user", "content": "test php"}],
        stream=True,
    )

    for message in response:
        print(message, flush=True, end='')
except:
    print("gpt-3.5-turbo except")

'''

try:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        provider=g4f.Provider.You,
        messages=[{"role": "user", "content": "test python"}],
        stream=True,
    )
    for message in response:
        print(message, flush=True, end='')
except:
    print("gpt-4 except")