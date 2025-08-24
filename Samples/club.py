clubs = {}
num_clubs = int(input("Enter the number of clubs: "))

for i in range(num_clubs):
    club_name = input(f"Enter name of club {i+1}: ")
    clubs[club_name] = set()
    
    num_members = int(input(f"Enter number of members for {club_name}: "))
    for j in range(num_members):
        member_id = int(input(f"Enter member ID for member {j+1}: "))
        member_name = input(f"Enter name for member {j+1}: ")
        clubs[club_name].add((member_id, member_name))

print("\nClub Information:")
for club1 in clubs:
    for club2 in clubs:
        if club1 < club2:
            common = clubs[club1] & clubs[club2]
            if common:
                print(f"Common members between {club1} and {club2}: {common}")

for club, members in clubs.items():
    print(f"{club}: {len(members)} members")
    print(f"Members: {members}")