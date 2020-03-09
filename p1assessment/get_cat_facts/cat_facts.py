import requests

def cat_facts(amount):
    response = requests.get(f"https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={amount}")
    data = response.json()
    for i in range(0,amount):
        print(data[i]["text"])
    # pass

cat_facts(10)
