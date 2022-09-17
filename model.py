import random
from match import Match

class Tournament:
    def __init__(self,name,venue,date,rounds,players,time_controll,description):
        self.name=name
        self.venue=venue
        self.date=date
        self.number_of_rounds=4
        self.rounds=rounds
        self.players=players
        self.time_controll=time_controll
        self.description=description

class Player:
    def __init__(self,id,last_name, first_name,DOB,sex,ranking):
        self.id=id
        self.last_name=last_name
        self.first_name=first_name
        self.DOB=DOB
        self.sex=sex
        self.ranking=ranking
        self.score=0

    def __repr__(self):
        return f'{self.first_name} {self.id}'

    def increase_score(self,score):
        self.score +=score


class Round:
    def __init__(self,match,round_name,start_date,end_date):
         self.matches=[match]
         self.name=round_name
         self.start_date=start_date
         self.end_date=end_date
         self.round=1


class PlayerLog:  
    def __init__(self,all_players):
        self.log_list={}
        self.all_players = all_players

    def get_log_list(self):
        return self.log_list

    def create_log_list(self):
        for player in self.all_players:
            self.log_list[f'{player.last_name} {player.first_name}']=[]


    def round1_log(self,players):
        for player in players:

            for player_name in self.log_list.keys():
                opponent = self.log_list[player_name].count(f'{player.last_name} {player.first_name}')

                if opponent==0:
                    self.log_list[player_name].append(f'{player.last_name} {player.first_name}')
        return self.log_list      

    # def round2_log(self,players):
    #     for player in players:

    #         for player_name in self.log_list.keys():
    #             opponent = self.log_list[player_name].count(f'{player.last_name} {player.first_name}')

    #             if opponent==0:
    #                 self.log_list[player_name].append(f'{player.last_name} {player.first_name}')
                
        


def name_generator():
    names = ('John', 'Andy', 'Joe', 'Johnson', 'Smith', 'Williams', 'Ola', 'Letty', 'Ade', 'Tawa')
    return random.choice(names)

def dob_generator():
    names = ('12.12.90', '01.04.89', '11.10.92', '06.06.88', '01.12.02', '07.03.89', '03.03.90')
    return random.choice(names)

def gender_generator():
    names = ('M', 'F')
    return random.choice(names)

      

def create_players():

    new_players = []
    for i in range(4):
        player = Player(i,name_generator(),name_generator(),dob_generator(),gender_generator(),i)
        new_players.append(player)
   
    n=1
    
    # while n<=4:
    #     print(f'\nENTER  PLAYER {n} INFO')
    #     first_name= input('First name: ')
    #     last_name= input('Last name: ')
    #     DOB= input('DOB: ')
    #     sex= input('Sex: ')
    #     rating= input('Rating: ')
    #     player=Player(last_name, first_name,DOB,sex,rating)
    #     new_players.append(player)
    #     n=n+1
    print('\n')
    return new_players
    

# def input_results(matches):
#     print(matches)
#     match_count=1
#     for match in matches:
#         print(f'\nMATCH {match_count} - {match[0][0]} VS {match[1][0]}')
#         player_count=1
#         for player in match:
#             print(f'\tPlayer {player_count} - {player[0]}')
#             player[1]= int(input('\tInput score:'))
#             player_count=player_count+1
#         match_count=match_count+1
def main():
  
    all_players=create_players()
    match = Match(all_players)
    
    match.pair_players_ranking()
    match.pair_players_score()
main()
# input_results(match.get_matches())





# def set_tournament(self):
#     name = "Chess Tournament"
#     venue = "Upanga"
#     date= "25.12.2022"
#     rounds= 
#     players= all_players
#     time_controll=
#     description=

# tournament(name,venue,date,rounds,players,time_controll,description)





