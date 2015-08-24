My wordcloud work:

I grabbed tweets from three promising president candidates: Donald Trump, Hillary Clinton and Jeb Bush. I made one word cloud (.png file in folder) for each of them with the help of np_extractor. I regard the pictures as a way to see these three candidates' appeals and personalities. The figure-like word clouds are just made for fun.

Donald Trump: He talks about his slogan a lot, which is Make America Great Again. He cares about illegal immigration, border issue, wars and jobs. He emphasizes his leadership ability and his entrepreneurship. It also seems like that he monitors his polling quite frequently. He tweets positive numbers of various adjectives, which might partially be his way of showing his sarcasm. He always announces his whereabouts and talks about other people. His pragmatism is shown by his direct and strong verbs, like make, work, support, need, etc. Also, his adjective words can be quite extreme.

Hillary Clinton: Her tweets contains mostly contents in her other accounts, like TheBreifing2016, HillaryforIA, HillaryInNH, etc. She often appeals with her feminine characters, such as women, family, people, parenthood, and human. Especially, she mentions 2SmallToFail program for kids with high frequency. She also frequently talks about democratic topics including economy, immigration, health, education, right and equality. Her tweets does not include many verbs or adjectives, which gives her twitter account a professional look.

Jeb Bush: His most distinguished appeal is education. EdReform center, ExcelinEd foundation and AFloridaPromise foundation are frequently mentioned. He often talks about school, student, teacher, learning and scholarship. Although immigration, work and tax are also his topics, his focus is mainly education. Since he is the Governor in Florida, he talks about Florida quite a lot. As positive adjectives are concerned, he often uses word 'great'. His twitter account is also professional like Hillary's.



Recommendations to data collection code:

1. Dump tweets to json file together in one time. I found that the json file would contain several lists of tweet entities if they are dumped separately. It would be easier and fast for me to use json.loads to process if tweet entities are in one list. (Please see the changed code in getUserTimeline.py)

2. Change the mismatch between sql tables and queries in parseUserTimeline.py. In addUser, empty strings do not work for followers, friends, favourites and statuses because the corresponding variables in sql tables are integer and not null. I temporarily assigned them to '0'. However, I think maybe it would be better to make the variables null or create different tables for mentioned users and replied users. I also fixed a little bug in addUserMentions. (Please see the changed code in parseUserTimeline.py)

3. Use character set utf8mb4. I bumped into mysql error 1360: Incorrect string value and found out that it was caused by the character set. I fixed the problem with reference to http://dchua.com/2014/08/15/migrating-from-utf8-to-utf8mb4-in-mysql/.

4. I think the data collection process in these two py files are comprehensive and it might help to add the sql tables more structure. Current sql tables include hashtags, links, mentions, tweets and users. This database records the data from Twitter very well, but I do not find much difference between storing tweets in json and in DB except for being ready for Django. I also think it might be better to separate users, mentioned users and replied users. Since I have no deep understanding of the research right now, maybe I have no knowledge of your concerns in storing them this way.
