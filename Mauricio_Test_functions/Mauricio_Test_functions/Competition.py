from players import Players
from playerstats import PlayerStats
from teams import Teams
from events import Events
from awards import Awards

PLAYERCSV = "player.csv"
PLAYERSQL = "Player.sqlite"


def main():
    print("""######\tTests players.py\t######""")
    a = Players()
    a.see_all()


    print("""######\tTests PlayerStats\t######""")
    b = PlayerStats(a)
    b.see_all()
    print()

    print("""######\tTests Events\t######""")
    d = Events()
    d.see_all()
    print()

    print("""######\tTests Teams\t######""")
    c = Teams(a, d)
    c.see_all()
    print()

    print("""######\tTests Awards\t######""")
    e = Awards()
    e.see_all()
    print()



if __name__ == "__main__":
    main()