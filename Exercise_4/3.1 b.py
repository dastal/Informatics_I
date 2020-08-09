cl_standings = [["A", ("Manchester United",9), ("FC Basel", 6),
    ("CSKA Moscow", 3), ("Benfica", 0)],\
        ["B", ("PSG",9), ("FC Bayern", 6), ("Celtic FC", 3),
         ("Anderlecht", 0)],\
        ["C", ("Chelsea FC",7), ("AS Roma", 5), ("Atl. Madrid", 2),
         ("Qarabag", 1)],\
        ["D", ("FC Barcelona",9), ("Juventus", 6), ("Sporting Lisbon",3),
         ("Olimpiakos", 0)],\
        ["E", ("Spartak Moscow",5), ("Liverpool FC", 5), ("Sevilla FC", 4),
         ("NK Maribor", 1)],\
        ["F", ("Manchester City FC",9), ("FC Shakhtar Donetsk", 6),
         ("SCC Napoli", 3), ("Feyenoord", 0)],\
        ["G", ("Besiktas",9), ("RB Leipzig", 4), ("FC Porto", 3),
         ("AS Monaco", 1)],\
        ["H", ("Real Madrid CF",7), ("Tottenham Hotspur FC", 7),
         ("Apoel FC", 1), ("Borussia Dortmund", 1)],\
    ]


def add_teams(list):
    i = 0
    cl_standings_dict = {}
    while i <= len(list)-1:
        cl_standings_dict[list[i][0]] = list[i][1:]
        i += 1
    return cl_standings_dict


standings_dict = add_teams(cl_standings)
print(standings_dict)
print(standings_dict["G"])
print(standings_dict["A"][1])