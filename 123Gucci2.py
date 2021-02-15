title = original['product_name']
gender = original['gender'].title().replace("Women","Women\'s").replace("Men","Men\'s")

#onesize_list = ["ONE SIZE", "one size", "OneSize", "One_Size", "One Size", "one_size", "ONE_SIZE"]
#for onesize in onesize_list:
#title = title.replace(onesize, "")

def nte(title):
	return '' if title is None else title.title()

if original['brand'] not in title and original['colours'] not in original['brand']:
  title = re.sub(ur'( +{0}$| +{0} +|^{0} +)'.format(original['colours']), ' ', title, flags=re.IGNORECASE).strip()

title = re.sub(ur'( +{0}$| +{0} +|^{0} +)'.format(original['gender']), ' ', title, flags=re.IGNORECASE).strip()

title = re.sub(ur'( +{0}$| +{0} +|^{0} +)'.format(original['materials']), ' ', title, flags=re.IGNORECASE).strip()

#title = re.sub(ur'( +{0}$| +{0} +|^{0} +)'.format(original['sizes']), ' ', title, flags=re.IGNORECASE).strip()

if len(nte(title) + ", " + nte(original['colours']) + ", " + nte(original['materials']) + ", " + nte(gender))>150:
  if len(nte(title) + ", " + nte(original['colours']) + ", " + nte(gender))>150:
    if len(nte(title) + ", " + nte(original['colours']))>150:
      return nte(title)
    else:
      return nte(title) + ", " + nte(original['colours'])
  else:
    return nte(title) + ", " + nte(original['colours']) + ", " + nte(gender)
else:
  return nte(title) + ", " + nte(original['colours']) + ", " + nte(original['materials']) + ", " + nte(gender)