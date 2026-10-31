"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "Evelyn Tams was born on April 5th! We are going to call her Evvie (Eh-vee) for short. Everyone is doing great, and we are loving the time at home with our little family. Hope all is well with you.",
            "Thank you for reaching out and it was nice chatting with you. Please find the contract attached and we will appreciate it if you can review and sign/share with us at your earliest convenience. Be free to let us know if you have any questions. Thank you very much and we look forward to working with you soon!",
            "Am we the only residents who grout was done particularly badly this week? A bad job is almost worse than no job at all, although I know some people had loose bricks and such.",
            "I really enjoyed the group training class. Due to my life status changes, please rule me out from the badminton training class starting from November.",
            "I reviewed your corrections and they all look great. At this time I'm just waiting for your fingerprint results, which I will have hopefully Friday. Please let me know if you have any questions.",
            "The outdoor can have a different brand, its only a single stage. Switching it to a carrier brand will not get any benefits besides the brand. It will also push the cost up about $400",
            "Thank you for reaching out to us about this issue. The water heater in use is 50 gallons and the only one that works for your unit will be a made by a company called State. I spoke to Jeff the owner of J Hood services about the issues you are facing and he willing to help with any questions you have.",
            "This looks good! Could you please update 'Name and Mailing Address' (on p.2) to our residence address? Please share the application and we will fill it out. Thank you very much!",
            "Thank you for the updates. I had two bookings, only one of them shown in the hotel system. They said they were not able to find the booking below. Is my confirmation number in the hotel system now?",
            "You sent me some pictures about the suite with bed before. It seems like on upper floor to me as surrounded by trees. I am not sure is it the lower space? How much is the ceremony fee? Is it additional to the rooms fee?",
        ],
    },

    {
        "name": "score spread",
        "criterion": 2,
        "texts": [
            "Urban commuting refers to the daily travel between home and workplace that millions of city residents undertake. It is a defining feature of modern metropolitan life, shaped by the spatial separation between residential areas and centers of employment. Commuters typically rely on a mix of transportation modes, including private cars, buses, subways, bicycles, and walking. The choice of mode depends on factors such as distance, cost, convenience, and the quality of available infrastructure.The scale of urban commuting has significant consequences for both individuals and cities. For individuals, long commutes can consume several hours each day, reducing time available for family, rest, and leisure, and contributing to stress and fatigue. For cities, mass commuting generates traffic congestion, air pollution, and carbon emissions, while also placing heavy demands on public transport systems. Peak-hour crowding on subways and buses is a common challenge in large cities worldwide.In response, urban planners and policymakers have promoted strategies such as expanding public transit networks, developing park-and-ride facilities, encouraging cycling through dedicated lanes, and implementing congestion pricing. The rise of remote and hybrid work arrangements has also begun to reshape commuting patterns, reducing peak demand on certain days. Ultimately, efficient and sustainable urban commuting requires integrated planning that balances housing, employment distribution, and transport infrastructure, so that cities remain accessible, productive, and livable for their residents.",
            "We talked earlier on the phone and I would like to hold a small ceremony during my stay. The dates I booked are May 19 - 21. You mentioned that we can request for mowing the lawn with $500. I would like to have that. Please let me know the way you would like to receive the payment. - I am still hesitating about the place for the floral arch and the ceremony, near the gazebo or near the pond or near the house / grill. If you have the pictures handy, could you share a few with me? - What does the extra room (previous staff room) look like? - We will have <20 people on site during the ceremony, half of them will leave the retreat when it is done. I am also wondering if your team would consider providing the dinner options for us.Looking forward to hearing from you.Thank you! Have a nice day!",
            "I hope you and your family are safe and healthy! I want to take a moment to let you know that I have stepped down from the role of graduate program director. Moving forward, please contact the new graduate co-directors, Prof. Marty and Prof. Wan, for any issues/questions related to your graduate studies. It has been my pleasure and privilege to work with each of you, and I want to thank you for your patience and support, which makes my job a lot easier. I felt fortunate to get to know many of you and your graduate work. The Statistics department has many outstanding faculty. I am confident that you will have a fruitful graduate study at Mason and a successful career in your profession."
            "Urban commuting means the daily travel between home and office that millions of people doing daily. It is a defining feature of modern metropolitan life, shaped by the spatial separation between residential areas and centers of employment. Commuters typically rely on a mix of transportation modes, including private cars, buses, subways, bicycles. The choice of mode depends on factors such as distance, cost, convenience, and the quality of available infrastructure.The scale of urban commuting has significantly consequences for both individuals and cities. For individuals, long commutes can consume several hours each day, reducing time available for family, rest, and leisure, and contributing to stress and fatigue. For cities, mass commuting generates traffic congestion, air pollution, and carbon emissions, while also placing heavy demands on public transport systems. Peak-hour crowding on subways and buses are a common challenge in large cities worldwide.In response, urban planners and policymakers have promoted strategies such as expanding public transit networks, developing park-and-ride facilities, encouraging cycling through dedicated lanes, and implementing congestion pricing. The rise of remote and hybrid work arrangements has also begun to reshape commuting patterns, reducing peak demand on certain days. Ultimately, efficient and sustainable urban commuting requires integrated planning that balances housing, employment distribution, and transport infrastructure, so that cities remain accessible, productive, and livable for their residents.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "Urban commuting refers to the daily travel between home and workplace that millions of city residents undertake. It is a defining feature of modern metropolitan life, shaped by the spatial separation between residential areas and centers of employment. Commuters typically rely on a mix of transportation modes, including private cars, buses, subways, bicycles, and walking. The choice of mode depends on factors such as distance, cost, convenience, and the quality of available infrastructure.The scale of urban commuting has significant consequences for both individuals and cities. For individuals, long commutes can consume several hours each day, reducing time available for family, rest, and leisure, and contributing to stress and fatigue. For cities, mass commuting generates traffic congestion, air pollution, and carbon emissions, while also placing heavy demands on public transport systems. Peak-hour crowding on subways and buses is a common challenge in large cities worldwide.In response, urban planners and policymakers have promoted strategies such as expanding public transit networks, developing park-and-ride facilities, encouraging cycling through dedicated lanes, and implementing congestion pricing. The rise of remote and hybrid work arrangements has also begun to reshape commuting patterns, reducing peak demand on certain days. Ultimately, efficient and sustainable urban commuting requires integrated planning that balances housing, employment distribution, and transport infrastructure, so that cities remain accessible, productive, and livable for their residents.",
            "We talked earlier on the phone and I would like to hold a small ceremony during my stay. The dates I booked are May 19 - 21. You mentioned that we can request for mowing the lawn with $500. I would like to have that. Please let me know the way you would like to receive the payment. - I am still hesitating about the place for the floral arch and the ceremony, near the gazebo or near the pond or near the house / grill. If you have the pictures handy, could you share a few with me? - What does the extra room (previous staff room) look like? - We will have <20 people on site during the ceremony, half of them will leave the retreat when it is done. I am also wondering if your team would consider providing the dinner options for us.Looking forward to hearing from you.Thank you! Have a nice day!",
            "Commuting is one of those everyday routines that quietly structures urban life. Most working adults in large cities travel between home and workplace on a daily basis, and the way they do so—car, bus, subway, bicycle, or on foot—depends on distance, cost, and how good the local infrastructure happens to be. The effects are easy to underestimate. Long commutes eat into time that might otherwise go to family, rest, or simply doing nothing, and they tend to leave people tired before the workday has even begun. Cities feel the pressure too: congestion, air pollution, and overcrowded trains during peak hours are familiar problems almost everywhere. Planners have responded with expanded transit networks, cycling lanes, park-and-ride schemes, and in some places congestion charges, though results vary considerably. Remote and hybrid work has recently changed the picture as well, thinning out peak-hour demand on certain days—though I suspect the effect is smaller than headlines suggest. What seems clear is that commuting cannot be fixed by transport policy alone; it also depends on where housing is built and where jobs are located. Get those wrong, and even a good subway system will struggle.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},              # no text field
            {"text": "", "creator_id": "eval_bad_empty"},    # empty string
            {"text": None, "creator_id": "eval_bad_null"},   # null
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
        ],
    },
    ]

def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
