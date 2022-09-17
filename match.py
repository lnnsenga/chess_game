class Match:
    def __init__(self,all_players):
        self.players = all_players
        self.matches=[]
        self.round=1
        self.tracker = {}
  
    def sort_by_ranking(self): 
        return sorted(self.players,key=lambda player:player.ranking)


    def sort_by_score(self):
        return sorted(self.players,key=lambda player:(player.score), reverse = True)
        
    def update_tracker(self,first_player_id, second_player_id):
        try:
            player_list = self.tracker[first_player_id]
            player_list.append(second_player_id)
        except:
            self.tracker[first_player_id]=[second_player_id]
    
    def set_matches(self,matches):
        self.matches=matches

    def get_matches(self):
        return self.matches

    def sort_all_players(self):      
        if(self.round==1):
            return self.sort_by_ranking()
        return self.sort_by_score()       
       
    def pair_players_ranking(self):
        # create two groups
        sorted_players = self.sort_by_score()
    
        length = len(sorted_players)

        middle_index = length // 2

        first_half = sorted_players[:middle_index]
        second_half = sorted_players[middle_index:]

        matches=[]
        for i in range(len(first_half)):
            score = self.input_results([first_half[i],second_half[i]])
            first_half[i].increase_score(score[0])
            second_half[i].increase_score(score[1])
            match=self.new_match(first_half[i],score[0],second_half[i],score[1])
            matches.append(match)
            self.update_tracker(first_half[i].id,second_half[i].id)
            self.update_tracker(second_half[i].id,first_half[i].id)
        print(self.tracker,"tracker")
        self.set_matches(matches)
        self.round+=1
        return matches
        # divide each group into pairs

    def pair_players_score(self):
        # create two groups
        sorted_players = self.sort_all_players()
        print(sorted_players,"SORTED Players")

        length = len(sorted_players)

        middle_index = length // 2

        first_half = sorted_players[:middle_index]
        second_half = sorted_players[middle_index:]

      
        matches=[]
        has_paired = []
        for i in range(len(first_half)):
            for j in range(i + 1, len(sorted_players)):
                first_player_id, second_player_id = sorted_players[i], sorted_players[j]
                if not self.has_played(sorted_players[i].id, sorted_players[j].id) \
                    and first_player_id not in has_paired \
                    and second_player_id not in has_paired:
                    match=self.new_match(first_half[i],0,second_half[i],0)
                    self.update_tracker(sorted_players[i].id, sorted_players[j].id)
                    self.update_tracker(sorted_players[j].id, sorted_players[i].id)                    
                    has_paired.extend((first_player_id.id, second_player_id.id))
                    matches.append(match)
                    break
        self.set_matches(matches)

        has_paired = []
        print (self.tracker,"TRACKER")
        print(self.get_matches,"MATCHES")
        return matches



        # matches=[]
        # for i in range(len(first_half)):
        #     for j in range(i+1,len(sorted_players)):
        #         first_player_id , second_player_id = sorted_players[i].id,sorted_players[j].id
        #         if not self.has_played(first_player_id, second_player_id):
        #             match=self.new_match(first_half[i],0,second_half[i],0)
        #             self.update_tracker(first_half[i].id,second_half[i].id)
        #             self.update_tracker(second_half[i].id,first_half[i].id)
        #             matches.append(match)
        # self.set_matches(matches)
        # print(self.tracker,"tracker rounde2")
        # return matches
        # # divide each group into pairs




    def has_played(self,first_player_id, second_player_id):
        first_player_opponnents = self.tracker[first_player_id]
        return second_player_id in first_player_opponnents

    def input_results(self,matches):
        print(matches)
        score=[]
      
        print(f'\nMATCH - {matches[0]} VS {matches[1]}')
        player_count=1
        for player in matches:
            print(f'\tPlayer {player_count} - {player}')
            score.append(int(input('\tInput score:'))) 
        return score


    def set_players(self,player1,player2):
        self.player1=player1
        self.player2=player2

    def get_players(self):
        return self.players
        
       
    def set_scores(self,player1_score, player2_score):
        self.player1_score=player1_score
        self.player2_score=player2_score  

    def new_match(self,player1,player1_score,player2,player2_score):
        new_match = ([player1,player1_score],[player2,player2_score])
        return new_match
