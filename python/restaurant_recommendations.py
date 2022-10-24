class Solution(object):
    def restaurant_recommendations(self, friends_list, restaurants_map):
        final_map = {}
        for group in friends_list:
            all_recommendations = ()
            # flatten the map to get all the recommendations
            for friend in group :
                restaurants =  restaurants_map.get(friend)
                for r in restaurants:
                    all_recommendations += tuple(r)
            # end
            for friend in group:
                temp = []
                # temp_set = all_recommendations
                for a in all_recommendations:
                    if a not in  restaurants_map.get(friend):
                        temp.append(a)
                if friend in final_map:
                    existing_friend_recommendation = final_map.get(friend)
                    for e in existing_friend_recommendation:
                        if e not in temp:
                            temp.append(e)
                    final_map[friend] = sorted(list(set(temp)))
                else:
                    final_map[friend] = sorted(list(set(temp)))
        return final_map


s = Solution()
friends_list = [[1,2]] 
restaurants_map = {1:['A','B'], 2:['B','C','D']}
print(s.restaurant_recommendations(friends_list, restaurants_map))

friends_list = [[1,2], [2,3,4]] 
restaurants_map = {1:['A','B'], 2:['B','C','D'], 3:['D','E','F'], 4:['G','Q','P']}
print(s.restaurant_recommendations(friends_list, restaurants_map))