
def make_filter(name, IP_1, IP_2, community):
  s = ""
  s += "print '"+name+"\\n'\n"
  s += "bgp router "+IP_1+"\n"
  s += "	peer "+IP_2+"\n"
  # filter in
  s += "		filter in add-rule\n"
  s += "			match any\n"
  s += "			action 'community add "+community+"'\n"
  s += "			exit\n"
  # filter out
  s += "		filter out add-rule\n"
  s += "			match 'community "+community+"'\n"
  s += "			action deny\n"
  s += "			exit\n"
  s += "		exit\n"
  s += "	exit\n"
  return s

print make_filter('R1', '1.1.0.1', '4.0.0.3', '2')
