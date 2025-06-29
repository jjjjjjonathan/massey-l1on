def findTeamIndex(team_id, teams):
  for index, team in enumerate(teams):
    if team[0] == team_id:
      return index
    
def buildScoresArray(matches, teams):
  rows = []
  for match in matches:
    row = [0] * len(teams)
    if match[1] >= match[2]:
      row[findTeamIndex(match[3], teams)] = 1
      row[findTeamIndex(match[4], teams)] = -1
      rows.append(row)
    else:
      row[findTeamIndex(match[4], teams)] = 1
      row[findTeamIndex(match[3], teams)] = -1
      rows.append(row)
  return rows

def buildGDArray(matches, teams, limit=99):
  gd_list = []
  for team in teams:
    gd = 0
    for match in matches:
      if team[0] == match[3]:
        result = match[1] - match[2]
        if abs(result) > limit:
          if match[1] > match[2]:
            gd += limit
          else:
            gd -= limit
        else:
          gd += (match[1] - match[2])
      
      if team[0] == match[4]:
        result = match[2] - match[1]
        if abs(result) > limit:
          if match[2] > match[1]:
            gd += limit
          else:
            gd -= limit
        else:
          gd += (match[2] - match[1])
    gd_list.append([gd])
  return gd_list
