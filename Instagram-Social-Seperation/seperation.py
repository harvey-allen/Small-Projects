from InstagramAPI import InstagramAPI

api = InstagramAPI("username", "password") #Enter credentials
api.login()

def getFollowing(userID): #List of all the users that are follwing
    api.getUsernameInfo(userID)
    api.LastJson
    following = []
    nextID = True
    while nextID:
        if nextID is True:
            nextID = ''
        add = api.getUserFollowings(userID, maxid=nextID)
        following.extend(api.LastJson.get('users', []))
        nextID = api.LastJson.get('next_max_id', '')
    return following

def getFriends(userID): #Returns a list of friends
    followers = api.getTotalFollowers(userID) #List of all the users that are followed
    followersID = []
    following = getFollowing(userID)
    followingID = []
    for users in followers:
        if not users['is_private']: #Removes private users
            followersID.append(users['pk']) #Only the user ID's
    for users in following:
        if not users['is_private']:
            followingID.append(users['pk'])
    friends = set(followersID) & set(followingID) #Intersection of the sets
    return list(friends)

def bubbleSort(list): #Sorting algorithm
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return list

def binarySearch(list, left, right, x): #Recursive Binary Search algorithm
  if right >= left:
      middle = l + (right - left)//2
      if list[middle] == x:
          return True
      elif list[middle] > x:
          return binarySearch(list, left, middle-1, x)
      else:
          return binarySearch(list, middle+1, right, x)
  else:
      return False

def search(startID, endID, seperation = 0): #Recursive function
    found = False
    seperation += 1
    currenSsearch = bubbleSort(getFriends(startID)) #Order list of friends
    while not found:
        if binarySearch(currenSsearch, 0, len(currenSsearch)-1, endID):
            return seperation #Degrees of sepeartion between users
            found = True
        else:
            for user in currenSsearch:
                search(friend, endID, seperation)
                
