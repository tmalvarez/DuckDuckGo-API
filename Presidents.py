import requests

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&t=h_&ia=web&format=json")
    rsp_data = resp.json()
    Us_presidents = [
        'Washington','Adams','Jefferson','Madison','Monroe','Jackson','Van Buren','Harrison',
        'Tyler','Polk','Taylor','Fillmore','Pierce','Buchanan','Lincoln','Johnson','Grant','Hayes',
        'Garfield','Arthur','Cleveland','Harrison','McKinley','Roosevelt','Taft','Wilson','Harding',
        'Coolidge','Hoover','Roosevelt','Truman','Eisenhower','Kennedy','Johnson','Nixon','Ford','Carter','Reagan',
        'Bush','Clinton','Bush','Obama','Trump','Biden'
    ]
    for textPres in rsp_data['RelatedTopics']:
        for president in Us_presidents:

            if president in textPres['Text']:
                Us_presidents.remove(president)
                print(president)
    assert len(Us_presidents) == 0
