from bs4 import BeautifulSoup

import requests
import pandas as pd

def get_context(url):
	url_list = ['https://hypeauditor.com/en/top-instagram/?p='+str(i+1) for i in range(20)]
	df = pd.DataFrame(columns=['real_name', 'user_name', 'follower', 'engagement', 'topic', 'country'])

	for url in url_list:
		r  = requests.get(url)
		data = r.content
		soup = BeautifulSoup(data, 'html.parser')

		tmp = soup.find_all(class_='kyb-table bloggers-top-table')
		raws = tmp[0].find_all('tr')
		for i in raws[1:]:
			# real name
			real_name = i.h4.text

			# user name
			user_name = i.find(class_='kyb-ellipsis').text

			# Followers
			follower = i.find_all(class_='t-a-r')[1].text

			# engagement
			engagement = i.find_all(class_='t-a-r')[2].text.lstrip()

			# topics
			topic_list = i.find_all('span', class_='bloggers-top-topic')
			topic_tmp = [i.text for i in topic_list]
			topic_str = ','.join(topic_tmp)

			# country
			country = i.find_all('td')[5].text

			tmp_dict = {'real_name': real_name, 'user_name': user_name, 'follower':follower, 'engagement':engagement, 'topic':topic_str, 'country':country}
			df = df.append(tmp_dict, ignore_index=True)

	return df


if __name__ == '__main__':
	url = 'https://hypeauditor.com/en/top-instagram/?p=1'
	df = get_context(url)
	df.to_csv(r'1000_ins.csv',index=False)