
# communities:
# 0: client
# 1: peer
# 2: provider

def filter_client(CLIENT_IP, PROVIDER_IP):
  s = ""
  # client router
  s += "bgp router "+CLIENT_IP+"\n"
  s += "	peer "+PROVIDER_IP+"\n"
  # tag routes from provider, low preference
  s += "		filter in add-rule\n"
  s += "			match any\n"
  s += "			action 'community add 2'\n"
  s += "			action 'local-pref 2'\n"
  s += "			exit\n" # exit filter
  # do not share routes from peers to provider
  s += "		filter out add-rule\n"
  s += "			match 'community is 1'\n"
  s += "			action deny\n"
  s += "			exit\n" # exit filter
  # do not share routes from providers to provider
  s += "		filter out add-rule\n"
  s += "			match 'community is 2'\n"
  s += "			action deny\n"
  s += "			exit\n" # exit filter
  s += "		exit\n" # exit peer
  s += "	exit\n" # exit router
  # return result
  return s

def filter_provider(PROVIDER_IP, CLIENT_IP):
  s = ""
  # provider router
  s += "bgp router "+PROVIDER_IP+"\n"
  s += "	peer "+CLIENT_IP+"\n"
  # tag routes from client, high preference
  s += "		filter in add-rule\n"
  s += "			match any\n"
  s += "			action 'community add 0'\n"
  s += "			action 'local-pref 100'\n"
  s += "			exit\n" # exit filter
  s += "		exit\n" # exit peer
  s += "	exit\n" # exit router
  # return result
  return s

def filter_peers(PEER1_IP, PEER2_IP):
  s = ""
  s += "bgp router "+PEER1_IP+"\n"
  s += "	peer "+PEER2_IP+"\n"
  # tag routes from peer, medium preference
  s += "		filter in add-rule\n"
  s += "			match any\n"
  s += "			action 'community add 1'\n"
  s += "			action 'local-pref 10'\n"
  s += "			exit\n" # exit filter
  # do not share routes from peers to peer
  s += "		filter out add-rule\n"
  s += "			match 'community is 1'\n"
  s += "			action deny\n"
  s += "			exit\n" # exit filter
  # do not share routes from providers to peer
  s += "		filter out add-rule\n"
  s += "			match 'community is 2'\n"
  s += "			action deny\n"
  s += "			exit\n" # exit filter
  s += "		exit\n" # exit peer
  s += "	exit\n" # exit router
  return s

def make_filters(combinaisons):
  s = ""
  for c in combinaisons:
    # check relation
    if c[7] == "0": # R1 client to R2
      s += filter_client(c[0], c[1])
      s += filter_provider(c[1], c[0])
    elif c[7] == "2": # R1 provider to R2
      s += filter_client(c[1], c[0])
      s += filter_provider(c[0], c[1])
    elif c[7] == "1": # pairs
      s += filter_peers(c[1], c[0])
      s += filter_peers(c[0], c[1])
    s += "\n"
  return s


if __name__ == '__main__':
  from routesgen import combinaisons
  f = open('filters.cbgp', 'w')
  content = make_filters(combinaisons)
  f.write(content)
  f.close()
