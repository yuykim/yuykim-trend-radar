



# Early Detection of Research 

# Trends 

Angelo Antonio Salatino 

Knowledge Media Institute 

The Open University 

This dissertation is submitted for the degree of 

_Doctor of Philosophy_ 

Advisers: Prof. Enrico Motta 

Dr. Francesco Osborne 

November 2018 

© Copyright by Angelo Antonio Salatino, 2018. 

All rights reserved. 

## **Abstract** 

Being able to rapidly recognise new research trends is strategic for many stakeholders, including universities, institutional funding bodies, academic publishers and companies. The literature presents several approaches to identifying the emergence of new research topics, which rely on the assumption that the topic is already exhibiting a certain degree of popularity and consistently referred to by a community of researchers. However, detecting the emergence of a new research area at an embryonic stage, i.e., before the topic has been consistently labelled by a community of researchers and associated with a number of publications, is still an open challenge. In this dissertation, we begin to address this challenge by performing a study of the dynamics preceding the creation of new topics. This study indicates that the emergence of a new topic is anticipated by a significant increase in the pace of collaboration between relevant research areas, which can be seen as the ancestors of the new topic. Based on this understanding, we developed Augur, a novel approach to effectively detect the emergence of new research topics. Augur analyses the diachronic relationships between research areas and is able to detect clusters of topics that exhibit dynamics correlated with the emergence of new research topics. Here we also present the Advanced Clique Percolation Method (ACPM), a new community detection algorithm developed specifically for supporting this task. Augur was evaluated on a gold standard of 1,408 debutant topics in the 2000-2011 timeframe and outperformed four alternative approaches in terms of both precision and recall. 

iii 

iv 

To those who keep feeding my spirit of inquiry. 

v 

## **Acknowledgements** 

The PhD journey is a tough one. It is meant to last between 3 to 4 years in which you are involved in a wide range of activities, you face several challenges, and it requires an enormous amount of energies. It is not all doom and gloom, though. I have been fortunate enough to be constantly surrounded by amazing people, and I would like to use this space to express my gratitude to those who contributed in different ways to this journey. 

First and foremost, I would like to thank Beppe. He is involved in this journey as much as I am. He helped me in applying to this studentship and provided useful insights while writing my research proposal. We know each other since 2007, we went to university together and we both started a PhD at the KMi. The “barese couple” I believe we were called at that time. Being with him here, made my move to the UK smoother. We were doing a lot of stuff together, except playing League of Legends. I grew a lot beside him. I owe him a debt of gratitude. 

Special thanks go to my _intellectual fathers_ Enrico and Francesco, who gave me the opportunity to grow as a researcher under their mentorship. Their support and guidance have been crucial for the development of my work and skills. Enrico is an experienced supervisor. Every time I would face difficulties, he would jump on board and simplify my overcomplicated thoughts. Francesco is an engine of ideas. He is very knowledgeable, and he is able to break down problems and challenge ideas on the fly. It was a privilege being supervised by them. 

I also would like to thank both my examiners, Kalina Bontcheva and Alun Preece, for making my defence enjoyable and fairly though, and for their valuable comments aiming at improving this dissertation. It was a very interesting discussion. 

Throughout this journey, I also had the privilege to meet unique people, with whom I shared the pains and joys of this journey: Patrizia, Pinelopi, Loua, Tina. 

vi 

Always there providing advice, help and encouragement. To say thank you is not enough. 

A great thank also goes to Alberto, Alessandro, Andrea, Thiviyan, Giorgio, Paco, Maria, Ilaria, Manu, Martin, Matteo, Simon, Marilena, and many others, who made my life in Milton Keynes always warm and enjoyable. 

I extend my gratitude to all my colleagues in the Knowledge Media Institute (kmiers). Their professional support, along with their unique positive spirit and attitude, make KMi one of the best and most unique places to work. 

Special recognition goes to my family, which allowed me to follow my dreams and supported me in every possible mean. From them, I inherited two important values that allowed me also to succeed in this mission: patience and persistence. 

I am also grateful to my friends in Sannicandro di Bari for making my homecoming as if I never left, and for tirelessly trying to convince me in moving back home. 

Last but not least, I would like to thank Alessia for standing by me when the going was tough. Thank you all. 

vii 

# **Contents** 

|Abstract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|iii|
|---|---|
|Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|vi|
|List of Figures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xiii|
|List of Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xxi|
|Code Fragments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xxv|
|**I**<br>**Introduction and State of the Art**|**1**|
|**1**<br>**Introduction**|**2**|
|1.1<br>Problem statement . . . . . . . . . . . . . . . . . . . . . . . . . . . .|3|
|1.2<br>Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|5|
|1.3<br>Research questions . . . . . . . . . . . . . . . . . . . . . . . . . . . .|6|
|1.3.1<br>RQ1: Is it possible to precisely define the notion of established||
|topic?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|7|
|1.3.2<br>RQ2: How early in the topic lifecycle is it possible to identify||
|an emerging topic? . . . . . . . . . . . . . . . . . . . . . . . .|8|
|1.3.3<br>RQ3: What are the indicators that can be exploited to predict||
|the emergence of new topics?<br>. . . . . . . . . . . . . . . . . .|9|
|1.3.4<br>RQ4:<br>Is it possible to develop an effective computational||
|method that can support this prediction task? . . . . . . . . .|10|



viii 

||1.3.5|RQ5: Are there commonalities between our approach to pre-||
|---|---|---|---|
|||dicting the emergence of new topics and epistemological theo-||
|||ries of research dynamics? . . . . . . . . . . . . . . . . . . . .|11|
||1.3.6|RQ6: What evaluation mechanisms are appropriate for this||
|||task?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
|1.4|Resea|rch hypotheses<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
|1.5|Resea|rch methodology<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|14|
|1.6|The A|ugur framework<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|16|
|1.7|Contr|ibutions and structure of this dissertation<br>. . . . . . . . . . . .|17|
||1.7.1|Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . .|17|
||1.7.2|Structure of the dissertation . . . . . . . . . . . . . . . . . . .|18|
|1.8|Publi|cations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|
|**2**<br>**Lit**|**erature**|**Review**|**22**|
|2.1|Resea|rch topics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|23|
||2.1.1|The Computer Science Ontology . . . . . . . . . . . . . . . . .|26|
|2.2|Lifecy|cle of research topics . . . . . . . . . . . . . . . . . . . . . . . .|28|
|2.3|Techn|ological background<br>. . . . . . . . . . . . . . . . . . . . . . . .|30|
||2.3.1|Topic detection in the scientific literature . . . . . . . . . . . .|30|
||2.3.2|Topic evolution . . . . . . . . . . . . . . . . . . . . . . . . . .|46|
|2.4|Philos|ophical background<br>. . . . . . . . . . . . . . . . . . . . . . . .|55|
|2.5|Embr|yonic stage<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|58|
|2.6|Netwo|rk-based perspective . . . . . . . . . . . . . . . . . . . . . . . .|59|
||2.6.1|Community detection . . . . . . . . . . . . . . . . . . . . . . .|60|
|2.7|Limit|ations of existing methods . . . . . . . . . . . . . . . . . . . . .|63|



ix 

|**II**<br>**A**|**UGU**|**R**|**64**|
|---|---|---|---|
|**3**<br>**Firs**|**t stud**|**y: analysis of dynamics**|**65**|
|3.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>65|
|3.2|Datas|et<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>67|
||3.2.1|Rexplore . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>68|
||3.2.2|Co-occurrence network . . . . . . . . . . . . . . .|. . . . . . .<br>69|
||3.2.3|Semantic-Enhanced Topic Network . . . . . . . .|. . . . . . .<br>71|
|3.3|Testin|g topics . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>72|
|3.4|Pace|of collaboration and network density<br>. . . . . . . .|. . . . . . .<br>74|
|3.5|Select|ion phase<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>75|
|3.6|Analy|sis phase<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>78|
||3.6.1|Pace of collaboration through cliques . . . . . . .|. . . . . . .<br>79|
||3.6.2|Density of network using triad census . . . . . . .|. . . . . . .<br>82|
|3.7|Evalu|ation . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>84|
||3.7.1|Measuring the pace of collaboration . . . . . . . .|. . . . . . .<br>85|
||3.7.2|Measuring the network density<br>. . . . . . . . . .|. . . . . . .<br>88|
|3.8|Exam|ples<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>92|
||3.8.1|Semantic Web . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>92|
||3.8.2|Deep Learning . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>92|
||3.8.3|Cloud Computing . . . . . . . . . . . . . . . . . .|. . . . . . .<br>95|
|3.9|Discu|ssion and limitations . . . . . . . . . . . . . . . . .|. . . . . . .<br>96|
|3.10|Concl|usions . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>99|
|**4**<br>**Sec**|**ond st**|**udy: early detection of topics**|**101**|
|4.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>101|
|4.2|Evolu|tionary networks . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>104|
|4.3|Clust|er of established topics . . . . . . . . . . . . . . . .|. . . . . . .<br>109|



x 

||4.3.1|Clique percolation method . . . . . . . . . . . . . . . . . . . .<br>110|
|---|---|---|
||4.3.2|Advanced Clique Percolation Method . . . . . . . . . . . . . .<br>114|
|4.4|From|cluster of topics to embryonic topics<br>. . . . . . . . . . . . . . .<br>124|
||4.4.1|Cluster aggregation and main topics<br>. . . . . . . . . . . . . .<br>124|
||4.4.2|Active authors<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>126|
||4.4.3|Relevant papers . . . . . . . . . . . . . . . . . . . . . . . . . .<br>128|
|4.5|Concl|usions: from the approach to the evaluation . . . . . . . . . . .<br>130|
|**III**|**Evalu**|**ation and Conclusion**<br>**132**|
|**5**<br>**Ev**|**aluatio**|**n of Augur**<br>**133**|
|5.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>133|
|5.2|From|the clusters to the evaluation . . . . . . . . . . . . . . . . . . .<br>134|
|5.3|Gold|Standard<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>136|
||5.3.1|Debutant topics . . . . . . . . . . . . . . . . . . . . . . . . . .<br>137|
||5.3.2|Extraction of related topics<br>. . . . . . . . . . . . . . . . . . .<br>139|
|5.4|Label|ling the clusters . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>143|
||5.4.1|Measures of performance . . . . . . . . . . . . . . . . . . . . .<br>146|
||5.4.2|Description of the main community detection algorithms . . .<br>150|
||5.4.3|Results with Fast Greedy Algorithm<br>. . . . . . . . . . . . . .<br>152|
||5.4.4|Results with Leading Eigenvector Algorithm . . . . . . . . . .<br>154|
||5.4.5|Results with Fuzzy C-Means . . . . . . . . . . . . . . . . . . .<br>157|
||5.4.6|Results with Clique Percolation Method<br>. . . . . . . . . . . .<br>162|
||5.4.7|Results with Advanced Clique Percolation Method<br>. . . . . .<br>166|
|5.5|Apply|ing semantic filters . . . . . . . . . . . . . . . . . . . . . . . . .<br>170|
|5.6|Sema|ntic enhancement . . . . . . . . . . . . . . . . . . . . . . . . . .<br>175|
|5.7|Discu|ssion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>187|
||5.7.1|When does a cluster match a debutant topic?<br>. . . . . . . . .<br>187|



xi 

||5.7.2|Why clusters can match more than one debutant topic and vice||
|---|---|---|---|
|||versa? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|192|
||5.7.3|To what extent the number of ancestors can influence the per-||
|||formance of Augur? . . . . . . . . . . . . . . . . . . . . . . . .|197|
||5.7.4|What else can be said regarding the decrease of performance in||
|||the last period of analysis? . . . . . . . . . . . . . . . . . . . .|199|
||5.7.5|Why are there still unmatched debutant topics? . . . . . . . .|204|
||5.7.6|Can authors support the identification of emerging areas? . . .|207|
||5.7.7|How does the final result look like? . . . . . . . . . . . . . . .|210|
|5.8|Final r|emarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|212|
|**6**<br>**Co**|**nclusion**||**214**|
|6.1|Overvi|ew of contributions and major findings<br>. . . . . . . . . . . . .|215|
|6.2|Limita|tions of the study and future directions . . . . . . . . . . . . .|220|
||6.2.1|Gold standard . . . . . . . . . . . . . . . . . . . . . . . . . . .|220|
||6.2.2|Evolutionary network . . . . . . . . . . . . . . . . . . . . . . .|221|
||6.2.3|Clustering Algorithm . . . . . . . . . . . . . . . . . . . . . . .|221|
||6.2.4|Post processing and sense making . . . . . . . . . . . . . . . .|222|
||6.2.5|Trying different windows of years . . . . . . . . . . . . . . . .|222|
||6.2.6|Testing new version of CSO . . . . . . . . . . . . . . . . . . .|223|
||6.2.7|Introducing further dynamics<br>. . . . . . . . . . . . . . . . . .|223|
||6.2.8|Scope<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|224|
||6.2.9|Scalability . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|226|
||6.2.10|Human-based evaluation . . . . . . . . . . . . . . . . . . . . .|227|
|6.3|Conclu|ding remarks . . . . . . . . . . . . . . . . . . . . . . . . . . . .|228|
|**Biblio**|**graphy**||**229**|
|**Index**|||**251**|



xii 

# **List of Figures** 

|1.1|Representation of a topic lifecycle in terms of published research papers.|4|
|---|---|---|
|1.2|Representation of a topic lifecycle, pointing out when it emerges, and||
||it starts to be detected by state-of-the-art approaches. . . . . . . . . .|8|
|1.3|Representation of the different stages of this doctoral work. . . . . . .|11|
|1.4|Simplified model representing the scholarly meta-data and their rela-||
||tionships.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|14|
|1.5|Overview of Augur according to the dissertation narrative. . . . . . .|16|
|2.1|Evolution of the topic_Semantic Web_in terms of number of publications||
||per year. The chart has been produced using the Rexplore system. . .|29|
|3.1|Screen capture of Rexplore while looking at the research trajectory of||
||the renowned _Artificial Intelligence_ researcher James A. Hendler.<br>. .|68|
|3.2|Size of 16 co-occurrence networks from 1995 to 2010. The number of||
||keywords correspond to the number of nodes in _V_ and the number of||
||co-occurrences correspond to the number of links in _E_. . . . . . . . .|70|
|3.3|Size of 16 topic networks from 1995 to 2010. The number of topics cor-||
||respond to the number of nodes in_V_ and the number of co-occurrences||
||correspond to the number of links in _E_. . . . . . . . . . . . . . . . . .|72|



xiii 

|3.4|Evolution of the topic _Software Agents_ in terms of number of authors<br>and number of publications per year. The chart has been produced||
|---|---|---|
||using the Rexplore system. . . . . . . . . . . . . . . . . . . . . . . . .|73|
|3.5|Workflow representing all the steps for the selection phase. . . . . . .|77|
|3.6|An instance of a 3-clique containing node_{A, B, C}_with node weights||
||_{pa, pb, pc}_ and link weights _{wab, wbc, wca}_. . . . . . . . . . . . . . . .|79|
|3.7|Main steps of the analysis phase.<br>. . . . . . . . . . . . . . . . . . . .|79|
|3.8|The four isomorphism classes of triad. The triad census consists in||
||counting the frequencies of _Hi_ of the input graph. . . . . . . . . . . .|82|
|3.9|Development in time of the frequencies of_Hi_ in the network related to||
||the emergence of _Artificial Bee Colonies_. . . . . . . . . . . . . . . . .|84|
|3.10|Average collaboration pace of the sub-graphs associated to the treat-||
||ment (DB) and control set (NDB), when selecting the 20, 40 and 60||
||most co-occurring topics. The thin vertical lines represent the ranges||
||of values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|86|
|3.11|Average collaboration pace per year of the sub-graphs related to input||
||topics in both debutant and control sets considering their 20 (a), 40||
||(b) and 60 (c) most co-occurring topics. The year refers to the year of||
||analysis of each topic. . . . . . . . . . . . . . . . . . . . . . . . . . . .|87|
|3.12|Average growth index per year of the sub-graphs related to the topics<br>in both debutant and non-debutant groups considering their 60 most<br>co-occurring topics and filtering links having with less than 3 (a), 10||
||(b) and 20 (c) publications.<br>. . . . . . . . . . . . . . . . . . . . . . .|90|
|3.13|Network suggesting the emergence of the _Semantic Web_ in the years||
||prior its emerging. The thickness of an edge reflects the pace of col-||
||laboration between the nodes it connects. The size of a node reflects<br>the centrality of the node in this small-world network. . . . . . . . . .|93|



xiv 

|3.14|Network envisioning the emergence of the _Deep Learning_. The thick-||
|---|---|---|
||ness of an edge reflects the pace of collaboration between the nodes it||
||connects. The size of a node reflects the centrality of the node in this||
||small-world network. . . . . . . . . . . . . . . . . . . . . . . . . . . .|94|
|3.15|Network envisioning the emergence of the _Cloud Computing_.<br>The||
||thickness of an edge reflects the pace of collaboration between the||
||nodes it connects. The size of a node reflects the centrality of the node||
||in this small-world network. . . . . . . . . . . . . . . . . . . . . . . .|95|
|4.1|Workflow for the first study in Chapter 3 (forward) and for this study||
||(backward). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|102|
|4.2|Representation of both input and output of the second study.<br>On||
||the left there are the topic networks that will be processed in search||
||of interesting sub-networks, while on the right there are the matched||
||debutant topics. The dashed circles within the topic networks represent||
||clusters of interest that are analysed over time and can potentially lead||
||to the emergence of new research topics.<br>. . . . . . . . . . . . . . . .|103|
|4.3|Workflow of Augur. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|104|
|4.4|Representation of the evolutionary network.<br>. . . . . . . . . . . . . .|107|
|4.5|Example of network. Our goal is to identify all cliques and create the||
||clique graph. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|111|
|4.6|Clique graph or _k-clique adjacency graph_. The two connected compo-<br>nents of this network map into the communities of the original network.|112|
|4.7|The two communities shown in Fig. 4.6 are now mapped on the original||
||network inFig. 4.5. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|112|



xv 

|4.8|Approximative representation of the k-clique adjacency graph as island||
|---|---|---|
||with complex terrain. The sea level represents the filter. With low||
||tide, in (a) the returned network is almost similar to the original one.||
||Increasing the level of the water, as in (b) the network splits in two||
||components. With high tide, as in (c), the network further splits in||
||more components but some of them might be covered. . . . . . . . . .|119|
|4.9|Graphical representation of the k-clique adjacency graph. Rather than<br>filtering with the sea level, we locate local maxima (peaks). . . . . . .|119|
|5.1|Histogram reporting the number of keywords that had their first ap-<br>pearance (hard debut) in the years between 1990 and 2012. . . . . . .|138|
|5.2|Histogram reporting the number of topics that had their soft debut in<br>the years between 2000 and 2011. . . . . . . . . . . . . . . . . . . . .|139|
|5.3|Graphical explanation of the_many-to-many_ relationship between clus-<br>ters and debutant topics. Since the number of matched cluster can be||
||different from the matched debutant topics, the value of precision and||
||recall need to take into account this difference. . . . . . . . . . . . . .|149|
|5.4|Distribution of the community sizes obtained from the Fast Greedy<br>algorithm in the different years. . . . . . . . . . . . . . . . . . . . . .|153|
|5.5|Results in terms of precision and recall obtained from evaluating the||
||Fast Greedy algorithm against the gold standard. . . . . . . . . . . .|155|
|5.6|Results in terms of precision and recall obtained from evaluating the||
||Leading Eigenvector algorithm against the gold standard. . . . . . . .|157|
|5.7|Sum of squared error in prediction (SSE) obtained from evaluating||
||the Fuzzy C-Means with different number clusters (from 5 to 200)||
||over the different evolutionary networks. We can see that for all the||
||evolutionary networks the elbow is located at 25.<br>. . . . . . . . . . .|159|



xvi 

|5.8|Results in terms of precision and recall obtained from evaluating the||
|---|---|---|
||Fuzzy C-Means against the gold standard. . . . . . . . . . . . . . . .|161|
|5.9|Evolutionary graph of the year 2000 split into communities using the||
||Clique Percolation Method. The largest community counts 1124 topics||
||and 10393 edges.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|164|
|5.10|Results in terms of precision and recall obtained from evaluating the||
||Clique Percolation Method against the gold standard. . . . . . . . . .|165|
|5.11|Distribution of the community sizes obtained from the Advanced||
||Clique Percolation Method in the different years.<br>. . . . . . . . . . .|167|
|5.12|Evolutionary graph of the year 2000 split into communities using the||
||Advanced Clique Percolation Method. . . . . . . . . . . . . . . . . . .|168|
|5.13|Results in terms of precision and recall obtained from evaluating the||
||Advanced Clique Percolation Method against the gold standard. . . .|169|
|5.14|Results in terms of precision and recall obtained from evaluating the<br>Fast Greedy against the gold standard after filtering the communities||
||semantically. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|170|
|5.15|Results in terms of precision and recall obtained from evaluating the<br>Leading Eigenvector against the gold standard after filtering the com-<br>munities semantically.<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|172|
|5.16|Results in terms of precision and recall obtained from evaluating the<br>Fuzzy C-Means against the gold standard after filtering the communi-||
||ties semantically.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|173|
|5.17|Results in terms of precision and recall obtained from evaluating the||
||Clique Percolation Method against the gold standard after filtering the<br>communities semantically.<br>. . . . . . . . . . . . . . . . . . . . . . . .|173|



xvii 

|5.18 Results in terms of precision and recall obtained from evaluating the||
|---|---|
|Advanced Clique Percolation Method against the gold standard after||
|filtering the communities semantically.<br>. . . . . . . . . . . . . . . . .|174|
|5.19 Results in terms of precision and recall obtained from evaluating the||
|Fast Greedy in year 1999 with different solution of semantic enhancement|f    .177|
|5.20 Results in terms of precision and recall obtained from evaluating the||
|Leading Eigenvector in year 1999 with different solution of semantic||
|enhancement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|177|
|5.21 Results in terms of precision and recall obtained from evaluating the||
|Fuzzy C-Means in year 1999 with different solution of semantic en-||
|hancement.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|178|
|5.22 Results in terms of precision and recall obtained from evaluating the||
|Clique Percolation Method in year 1999 with different solution of se-||
|mantic enhancement. . . . . . . . . . . . . . . . . . . . . . . . . . . .|178|
|5.23 Results in terms of precision and recall obtained from evaluating the||
|Advanced Clique Percolation Method in year 1999 with different solu-||
|tion of semantic enhancement. . . . . . . . . . . . . . . . . . . . . . .|179|
|5.24 Results in terms of precision and recall obtained from evaluating the||
|Advanced Clique Percolation Method in year 2000 with different solu-||
|tion of semantic enhancement. . . . . . . . . . . . . . . . . . . . . . .|180|
|5.25 Results in terms of precision and recall obtained from evaluating the||
|Advanced Clique Percolation Method after enhancing both clusters||
|and debutant topics with their super-areas. . . . . . . . . . . . . . . .|181|
|5.26 Comparison between the amount of debutant topics and cluster, re-||
|trieved each year. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|181|



xviii 

- 5.27 Results in terms of precision and recall obtained from evaluating the Fast Greedy after enhancing both clusters and debutant topics with their super-areas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182 

- 5.28 Results in terms of precision and recall obtained from evaluating the Leading Eigenvector after enhancing both clusters and debutant topics with their super-areas. . . . . . . . . . . . . . . . . . . . . . . . . . . 183 

- 5.29 Results in terms of precision and recall obtained from evaluating the Fuzzy C-Means after enhancing both clusters and debutant topics with their super-areas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184 

- 5.30 Results in terms of precision and recall obtained from evaluating the Clique Percolation Method after enhancing both clusters and debutant topics with their super-areas. . . . . . . . . . . . . . . . . . . . . . . 184 

- 5.31 Community extracted from the evolutionary network of year 1999 that matches with _Resource Description Framework_ debuting in 2000. Red nodes are the matched topics, blue nodes are the unmatched topics. . 192 

- 5.32 Community extracted from the evolutionary network of year 2003 that matches with _Lexical Resources_ and _Ontology Learning_ , respectively debuting in 2005 and 2004. Red nodes are the matched topics, while blue and green nodes are the topics that did not match with the ancestors of the two debutant topics. . . . . . . . . . . . . . . . . . . . 194 

- 5.33 Community of topics extracted in the evolutionary network of year 2004 that matched with more 40 debutant topics in the following two years. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197 

- 5.34 Results in terms of precision and recall obtained from evaluating the Advanced Clique Percolation Method against the gold standard with 15 ancestors. Both clusters and debutant topics have been enhanced with their super-areas. . . . . . . . . . . . . . . . . . . . . . . . . . . 198 

xix 

|5.35 Results in terms of precision and recall obtained from evaluating the||
|---|---|
|Advanced Clique Percolation Method against the gold standard with||
|20 ancestors. Both clusters and debutant topics have been enhanced||
|with their super-areas. . . . . . . . . . . . . . . . . . . . . . . . . . .|199|
|5.36 Comparison between the constant increase of published papers and the||
|decrease of emerging topics each year. . . . . . . . . . . . . . . . . . .|200|
|5.37 Differences in how the unmatched clusters, obtained in a certain year,||
|develop in the following year. A cluster can strengthen its ties, expand||
|its network, both expand its network and strengthen its ties, or not||
|developing.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|203|
|5.38 Differences in how the matched clusters, obtained in a certain year,||
|develop in the following year. A cluster can strengthen its ties, expand||
|its network, both expand its network and strengthen its ties, or not||
|developing.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|204|
|5.39 Distributions of pace of collaboration valued from the networks of an-||
|cestors of both matched and unmatched debutant topics. . . . . . . .|207|
|5.40 Network representation of the same cluster in Table 5.23 extracted||
|from the evolutionary network of year 2002.<br>. . . . . . . . . . . . . .|211|



xx 

# **List of Tables** 

|2.1|Characteristics and limitations of the four methods for topic modelling.||
|---|---|---|
||This table is an extract of Lee et al. (2010).<br>. . . . . . . . . . . . . .|36|
|2.2|Bag of words associated with the concept of Video Streaming, extracted||
||using LDA. This example is extracted from Cano-Basave et al. (2016).|37|
|3.1|Comparing year of debut and year of analysis for both treatment and||
||control sets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|73|
|3.2|Frequencies of _Hi_ obtained performing triad census on the debutant||
||topic _Artificial Bee Colonies_ . . . . . . . . . . . . . . . . . . . . . . .|83|
|3.3|P-values obtained performing the Student's t-test over the distributions||
||of both debutant and control sets considering their 20, 40 and 60 most||
||co-occurring topics. The best result is in bold. . . . . . . . . . . . . .|88|
|3.4|Collaboration pace of the sub-graphs associated to selected debutant||
||topics versus the average collaboration pace of the control set in the||
||same year of debut. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|89|
|3.5|P-values obtained performing the Student’s t-test over the distribu-||
||tions of both debutant and control sets considering their 60 most co-||
||occurring topics filtering links having with less than 3, 10 and 20 pub-||
||lications. The best result is bolded. . . . . . . . . . . . . . . . . . . .|90|



xxi 

|3.6|Growth indexes of sub-graphs associated to selected debutant topics<br>versus the average growth index of the control set in the same year of||
|---|---|---|
||debut (Standard Growth Index). . . . . . . . . . . . . . . . . . . . . .|91|
|3.7|Ranking of the cliques with highest slope value for the _Semantic Web_.|93|
|3.8|Ranking of the cliques with highest slope value for the _Deep Learning_.|94|
|3.9|Ranking of the cliques with highest slope value for the_Cloud Computing_.|96|
|4.1|The overlap matrix. This matrix is viewed as an adjacency matrix||
||whose nodes are cliques of the original network. The elements of the||
||matrix indicate whether pairs of cliques are adjacent (share 2 nodes)<br>or not in the graph. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|112|
|5.1|Mapping between _topics networks_ and _evolutionary graphs_. . . . . . .|134|
|5.2|Mapping the _evolutionary graphs_ and their clusters with the debutant<br>topics in the subsequent years. For instance, the clusters obtained from<br>the evolutionary network of the 2005 will be compared with the topics||
||emerged in the years 2006 and 2007.<br>. . . . . . . . . . . . . . . . . .|135|
|5.3|Example of ancestors extracted form the_Semantic Search_ topic debut-<br>ing in 2003. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|142|
|5.4|Example of cluster_Ci_ returned by Augur and ancestors_Dk_ of the topic||
||_Resource Description Framework_ available in the gold standard. . . .|144|
|5.5|Confusion matrix for a binary classifier. . . . . . . . . . . . . . . . . .|147|
|5.6|List of the community detection algorithms used for the evaluation. .|151|
|5.7|Number of communities and the size of the first ten communities using||
||the Fast Greedy algorithm over the different evolutionary networks<br>.|152|
|5.8|Number of communities and the size of the first ten communities us-||
||ing the Leading Eigenvector algorithm over the different evolutionary<br>networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|156|



xxii 

|5.9|Number of communities and the size of the first ten communities using||
|---|---|---|
||the Fuzzy C-Means algorithm over the different evolutionary networks.|161|
|5.10|Number of communities and the size of the first ten communities using||
||the Clique Percolation Method algorithm over the different evolution-<br>ary networks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|162|
|5.11|Some statistics for the evolutionary network of year 2000 and its largest<br>community of _Computer Science_.<br>. . . . . . . . . . . . . . . . . . . .|163|
|5.12|Number of communities and the size of the first ten communities using||
||the Advanced Clique Percolation Method algorithm over the different||
||evolutionary networks. . . . . . . . . . . . . . . . . . . . . . . . . . .|166|
|5.13|Listing the number of communities obtained using the Fast Greedy<br>(FG), Leading Eigenvector (LE), Fuzzy C-Means (FCM), Clique Per-<br>colation Method (CPM) and Advanced Clique Percolation Method||
||(ACPM), before (# comm.) and after filtering (# comm. filt.). Be-<br>low the table is reported the average percentage difference between the<br>initial value of community and the final number of communities after||
||filtering. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|171|
|5.14|Figures comparison for each approach before and after applying the||
||filter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|172|
|5.15|Figures comparison for each approach, when using only the cluster-||
||ing techniques, when applying semantic filtering and when enhancing<br>semantically the set of clusters and debutants. . . . . . . . . . . . . .|182|
|5.16|Values of Precision and Recall for the five approaches along time, at||
||similarity value of 0.1. In bold the best results.<br>. . . . . . . . . . . .|185|
|5.17|Values of Precision and Recall for the five approaches along time, at<br>similarity value of 0.15. In bold the best results. . . . . . . . . . . . .|185|



xxiii 

|5.18 Values of Precision and Recall for the five approaches along time, at||
|---|---|
|similarity value of 0.2. In bold the best results.<br>. . . . . . . . . . . .|186|
|5.19 Matchings between cluster and debutant topics with similarity measure||
|over 0.2. In this case the two clusters match the same debutant topic:||
|_Semantic Search_<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|189|
|5.20 Matchings between cluster and debutant topics with similarity measure||
|just above 0.2. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|191|
|5.21 Example of matching between one clusters and multiple debutant topics.|195|
|5.22 Number of matched and unmatched debutant topics in the years from||
|2000 to 2011 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|205|
|5.23 Example of output produced by Augur. The cluster associated with||
|the emergence of the _Semantic Search_ topic (in bold the topics that||
|match its ancestors). . . . . . . . . . . . . . . . . . . . . . . . . . . .|211|
|5.24 Example of output produced by Augur. On top, there are the top 10||
|active authors. At the bottom, the top 5 papers. . . . . . . . . . . . .|212|



xxiv 

# **Code Fragments** 

|1|Extracting the portion of topic networks associated to topics in both||
|---|---|---|
||treatment and control set. . . . . . . . . . . . . . . . . . . . . . . . . .|78|
|2|Clique Percolation Method. . . . . . . . . . . . . . . . . . . . . . . . .|113|
|3|Advanced Clique Percolation Method. . . . . . . . . . . . . . . . . . .|123|
|4|Algorithm for post-processing the clusters of topics. . . . . . . . . . . .|125|
|5|Algorithm for selecting the most active authors. . . . . . . . . . . . . .|128|
|6|Algorithm for selecting the most relevant papers. . . . . . . . . . . . .|130|
|7|Extracting the ancestors of debutant topics. . . . . . . . . . . . . . . .|142|
|8|Process of evaluation.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|146|
|9|Counting the number of clusters within the evolutionary networks using||
||the Elbow Method with Fuzzy C-Means. . . . . . . . . . . . . . . . . .|159|
|10|Extracting main authors of debutant topic.<br>. . . . . . . . . . . . . . .|209|



xxv 

# **Part I** 

# **Introduction and State of the Art** 

1 

# **Chapter 1** 

# **Introduction** 

The research environment changes and evolves rapidly: new research areas constantly emerge, whereas some others fade out. The ability to promptly recognise the emergence of new research topics is an important asset for anybody involved in the research environment, including journal editors, academic publishers, researchers, institutional funding bodies and other relevant stakeholders. Nowadays, as we are experiencing an exponential growth of research publications (Larsen and Von Ins, 2010), keeping up with new trends is becoming progressively more challenging. 

In the last two decades, very large repositories of scholarly data and other relevant sources have become available, opening the way to novel data-intensive approaches capable of detecting novel topics and their trends (Wu et al., 2016; He et al., 2009; Duvvuru et al., 2012; Bolelli et al., 2009). However, a timely detection of research topics is still an open challenge. 

In this work, we are going to face this challenge by creating a system able to anticipate the emergence of new research topics. Specifically, we define a research topic as a subject of study or issue that is of interest to the research community, and it is addressed in at least few research papers. Subjects of study can encompass different research areas and application-dependent concepts. For instance, a paper introducing 

2 

a new technology to classify data, is the event that triggers the emergence of new topic. Any paper discussing the implementation of such technology, its application, the release of a new efficient implementation, its evaluation and so on, are all part of the same research topic. We will provide further details about this definition in Section 2.1. 

## **1.1 Problem statement** 

Looking deeply into the evolution of research topics we can observe that they go through a sequence of life stages. Specifically, we can distinguish three main stages: (i) embryonic stage, (ii) early stage and (iii) recognised, as showed in Fig. 1.1. A research topic, in its _embryonic stage_ , is still an idea or concept and it did not emerge, yet. Specifically, in this stage, a topic has not yet been explicitly labelled and recognised by a research community, but it is already taking shape, as evidenced by the fact that researchers from a variety of fields are forming new collaborations and producing new work, starting to define the challenges and the paradigms associated with the emerging new area. A research topic in its _early stage_ , instead, has recently emerged and a relatively small group of researchers agree on certain theories which will allow the topic to thrive. As a result, there is a new label for it, and it is associated to a limited number of papers. Afterwards, when a research topic enters in its _recognised stage_ , it becomes mature and many researchers are actively producing and disseminating their results. The topic is then associated with a substantial number of papers. 

As an example, for the _Semantic Web_ , we can observe that before its emergence in 2001, in its embryonic stage, it still was a concept in which communities of researchers from _Artificial Intelligence_ , _World Wide Web_ , _Knowledge Representation_ , and _Knowledge-Based Systems_ were joining their forces. After the 2001, the topic 

3 



**Figure 1.1:** Representation of a topic lifecycle in terms of published research papers. 

emerges and enters in its early stage, earning its own identity, in which an increasing number of practitioners started to work in it. Around the 2005, the _Semantic Web_ reaches its own maturity (recognised phase) with over 1500 papers published each year. 

Current approaches for detecting research topics (Wu et al., 2016; He et al., 2009; Duvvuru et al., 2012; Bolelli et al., 2009), focus on highlighting topics that are already associated with a number of publications and consistently referred to by a community of researchers. This limitation means that these solutions can only identify topics that already have an initial degree of consolidation, i.e., after a certain latency from their emergence. As a result, they can only provide limited value to stakeholders who wish to anticipate and promptly react to new developments in the research landscape. 

A strategy to address this problem would be to anticipate the emergence of new research topics by detecting them at their embryonic stage. This stage was initially observed by Thomas Kuhn, who argued in his book (Kuhn, 1970, page 86) that, topics might exist in the form of embryo. However, it has never been studied quantitatively, probably due to the complexity of the issue and the difficulty of formally defining the notion of research topic. 

4 

Nevertheless, in this dissertation we address this problem by introducing a novel framework, Augur, for identifying the appearance of new topics at an embryonic stage. Augur analyses networks of research topics, detects areas exhibiting a significant increase in the pace of collaboration, and produces clusters of topics correlated with the future emergence of new research areas. For instance, if available, before 2001, Augur would have allowed us to observe that previously less connected topics (e.g., _Artificial Intelligence_ , _World Wide Web_ and _Knowledge-Based Systems_ ) were increasingly collaborating with each other<sup>1</sup> . These dynamics indeed led to the emergence of a new research area, later labelled as _Semantic Web_ by Berners-Lee Berners-Lee et al. (2001)<sup>2</sup> . 

In the following sections, we discuss the motivation behind this dissertation, and detail our research questions, hypotheses, methodology and approach, and contributions. 

## **1.2 Motivation** 

As already mentioned, understanding and reacting timely to new developments in the research landscape is critical for a variety of stakeholders. For instance, researchers need to stay up-to-date with new trends related to their topics and potentially interesting new research areas. Thanks to these insights, they can evolve their research agenda, ensuring they focus on ideas and concepts at the leading edge of the current landscape. 

> 1In this dissertation, we will use the expression “collaboration between research area” as a shortcut for “collaboration between research communities associated with specific research areas”. The community of a research area is given by the authors who publish in the area in question. 

> 2It should be noted that this term was first introduced in the book Weaving the web (Berners-Lee and Fischetti, 1999), but it was not really recognised by the scientific community until the Scientific American paper of 2001. 

5 

Institutional funding bodies and companies also need to be aware of the latest research developments and promising trends. For instance, this knowledge can inform business decisions and suggest the selection of technologies on which to invest. 

Similarly, it is crucial for academic publishers and editors to know in advance new emerging topics with the aim of offering the most up to date and interesting content. For instance, a publisher can gain a competitive advantage by being the first to recognise the importance of a new trend, and thus publish a special issue or a journal about it. Indeed, financial support for this doctoral project comes from _Springer Nature_ , which is a global publishing company. 

The undeniable potential of an approach for detecting novel research trends has recently attracted an increasing research interest to this area. However, as we will discuss in Chapter 2, current state-of-the-art solutions suffer from significant limitations when applied to the detection of trends at their early stage. 

## **1.3 Research questions** 

The main research question investigated in this dissertation is: 

**Is it possible to detect a new research topic at the embryonic stage before it is consistently recognised by a research community (e.g., there** 

#### **is an established label for it)?** 

We focused specifically on the creation of a novel approach that is able to detect the emergence of new research topics at their embryonic stage. Given the dimension of such problem, we articulated this main question in a set of related questions: 

RQ1: Is it possible to precisely define the notion of established topic? 

- RQ2: How early in the topic lifecycle is it possible to identify an emerging topic? 

6 

- RQ3: What are the indicators that can be exploited to predict the emergence of new topics? 

- RQ4: Is it possible to develop an effective computational method that can support this prediction task? 

- RQ5: Are there commonalities between our approach to predicting the emergence of new topics and epistemological theories of research dynamics? 

- RQ6: What evaluation mechanisms are appropriate for this task? 

In what follows, we will introduce and discuss these research questions. In the Conclusion (see Chapter 6), we will reprise each of them and summarise the answers according to the results showed in this dissertation. 

### **1.3.1 RQ1: Is it possible to precisely define the notion of established topic?** 

One of the recurring problems while reading the literature is the lack of widelyaccepted definition for research topic. This issue is present also in _Philosophy of Science_ , as philosophers do not agree about a shared definition. This is mainly because research topics come in all shapes and sizes and therefore it is very hard to create a formal definition that would fit them all. 

This limitation has led many approaches that extract topics from collections of documents to propose their own definition, often tightly-coupled with the algorithmic method they employ. Indeed, some approaches use keywords as proxies for topics, others match terms to manually-curated taxonomies, and some others apply statistical techniques to associate topics to bags of words. 

7 

It is not clear when a topic can be considered established, but intuitively this assessment could derive from a number of indicators such as the number of papers addressing it, the number of researchers working on it, and the time elapsed since its debut. Acknowledging when and which topics can be considered established allows us to define a category of topics against which we can compare the emerging ones. Indeed, in Chapter 3, we compare emerging topics with established topics, and we suggest some indicators to determine when a research topic is definitely established. 

### **1.3.2 RQ2: How early in the topic lifecycle is it possible to identify an emerging topic?** 

As already mentioned in Section 1.1, research topics go through different stages within their lifecycle. The literature presents several approaches that are able to detect research topics, and as we will discuss in Chapter 2, they are able to perform their detection only later in their lifecycle (see Fig. 1.2). This is mainly because most of them perform a statistical analysis of the popularity of the labels associated with a topic across a certain time period (typically 2-4 years). 



**Figure 1.2:** Representation of a topic lifecycle, pointing out when it emerges, and it starts to be detected by state-of-the-art approaches. 

8 

It would be much more useful to detect topics in their very early stage and thus react before the currently available approaches, i.e., within the blind spot showed in Fig. 1.2. Therefore, how early can we actually detect a new topic? 

Our hypothesis is that it is possible to detect a topic at the embryonic stage. This endeavour will then seek to forecast new topics that are about to emerge rather than simply acknowledging that they emerged. 

Therefore, the next question to answer is: how can we forecast the emergence of a new topic before it actually emerges? 

In Section 2.1, we will analyse in more detail the different stages that a research topic goes through, while in Chapter 3 and 4, we will discuss how soon it is possible to forecast the emergence of a new topic. 

### **1.3.3 RQ3: What are the indicators that can be exploited to predict the emergence of new topics?** 

A prediction system is a tool capable to make automatic and objective predictions about future or unknown events. These systems are usually built using statistical techniques such as predictive modelling, machine learning, and data mining to analyse historical data. This analysis consists of identifying patterns and latent relationships, given some indicators, that have predictive power. 

In this doctoral work, this analysis is crucial to determine the main indicators that drive the emergence of a new research topic. We will then develop a prediction system with the ability to sense such patterns, with the aim of forecasting the emergence of new topics. 

Therefore, what kind of indicators can be used to predict the emergence of new research topics? How can we analyse them? How we can be certain of their effectiveness? Will these indicators be general enough to consider the peculiarities of different fields (e.g., _Computer Science_ , _Business_ , _Medicine_ and so on)? Intuitively, 

9 

there could be a wide array of relevant indicators that could anticipate the creation of a new research area. These may include a new collaboration between two or more research communities, the creation of interdisciplinary workshops, a rise in the number of experts working on a certain combination of topics, a significant change in the vocabulary associated with relevant topics, and so on. 

In Chapter 3, we address this question by analysing some indicators associated with the emergence of novel research topics. In particular, we analyse whether the emergence of a novel research topic can be anticipated by a significant increase in the pace of collaboration and a change in the network density between its related research areas. 

### **1.3.4 RQ4: Is it possible to develop an effective computational method that can support this prediction task?** 

We believe that it is possible to use the indicators discussed in the previous section for devising new methods to forecast research topics. For instance, knowing that the pace of collaboration between existent research areas is associated with the emergence of a new topic suggests that we can analyse these dynamics and predict the characteristic of the topics that may emerge in the following years. This hypothesis opens up several other research questions. What kind of technologies can be adopted for mining large datasets with this purpose? How can we represent yet unlabelled research topics? How can we produce a scalable method for detecting the relevant dynamics? 

To address these questions, we organised this doctoral work in two parts, as depicted by Fig. 1.3. In the first part (Chapter 3), we perform a retrospective study for identifying indicators associated with the future emergence of research topics. In the second part (Chapter 4), we exploit these indicators to produce a number of approaches for predicting the emergence of research topics and we evaluate them against a gold standard. 

10 

We will address these questions in Chapter 3 and 4. 



**Figure 1.3:** Representation of the different stages of this doctoral work. 

### **1.3.5 RQ5: Are there commonalities between our approach to predicting the emergence of new topics and epistemological theories of research dynamics?** 

In the literature, we can find several epistemological theories regarding the emergence of a new research area. One of the main contributions comes from Kuhn (1970), who theorised that science evolves through paradigm shifts. Research is pursued using a set of paradigms and, when these paradigms cannot cope with certain problems anymore, there is a paradigm shift that can lead to the emergence of a new scientific discipline. This shift is usually characterised by a number of activities, such as the exchange of theories and methods between scientific fields, the definition of new challenges and paradigms, the formation of new collaborations and so on. 

There are also other theories, which mention that different communities of researchers can be engaged in an exchange of tools, methodologies, and theories, leading then to the emergence of a new research area (Becher and Trowler, 2001). 

In the following chapters, we will refer to some of these epistemological theories and we will highlight the similarities with our work. 

11 

### **1.3.6 RQ6: What evaluation mechanisms are appropriate for this task?** 

Evaluating our approach requires a formal framework for assessing the performance of a system predicting new research topics. Typically, a forecasting task is evaluated using historical data. In our case however, the research topics that we are trying to predict are not yet associated with a label. This makes the process more complex. What kind of information should be included in the gold standard? How can we compare the prediction of an emerging topic with the concrete dynamics of the research landscape? What are the metrics that we could use? 

In Chapter 5, we will address these questions and discuss the evaluation of our approach. 

## **1.4 Research hypotheses** 

In this section, we present three main hypotheses that are at the basis of this doctoral work. 

**Hypothesis 1:** _Before being labelled and recognised by research communities, new topics go through an embryonic stage, in which researchers from different topics start to work on it._ 

As we will see in Section 2.2, a research topic goes through different stages during its lifecycle, such as the _early stage_ and the _recognised phase_ . Existing approaches are able to work in the last two stages, as they focus on topics that are already associated with a number of publications and for which the communities of researchers have already reached a consensus for a label. 

12 

However, within the _Philosophy of Science_ there are some interesting theories about the emergence of new research topics, including the existence of an _embryonic stage_ . 

As already mentioned, at the embryonic stage a topic has not yet been explicitly labelled and recognised by a research community. However, the topic is already taking shape, as evidenced by the fact that researchers from a variety of fields are already working on it. 

Inspired by these theories, we hypothesise that such activity among researchers can be numerically measured and therefore it is possible to provide further evidence about its existence. 

**Hypothesis 2:** _The emergence of a new research topic is anticipated by an increased rate of interaction of pre-existing topics, involved in developing this new area which is still in its embryonic stage._ 

From a philosophical point of view, academic disciplines are specific branches of knowledge which together form the unity of knowledge that has been produced by the scientific endeavour. When two or more disciplines start to cooperate, they share their theories, concepts, methods and tools. The results of this cooperation may lead either to the creation of a new interdisciplinary research area or simply to a contribution in knowledge from one area to another. The basic hypothesis is that the creation of a topic is anticipated by a number of dynamics involving a variety of research entities, such as other topics, research communities, authors, venues and so on. Therefore, recognising these dynamics might enable a very early detection of emerging topics. 

**Hypothesis 3:** _It is possible to create an automatic approach for detecting new emerging topics in their embryonic stage by analysing the dynamics of existing topics (i.e., observing their patterns of collaboration)._ 

13 

Scholarly data can be used to analyse a large amount of research elements such as papers, authors, affiliations, venues, topics and communities (Osborne et al., 2014). All these research elements are inherently interconnected by semantic relationships. For instance, Fig. 1.4 shows some basic connections between the research elements according to our model. 



**Figure 1.4:** Simplified model representing the scholarly meta-data and their relationships. 

These connections can be used to derive a number of second order connections, e.g., authors are associated with a particular set of topics according to the papers they published. They also can be analysed in time to derive the dynamics that led to the emergence of a topic. 

Therefore, by exploiting the large variety of scholarly data, it should be possible to perform detection of topics at their embryonic stage. 

## **1.5 Research methodology** 

For answering the research questions presented above, we use the _experimental methodology_ , which is widely adopted within _Computer Science_ for evaluating new solutions for given problems (Elio et al., 2011). This experimental methodology consists of two different phases. Firstly, there is an exploratory phase in which the 

14 

researchers investigate the different variables affecting the experimental group and measuring their effect. Then, researchers report the results of their evaluation with an analytical discussion stating what they had learned. 

This research effort started with an extensive analysis of the body of literature, which is reported in Chapter 2. We then formulated the research questions discussed in Section 1.3 and explored a number of ideas for addressing them. As a next step, we formulated our hypotheses regarding the existence of an embryonic stage for emerging topics. 

Figure 1.5 summarises the process that we applied for going from these initial hypotheses to the creation and evaluation of Augur. We first conducted a preliminary study (described in Chapter 3) to investigate the hypothesis that the emergence of new topics can be anticipated by some indicators, such as an intensive collaboration among previously distant research communities. In this study, we generated a network of co-occurring topics from a sample of 3 million papers. We then compared the sections of the co-occurrence graphs where new topics are about to emerge with a control group of subgraphs associated with established topics. These graphs were analysed by using two novel approaches that integrate both statistics and semantics. The results provided evidence that the emergence of a novel research topic can be anticipated by a significant increase in the pace of collaboration between relevant research areas, which can be seen as the “ancestors” of the new topics. 

These dynamics and other insight yielded by the study were used to create Augur, a novel approach for predicting the emergence of research topics described in Chapter 4. Finally, we evaluated Augur versus four alternative approaches on a dataset of 3 million papers (Chapter 5). 

15 



**Figure 1.5:** Overview of Augur according to the dissertation narrative. 

## **1.6 The Augur framework** 

Augur is a novel framework that detects the emergence of new research areas by analysing topic networks and identifying clusters associated with an overall increase of the pace of collaboration. 

Augur operates in three steps. Firstly, it creates an evolutionary network describing the collaboration of research topics in time. The evolutionary graph is a fully weighted graph in which nodes represent the topics, and arcs represent the collaboration between those two topics. Then node and arc weights represent how much topics and their inner collaboration are growing in time. 

As a second step, Augur uses a novel clustering algorithm, the Advanced Clique Percolation Method (ACPM), for locating areas of the network that exhibit a significant increase in the pace of collaboration. ACPM crawls the evolutionary network and groups together nodes (i.e., topics) into sets of nodes (i.e., clusters), such that each cluster is densely connected internally (i.e., high pace of collaboration). 

16 

In the third and final step, Augur post-processes the results, by merging and filtering the resulting clusters. As some communities can overlap, Augur aggregates the most similar ones and for each cluster it returns the topics that have the most intense collaboration. 

The output of the process is sets of already existent topics that are nurturing a new research area that should shortly emerge, associated with relevant authors and publications. 

Augur was evaluated on the task of forecasting the emergence of 1,408 research topics in the 2000-2011 period and it outperformed four alternative approaches, successfully predicting many new research topics as soon as two years before they became explicitly recognised in the research community. 

## **1.7 Contributions and structure of this dissertation** 

### **1.7.1 Contributions** 

The main contribution of this work concerns a new approach to the early detection of research topics. In particular, it presents the first approach able to detect research topics in the embryonic stage, that is, before they are labelled and recognised by the relevant research communities. This allows stakeholders such as academic editors, researchers, and institutional funding bodies, to react timely to changes in the research environment. 

The contributions of the present dissertation can be summarised as follows: 

1. A comprehensive literature review that covers several aspects regarding the emergence of new research topics (Chapter 2). 

17 

2. New empirical evidence to fundamental theories in _Philosophy of Science_ , which are concerned with the evolution of scientific disciplines, supporting the existence of an embryonic stage for research topics (Chapter 3). 

3. A new framework for the detection of new research topics at their embryonic stage (Chapter 4). 

4. Advanced Clique Percolation Method, a community detection algorithm developed for supporting this task (Chapter 4). 

5. A gold standard composed of 1408 debutant topics in the period 2000-2011, including their ancestors (Chapter 5). 

### **1.7.2 Structure of the dissertation** 

This dissertation is articulated in three parts, described as follows. 

**Part I: Introduction and State of The Art** 

Chapter 2 provides the background for this thesis. We start by introducing the concept of research topic, discussing the different life stages it goes through. Then, we review the literature on the problem of the early detection of research trends through two different lenses. First, we take a technological perspective and discuss the approaches available in the state of the art for detecting topics and analyse their evolution in time. Then, we observe the literature with a philosophical lens and discuss the main contributions provided from historians of science and philosophers, such as Thomas Kuhn, Roy Anthony Becher and others. We provide also some details on community detection algorithm as approach we used to develop Augur. Finally, we discuss the gap in the literature that we want to address. 

18 

#### **Part II: Augur** 

This is the main part of the dissertation and includes two chapters which contain the details of the Augur framework. In Chapter 3, we describe our first study, which investigates some of the patterns that can lead to the emergence of new research topics. In Chapter 4, we describe the Augur framework and the Advanced Clique Percolation Method, a novel community detection algorithm. 

#### **Part III: Evaluation and Conclusions** 

The final part presents the evaluation of Augur and the discussion. In Chapter 5, we describe the gold standard and the evaluation process, and we report the result from the evaluation. Finally, Chapter 6 closes this dissertation by providing an answer to the research questions, discussing the limitations of our solution, and outlining the future directions. 

## **1.8 Publications** 

This dissertation is based on the following publication. 

#### **Chapter 1** 

- Angelo A. Salatino. “Early Detection and Forecasting of Research Trends.” ISWC-DC 2015, The ISWC 2015 Doctoral Consortium (2015): 49. 

#### **Chapter 3** 

- Angelo A. Salatino, Francesco Osborne, and Enrico Motta. “How are topics born? Understanding the research dynamics preceding the emergence of new areas.” PeerJ Computer Science 3 (2017): e119. 

19 

- Angelo A. Salatino, and Enrico Motta. “Detection of Embryonic Research Topics by Analysing Semantic Topic Networks.” International Workshop on Semantic, Analytics, Visualization. Springer, Cham, 2016. **(Best Paper Award)** 

#### **Chapter 4 and 5** 

- Angelo A. Salatino, Francesco Osborne, and Enrico Motta. “AUGUR: Forecasting the Emergence of New Research Topics.” In JCDL 18: The 18th ACM/IEEE Joint Conference on Digital Libraries, June 3-7, 2018, Fort Worth, TX, USA 

Here follow other papers on the field of scholarly data analytics that I published during my PhD and that provided useful insights that fostered the creation of Augur: 

- Francesco Osborne, Angelo A. Salatino, Aliaksandr Birukou, and Enrico Motta. “Automatic classification of springer nature proceedings with smart topic miner.” In The 15th International Semantic Web Conference (ISWC 2016), 17-21 October 2016, Kobe, Japan, Springer International Publishing, 2016. 

- Amparo Elizabeth Cano-Basave, Francesco Osborne, and Angelo A. Salatino. “Ontology Forecasting in Scientific Literature: Semantic Concepts Prediction based on Innovation-Adoption Priors.” In 20th International Conference on Knowledge Engineering and Knowledge Management (EKAW 2016), 19-23 November 2016, Bologna, Italy, Springer International Publishing, 2016. 

- Francesco Osborne, Angelo A. Salatino, Aliaksandr Birukou, and Enrico Motta. “Smart Topic Miner: Supporting Springer Nature Editors with Semantic Web Technologies.” In (Poster and Demo session) @ The 15th International Semantic Web Conference (ISWC 2016), 17-21 October 2016, Kobe, Japan, 2016. 

   - 20 

- Francesco Osborne, Thiviyan Thanapalasingam, Angelo Salatino, Aliaksandr Birukou, and Enrico Motta. “Smart Book Recommender: A Semantic Recommendation Engine for Editorial Products.” In (Poster and Demo session) @ The 16th International Semantic Web Conference (ISWC 2017), 21-25 October 2017, Vienna, Austria, 2017. 

- Francesco Osborne, Angelo Salatino, Aliaksandr Birukou, Thiviyan Thanapalasingam, and Enrico Motta. “Supporting Springer Nature Editors by means of Semantic Technologies.” In Industry Track @ The 16th International Semantic Web Conference (ISWC 2017), 21-25 October 2017, Vienna, Austria, 2017. 

- Andrea Mannocci, Angelo A. Salatino, Francesco Osborne, and Enrico Motta. “2100 AI: Reflections on the mechanisation of scientific discovery.” In Workshop Re-Coding Black Mirror, at International Semantic Web Conference (ISWC) 2017 , 21-25 October 2017, Vienna, Austria, 2017. 

- Angelo A. Salatino, Thiviyan Thanapalasingam, Andrea Mannocci, Francesco Osborne, Enrico Motta. “The Computer Science Ontology: A Large-Scale Taxonomy of Research Areas.” In The 17th International Semantic Web Conference (ISWC 2018), 8-12 October 2018, Monterey, California, USA, Springer International Publishing, 2018. 

- Angelo A. Salatino, Thiviyan Thanapalasingam, Andrea Mannocci, Francesco Osborne, Enrico Motta. “Classifying Research Papers with the Computer Science Ontology”. In (ISWC 2018 Posters & Demonstrations and Industry Tracks) @ The 17th International Semantic Web Conference, 8-12 October 2018, Monterey, California, USA, 2018. 

21 

# **Chapter 2** 

# **Literature Review** 

Detecting topics and tracking their trends has attracted considerable attention in the last two decades. In the literature, we can find several approaches applied to different domains, such as news articles (Schultz and Liberman, 1999; Dai et al., 2010), social networks (Cataldi et al., 2010; Mathioudakis and Koudas, 2010), blogs (Gruhl et al., 2004; Oka et al., 2006), emails (Morinaga and Yamanishi, 2004) and scientific literature (Bolelli et al., 2009; Sun et al., 2016; Osborne et al., 2014; Erten et al., 2004; Decker, 2007). 

In this chapter, we present the main approaches and theories available in the state of the art, with regard to the problem of the early detection of research trends. 

We start this chapter by showing how we defined a research topic within the context of our work, and the reasons why philosophers were not able to provide a widely accepted definition of it. In the same section, we also explain how we used the Computer Science Ontology to support our definition. 

In Section 2.2 we describe the different stages of life in which a topic goes through. Then, we review the literature through two different lenses. The first, in Section 2.3, is the technological lens in which we describe all the main approaches available to detect topics and keep track of their trends. We point out their main strengths, 

22 

and also the limitations that we plan to address in this dissertation. The second lens, in Section 2.4, focuses on the philosophical perspective of the matter. We describe the main ideas from historians of science, such as Thomas Kuhn, which helps us in designing a new innovative approach that aims to fill the current gaps. 

We devote Section 2.5 to describe the embryonic stage, a particular stage of the topic lifecycle that anticipates its emergence. In Section 2.6, instead, we then briefly describe some community detection algorithms that can be used to identify topics in such stage. 

In conclusion, in Section 2.7 we highlight the main limitations and the gap in literature. 

## **2.1 Research topics** 

Currently, the state of the art does not present any universally accepted definition of research topic. 

Indeed, as Becher and Trowler point out, “the concept of academic discipline [and by extension research topic] is not altogether straightforward” (Becher and Trowler, 2001, page 41). On the same note, Nordenstreng (2007) mentions that “the nature of the [academic] discipline often remains unclear, while its identity is typically determined by administrative convenience and market demand rather than analysis of its historical development and scholarly position within the system of arts and sciences.” These claims suggest that disciplines can encompass complex combinations of bodies of knowledge, methods, norms and organisations (Sun et al., 2013). 

One might attempt to observe the characteristics of academic disciplines from different angles. For instance, from a philosophical point of view, academic disciplines are seen as branches of knowledge, which taken together, form the whole knowledge that has been created from the scientific endeavour. Academic disciplines have bound- 

23 

aries, within which we can find coherence in terms of theories, concepts, methodologies, and rules that allow us to test and validate our hypotheses. In general, the kind of questions the discipline tries to answer, the problems it tries to solve, the explanations it attempts to provide, as well as the kind of scientific language it uses, define the boundaries of an academic discipline. These boundaries make disciplines different from each other (Becher and Trowler, 2001, page 58). From an anthropological perspective, academic disciplines consist of cohesive groups of scientists with a high degree of agreement about methods and contents. Scientific communities with their cultural practices shape their own academic discipline, as if they belong to different tribes (Becher and Trowler, 2001, page 23). 

The lack of a widely accepted definition has led to the emergence of alternative ones. For instance, Jo et al. (2007) define topics as semantic units that can function as building blocks for discovering knowledge. For Ding (2011), topics can function as categories of a set of documents and can have different facets, they can be domainspecific, application-dependent, and context-sensitive. 

Inspired by Kuhn’s work, Madlock-Brown (2014) defines research topics as specific areas of study, methods or tools studied by different scientific communities. Indeed, we can see some similarities between this definition of topic and the definition of paradigm. 

Many studies, such as Upham and Small (2010), Chen (2006), Morris et al. (2003), and some others, consider research topics as research fronts. This concept of research front has been introduced by Price (1965), who observed that among scholars, there is this tendency of citing the most recently published papers. Therefore, he sees those sets of papers that scientists actively cite as research fronts. 

We can also find more practical definitions, such as the ones based on topic modelling, which consider topics as sets of words closely related to each other with a certain probability (Blei et al., 2003; Blei and Lafferty, 2006; Blei, 2012). Other ap- 

24 

proaches are based on the simple adoption of keywords (Erten et al., 2004; Decker, 2007), or use conceptual labels (Afzal et al., 2016) to describe the different domains covered by a collection of documents. In Section 2.3, we will observe different approaches for characterising and detecting topics in a collection of documents. All those approaches differ from each other based on the kind of data they process (e.g., abstract, keywords, citations) to characterise the topic structure. 

The definition of research topic the we use for this dissertation stems from Allan et al. (1998). 

In particular, we define research topic as a subject of study or issue that is of interest to the research community and it is addressed in at least few research papers. Subjects of study can encompass different research areas and application-dependent concepts. For instance, a paper introducing a new technology to classify data, is the event that triggers the emergence of new topic. Any paper discussing the implementation of such technology, its application, the release of a new efficient implementation, its evaluation and so on, are all part of the same research topic. Papers discussing another technology to perform classification are not likely to be on the same topic. 

In practice, we define research topic as subject of studies whose label is associated to a related concept in an ontology of research areas, such as, _Acoustics_<sup>1</sup> in the PhySH<sup>2</sup> taxonomy, _Hydrocodone_<sup>3</sup> in MeSH<sup>4</sup> , or _Web Ontology Language (OWL)_<sup>5</sup> in ACM CCS<sup>6</sup> . 

For this doctoral work, the main data source is the Rexplore dataset (see Section 3.2.1), containing the co-occurrence networks between keywords, that are provided by authors when tagging their papers (see Section 3.2.2). However, since keywords 

> 1 `https://physh.aps.org/concepts/40a5bd01-6544-4502-8321-458c33878bf3` 

> 2 `https://physh.aps.org/` 

> 3 `https://meshb.nlm.nih.gov/record/ui?ui=D006853` 

> 4 `https://meshb.nlm.nih.gov/` 

> 5 `https://dl.acm.org/ccs/ccs.cfm?id=10003316&lid=0.10002951.10003260.10003309. 10003315.10003316` 

> 6 `https://www.acm.org/publications/class-2012` 

25 

appear in various forms, for example, singular, plural, acronym and so on, we use the Computer Science Ontology (Salatino et al., 2018b) produced by Klink-2 (Osborne and Motta, 2015). In this way, we can abstract from the different keywords that may refer to the same research topic and also filter out all the keywords that do not represent topics. 

In the following sections, we will provide further details regarding the Computer Science Ontology, that allowed us to define the concept of research topic. 

### **2.1.1 The Computer Science Ontology** 

The Computer Science Ontology (CSO) describes the relationships between research topics extracted from a corpus of 16 million publications, mainly from the field of _Computer Science_ . The version of CSO used in this studies includes more than 17 000 concepts and over 70 000 semantic relationship as well as 8 levels of granularity. Its main root is _Computer Science_ , however CSO includes also other topics as secondary roots, such as _Semantics_ , _Linguistics_ , _Geometry_ and so on. This ontology is produced using Klink-2 (Osborne and Motta, 2015) and it is regularly updated when the Rexplore dataset imports new scientific publications. Indeed, from the beginning of 2018, we released a new and more fine-grained version<sup>7</sup> of the ontology, including more than 26K concepts and over 226K semantic relationships. However, as these studies were already completed by the end of 2017, Augur currently does not take advantage of this new version of the ontology. 

The Klink-2 algorithm takes as input a set of scholarly keywords and their relationship, i.e., the number of times certain keywords co-occur in the different years. Klink-2 combines this information with knowledge from external sources (e.g., DBpedia, calls for papers, web pages) and with various semantic technologies and machine 7Computer Science Ontology version 2.0 `http://w3id.org/cso/downloads` 

26 

learning techniques, to automatically generating an ontology of research areas, according to three main semantic relations: 

- (i) _relatedEquivalent_ , indicates that there are two ways of referring to a particular research area and they can be treated as equivalent for the purpose of exploring research data, e.g., “ontology matching” and “ontology mapping”; 

- (ii) _skos:broaderGeneric_ , indicates that a topic is a sub-area of another one, e.g., _Linked Data_ is considered a sub-area of _Semantic Web_ ; 

- (iii) _contributesTo_ , indicates that the research output of one topic is relevant and therefore contributes to the research of another topic. For instance, research in _Ontology Engineering_ contributes to the Semantic Web, but arguably _Ontology Engineering_ is not a sub-area of the _Semantic Web_ , as there is plenty of research in _Ontology Engineering_ outside the context of _Semantic Web_ research. 

In particular, for each pair of associated keywords (i.e., keywords appearing together in a certain number of papers), the algorithm aims to define their kind of relationship, based on how this relationship developed in time (Osborne and Motta, 2015). 

Among these three relationships, _relatedEquivalent_ and _skos:broaderGeneric_ are necessary to create the taxonomy of research topics and to handle different labels for the same research areas, while _contributesTo_ provides additional information that can be explored and used in other applications, such as analysing research data (Osborne and Motta, 2012). 

This ontology of research topics can be downloaded from the CSO Portal<sup>8</sup> , which is a web application that enables users both to explore CSO and also provide granular feedbacks. For a given research topic, the portal displays all its relationships, allowing user to seamlessly browse the network of topics. 

> 8CSO Portal `https://cso.kmi.open.ac.uk` 

27 

For this work, we rely on CSO because it allows to semantically enhance the cooccurrence network (see Section 3.2.2) by removing all keywords that do not refer to research areas and by aggregating keywords representing the same concept, i.e., keywords linked by a _relatedEquivalent_ relationship in the ontology. For instance, we aggregated keywords such as: 

- “ontology mapping”, “ontology matching” and “ontology alignment”, or 

- “knowledge-based systems” and “knowledge based systems”, or 

- “wireless ad hoc networks”, “wireless ad hoc network” and “wireless ad-hoc networks”; 

in single semantic research topics which will then group together all the publications associated with these keywords. 

## **2.2 Lifecycle of research topics** 

It is well known that science is a dynamic environment, and by constantly splitting and merging, communities of scholars shape its landscape (Di Caro et al., 2017). These social interactions among scientists guide the birth and evolution of research topics. 

According to Braun et al. (2000) the lifecycle of a research topic can be expressed as an S-curve, as depicted in Fig. 2.1, however there is no common agreement on the number of stages the topic goes through during its lifecycle. Braun et al. (2000) characterise the lifecycle of a topic with four stages: birth, growth, maturity, and senility. Instead, Tu and Seng (2012) believe that a research topic evolves sequentially through five stages: initial stage, early stage, expansion stage, maturation stage, and decline stage. Shneider (2009) claims instead that each scientific discipline faces four stages, while match the activities pursued by scholars. At the first stage, scientists introduce 

28 

a new language to describe the new subject matter. At the second stage, they develop the main techniques. The third stage is when the discipline is in its maturity, with scientists creating new insights, new answers and new questions. The fourth stage, instead, is more applicative. This last stage consists in deploying knowledge for practical purposes so that it can have an actual impact into the society. 

In general, from the literature it is clear that when a new scientific area emerges, it goes through an initial phase, also called early stage, in which a group of scientists agree on some basic tenets, build the conceptual framework and begin to establish a new scientific community. Afterwards, the research area enters into a recognised phase, when it reaches its own maturity and a substantial number of authors become active in the area, producing and disseminating results. In Fig 1.1, at page 4, we can observe how these stages are located within a timeline. In Fig. 2.1, instead, we can see an example of a specific case regarding the _Semantic Web_ showing the amount of scientific papers published per year, in this area. Through this graph it is possible to observe that it emerges around the year 2001, in agreement with the Tim Berners Lee’s seminal paper (Berners-Lee et al., 2001), therefore it directly moves to the early stage when several authors start to define scientific field until it gets mature few years after. 



**Figure 2.1:** Evolution of the topic _Semantic Web_ in terms of number of publications per year. The chart has been produced using the Rexplore system. 

29 

As we will see throughout this chapter, all the approaches available in literature can identify new research topics only once they have emerged and they have been explicitly labelled and recognised by researchers. Therefore, the problem of detecting research topics, before they emerge, still needs to be addressed. For this reason, we will rely on the hypothesised embryonic stage, as initially conceived by Kuhn (Kuhn, 1970), to analyse and forecast the emergence of new research topics. 

## **2.3 Technological background** 

The detection of research trends involves two main tasks: (i) identifying topics within a collection of documents, and (ii) determining their development in time (i.e., tracking their trends). In literature, we can find studies focusing only on detecting topics, and some other studies aiming to detect trends, which include technologies for both detecting topics and analysing their evolution. Since, there are different studies tackling different elements of the problem, we believe we can provide a better literature review by separately looking at the different technologies, that aim to resolve the tasks of topic detection and tracking. To this end, when discussing such approaches, rather than reviewing the whole studies, we will focus on the specific technologies adopted for performing each of these tasks, independently. 

Therefore, we organise this section in two parts. Section 2.3.1, considers all the main approaches for detecting topics within corpora, while Section 2.3.2 will describe the main techniques for tracking the evolution of topics. 

### **2.3.1 Topic detection in the scientific literature** 

The aim of topic detection is to break the whole collection of documents and to arrange them into groups of topics. Different approaches will produce different results when run on the same corpus also because the concept of topic does not have a widely 

30 

accepted definition. Indeed, the definitions adopted by different approaches usually depend on the scope of the application. As a matter of fact, sometimes topics are algorithmically defined, which means that they are defined only implicitly as the output of an algorithm. 

One of the very first attempts dates back to 1983, when in a seminal paper, Callon et al. (1983) introduced the method of co-word analysis to study the content of documents. Their main assumption is that “key words<sup>9</sup> ” (or macro-terms) within papers constitute an adequate description of their content. In this way, the key words used for describing the content of a publication can be used as the basic building blocks to characterise the structure of science. In particular, this approach extracts those key words and measures their co-occurrence within the documents. Then, it creates a network, in which the nodes are words and the links represent whether their co-occurrence value exceeds a certain threshold. The role of each macro-term of an article, is to help in placing that article in the corresponding area of the network. The approach, then, organises this network of key words into group of words according to the frequency with which they appear together. The resulting clusters will represent the themes or concepts in the scientific literature. While Callon and his colleagues focused only on few case studies, when the computational power of machines increased, many other research groups extended this work and focused on larger case studies, such as analysing the interactions between basic and technological research (Callon et al., 1991), mapping knowledge evolution in the field of _Scientometrics_ (Courtial, 1994), and studying a number of fields, such as _Software Engineering_ (Coulter et al., 1998), _Information Research_ (Ding et al., 2001), _Ethics_ and _Dementia_ (Baldwin et al., 2003), _Geographic Information System_ (Tian et al., 2008), and others. However, the main drawback is that such approach relies on the appearance of specific words and 

> 9The key words are different form the keywords that authors use nowadays to tag their papers. In the context of Callon et al. (1983) work, a key word or macro-term is a signal word that acts as agent of contextualisation. 

31 

it does not consider the context, therefore it cannot handle issues of synonymy and polysemy. 

Another study that laid the groundwork for this field was the _Topic Detection and Tracking_ (TDT) program developed by the Defense Advanced Research Projects Agency (DARPA) (Allan et al., 1998). Although the domain of interest for this program was on broadcasted news, it articulated the problem and provided interesting insights on how to automatically extract topics and organise a stream of documents. To detect topics, they perform cluster analysis so that items are grouped by their relatedness within bins that represent topics. Allan and his colleagues tested different solutions for clustering (Allan et al., 1998). One approach is based on Eichmann et al. (1999) and uses _term frequency inverse document frequency_ index (tf-idf) to select the most significant words and then it computes the cosine similarity between all pairwise news to create clusters. Another approach uses the Kullback-Leibler distance as metric to group together news on similar topic (Allan et al., 1998). 

One of the main contributions of this work was to formalise the problem of Topic Detection and Tracking, which helped this field to flourish. Indeed, in the literature we can find many approaches based on one of the tasks formalised by Allan et al. (1998). 

Allan and his colleagues organised the problem around five research tasks: _Topic Tracking_ , _Story Link Detection_ , _Clustering_ (or _Topic Detection_ ), _First Story Detection_ , and _Story Segmentation_ . In particular, the _clustering_ task helps in finding the thematic structure within the corpus and it mainly consists of technologies to summarise the content of documents and group them based on the topics they discuss. 

All the available approaches in literature can be classified based on the kind of information they use. For collections of scientific documents, the main information exploited by the approaches for detecting topics are titles, abstracts, keywords, full content, and citations. Some approaches rely on just one set of information (e.g., 

32 

keywords), while some others can combine more than one set of information (e.g., the combination of abstract and keywords), with the aim of improving clustering performance. However, it is also worth to point out that sometimes the corpus itself can introduce some constraints over the designed approach. For instance, some approaches cannot take advantage of the full content of papers simply because this information may not be available. 

In what follow, we discuss the main approaches for topic detection according to the kind of information they adopt, such as: (i) abstract or full content, (ii) citations, (iii) keywords and taxonomies, and (iv) hybrid solutions, which combine more than one entity. 

#### **Abstract or full content** 

Approaches relying on either or both abstracts and full content<sup>10</sup> of documents, usually aim to synthesise the content of scientific papers first. This process of dimensionality reduction is accomplished by extracting some meaningful words, so that now papers are treated as “bag of words”, with the assumption that these words can reflect its content. 

One of the first approaches that helped to extract meaningful words from the content of documents is the already mentioned tf-idf. This technique computes an index for each word, reflecting how important they are and then only those with higher value are retained (Salton and Buckley, 1988). Then, text documents are clustered on the basis of shared words, using cosine similarity (Schultz and Liberman, 1999). Roche et al. (2010) used a similar approach on the field of _Molecular Biology_ . However, while the tf-idf can identify sets of words that are discriminative for documents, it does not capture position in text, semantics and co-occurrences in different documents. 10Approaches using the full content take advantage of the full text of a document. 

33 

Besides, the dimensionality reduction is very little and it does not provide enough information about the inter- or intra-document statistical structure. 

Hence, the next generation of approaches for topic detection adopted topic modelling. One of the most influential approaches is the Latent Dirichlet Analysis developed by Blei et al. (2003). LDA is a three-level hierarchical Bayesian model to retrieve latent patterns in texts. The basic idea is that each document is modelled as a mixture of topics, where a topic is a multinomial distribution over words characterised as a discrete probability distribution defining the likelihood that each word will appear in a given topic. LDA aims to discover the hidden–or latent–structure which is words per topic and topic per document. In order to do so, it computes the conditional distribution of the hidden variables (topics) given the observed variables (words) (Blei, 2012). 

A major difference between tf-idf and LDA is that the former works at lexical level, for example a document discussing networks might be considered dissimilar from a document about graphs when adopting tf-idf. On the other hand, since networks and graphs frequently co-occur in articles, they are likely to be associated with the same topic, so the LDA is likely to produce a similar representation for these articles. 

Other approaches that fall within the same category of topic modelling are the Latent Semantic Analysis (LSA), the Probabilistic Latent Semantic Analysis (pLSA) and the Correlated Topic Model (CTM). 

The Latent Semantic Analysis was actually one of the first attempts to cope with the shortcomings of tf-idf, as it can achieve significant reduction in dimensionality, in large collections (Deerwester et al., 1990). In particular, LSA counts the frequencies of each word per documents and then it uses the singular value decomposition (SVD) technique to reduce the number of rows while preserving the similarity structure among columns. In this way, LSA is able to group together the documents, which use similar words, as well as the meaningful words, shared by a similar set of documents. 

34 

In addition, it can capture some basic linguistic aspects such as synonymy and polysemy. Such patterns are used to detect the latent components within the collection of documents. 

An alternative approach to the LSA is the Probabilistic Latent Semantic Analysis (pLSA) developed by Hofmann (1999). The pLSA models words of documents as samples from a mixture model, then by means of the Expectation-Maximization algorithm, it performs the extraction of topics that are represented as multinomial random variables, thereby components of the mixture. In developing the LDA, Blei and his colleagues, aimed to fix some weaknesses introduced by the pLSA, such as (i) it learns the topic mixtures only for documents seen in the training phase, so basically it is not able to assign probability to previously unseen documents; and (ii) the number of parameters increase linearly with the size of the corpus, indicating that the model suffers from overfitting problems (Blei et al., 2003). 

The Correlated Topic Model (Blei and Lafferty, 2006) uses the logistic normal distribution instead of the Dirichlet, to solve the fact that LDA fails to model the correlation between topics. This approach fits the process of extracting topics from scientific text corpora since it is natural to expect that subset of the underlying latent topics will be highly correlated. For instance, a scientific paper about _Genetics_ is likely to be also about _Health_ and _Disease_ . 

Lee et al. (2010) and Alghamdi and Alfalqi (2015) analysed in more detail the main differences among these four methods for topic modelling. In Table 2.1, are reported the main characteristics and limitation summarised from Lee et al. (2010). As we can see, each method has its strengths and weaknesses, and the selection of one method over another mainly depends on the kind of application a researcher has in mind (Lee et al., 2010). However, LDA is the most frequently used approach for modelling topics. Indeed, since its introduction, LDA has been extended and adapted in several applications. Some approaches include temporal text mining, author-topic 

35 

analysis, supervised topic models, latent Dirichlet co-clustering and LDA based bioinformatics (Wang and McCallum, 2006; Shen et al., 2008). Other extensions of LDA include the hierarchical LDA where topics are grouped together in a hierarchy (Griffiths et al., 2004) and the relational topic model which is a combination of topic model and network model for collections of linked documents (Chang and Blei, 2010). 

**Table 2.1:** Characteristics and limitations of the four methods for topic modelling. This table is an extract of Lee et al. (2010). 

|**Method**|**Characteristics**|**Limitations**|
|---|---|---|
|Latent Semantic<br>Analysis (LSA)|i) Can get from the topic if<br>there are any synonym words.<br>ii) Reduces dimensionality of<br>tf-idf using the svd method.<br>iii) Not robust statistical<br>background.|i) Hard to determine the<br>number of topics.<br>ii) Hard to interpret loading<br>values with probability<br>meaning.<br>iii) Difficult to label a topic<br>with the words within the<br>topic|
|Probabilistic<br>Latent Semantic<br>Analysis<br>(PLSA)|i) It can generate each word<br>from a single topic; even<br>though various words in one<br>document may be generated<br>from different topics.<br>ii) Partially handles polysemy.|i) At the level of documents,<br>PLSA cannot do probabilistic<br>model.|
|Latent<br>Dirichelet<br>Allocation<br>(LDA)|i) Need to pre-process<br>documents to remove<br>stop-words, first.<br>ii)Can handle longdocuments|i) Cannot model the relations<br>among topics.|
|Correlated<br>Topic Model<br>(CTM)|i) Uses the logistic normal<br>distribution to create relations<br>among topics.<br>ii) Allows the occurrences of<br>words in other topics and<br>topic graphs|i) Computationally expensive.<br>ii) Contains general words<br>within topics.|



However, one of the main issues with the LDA, and actually recurring in all the approaches for topic modelling, is that topics are bereft of labels. These approaches represent a topic with a set of words that are also representative for the topic itself, however it is very difficult to select one of them as label, at least automatically. As an 

36 

illustration, in Table 2.2, there is an example of word distribution, which we manually associated to the semantic concept of _Video-stream_ (Cano-Basave et al., 2016). 

**Table 2.2:** Bag of words associated with the concept of Video Streaming, extracted using LDA. This example is extracted from Cano-Basave et al. (2016). 

video, stream, network, rate, system, application, adapt, bandwidth, <u>packet,</u> internet 

Another approach that uses the full text to determine the structure of topics within the collection of documents is Morinaga and Yamanishi (2004). This approach uses the Finite Mixture Model to detect topics and in addition by analysing the changes in the extracted components (clusters of words), it can track the emergence of new topics. This is done by using an improved version of Kleinberg’s approach (Kleinberg, 2003) which will be described in the next section about topic evolution. In their work, Morinaga and his colleagues represent a topic as a single mixture component and then they use the finite mixture to model the topic structure. Then, by dynamically learning the finite mixture model and tracking the changes of main components they can recognise a change in the topic structure and therefore identify topics trends. However, this approach was evaluated on an email corpus and therefore is not clear how will it would perform on scientific literature. 

Chavalarias and Cointet (2013) developed a method to automatically reconstruct representations of the evolution of science. They analysed a collection of 200 000 articles from the Thomson Web Of Science corpus related to research in Embryology. With the CorText Manager tool they extracted a list of 2000 n-grams representing the most salient terms. Then they derived a co-occurrence matrix upon which, with the clique detection approach, they performed clustering analysis to discover patterns in the evolution of science. Another network-based approach is from Sayyadi and Raschid (2013). Sayyadi and his colleague developed an approach that extracts all meaningful words from the content of papers. Next, they represent the collection of documents as keywords co-occurrence network. Then, upon this network they run 

37 

a community detection algorithm to locate clusters of keywords that can represent topics. 

#### **Citations** 

Today, we can find many approach using citation networks, and most of them are based on the principle of clustering scientific documents by means of the co-citation analysis, introduced by Small (1973). The use of citations for detecting topics has been explored in many different ways and some approaches combine citations with other entities such as keywords and abstracts. 

One of the first approaches using citation for detecting topics was described by Small (1977). Small identified “hot fields” by clustering highly co-cited documents each year and linking them through time. This analysis has been performed more recently in Small (1999) and Boyack and Klavans (2014) arguing that even if the thresholds and normalizations have changed along time, the basic process is still valuable. 

Similar studies come from Upham and Small (2010) and Small et al. (2014). The first study used the ISI corpus (which now is Web of Science<sup>11</sup> ) to identify 20 emerging topics within the years 1999-2004, representing co-citation clusters. The study of Small et al. (2014), instead, performs co-citation analysis over Scopus data, allowing them to perform a more global analysis, rather than focusing on a confined area. 

Chen (2006) designed a tool called CiteSpace which combines co-citation analysis and burst detection (Kleinberg, 2003) to identify new emerging trends. In particular, they perform a progressive network analysis which synthesises slices of networks and focuses on critical nodes which play a crucial role in the evolution of network over time. CiteSpace has been employed to characterise new emerging topics within the field of _Mass-extinction_ and _Terrorism_ (Chen, 2006), _String Theory_ , _Gene Target-_ 

> 11Web of Science `http://wokinfo.com/` 

38 

_ing_ and _Peptic Ulcer_ (Chen et al., 2009) and _Regenerative Medicine_ (Chen et al., 2012). According to their results, two of the main factors related to the emergence of new topics are the burst in citation and the betweenness centrality of their papers. This suggests that such emerging topics or clusters were the result of collaborations between two or more existing topics. 

Another study is from Jo et al. (2007), who developed an approach to detect topics combining distributions of terms (i.e., n-grams) with the distribution of the citation graph related to publications containing that term. Their work is based on the intuition that if a term is relevant to a particular topic, documents containing that term will have a stronger connection than randomly selected ones. In their first approximation, that term would also represent the label for that topic, but they extended their algorithm so that it can consider topics as a relation of multiple terms. The main drawback with these approaches based on co-citation analysis is that they are able to assign each document to only one topic. A document is rarely monothematic. Therefore, these approaches can create clusters of documents that are not coherent. 

#### **Keywords and taxonomies** 

Another category of approaches for detecting topics in a collection of documents use keywords. Keywords (also called _subject terms_ ), are terms carefully selected by scholars to identify the research focus of their manuscript (Abrahamson, 1996; McCloskey, 1998). They represent the key concepts and the main ideas of papers, as well as reflecting their novelty. Such representation, is also beneficial for search engines for returning relevant papers to a given query. 

In the literature there are many approaches aiming to detect topics which rely on keywords. For instance, Duvvuru et al. (2012, 2013) analysed keywords and the networks of their co-occurrence in order to monitor how the link weights develop in 

39 

time. In this way, they aim to detect research trends as well as emerging research areas. However, we can argue that using keywords as a proxy for topics brings several drawbacks. Indeed, Osborne and Motta (2015) point out that keywords tend to be noisy and do not always represent research topics, such as the keyword “case study”. Moreover, they also cannot handle synonymy and polysemy, since many keywords can refer to the same topic or a single keyword can represent more topics. Yi and Choi (2012) developed an approach that tackles some of the issues of Duvvuru et al. (2012). Before creating the keyword network, the authors designed a procedure to clean the keyword set. For instance, when multiple keywords are considered similar, they are transformed into a single form, such as “agent” and “agents” into “agent”. In addition, if keywords consist of multiple independent keywords, they are split, like “efficiency and effectiveness” into “efficiency” and “effectiveness”. However, few details are provided regarding the implementation of this procedure. 

Decker (2007) developed an approach that generates paper-topic relationships by exploiting keywords and words extracted from the abstracts in order to analyse the trends of topics on different timescales. In particular, this approach matches a collection of scientific manuscripts with a manually curated taxonomy of topics. This taxonomy has been manually crafted using topics appearing in proceedings, and then complemented with keywords and terms from the abstracts (Cameron et al., 2010). Then, by analysing the changes in the number of publications associated with topics, they can detect research trends. Similarly, Erten et al. (2004) adopted the ACM Computing taxonomy for analysing the evolution of topic graphs to monitor research trends. Since, these last two approaches rely on taxonomies of topics, they can be considered as an improvement with respect to the approach of Duvvuru et al. (2012), which simply uses keywords. However, the main issue is that both taxonomies are manually curated. Indeed, focusing on the field of _Computer Science_ , which we know it is a constantly expanding field, manual taxonomies tend to become quickly 

40 

outdated. Not to mention that the last update of the ACM Computing taxonomy occurred in 2012<sup>12</sup> (6 years before, at the time of writing), replacing its previous version released in 1998<sup>13</sup> . In this way, new emerging topics do not get the chance to be included in the taxonomy, preventing the process of clustering to be accurate enough. 

Herrera et al. (2010) offered an approach for categorising physics literature described through the Physics and Astronomy Classification Scheme (PACS)<sup>14</sup> codes. In particular, they create a scientific concept network in which each node represents a PACS code, which refers to a specific topic in Physics. Two nodes are then linked if the two corresponing codes co-occur together in at least one paper. In order to study the evolution of different fields, the authors used the Clique Percolation Method to identify communities in the PACS network and linked together similar communities along time using the method proposed by Palla et al. (2007a). The PACS scheme, which has now been replaced by the Physics Subject Headings (PhySH)<sup>15</sup> , was maintained by the American Institute of Physics (AIP) and we can argue that it had the same issues of the ACM Computing taxonomy. On the other hand, PhySH has the advantage of being crowdsourced with the support of authors, reviewers, editors, and organisers of scientific conferences, so that it is constantly updated with new terms. A similar analysis in the field of _Medicine_ has been performed by Ohniwa et al. (2010), using the Medical Subject Heading (MeSH)<sup>16</sup> . The MeSH taxonomy is maintained by the National Library of Medicine of the United States and has similar characteristics to PhySH, since it is constantly updated collecting new terms as they appear in the scientific literature or in emerging areas of research. 

> 12The 2012 ACM Computing Classification System `http://www.acm.org/publications/ class-2012` 

> 13ACM Computing Classification System ToC `http://www.acm.org/about-acm/class` 

> 14PACS - Physics and Astronomy Classification Scheme `https://publishing.aip.org/ publishing/pacs` 

> 15PhySH - Physics Subject Headings `https://physh.aps.org/about` 

> 16MeSH - Medical Subject Headings `https://www.nlm.nih.gov/mesh/` 

41 

Another approach falling into the same category is Klink-2 of Osborne and Motta (2015), which is an algorithm to automatically generate an ontology of research areas in _Computing_ , the Computer Science Ontology<sup>17</sup> . Klink-2 is able to detect relationships and then build a semantic network of research areas, from keywords associated with a collection of documents, exploiting semantic technologies, machine learning and knowledge from external sources (e.g., DBpedia, calls for papers). Similarly to the approaches of Decker (2007); Duvvuru et al. (2012); Erten et al. (2004), Klink-2 also relies on keywords, but it adds a conceptual layer aiming to resolve some of the aforementioned drawbacks removing the keywords that do not represent a topic and introducing three relationships between keywords: _skos:broaderGeneric_ , _relatedEquivalent_ and _contributesTo_ . This automatically generated ontology presents two main advantages compared to the manually crafted ones, e.g., the ACM Computing taxonomy. Firstly, the ontology is automatically generated and therefore can be easily updated to include new emerging topics by re-running Klink-2 over an updated collection of documents. The second advantage is that Klink-2 can create relations between a wider set of terms, compared to the other taxonomies. This semantic characterisation of research topics has been beneficial in many applications, such as _Rexplore_ , a platform for exploring and making sense of scholarly data (Osborne et al., 2013), _Smart Topic Miner_ for supporting academic editors in classifying scholarly publications (Osborne et al., 2016), _Smart Book Recommender_ to support the Springer Nature editorial team in promoting their publications (Osborne et al., 2017) and the detection of topic-based research communities (Osborne et al., 2014). 

In brief, the state of the art presents several approaches for detecting research topics using keywords. Some approaches directly rely on keywords, but as we have already observed they tend to suffer from polysemy, synonymy and a number of other issues. Instead, other approaches only indirectly rely on keywords, using taxonomies 

> 17Computer Science Ontology `http://cso.kmi.open.ac.uk` 

42 

of topics, which produce more accurate results. However, those approaches to topic detection that rely on automatically generated taxonomies tend of course to be more comprehensive and up to date. 

#### **Hybrid approaches** 

So far, we have analysed approaches that aim to find topics using some important entities which can be extracted from scientific papers, such as the abstract or the full content, the citations and the keywords. In this section we describe the hybrid approaches that use a different kind of metadata such as titles, venues (i.e., journals, conferences), and authors. While some approaches might exclusively use one of these entities, some others use a combination of them. 

Authors are the main agents within the scientific endeavour. They perform scientific research, report and publish results. The information about them can be beneficial and provide interesting insights when investigating the topical structure of a corpus. In particular, author networks, in which links represent co-authorship relation, are used by a variety of approaches to analyse the research landscape (Zhou et al., 2006). Other approaches describe authors using the probabilistic topics model described in the previous section. For example, Rosen-Zvi et al. (2004) proposed the author-topic model (ATM) which improves LDA (Blei et al., 2003) by including authorship information. Starting from the LDA assumption, in which every document is a distribution of topics, their approach further extends the concept of topics as distributions over both words and authors. Their model returns the set of topics that appear in the corpus and identifies which topics are relevant to which authors. The same research team aimed to improve the results of ATM by proposing the Probabilistic Author-Topic model (Steyvers et al., 2004), which models documents as a composition of multiple topics, topics as probability distribution over words, and authors as probability distribution over topics. Instead of using the LDA, they extend 

43 

the Probabilistic Latent Semantic Analysis introduced by Hofmann (1999). Nevertheless, the probabilistic model is quite simple and disregards some aspects such as topic correlation and author interaction. Bolelli et al. (2009) further extended the ATM introducing the Segmented Author-Topic model (S-ATM), a generative model that uses temporal ordering of documents in order to identify topic evolution and then exploits citations to evaluate the weights for the main terms in documents. 

Conferences and journals can also provide significant insights in the contest of studying the evolution of scientific fields and identifying topics. Indeed, publication venues can influence the shape of a research topic over time. In the state of the art, several approaches exploit publication venues and they can be classified as approaches extending topics models and approaches based on network analysis. For instance, Tang et al. (2008) presented a unified topic model for simultaneously modelling the topical distribution of papers, authors, and conferences called Author-ConferenceTopic (ACT) model. This model further extends the Author-Topic model of RosenZvi et al. (2004), including conference and journal information. In particular, they present three different implementations of the model, which differ from each other in the way they model the association between authors, distribution of topics and conference information. Yan and his colleagues (Yan et al., 2012), adopted the ACT model to demonstrate that communities of scholars and research topics are intertwined and co-evolve, instead of being two disconnected entities. However, Wang et al. (2012) identify a limitation of the Author-Conference-Topic model, pointing out that this model extracts topics for the corpus of documents and then it maps them to the research areas available within the “call for papers” of conferences. This operation is not always possible because the latent topics extracted with the LDA may not match the conference topics. Therefore, Wang and his colleagues presented a further extension, the Author Conference Topic Connection (ACTC) model, which aims to 

44 

improve this aspect by adding subject information of the conference and the latent mapping information between subjects and topics. 

Examples of network-based approaches using information from venues are Sun et al. (2016), Boyack et al. (2005) and Pham et al. (2011). Sun et al. (2016) used a similar approach to Herrera et al. (2010) and Duvvuru et al. (2012), mentioned above, as they created a network of entities in order to identify scientific fields and analyse their evolution. However, the approach of Sun and her colleagues differs from the latter ideas since they measure the similarity between conferences using author co-occurrences. In particular, for each year, they create a network in which each node represents an active conference in that year and the link between them is determined based on the amount of authors that publish in both conferences. Once the network is created, they identify scientific fields by detecting communities within the network using the Louvain method (Blondel et al., 2008). 

Another approach, that has the potential to be extended and used to find topics is from Boyack et al. (2005). In this approach, the authors built a map representing the structure of all of science using journal citation data. They designed eight similarity measures to group together journals based on how they cite each other. Although this approach serves for visualisation purposes, the authors show that each cluster of journals is related to a particular research field. Indeed, with the same strategy, Pham et al. (2011) analysed the development of Computer Science disciplines by visualising the knowledge network at different time points. Their approach combines data on venues and citations coming from DBLP and CiteSeerX, respectively. Initially, they created a venue knowledge network in which both journals and conferences are linked to each other based on their citations. Then, they identify sub-areas of Computer Science by clustering the network and tracing their development. Such journal maps, have been investigated by other research teams, such as Leydesdorff and Rafols (2012) and Leydesdorff et al. (2013). In these studies, the authors aggregated data from the 

45 

Journal Citation Reports (JCR) and Social Sciences Citation Index (SSCI) to create global maps of science based on the journal-journal citation relations. In addition, we can find other approaches which share plenty of similarities with the ones just mentioned (B¨orner, 2010; Van Eck and Waltman, 2010; Boyack et al., 2008). 

Fried and Kobourov (2014) proposed an approach that creates maps of Computer Science (MoCS) by taking advantage of titles of papers from the DBLP database. They firstly extract prominent words and phrases and then calculate their similarity based on co-occurrence in titles. Next, these words are clustered based on their similarity values, providing a visual representation of topic space. The main reason why authors are using only titles in their analysis is mainly due to the corpus, as the available information in DBLP is limited to titles, authors and venues. However, there are some drawbacks as the title of a paper may not necessarily reflect all the topics that are discussed within the paper. 

As we can see, the state of the art proposes plenty of approaches to identify topics within a collection of documents. The design and the adoption of a certain approach can be influenced by the comprehensiveness of the corpus and whether certain entities are available. To this end, we organised this review by grouping together approaches that use similar set of entities, and towards the end we also presented approaches that combine more than one entity. Before analysing the limitations of the state of the art, we devote the next section to review the approaches that aim to track the evolution of topics, with particular attention on how they aim to detect emerging topics. 

### **2.3.2 Topic evolution** 

The task of topic detection deals with the static component of a topic, i.e., its identification within a collection of documents. Instead, topic evolution involves the dynamic component of topics, i.e., their development over time. 

46 

In particular, Allan et al. (1998) considered two tasks: First Story Detection and Tracking. 

The First Story Detection (FSD) task aims to recognise new emerging topics that had not been discussed earlier. Specifically, this task monitors the stream of incoming documents and identifies the presence of a new topic. For instance, a good FSD system should detect the first articles reporting about the _Semantic Web_ around 2001 or _Deep Learning_ and _Cloud Computing_ in the middle of the previous decade (2000-2009). In this case, however, this task is only able to detect topics once they are already emerged, rather than anticipating, i.e., forecasting, their emergence. Considering such limitation, we chose to rely on a network-based approach instead, which we will discuss in Section 2.6. 

Alternatively, the task of Tracking identifies new articles that discuss previously known topics. The system performing such task, is aware of the topics present in a collection of documents and, when analysing the stream of incoming articles, it should be able to sort them properly. This means that for each new document, it will extract its topics and classify them with the documents already in the collection, which discuss the same topics. At this point, the system can perform an analysis (i.e., using statistical methods) to observe the state and understand the development of each topic. Some technologies to help in achieving this task were quite mature already twenty years ago. Indeed, the state of the art could already provide approaches to extract topics from documents, such as PLSA (Hofmann, 1999) and some similarity measures to aggregate documents according to their topics. 

Basically, these two tasks allow users to keep track and analyse the dynamicity of topics, from the moment they emerge onwards. However, even if they are two different tasks, some approaches combine them together so that, when organising the set of incoming documents, they are able to analyse the state of each topic as well as identifying new topics. Indeed, as we will describe later, Di Caro et al. (2017) 

47 

developed an approach for observing the development of topics within a corpus in different time windows. With their approach, they could also observe the emergence of new topics that had no antecedents in previous time windows. 

In general, in the literature we can find several approaches that aim to track the development of topics as well as their emergence. Some of them use custom metrics relying on the number of documents associated to the topic (Kleinberg, 2003; Ho et al., 2014) or number of authors (Guo et al., 2011), while some other approaches perform more complex analysis (Bettencourt et al., 2009; Jo et al., 2007). A second category of approaches use citation analysis which focus on determining the citation patterns between documents (Shibata et al., 2008; Jo et al., 2007), others might use co-word analysis which, as already seen, studies the co-occurrence of words within documents (Furukawa et al., 2015; Morinaga and Yamanishi, 2004; Di Caro et al., 2017), as well as hybrid studies (Bettencourt et al., 2009). Finally, a third kind of approaches exploit overlay mapping techniques to build maps of science and rely on human experts to assess emerging topics (Leydesdorff et al., 2013; Boyack et al., 2005). 

Although, many of these approaches are capable of both tracking the development of topics over time and acknowledge their emergence, for the purposes of this study, we will review them according to their ability to detect new emerging topics. 

In what follow, we discuss the main approaches according to the technique they use: (i) burst detection, (ii) shift in citation patterns, (iii) connectedness in co-authorship network, (iv) co-word analysis, and (v) overlay mapping. 

#### **Burst detection** 

According to Small et al. (2014), two of the main features associated with the emergence are novelty (or newness) and growth. A method for identifying emerging topics, is the burst detection algorithm of Kleinberg (2003), which detects the rapid growth 

48 

of term usage. This approach has inspired a good number of methods for detecting research trends (Mane and B¨orner, 2004; Jo et al., 2007; Decker, 2007; Ke et al., 2004; Boyack et al., 2004; He et al., 2011). Some of these approaches have already been mentioned in the previous section. The burst detection algorithm has also been incorporated in larger tool sets such as Citespace II (Chen, 2006), the Network Workbench (B¨orner et al., 2010) and Sci2<sup>18</sup> . 

The overall idea behind Kleinberg’s approach is to analyse a stream of documents and find features whose behaviour is “bursty”, or in other words they occur with high intensity over a limited period of time. The approach uses a probabilistic automaton having different states corresponding to the frequencies of each individual word. There are as many automata as the number of words, and they change state when the frequency of their associated word changes significantly: at the beginning or end of the period of burst. This approach can be used to identify topics and concepts that came into adoption and were actively discussed for a period of time. However, it performs burst analysis for every word (including stop words), therefore it must be included in a pipeline that first pre-processes the documents (Kleinberg, 2003). 

Because identifying and tracking emerging trends can be very difficult when relying only on raw text, the task is usually accomplished taking into account more information, such as citation networks. In Section 2.3.1, we mentioned the approach of Jo et al. (2007) and CiteSpace (Chen, 2006) which combine distributions of terms and citation networks to detect topics. Their primary goal, however, is to facilitate the analysis of emerging trends, which is inspired by the burst detection approach of Kleinberg (2003). Similarly, Jo et al. (2007), developed an approach that combined distributions of terms (i.e., n-grams) with the distribution of the citation graph related to publications containing that term. In particular, the authors assume that if a term is relevant for a topic, documents containing that term will have a stronger 

> 18Science of Science (Sci2) tool `http://sci2.wiki.cns.iu.edu/` 

49 

connection than randomly selected ones. Then, their algorithm aimed at locating the set of terms having citation patterns that exhibit synergy. Their results showed that the algorithm is effective and it is also able to detect new emerging topics. However, their approach introduces a time lag, since it takes time for the citation network of a term to become tightly connected. 

#### **Shift in citation patterns** 

In the state of the art, we can find several approaches that identify the emergence of a new area, by analysing the shifts in citations patterns over time (Morris et al., 2003; Morris, 2005; Takeda and Kajikawa, 2009; Shibata et al., 2008; Small and Upham, 2009;<sup>˚</sup> Astr¨om, 2007). These approaches are based on the intuition that the fact that two previously unconnected, or loosely connected, areas are getting close to each other, may indicate the emergence of a new area that can extend previous research. Takeda and Kajikawa (2009) use the citation network and by means of a modularitybased community detection algorithm, they detect part of the networks representing topics where they then manually identify emerging trends. However, such manual analysis could be accomplished because the authors were focusing on the relatively small area of _Optics_ , whilst we can argue that such approach might not be scalable when broadening the domain. Morris et al. (2003) use co-citation networks to cluster documents that are bibliographically coupled (Kessler, 1963), or in other words they share a certain amount of cited papers. However, this approach suffers from the same issues mentioned for Takeda and Kajikawa (2009). In addition, these approaches do not provide any statistical measure to assess the emergence of a new topic, as their evaluation is performed by human expert. 

On the other hand, Shibata et al. (2008) introduced topological measures to detect the emergence of new topics without the support of experts. In this study, the authors performed clustering over the citation network and labelled each cluster with its most 

50 

representative word. To detect the emerging topics, the approach tracks the age of the cluster. An interesting claim the authors make, which is actually in line with our view, is that this approach suffers of time lag. In fact, this issue is quite common for each approach based on citation and co-citation networks. Sometimes, newly published papers might need 2 years before being cited and therefore they tend to be underrepresented in such networks. Indeed, Shibata et al. (2008) advise that to detect the emergence of new topics, these approaches should be complemented with information coming from other entities such as venues. 

A slightly different approach, that uses citations but does not perform a topological analysis over the network, comes from Clarivate Analytics<sup>19</sup> . Each year, from 2013 onwards, Clarivate Analytics publishes a report called _Research Fronts_ revealing a selection of key research fronts (i.e., hot and new emerging ones). According to “Research Fronts 2017”<sup>20</sup> which identifies 100 hot research fronts and 43 emerging ones, “a research front consists of a core of highly cited papers along with the citing papers that have frequently co-cited the core.” 

To select hot research fronts, they group the whole set of research fronts (9,690) within 10 macro-areas. Then, for each of these 10 groups they select the top 10 research fronts based on the average year of their highly cited papers (core papers). The results are then presented with the identified core papers, affiliated countries, and institutions. 

For selecting the emerging research fronts, instead, they select specialties whose core papers have been published in the previous two years (for this report, from 2015 onwards). 

These emerging research fronts are then analysed and interpreted by human experts to understand the ongoing trends and assess their significance. 

> 19 `https://clarivate.com/` 

> 20Research Fronts 2017 `https://web.archive.org/web/20180515085946/https://clarivate. com.cn/research_fronts_2017/2017_research_front_en.pdf` (web archived) 

51 

In this approach we can see two main issues. As with the other approaches based on citations analysis, this approach suffers of a time lag between the actual emergence of a research topic (i.e., emerging research fronts) and the actual time it is identified. Even though this time lag can reach at most two years, in the worstcase scenario we can acknowledge the emergence of a new topic two years later. The second issue concerns the potentially low recall of the approach. Even if the report does not provide any statistical values about precision and recall in identifying hot and emerging research fronts, based on the methodology, it is easy to recognise such issue. Indeed, many novel topics might not be identified because their core papers did not reach a high enough number of citations in the previous two years. 

#### **Co-authorship networks** 

Authors and co-authorship networks have also been considered to understand how the growth in the number of authors could impact on the emergence of new topics. Guo et al. (2011) proposed a model that looked at three different indicators of emergence. They used frequency of keywords, growing number of authors, and interdisciplinarity of cited references. The last indicator is computed using the year-average Rao-Stirling diversity index (Rao, 1982; Stirling, 2007). Their results show that the emergence of new topics is consistent with the pattern in which bursts of keywords are followed by the rapid growth in the number of authors and by an increase in the interdisciplinarity of cited references. 

Bettencourt et al. (2009) also examined co-authorship networks to identify patterns associated with the emergence of new research fields. In particular, they observed three main patterns, such as: (i) the average number of edges per node increases, meaning that the network around such nodes is becoming denser, (ii) the average path length between two nodes remains stable or decreases, if the diameter of the network is changing, and (iii) there is an increase in the number of edges in 

52 

the largest component. These patterns can all be seen as indicators of an increased connectedness within the co-authorship network. Therefore the emergence of a new community of scholars is considered as an indicator of emerging topics. 

#### **Co-word approaches** 

Among the approaches using co-word analysis the most representative is from Furukawa et al. (2015). The authors proposed a method which analyses the development of conference networks to indicate the emergence of topics. In particular, using coword analysis, they firstly created a progressive conference network, in which nodes represent conferences, and links represents their similarity in terms of keywords extracted from the published papers. Then, as indicator for emerging topics, they consider conferences that are becoming similar and thus they are collapsing over each other. 

Di Caro et al. (2017) designed an approach for observing how topics evolve over time. After splitting the collection of documents according to different time windows, the approach selects two consecutive slices of the corpus, it extracts topics with LDA, and it analyses how these topics changed from one time window to the other. The main assumption is that when comparing the topics generated in two adjacent time windows, it is possible to observe how topics evolve as well as capture their birth and death. 

Morinaga and Yamanishi (2004) developed an algorithm to detect the emergence of a new topic, employing a probabilistic model called Finite Mixture Model. With this algorithm, the authors dynamically learned the structure of topics from the documents in each year. Then, they analysed the changes in the extracted components to track emerging topics. However, their analysis has not been tested on a collection of scientific documents, therefore it is not clear how it would perform when attempting to forecast the emergence of new research topics. 

53 

#### **Overlay mapping** 

One of the first approaches based on the overlay mapping is from Boyack et al. (2005), who mapped the “backbone of science”. In their approach, they firstly split the corpus along time, and for each time window (i.e., year), they collected clusters of words and associated them to research fields. Then, by observing the clusters in two consecutive years they were able to both match similar topics along time and also identify new clusters related to new topics. In the same way, Leydesdorff et al. (2013) generated overlay maps to support policy makers in locating bodies of research that cross their traditional disciplinary boundaries. These approaches based on overlay mapping can be interesting as they enable users to visually analyse areas with a rapid increase in the number of papers, within the global context of science. However, they are able to provide only a coarse-grained perspective and miss weak interactions between research areas. Indeed, Rafols et al. (2010) advise to use them in combination with other maps providing more detailed perspectives. 

In brief, the state of the art presents several approaches for detecting the emergence of research trends and, like the approaches for topic detection, they can be classified according to the kind of analysis and kind of entities they rely on. Although each approach has its own limitations, these can be generalised with respect to the state of the art as a whole. Approaches based on citation analysis introduce a time lag, which does not allow users to recognise new emerging topics promptly. Approaches using co-word analysis focus on already recognised topics, associated either with a label or, in the case of topics model, with a bag of words. The overlay maps provide a broad perspective of science, however they lose important details that could help in detecting new emerging topic. In addition, all these approaches are able to identify a new topic only after it has emerged. To the best of our knowledge, the state of the art does not offer any approach able to forecast the appearance of new research topics years before they actually emerge. 

54 

## **2.4 Philosophical background** 

The problem of detecting the emergence of new research topics can be framed also within the literature in _Philosophy of Science_ . Philosophy of Science, is a branch of _Philosophy_ , aiming to answer fundamental questions around science and its endeavour, and it deals with the understanding of the evolution of scientific paradigms within a discipline. 

One of the main contributions to this field comes from Thomas Kuhn and his landmark book, _The Structure of Scientific Revolution_ . In this book, Kuhn introduces the concept of paradigm, to express the idea that disciplines are organised around a certain way of thinking, a set of assumptions, legitimate theories or a framework able to explain empirical phenomena in that discipline or field. Indeed, he defines it as “a universally recognized scientific achievements that, for a time, provide model problems and solutions for a community of practitioners” (Kuhn, 1970, page viii). 

Kuhn also describes the dynamics involving the influence of a new scientific discipline as a _paradigm shift_ , in which a revolution in ideas, knowledge and research project can lead to “the successive transition from one paradigm to another via revolution” (Kuhn, 1970, page 12). This kind of phenomena occurs when a paradigm cannot cope with anomalies, which lead to a crisis that will persist until a new outcome redirects research through a new paradigm. Kuhn’s intuition was that science is an alternating of progress and changes. Hence he designed a model, in particular a cycle model, which explains how science evolves. This model consists of three main stages: pre-paradigm, normal science and revolution. 

In the pre-paradigm phase, there are several incompatible and incomplete theories and there is no consensus on them. If a group of scientists concur with some theories, as a new scientific community they build a conceptual framework and ultimately, they disseminate their methods, terminologies and also the kind of experiments that will contribute to the progress in knowledge. 

55 

In the stage of normal science, science progresses within the existing paradigm accumulating knowledge. The research is firmly based upon one or more past scientific achievements, which are acknowledged from a particular scientific community in order to provide the basis for further developments. 

In the revolution phase, the boundaries of the fields are crossed, and some unanswerable questions are discovered. This triggers a crisis derived from the fact that an old paradigm cannot explain some important observations and then the model is no longer capable to solve current problems. The revolution starts when a new paradigm challenges the previous one to encompass explanations and resolve some outstanding and generally recognised problems. The new paradigm settles in when it has a number of influential supporters and thus a new cycle begins all over again. 

As evidence of his claims, Kuhn analysed several historical examples of discovery, especially from the history of _Physics_ with the shift from Newtonian mechanics to Einstein’s special theory of relativity and _Cosmology_ from the Ptolemaic system to the Copernican heliocentrism. 

Kuhn’s work had profound influence on the _History_ , _Philosophy_ and _Sociology of Science_ although it attracted plenty of criticism. However, for what concerns this doctoral work we can take a valuable insight from his work. A scientific field is composed by a set of paradigms, each of them addressesing a different issue. Researchers pursue their research within the defined set of paradigms. When the set of existing paradigms cannot cope with the current challenges, they fall into a crisis, which leads new paradigms to replace the old ones. The emergence of such new paradigms can foster the emergence of a new field. All these dynamics leave trails that can be analysed both on a qualitative level, as done by historians of science (i.e., Kuhn), and on a quantitative level as already performed by Yi and Choi (2012); Upham and Small (2010); Di Caro et al. (2017); Chen et al. (2017) and so on. As an example, we can 

56 

think of an exchange of theories between two not-so-distant scientific fields, which help to create a brand-new paradigm capable of solving recent challenges. 

Another contribution regarding the evolution of science comes from Becher and Trowler and their book _Academic Tribes and Territories_ . In this book, the authors analysed the linkages between academic knowledge (i.e., _territories_ ) and those who inhabit it ( _academic tribes_ ). In particular, when focusing on the different cultures of academics, they argue that the scientific area specifies the characteristics and the structures of the knowledge domain, within which a group of academics place their attitudes, values, activities and cognitive styles (Becher and Trowler, 2001). This line of thought is very similar to Kuhn’s idea regarding the connection between paradigms and scientific communities, stating that “a paradigm is what the members of a scientific community share, and, conversely, a scientific community consists of men who share a paradigm” (Kuhn, 1970, page 176). 

Becher and Trowler concluded that those characteristics of scientific community are quite similar to the social aspects of a tribe, and thus they coined the term “academic tribes”. In addition, citing the work of Clark (1962), they claim that as research fields are proceeding towards specialised environments, scientists across different disciplines have fewer and fewer things in common, in terms of education, experiences and daily problems to cope with. As a result, they become less compatible and less prone to cooperate with each other. However, as the authors also point out, the existing barriers between communities of scholars are not so high, therefore friendly relationships can be established for mutual benefit (Becher and Trowler, 2001). Surowiecki in _The Wisdom of Crowds_ has a similar view, “collaboration allows scientists to incorporate many different kinds of knowledge . . . makes it easier for scientists to work on interdisciplinary problems” (Surowiecki, 2005, page 161). 

Collaboration puts together the efforts of different disciplines and guarantees a diversity in perspectives. This can definitely have a role in reshaping the set of theories 

57 

and methodologies and therefore leading to the emergence of new paradigms, as well as new research areas. 

Here, we want to emphasise that there is a strong connection between groups of academics and their respective fields. In particular, the activities, attributes, and cognitive styles of the former are related to the structures and characteristics of the latter. It is important also to point out that the dynamics involving the different research entities can potentially lead to a new paradigm. Since such dynamics are discoverable and can be analysed, they could theoretically be exploited to forecast a scientific revolution or the emergence of a new topic, when it is still an embryo. In the next section, we will discuss more in detail the embryonic stage as part of the topic lifecycle. 

## **2.5 Embryonic stage** 

Discussing the literature from a philosophical angle helped us to open up new lines of thought in which we could develop interesting hypotheses. In particular, we observed that the social activities of communities of scholars can suggest that the development of new topics is encouraged by the cross-fertilisation of established research areas, and recognised that multidisciplinary approaches foster new developments and innovative thinking. Sun et al. (2013), Osborne et al. (2014) and Price (1986) provided empirical evidence to these theories by analysing the social dynamics of researchers and their effects on the formation and lifecycle of research communities and topics. 

All these theories support the idea of another phase, which we name _embryonic stage_ , occurring before the the _early stage_ , as showed in Fig 1.1 at page 4. In this phase, a topic has not yet been explicitly labelled and recognised by a research community, but it is already taking shape, as evidenced by the fact that researchers from a variety of fields are forming new collaborations and producing new work, starting 

58 

to define the challenges and the paradigms associated with the emerging new area. Kuhn also pointed out that “often a new paradigm emerges, at least in embryo, before a crisis has developed far or been explicitly recognized” (Kuhn, 1970, page 86). 

In fact, it can be argued that a number of topics start to exist in an embryonic way, often as a combination of other topics, before being officially identified and then named by researchers. For example, the _Semantic Web_ emerged as a common area for researchers working on _Artificial Intelligence_ , _World Wide Web_ and _Knowledge-Based Systems_ , before being acknowledged and labelled in the 2001 paper by Berners-Lee et al. (2001). According to Fig. 2.1 at page 29, we can locate the embryonic stage of the _Semantic Web_ in the years before 2001 when different communities of scholars were joining forces to create this new interdisciplinary research topic. 

The existence of the embryonic stage for research topics is crucial because it would allow us to anticipate their emergence. Indeed, in the first study presented in Chapter 3, we empirically confirmed that the existence of this stage can be numerically measured. 

## **2.6 Network-based perspective** 

To tackle the problem of forecasting new research trends, we developed a networkbased approach that looks for topics in the embryonic stage by analysing the patterns of other existing topics. Specifically, we relied on clustering algorithms, that scan the co-occurring networks of topics and identify clusters (i.e., areas of topics) having an intense collaboration. 

In _Network Science_ , these clusters or areas are also called communities and the action of clustering is often referred as community detection (Fortunato, 2010). In this section, we will provide further details to understand the concept of community and how the underlying community structure of a network can be detected. Then 

59 

we will introduce the approach that Augur uses to identify communities within the evolutionary networks. 

### **2.6.1 Community detection** 

Most real-world complex networks are usually organised in compartments or, in other words, areas in which nodes are more connected between themselves than to the rest of the network (Lancichinetti and Fortunato, 2009). These groups of nodes are usually called communities, clusters of cohesive groups or modules that can have their own role and/or function. Community detection can help to explain the organisation of complex networks and their function. 

The idea of communities and in particular social communities is intuitively clear. People tend to form groups with their co-workers, family, and friends. And these groupings have been widely studied for a long time in _Sociology_ (Coleman et al., 1964; Freeman, 2004; Moody and White, 2003) and _Social Anthropology_ (Kottak, 1991; Scupin, 1998). Communities have also been analysed in networks that emerged from fields like _Computer Science_ (Flake et al., 2002; Dourisboure et al., 2007), _Engineering_ (Kahng et al., 2011; Guimer et al., 2005), _Natural Science_ (Guimera and Amaral, 2005; Kepes, 2007; Zhang et al., 2005), _Economics_ (Burt, 2000; Cowan and Jonard, 2004), _Politics_ (Fowler, 2006; Fowler and Jeon, 2008; Zhang et al., 2008; Waugh et al., 2009; Porter et al., 2007) and so on. 

To analyse such networks and detect communities, the state of the art proposes different methods, that are mostly based on tools and techniques imported from other disciplines, like _Computer Science_ , _Physics_ , _Biology_ , _Applied Math_ and _Social Science_ . However, it is always hard to determine which algorithm performs best for a given case, since the concept of community has not been rigorously defined (Fortunato, 2010). Indeed, many algorithms differ from each other because they implement their own definition of community. Their general guideline is, as already mentioned, that a 

60 

community is a connected subnetwork whose nodes have more links to other nodes in the same community than to the nodes that belong to other communities (Radicchi et al., 2004). 

However, even if we cannot know a priori which algorithm to use, the state of the art proposes the notion of _modularity_ as a way to assess the goodness of a given partition (Newman, 2006b). Modularity is a quality function that measures, for each partition, the fraction of links that fall within them versus the fraction one would expect if links were placed randomly. Therefore, high values of modularity suggest that most of the links fall into the partitions rather than in random distributions. Hence these partitions represent potential communities. This indicator has been widely adopted, to the extent that many algorithms for community detection aim to maximise this function, e.g. Edge Betweenness (Newman and Girvan, 2004), Fast Greedy (Clauset et al., 2004), Leading Eigenvector (Newman, 2006a), Spin Glass (Reichardt and Bornholdt, 2006), Louvain (Blondel et al., 2008) and many other versions (Radicchi et al., 2004; Blondel et al., 2008; Brandes et al., 2008). Other methods available in the state of the art that might not directly use modularity are based on spectral analysis (Donetti and Munoz, 2004; Capocci et al., 2005), random walks (Pons and Latapy, 2005), spin-spin interactions (Blatt et al., 1996; Reichardt and Bornholdt, 2004), label propagation (Raghavan et al., 2007) and many other techniques (Arenas et al., 2006; Boccaletti et al., 2007; Long et al., 2007; Papadopoulos et al., 2009). 

Another feature to take into account when detecting communities within networks is the kind of partition. In _Network Science_ , a partition is defined as the division of the network in an arbitrary number of clusters, such that each node belongs to only one clusters. This is called _crisp_ partitioning. However, a node is rarely confined into a single community. For instance, in social networks an individual can belong to different communities consisting of family, friends, co-workers, old schoolmates and 

61 

so on. Other individuals from the same communities can in turn belong to other communities, making the network a space of intertwined overlapping communities. This partitioning is instead called _fuzzy_ . 

Overlapping communities are not limited to social networks. As Osborne et al. (2013) pointed out, in a scientific collaboration network, researchers can belong to different communities of scholars because they might be involved in multidisciplinary collaborations. Also, in biological networks we can observe that different clusters of diseases overlap because the same genes are often involved in different disorders (Barab´asi et al., 2011). We can argue that also in topic networks, and by extension, evolutionary network, is possible to observe a similar phenomenon given that a topic can be involved in the process of fostering the emergence of more than one new area. 

The state of the art proposes different algorithms that can detect overlapping communities. The most popular is the Clique Percolation Method proposed by Palla et al. (2005), which has been extended so that it can work for weighted networks (Farkas et al., 2007) and directed networks (Palla et al., 2007b). Other algorithms are the Link Clustering (Ahn et al., 2010; Evans and Lambiotte, 2009), the Fuzzy C-Means (Bezdek, 1981; Zhang et al., 2007), and others (Baumes et al., 2005; Nepusz et al., 2008). 

As part of assessing the validity of our approach (see evaluation in, Chapter 5), we compared our results against some approaches, such as Fast Greedy (Clauset et al., 2004), Clique Percolation Method (Palla et al., 2005), Fuzzy C-Means (Bezdek, 1981), and Leiden Eigenvector (Newman, 2006a), which failed to provide a good characterisation of the community structure within the evolutionary networks. However, those experiments allowed us to learn some interesting peculiarities of the evolutionary networks. This understanding allowed us to design the Advanced Clique Percolation Method, which extends the Clique Percolation Method (Palla et al., 2005), and works much better on this task. 

62 

## **2.7 Limitations of existing methods** 

In Section 2.3, we presented an overview of the main approaches and directions for detecting topics and tracking their evolution. As discussed, a good number of methods deal with the detection of new emerging topics, but they can be applied only on already emerged topics, associated either with a label or a bag of words. Indeed, they can identify topics that _recently_ emerged, and exhibit dynamics related to their adoption by a research community, e.g., a good number of publications containing a keyword and a new pattern in the citation graph. On the other hand, the state of the art is still missing a comprehensive solution for detecting topics that are _about to_ or _will_ emerge. 

In Section 2.4, we observed the literature with another lens, discussing the evolution of science from a philosophical perspective. There is a significant body of knowledge claiming that the emergence of new scientific fields is tied to the dynamics of group of scholars that exchange theories and methodologies. This form of collaboration can be analysed and it has great potential for supporting the detection of new emerging topics. 

To sum up, on the one hand we have the currently available approaches, which are unable to identify new topics before their actual emergence, but on the other hand we a have solid philosophical background suggesting that is possible to spot clear signs of evolutionary stages that can lead to the emergence of a new topic. 

In the following chapter, we will elaborate on how to close the gap and specifically design an approach that is able to take into account the aforementioned philosophical insights for detecting new topics at an embryonic stage. 

63 

# **Part II** 

# **AUGUR** 

In ancient Rome, a religious official who observed natural signs, especially the behaviour of birds, interpreting these as an indication of divine approval or disapproval of a proposed action. 

Today, an automatic system that observes natural signs, especially the behaviour of topics, interpreting these as an indication of the emergence of new areas. 

64 

# **Chapter 3** 

# **First study: analysis of dynamics** 

## **3.1 Introduction** 

The goal of our research is to detect the emergence of new research topics. In the previous chapter, we contextualised the topic and we analysed its anatomy (Section 2.1). Then, we observed the different life stages it goes through. We found also a number of interesting theories in _Philosophy of Science_ (Herrera et al., 2010; Sun et al., 2013; Nowotny et al., 2013; Kuhn and Hawkins, 1963; Becher and Trowler, 2001), supporting the idea that the life of a research topic starts with an _embryonic stage_ . Specifically, in this stage, a topic has not yet been explicitly labelled and recognised by a research community, but it is already taking shape, as evidenced by the fact that researchers from a variety of fields are forming new collaborations and producing new work, starting to define the challenges and the paradigms associated with the emerging new area. For this reason, we hypothesise that topics can actually be detected in such phase. 

Hence, our research question is: “ **How we can detect new emerging topics at the embryonic stage?** ” 

65 

In Section 2.5, we mentioned that the development of new topics is usually fostered by the cross-fertilisation of established research areas. Therefore, to try to answer the question above, we can analyse the _dynamics_ of the “procreators” or “ancestors” of new emerging topics. In particular, we can analyse the interactions between topics and those between entities linked to these topics, such as publications, authors, venues. For example, the sudden appearance of some publications concerning a combination of previously uncorrelated topics may suggest that some pioneer researchers are investigating new possibilities and maybe shaping a new emerging area. 

In this chapter, we present a study that aims to uncover key elements associated with the research dynamics preceding the creation of novel topics. In particular, we compare the pace of collaboration and the network density within sections of the cooccurrence graph associated to new emerging topics (treatment set) and established topics (control set). Our results show that the pace of collaboration and the density measured in the sections of the network that will give rise to a new topic are significantly higher than those in the control set. Furthermore, these findings support our hypothesis that the existence of an embryonic phase can be numerically measured and also yield new empirical evidence consistent with the already available theories in _Philosophy of Science_ . 

The results, and in general the overall study, presented in this chapter have led to two articles: 

- (Salatino and Motta, 2016) at SAVE-SD workshop co-located with The Web Conference (once World Wide Web conference) and 

- (Salatino et al., 2017) published by PeerJ Computer Science. 

The raw data, which include the list of both emerging and established topics as well as their procreators is available at `https://osf.io/bd8ex/` . 

66 

The remainder of the chapter is organised as follows. In Section 3.2 we describe the data we will use to carry out our experiments. In Section 3.3, we describe the group of topics upon which we performed our analysis. In Section 3.4, we describe the dynamics that we aim to investigate. Then, we describe the experimental approach consisting of two main steps: 

- Step 1. **Selection phase** , described in Section 3.5, in which we select the emerging topics and their counterpart as control set. Then for each topic we select and extract the portion of network related to them, prior to their emergence. 

- Step 2. **Analysis phase** , described in Section 3.6, integrates statistics and semantics, and aims to analyse the differences within the networks extracted for the two groups of topics. To measure the two dynamics this phase uses two methods: 

   - Step 2.a. Cliques for measuring the **pace of collaboration** , described in Section 3.6.1 

   - Step 2.b. Triad-census for measuring the **network density** , which is described in Section 3.6.2 

Finally, we evaluate and discuss our results, we highlight some limitations and we summarise the main conclusions. 

## **3.2 Dataset** 

In this section, we briefly describe the Rexplore dataset (Osborne et al., 2013) which includes different metadata mainly in the field of _Computer Science_ . Then, we will describe some network datasets we will use to carry out our experiments. 

67 

### **3.2.1 Rexplore** 

Rexplore<sup>1</sup> is a web application that combines large-scale data mining, data visualisation and semantic technologies to explore and make sense of the research environment. In particular, Rexplore offers an advanced graphical interface, including a variety of innovative and fine grained visualisations, which support users in: (i) performing advanced search using a variety of parameters, on authors, papers, research areas and research group; (ii) investigating how research communities develop in time, whether they merge, split, grow, contract and so on; (iii) exploring the research trajectory of researchers, in terms of their main areas of interest and contributions in time, as shown in Fig. 3.1; (iv) identifying a variety of interesting relations between researchers, e.g., recognising authors who share similar research trajectories; (v) detecting important trends in research, such as, significant migrations of researchers from one area to another, (vi) classifying book collections, authors, conferences and other research entities according to the associated research topics. 



**Figure 3.1:** Screen capture of Rexplore while looking at the research trajectory of the renowned _Artificial Intelligence_ researcher James A. Hendler. 

> 1Link to Rexplore: `https://technologies.kmi.open.ac.uk/rexplore/` . 

68 

Rexplore builds on a very large collection of data that integrates scholarly data from major commercial publishers, including _Scopus_ , _Springer_ and _Microsoft Academic Search_ . 

At the moment, the Rexplore corpus includes metadata on 16 million papers and 11 million authors, mostly covering the field of _Computer Science_ , and partially other fields like _Biomedics_ . This metadata describes different attributes of research papers, e.g., titles, abstract, keywords, number of citations, references, venues and many others, as well as information about from authors, such as name, organisation, number of citations, h-index and so on. 

Rexplore relies also on the Computer Science Ontology, to represent the different topics the scientific papers are associated with. 

In the following sections, we will describe in more detail some segments of the Rexplore dataset that we have used in our experiments. In particular, we will describe the co-occurence network and the semantic-enhanced topic network. 

### **3.2.2 Co-occurrence network** 

The co-occurrence network, or simply _keyword network_ , is a graph<sup>2</sup> describing the interaction between keywords. Specifically, the co-occurrence network connects the different keywords, used by authors to tag their papers, and this connection is determined by the amount of scientific publications in which they appear together (i.e., co-occur) in a particular year. The Rexplore dataset contains a co-occurrence network per each year _t_ , and naturally the amount of co-occurrences between a couple of keyword can change over time. Therefore, it is possible to perform a diachronic analysis to understand whether the interaction between particular keywords is increasing or 

> 2There is a subtle distinction between graph and network. _Network_ is generally a concept, like network of web documents, while a _graph_ is the mathematical representation of a network. Throughout this dissertation we will use them interchangeably. 

69 

decreasing. In more detail, the co-occurrence network is a fully weighted graph, as described in Eq. 3.1. 



In particular, _V_ is the set of keywords while _E_ is the set of links representing the co-occurrences between keywords. The node weights in _p_ represent the number of publications in which the keyword appears in year _t_ , while the link weights in _w_ is equal to the number of publications in which two keywords co-occur together in the same year _t_ . The union of all these co-occurrence graph over time represents the whole collection co-occurrence networks, as showed in Eq. 3.2. 





**Figure 3.2:** Size of 16 co-occurrence networks from 1995 to 2010. The number of keywords correspond to the number of nodes in _V_ and the number of co-occurrences correspond to the number of links in _E_ . 

In Fig. 3.2 we reported the number of unique keywords (light blue line), for each year from 1995 to 2010, which are also the nodes of the co-occurrence network. In addition, we reported the number of links (black line) between these keywords 

70 

which correspond to the amount of interactions in terms of co-occurrences between keywords. 

### **3.2.3 Semantic-Enhanced Topic Network** 

The _Semantic-Enhanced Topic Network_ , also referred to simply as _topic network_ , is a network that represents the interactions between research topics. This network is the result of a semantic enhancement of the co-occurrence network using the Computer Science Ontology. 

CSO allowed us to filter out all keywords that do not refer to research areas, i.e., “case study”, “error”, “methodology”, and so forth. Furthermore, using the _relatedEquivalent_ relationship from the ontology, we were able to aggregate different keywords representing the same concept. For example, it has been possible to aggregate keywords like “semantic web”, “semantic web technology” and “semantic web technologies” in one single semantic topic. It also allowed us to associate a keyword to a related acronym, e.g., “resource description framework” and “rdf”, or even more complex associations, e.g., “fuzzy c mean”, “fuzzy c-means (fcm)”, “fuzzy c-means”, “fuzzy c means clustering”, “fuzzy c-means clustering”, “fuzzy c-means algorithms” and “fuzzy c-means algorithm”. 

More formally, like the co-occurrence network, the topic network is also a fully weighted graph, as described in Eq. 3.1. As before, the set of nodes _V_ represents topics while _E_ is the set of links representing the topic co-occurrences. The node weight in _p_ represents the number of publications in which the topic appears in the year _t_ , while the link weight in _w_ is equal to the number of publications in which two topics co-occur together in the same year _t_ . 

In Fig. 3.3 we show the number of unique topics (light blue line), for each year from the 1995 to 2010, which are also the nodes of the topic network. In addition, we 

71 



**Figure 3.3:** Size of 16 topic networks from 1995 to 2010. The number of topics correspond to the number of nodes in _V_ and the number of co-occurrences correspond to the number of links in _E_ . 

also show the number of links (black line) between these topics, which correspond to the amount of collaborations between these topics. 

## **3.3 Testing topics** 

With this study, we want to understand whether the emergence of a new research topic can be encouraged by new intense collaborations among its related topics, presumably its “ancestors”. To this end, we randomly selected a set of 75 new topics in the decade 2000-2010, so that we can aim to select their procreators and understand their dynamics, in the years prior to their emergence. This group of topics is also referred as the _treatment set_ . A topic emerges in the year, also called _year of debut_ , in which its label first appears in a research paper. Although the process of selecting emerging topics was completely random, we aimed at having a balanced number of topics over the years. In this way, we avoided the emergence of a bias due to the time in which they were analysed. 

72 

For the sake of comparison, as a control set, we selected a set of 100 established topics (also referred to as the _non-debutant group_ ) and assigned them a random _year of analysis_ within the decade 2000-2010. A topic is considered established if: i) it debuted before 2000, so that it can be in its recognised phase at the time when we analyse the emerging topics, ii) it appears in the CSO Ontology, iii) it is associated each year with a substantial and consistent number of publications. As an instance, Fig. 3.4 shows the evolution over time of the well-established topic _Software Agents_ , in terms of number of active authors and publications. 



**Figure 3.4:** Evolution of the topic _Software Agents_ in terms of number of authors and number of publications per year. The chart has been produced using the Rexplore system. 

The figure shows that the topic made its debut in 1993 and in the year 2000 reached a rate of over 500 publications per year with more than 1500 authors working on it. It can thus be considered established in the context of our study. 

Table 3.1 compares topics in both treatment and control sets, showing when they emerged and in which years we performed their analysis. 

**Table 3.1:** Comparing year of debut and year of analysis for both treatment and control sets. 

|**Testing topics**|**Emerging**|**Year of analysis**|
|---|---|---|
|Debutant topics|2000-2010|_year of debut_ (2000-10)|
|Non-debutant topics|before 2000|randomly assigned in decade 2000-10|



73 

Both treatment and control sets are crucial for this analysis. In particular, investigating the dynamics within the sections of networks associated with the two sets and comparing their results allow us to understand whether the investigated dynamics are exclusive for the emerging topics or they appear in both sets. In this way, we can provide further evidence to the existence of the embryonic stage. 

## **3.4 Pace of collaboration and network density** 

For this study, we hypothesise that the existence of an embryonic phase can be measured and that it is possible to detect new topics within this stage by analysing the dynamics of existent topics which presumably are also their ancestors. In particular, the dynamics we aim to investigate are the pace of collaboration and network density. 

As already mentioned in the previous chapter, collaboration between scientists of different disciplines is a key driving force for the scientific enterprise. Indeed, collaboration makes it easier to work on interdisciplinary problems, allows researchers to incorporate different kinds of knowledge and guarantees diversity in perspective. To this end, we consider collaboration as the central core of our investigation and we analyse both increase in the pace of collaboration between topics and also the creation of brand-new collaborations over time. 

The analysis of the pace of collaboration between two or more topics aims to observe whether the topics are strengthening their ties. In particular, if the percentage of papers shared by these topics is increasing it means that these topics are increasing their collaboration and they are getting closer to each other. In addition, this growing closeness between topics can eventually lead to a new interdisciplinary field. For instance, it is well-acknowledged that the communities interested in _Artificial Intelligence_ , _World Wide Web_ and _Knowledge Based Systems_ started to collaborate on novel ideas, giving rise to a novel research area later labelled _Semantic Web_ by 

74 

Berners-Lee et al. (2001). In Section 3.6.1, we will observe in more detail how we compute the pace of collaboration between the ancestors of a debutant topic. 

On the other hand, to observe whether topic networks are expanding in time and therefore whether within the network some topics are introducing new collaborations, we use the notion of network density. This is important because the fact that a number of authors from previously unrelated research communities or topics are starting to collaborate together may also suggest the emergence of a new interdisciplinary research area. In Section 3.6.2, we will show a method for evaluating the creation of new collaborations between topics. 

## **3.5 Selection phase** 

The selection phase is the first step of the study and, as already mentioned, it aims to select and extract portions of the topic networks that are related to topics of both treatment and control set, in a few years prior to the year of analysis. Afterwards, the analysis phase (in Section 3.6) will analyse the differences within the networks belonging to the two sets, suggesting the dynamics that may be involved in the process of creation of a new topic. 

In our previous study (Salatino and Motta, 2016), we firstly analysed two wellknown topics, _Semantic Web_ (debuting in 2001) and _Cloud Computing_ (debuting in 2006), so that we could tune our approach, and then we tested 50 topics debuting in the period between 2000 and 2010 and 50 non-debutant topics. Here we report a follow-up study, in which this set of topics has been extended to 75 topics debuting in the same period and 100 non-debutant topics (Salatino et al., 2017). In particular, from 50 debutant topics, in the treatment set, we iteratively added new topics until we reached 75 topics and data saturation (Fusch and Ness, 2015), to the extent that the results of the analysis did not significantly vary with the inclusion of new data 

75 

points. On the other hand, for the control set, we randomly assigned another year of analysis to each topic, with the consequence of doubling the amount of non-debutant topics (from 50 to 100). 

After selecting the testing topics (topics in both groups), we can proceed with selecting and extracting the portion of network related to them. We assume that a new emerging topic will continue to collaborate with the topics that contributed to its creation for a certain time after its debut. Indeed, as part of the nurturing phase, its procreator will still collaborate with the emerging topic until it reaches its maturity. This assumption was also discussed and tested in a previous study (Osborne and Motta, 2012), where it was used to find historical subsumption links between research areas. Being able to select the procreators of a given topic allows us to analyse the dynamics involved in their interactions before the new topic emerged. 

To this end, for each debutant topic we firstly selected its 20 most co-occurring topics from the year of debut to 2014 and then we extracted the portion of topic networks containing such topics in the five years preceding the year of debut. For instance, if a topic _A_ made its debut in 2003, we analyse the portion of network containing its most co-occurring topics in the 1998-2002 timeframe. However, since we want to analyse how the dimension of these subgraphs can influence the results, we also tested solutions with 40 and 60 most co-occurring topics. We repeated the same procedure on the topics in the control set, using the year of analysis we randomly assigned (within the decade 2000-2010), rather than their actual year of debut. The workflow representing this approach is showed in Fig. 3.5, while its pseudocode is available in Code 1. 

In brief, the selection phase associates to each topic in both treatment and control sets a graph _G_<sup>_topic_</sup> , shown in Eq. 3.3. 



76 

This graph _G_<sup>_topic_</sup> corresponds to a section of collaboration networks related to a debutant topic in the five years prior to its emergence (or year of analysis for nondebutant topics). In particular, each year corresponds to the induced subgraph of the topic networks (see Section 3.2.3) containing its _n_ most co-occurring topics (or procreators _Vyear_<sup>_topic_</sup> _−i_<sup>),thelinksbetweenthem</sup><sup>_E_</sup> _year_<sup>_topic_</sup> _−i_<sup>,andalsobothnodeandlink</sup> weights ( _Pyear_<sup>_topic_</sup> _−i_<sup>and</sup><sup>_W topic_</sup> _year−i_<sup>,asreportedinEq.3.4).</sup> 





**Figure 3.5:** Workflow representing all the steps for the selection phase. 

The networks associated to the debutant topics included 1,357 unique topics, while the ones associated to the control set included 1,060 topics. 

77 

**Code 1:** Extracting the portion of topic networks associated to topics in both <u>treatment and control set.</u> 

**Input :** List of Testing Topics _db.topics_ and _ndb.topics_ **Output:** Networks containing their ancestors _db.networks_ and _ndb.networks_ **def function** `ExtractNetwork(` _topic, year_ `) /* returns networks */` related.topics _←_ SelectCoOccurringTopics(topic, from=year, to=2017); **for** _yr ←_ ( _year −_ 5) **to** _year_ **do** ancestors.network[yr] _←_ InducedSubgraph(related.topics,year); **end for** return(ancestors.network); **end definition** `// Algorithm starts here` **foreach** _topic in db.topics_ **do** year _←_ GetYearOfSoftDebut(topic); db.networks[topic] _←_ ExtractNetwork(topic,year); **end foreach foreach** _topic in ndb.topics_ **do** year _←_ AssignRandomYear(from=2000, to=2010); ndb.networks[topic] _←_ ExtractNetwork(topic,year); **end foreach** 

## **3.6 Analysis phase** 

In this second phase, we assess the dynamics in the graphs associated to both the two sets with two approaches: cliques-based and triad-based. The first approach, described in Section 3.6.1, measures the pace of collaboration and in particular it transforms the graphs in 3-cliques, then it associates to each of them a measure reflecting the strength of collaboration between relevant topics, and finally it analyses how these collaborations change over time. The second approach, described in Section 3.6.2, evaluates the differences between the graphs associated to the two sets by measuring the changes in the graph density using the triad census technique (Davis and Leinhardt, 1967). We devote the following subsections to describe the two mentioned approaches, while their results will be evaluated in Section 3.7. 

78 

### **3.6.1 Pace of collaboration through cliques** 

In this first approach, we measure the pace of collaboration of the graphs associated to the topics, in both treatment and control sets, by analysing the diachronic activity of triangles of their collaborating topics. To this end, we firstly extract all 3-cliques from the five sub-graphs associated to each topic under analysis. A 3-clique, as shown in Fig. 3.6, is a complete sub-graph of order three in which all nodes are connected to one another. A 3-clique plays an important role in many applications (Eppstein et al., 2010) since it can model small groups of entities close to each other (Luce and Perry, 1949). 



**Figure 3.6:** An instance of a 3-clique containing node _{A, B, C}_ with node weights _{pa, pb, pc}_ and link weights _{wab, wbc, wca}_ . 



**Figure 3.7:** Main steps of the analysis phase. 

To study the dynamics preceding the debut of each topic, we analyse the evolution of the same 3-clique in subsequent years. Figure 3.7 summarises the process. 79 

Considering a 3-clique having nodes _{A, B, C}_ , we quantify its _collaboration index µ_ ∆ in a year by taking into account both node weights _{pa, pb, pc}_ and link weights _{wab, wbc, wca}_ . 



The index _µ_ ∆ is computed by aggregating the three coefficients _µ_ ( _A−B_ ), _µ_ ( _B−C_ ) and _µ_ ( _C−A_ ) as illustrated by Eq. 3.5. The _strength of collaboration µ_ ( _x−y_ ) between two nodes of the topic network, _x_ and _y_ , is computed as the mean of the conditional probabilities _P_ ( _y|x_ ) and _P_ ( _x|y_ ), where _P_ ( _y|x_ ) is the probability that a publication associated with a topic _x_ will be associated also with a topic _y_ in a certain year. The advantage of using conditional probabilities instead of the number of co-occurrences is that the value _µ_ ( _x−y_ ) is normalised to the number of publications associated to each topic. Finally, _µ_ ∆ is computed as the mean of the strengths of collaboration of the three links in a 3-clique. In our previous experiment (Salatino and Motta, 2016), we found that the harmonic mean provides better results than the arithmetic mean. The evolution of the 3-clique collaboration pace can be represented as a timeline of values in which each year is associated with its average strength of collaboration, as in Eq. 3.6. We assess the increase of the collaboration pace in the period under analysis by computing the slope of the linear regression of these values. 



Initially, we tried to determine the increase in the collaboration pace exhibited by a clique by simply taking the difference between the first and last values of the timeline ( _µ_ ∆yr _−_ 5 _− µ_ ∆yr _−_ 1). However, as reported in (Salatino and Motta, 2016) this method 

80 

ignores the other values in the timeline and can thus neglect important information. For this reason, we applied instead the linear interpolation method on the five measures using the least-squares approximation to determine the linear regression of the time series _f_ ( _x_ ) = _αx_ + _β_ . The slope _α_ , showed in Eq. 3.7, is then used to assess the increase of collaboration in a clique. In particular, _<u>µ</u>_ ∆yr represents the mean value of the five collaboration indices within _µ_<sup>_clique_</sup> ∆time<sup>,</sup> _<u>year</u>_ is the mean value of all the years the extracted cliques refer to _{yeart, yeart−_ 1 _, yeart−_ 2 _, yeart−_ 3 _, yeart−_ 4 _}_ , and _yeart−i_ is the instance value from that set. 

When _α_ is positive the degree of collaboration between the topics in the clique is increasing over time, while, when it is negative, the number and intensity of collaborations are decreasing. 



Finally, the overall pace of collaboration associated to each sub-graph (and therefore each testing topic) is measured by computing the average of all slopes associated with the timelines of 3-cliques. 

In brief, for each testing topic we select a subgraph of related topics in the five years preceding the year of debut (or _analysis_ for topics in the control set). We then extract the 3-cliques and associate each of them with a vector representing the evolution of their pace of collaboration. The trend of each clique is computed as the angular coefficient of the linear regression of these values. Finally, the increase in the pace of collaboration of a subgraph is obtained by averaging these values. 

81 

### **3.6.2 Density of network using triad census** 

The second approach employs the _triad census_ (Davis and Leinhardt, 1967) to measure the change of topology and the increasing density of the subgraphs during the five year period. The triad census of an undirected graph, also referred as _global 3- profiles_ , is a four-dimensional vector representing the frequencies of the four isomorphism classes of triad, as shown in Fig. 3.8. The triad census summarises structural information in networks and is useful to analyse the structural properties of social networks. It has been applied to several scenarios, such as identifying spam (Kamaliha et al., 2008; O’Callaghan et al., 2012), comparing networks (Prˇzulj, 2007), and analysing social networks (Faust, 2010; Ugander et al., 2013). 



**Figure 3.8:** The four isomorphism classes of triad. The triad census consists in counting the frequencies of _Hi_ of the input graph. 

In this study, we use triad census to describe all the sub-graphs _G_<sup>_topic_</sup> _year−i_<sup>associated</sup> to a input topic in terms of frequencies of _Hi_ (see Fig. 3.8 and then evaluate how the frequencies of _empties_ ( _H0_ ), _one edges_ ( _H1_ ), _two-stars_ ( _H2_ ) and _triangles_ ( _H3_ ) change in time. Figure 3.8 illustrates the four classes of triads for an undirected graph in the case of topic networks. An increase in the numbers of triangles suggests the appearance of new collaboration clusters among previously distant topics. Differently from the previous approach, the triad census treats the topic networks as binary graphs. It does not consider the weight of the links, but only their existence. Hence, it is useful to assess how including links with different strengths affects the analysis. To this end, we performed three experiments in which we considered only links associated with more than 3, 10 and 20 topic co-occurrences. 

82 

We initially perform the triad census over the five graphs associated to each input topic. For example, Table 3.2 shows the results of the triad census over the five sub-graphs associated with the debutant topic _Artificial Bee Colonies_ . 

**Table 3.2:** Frequencies of _Hi_ obtained performing triad census on the debutant topic _Artificial Bee Colonies_ 

|**Graph**|_H_0|_H_1|_H_2|_H_3|
|---|---|---|---|---|
|_G_<sup>_topic_</sup><br>(_year−_5)<br>|446|790|807|882|
|_G_<sup>_topic_</sup><br>(_year−_4)<br>|443|854|915|1064|
|_G_<sup>_topic_</sup><br>(_year−_3)<br>|125|486|967|1698|
|_G_<sup>_topic_</sup><br>(_year−_2)<br>|100|410|908|1858|
|_G_<sup>_topic_</sup><br>(_year−_1)|68|486|849|2251|



Next, we check whether the co-occurrence graph was becoming denser by analysing the change of frequencies associated with _Hi_ (see Fig. 3.9). We first calculate the percentage growth of each _Hi_ (Eq. 3.8) and then compute their weighted summation (Eq. 3.9), here labelled _growth index_ . We empirically tested other solutions for aggregating the various contributions (e.g., considering only _H_ 3, summing the values, weighing the sum in a variety of ways) and found that the use of a growth index provides the best discrimination between the two classes of graphs. 





Although, we can argue that the number of triangles ( _H_ 3) can by itself be a fair indicator of the density, the _growth index_ , showed in Eq. 3.9, takes into account all the isomorphism classes. Indeed, previous studies by (Faust, 2010; Holland and Leinhardt, 1976) have shown that all four classes of triads are useful for computing useful properties of the network, including transitivity, intransitivity and density. 

83 

Considering only _H_ 3 might fail to detect some subtler cases, characterised for example by a contemporary increase of _H_ 2 and decrease of _H_ 1 and _H_ 0. 



**Figure 3.9:** Development in time of the frequencies of _Hi_ in the network related to the emergence of _Artificial Bee Colonies_ . 

In brief, this approach receives the same input as the previous. For each of the five subgraphs associated to a topic, we perform the triad census obtaining the different frequencies _Hi_ in different years. We then analyse them diachronically to quantify the increase in density. 

## **3.7 Evaluation** 

In a recent paper (Salatino and Motta, 2016), we reported the results of a preliminary evaluation that allowed us to fine tune the final approach for measuring the pace of collaboration. In particular, we focused on two well-known topics such as _Semantic Web_ and _Cloud Computing_ and the results of such approach allowed us to select the best methods for determining the strength of collaboration in Eq. 3.5 (by means of harmonic mean) and the pace of collaboration in Eq. 3.6 (using the least-squared method). 

84 

In this section, instead, we want to focus on the results obtained with the two previously discussed approaches using 75 debutant topics in the treatment set and 100 non-debutant topics in the control set. 

### **3.7.1 Measuring the pace of collaboration** 

We applied the cliques-based method, described in Section 3.6.1, on the subgraphs associated to topics in the treatment and control sets. Figure 3.10 reports the results obtained by using subgraphs composed by the 20, 40 and 60 topics with the highest co-occurrence. Each bar shows the mean value of the average pace of collaboration for the debutant (DB) and non-debutant (NDB) topics, while the thin vertical lines represent their range of values. The results support the initial hypothesis: the pace of collaboration of the cliques within the portion of network associated with the emergence of new topics is positive and higher than the ones of the control set. Interestingly, the pace of collaboration of the control set is also slightly positive. Further analysis revealed that this behaviour is probably caused by the fact that the topic network becomes denser and noisier in time. 

Since the pace of collaboration shows significant changes within the period considered, we studied its behaviour across the 2000-2010 interval. Figure 3.11a, 3.11b and 3.11c, show the yearly average of collaboration pace when considering the 20, 40 and 60 most co-occurring topics. In all cases, the collaboration pace for the debutant topics is higher than the one for the control set. We can also notice that in the last five years the overall pace of collaboration suffered a fall for both debutant and non-debutant topics. As outlined above, this may also be due to the fact that the topic network became denser and noisier in the last years of the analysed period. Moreover, the most recent debutant topics often have an underdeveloped network of co-occurrences, which may result in a suboptimal selection of the group of topics to be 

85 



**Figure 3.10:** Average collaboration pace of the sub-graphs associated to the treatment (DB) and control set (NDB), when selecting the 20, 40 and 60 most co-occurring topics. The thin vertical lines represent the ranges of values. 

analysed in the previous years. Therefore, simply selecting the 20 most co-occurring topics may not allow us to highlight the real dynamics preceding the topic creation. 

With the null hypothesis: “ _The differences in the pace of collaboration between the debutant topics and topics in the control set result purely from chance_ ”, we ran Student's t-test on the sample of data provided by this approach, to verify whether the two sets belong to different populations. The test yielded _p <_ 0 _._ 0001 which allowed us to reject the null hypothesis<sup>3</sup> . In particular, assuming that there are no differences between the two distributions, then there is less than 0.01 probability that a difference like this (at least as extreme as this) will be observed. 

The results of the Student's t-test also suggest that the experiment involving the 60 most co-occurring topics, represented in Fig. 3.11c, provides a better discrimination 

> 3We consider _p <_ 0 _._ 0001 as a conventional statistical representation to indicate an extremely high statistical significance ( _>_ 500 times stronger than the conventional 0.05 threshold for claiming significance). It includes all mathematical outcomes below 0.0001, which are essentially equivalent in assessing excellent significance. 

86 







<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->





<!-- Start of picture text -->
(c)<br>cliques<br><!-- End of picture text -->

**Figure 3.11:** Average collaboration pace per year of the sub-graphs related to input topics in both debutant and control sets considering their 20 (a), 40 (b) and 60 (c) most co-occurring topics. The year refers to the year of analysis of each topic. 

of debutant topics from non-debutant ones. For the sake of completeness, in Table 3.3 we report the p-values yielded by each experiment. 

As an example, Table 3.4 compares the collaboration pace of 23 debutant topics with the collaboration pace of the control set in the same year. We can see how the appearance of a good number of well-known topics, which emerged in the last decade, was anticipated by the dynamics of the topic network. 

In conclusion, the results confirm that the portions of the topic network in which a novel topic will eventually appear exhibit a measurable fingerprint, in terms of increased collaboration pace, well before the topic is recognised and labelled by researchers. 

87 

**Table 3.3:** P-values obtained performing the Student's t-test over the distributions of both debutant and control sets considering their 20, 40 and 60 most co-occurring topics. The best result is in bold. 

|**Experiment**|**p-value**|**Associated chart**|
|---|---|---|
|20 most co-occurring topics|4_._22_·_10<sup>_−_2</sup>|Fig. 3.11a|
|40 most co-occurring topics|6_._84_·_10<sup>_−_2</sup>|Fig. 3.11b|
|**60 most co-occurring topics**|4_._64_·_10<sup>_−_45</sup>|Fig. 3.11c|



### **3.7.2 Measuring the network density** 

We applied the triad-based methods, described in Section 3.6.2 on the subgraphs composed by the 60 most co-occurring topics, since this configuration provided the best outcomes in previous tests. We performed multiple tests by filtering links associated with less than 3, 10 and 20 co-occurrences, to understand how collaboration strength influences the outcome. 

Figure 3.12a reports the average value of the growth indexes when discarding links with less than 3 co-occurrences. The approach allows us to discriminate well the portion of networks related to debutant topics from the ones related to the control set. In particular, the density of network associated with the debutant topics is always higher than its counterpart. Figure 3.12b and 3.12c report the results obtained by removing links with less than 10 and 20 co-occurrences. 

With the null hypothesis “ _The differences in growth index between the debutant topics and topics in the control set result purely from chance_ ”, we ran Student's t- test over the two distributions of growth indexes, for all three experiments. For each experiment, the test yielded _p <_ 0 _._ 0001 allowing us to reject the null hypothesis. Assuming that there are no differences between the growth-indexes of both sets of topics, then there is less than a 0.01 probability that a difference like this (at least as extreme as this) will be observed. More details about the computed p-values per each experiment performed in this triad-based study can be found in Table 3.5. 

88 

**Table 3.4:** Collaboration pace of the sub-graphs associated to selected debutant topics versus the average collaboration pace of the control set in the same year of debut. 

|**Topic (year of debut)**|**Collaboration**<br>**Pace**|**Standard**<br>**Collaboration**<br>**pace**|
|---|---|---|
|Service discovery (2000)|0.455|0.156|
|Ontology engineering (2000)|0.435|0.156|
|Ontology alignment (2005)|0.386|0.273|
|Service-oriented architecture (2003)|0.360|0.177|
|Smart power grids (2005)|0.358|0.273|
|Sentiment analysis (2005)|0.349|0.273|
|Semantic web services (2003)|0.349|0.177|
|Linked data (2004)|0.348|0.250|
|Semantic web technology (2001)|0.343|0.147|
|Vehicular ad hoc networks (2004)|0.342|0.250|
|Mobile ad-hoc networks (2001)|0.342|0.147|
|P2p network (2002)|0.340|0.145|
|Location based services (2001)|0.331|0.147|
|Service oriented computing (2003)|0.331|0.177|
|Ambient intelligence (2002)|0.289|0.145|
|Social tagging (2006)|0.263|0.192|
|Community detection (2006)|0.243|0.192|
|Cloud computing (2006)|0.241|0.192|
|User-generated content (2006)|0.240|0.192|
|Information retrieval technology (2008)|0.231|0.057|
|Web 2.0 (2006)|0.224|0.192|
|Ambient assisted living (2006)|0.224|0.192|
|Internet of things (2009)|0.221|0.116|



Similarly to the previous experiment, we used the results of the Student's t-test to understand among the three tests which one could provide better discrimination between the two classes of topics. In particular, the results in Table 3.5 suggest that the experiment in which we discard links with less than three co-occurrences provides a better discrimination of debutant topics from non-debutant ones. This suggests that considering weak connections is more beneficial for discriminating the two groups. Regarding the peak in the year 2004, we performed a qualitative investigation, which allowed us to determine that its presence is mostly caused by the debut of a number of 

89 

topics associated with particularly strong underlying dynamics, such as _Linked Data_ , _Pairing-based Cryptography_ , _Microgrid_ and _Privacy Preservation_ . 







<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->





<!-- Start of picture text -->
(c)<br><!-- End of picture text -->

**Figure 3.12:** Average growth index per year of the sub-graphs related to the topics in both debutant and non-debutant groups considering their 60 most co-occurring topics and filtering links having with less than 3 (a), 10 (b) and 20 (c) publications. 

**Table 3.5:** P-values obtained performing the Student’s t-test over the distributions of both debutant and control sets considering their 60 most co-occurring topics filtering links having with less than 3, 10 and 20 publications. The best result is bolded. 

|**Experiment**|**p-value**<br>**Ass**|**ociated chart**|
|---|---|---|
|**less than 3 publications**|6_._43_·_10<sup>_−_16</sup><br>Fig.|3.12a|
|less than 10 publications|1_._69_·_10<sup>_−_11</sup><br>Fig.|3.12b|
|less than 20 publications|3_._52_·_10<sup>_−_10</sup><br>Fig.|3.12c|



Table 3.6 shows a selection of debutant topics and their growth indexes compared with the growth index of the control set in the same year. If we compare this table 

90 

to Table 3.4, we can see that the two methods used in this study reflect the same dynamics. 

Hence, the results from this second experiment confirm our initial hypothesis too. In addition, per Table 3.5, the results from the t-test also suggest that the first experiment, which ignores the links associated with less than 3 publications, better discriminates the two populations. 

**Table 3.6:** Growth indexes of sub-graphs associated to selected debutant topics versus the average growth index of the control set in the same year of debut (Standard Growth Index). 

|**Topic (year of debut)**|**Growth Index**|**Standard**<br>**Growth Index**|
|---|---|---|
|Service discovery (2000)|290.29|35.97|
|Ontology engineering (2000)|207.22|35.97|
|Ontology alignment (2005)|399.60|186.89|
|Service-oriented architecture (2003)|628.07|140.17|
|Smart power grids (2005)|637.53|186.89|
|Sentiment analysis (2005)|354.10|186.89|
|Semantic web services (2003)|439.85|140.17|
|Linked data (2004)|590.81|289.94|
|Semantic web technology (2001)|465.53|72.71|
|Vehicular ad hoc networks (2004)|859.44|289.94|
|Mobile ad-hoc networks (2001)|87.31|72.71|
|P2p network (2002)|305.28|18.92|
|Location based services (2001)|595.90|72.71|
|Service oriented computing (2003)|422.92|140.17|
|Ambient intelligence (2002)|308.34|18.92|
|Social tagging (2006)|429.77|157.69|
|Community detection (2006)|583.21|157.69|
|Cloud computing (2006)|695.79|157.69|
|User-generated content (2006)|485.89|157.69|
|Information retrieval technology (2008)|552.14|227.02|
|Web 2.0 (2006)|387.42|157.69|
|Ambient assisted living (2006)|940.79|157.69|
|Internet of things (2009)|580.33|167.86|



91 

## **3.8 Examples** 

The results of this first study also allowed us to get interesting insights on the creation of some well-known research topics. In particular, analysing the most promising cliques extracted within the selected networks related to the debutant topics we can have a glimpse of the main areas that most certainly contributed to their emergence. In the following, we will focus on _Semantic Web_ , _Deep Learning_ and _Cloud Computing_ as examples. 

### **3.8.1 Semantic Web** 

Within the network associated to the _Semantic Web_ , we can locate the cliques which exhibited the steepest slope, which are listed in Table 3.7. We can see that _Semantic Web_ was anticipated in the 1996-2001 timeframe by a significant increase in collaboration of the _World Wide Web_ area with topics such as _Information Retrieval_ , _Artificial Intelligence_ , and _Knowledge Based Systems_ . This is consistent with the initial vision of the _Semantic Web_ , defined in the 2001 by the seminal work of Tim Berners-Lee (Berners-Lee et al., 2001). However, there are other topics that surely have played a role in this dynamic, such as _Knowledge Representation_ and _Search Engines_ . 

In Fig. 3.13 there is a snapshot of the network that shows the pace of collaboration between the active research areas that contributed to the emergence of the _Semantic Web_ . 

### **3.8.2 Deep Learning** 

In Fig. 3.14 there is a snapshot of the network that shows the pace of collaboration between the active research areas that contributed to the emergence of _Deep Learning_ . In Table 3.8 we show the most active collaborations that eventually led to the emergence of this research area. In particular, we can see that the most active areas 

92 

**Table 3.7:** Ranking of the cliques with highest slope value for the _Semantic Web_ . 

|**Topic 1**|**Topic 2**|**Topic 3**|**Slope**|
|---|---|---|---|
|world wide web|information retrieval|search engines|2.529|
|world wide web|user interfaces|artificial intelligence|1.125|
|world wide web|knowledge based systems|knowledge representation|0.982|
|world wide web|artificial intelligence|knowledge representation|0.974|
|world wide web|information retrieval|metadata|0.897|
|world wide web|user interfaces|knowledge representation|0.885|
|world wide web|knowledge based systems|artificial intelligence|0.84|
|world wide web|information retrieval|websites|0.834|
|websites|metadata|information services|0.822|
|user interfaces|search engines|websites|0.812|





**Figure 3.13:** Network suggesting the emergence of the _Semantic Web_ in the years prior its emerging. The thickness of an edge reflects the pace of collaboration between the nodes it connects. The size of a node reflects the centrality of the node in this small-world network. 

93 

include _Neural Networks_ , _Classification_ , _Pattern Recognition_ , _Object Recognition_ and so on. 



**Figure 3.14:** Network envisioning the emergence of the _Deep Learning_ . The thickness of an edge reflects the pace of collaboration between the nodes it connects. The size of a node reflects the centrality of the node in this small-world network. 

**Table 3.8:** Ranking of the cliques with highest slope value for the _Deep Learning_ . 

|**Topic 1**|**Topic 2**|**Topic 3**|**Slope**|
|---|---|---|---|
|classification|pattern recognition|feature extraction|1.156|
|learning systems|classification|pattern recognition|1.043|
|classification|object recognition|feature extraction|1.038|
|learning systems|classification|feature extraction|0.986|
|learning algorithms|classification|feature extraction|0.953|
|learning algorithms|classification|pattern recognition|0.920|
|learning algorithms|object recognition|feature extraction|0.879|
|neural networks|learning algorithms|classification|0.843|
|neural networks|learning systems|classification|0.819|



94 

### **3.8.3 Cloud Computing** 

_Cloud Computing_ , as we can see from Table 3.9, was anticipated by an increase in the collaboration between topics such as _Grid Computing_ , _Web Services_ , _Distributed Computer Systems_ , _Information Management_ , _Quality of Service_ and _Internet_ . Figure 3.15 shows the network that represents the main interactions between the topics that fostered the emergence of _Cloud Computing_ . 



**Figure 3.15:** Network envisioning the emergence of the _Cloud Computing_ . The thickness of an edge reflects the pace of collaboration between the nodes it connects. The size of a node reflects the centrality of the node in this small-world network. 

95 

**Table 3.9:** Ranking of the cliques with highest slope value for the _Cloud Computing_ . 

|**Topic 1**|**Topic 2**|**Topic 3**|**Slope**|
|---|---|---|---|
|grid computing|distributed computer systems|web services|1.252|
|quality of service|distributed computer systems|web services|1.245|
|grid computing|distributed computer systems|resource allocation|1.131|
|internet|quality of service|web services|1.087|
|grid computing|distributed computer systems|quality of service|1.036|
|grid computing|quality of service|resource allocation|1.007|
|web services|distributed computer systems|information management|0.991|
|internet|distributed computer systems|web services|0.886|
|grid computing|quality of service|web services|0.879|
|quality of service|resource allocation|web services|0.812|
|quality of service|information management|web services|0.805|



## **3.9 Discussion and limitations** 

In this study, we analysed the topic networks with the aim of experimentally confirming our hypothesis that the emergence of new research areas is anticipated by an increased interaction of pre-existing topics. We examined the pace of collaboration (via the cliques-based method described in Section 3.6.1) and the change in topology (via the triads-based method described in Section 3.6.2) in portions of the network related to debutant topics, showing that it is possible to effectively discriminate areas of the topic graph associated with the future emergence of new topics. The first approach showed that the subgraphs, associated with the emergence of a new topic, exhibit a significantly higher pace of collaboration than the control set of subgraphs associated with established topics. Similarly, the second approach showed that the graphs associated with a new topic display a significantly higher increase in their density than the control set. We can thus confirm that these two dynamics are good indicators for detecting embryonic topics. 

96 

Interestingly, the ability of these two approaches in discriminating the debutant graph from the control set varies with the time interval considered. Looking at the best results obtained for both experiments, it appears that the cliques-based approach (Fig. 3.11c) works better in the first years of the decade (2000-2004), while the triadsbased method (Fig. 3.12a), performs better in the central period (2004-2007). As a possible future work, we can try to better understand whether these behaviours are associated with specific characteristics of the network. In addition, we also intend to explore other dynamics correlated with the emergence of new research topics. Indeed, we believe that pace of collaboration and network density are just two of a variety of dynamics that could be exploited to understand the patterns that precede the emergence of research topics. These dynamics may involve also other dimensions such as authors (e.g., a rise in the number of experts working on a certain combination of topics), venues (e.g., the creation of interdisciplinary workshops), citations and other scholarly entities, including new collaborations between two or more research communities (Osborne et al., 2014) or a significant change in the vocabulary associated with relevant topics (Cano-Basave et al., 2016), and so on. 

Ultimately, the results of these two experiments allow us to effectively discriminate specific sections of the topic networks and suggest that a significant increase in the rate of collaboration between existing topics provides a strong indicator for predicting the emergence of new research areas. Indeed, these dynamics could be used as the starting point for developing new automatic methods, which could detect the emergence of a new research topic well before this becomes explicitly recognised and established. However, while these results are satisfactory, our analysis presents some limitations, which we shall address in the next study. 

In particular, we identified the relevant subgraph during the selection phase simply by selecting the _n_ most co-occurrent topics of the topic under analysis. This solution allows us to compare graphs of the same dimension, however it introduces three issues. 

97 

First of all, it assumes that all topics derive from the same number of research areas, which is an obvious simplification. Emerging topics may have a different nature, based on their origin, development patterns, interactions of pioneer researchers, and so on. Therefore, each of them will be linked to a different number of established research areas. A manual analysis of the data suggests that using a constant number of co-occurring topics is one of the reasons why the overall pace of collaboration and growth index associated with the emergent topics are not much higher than the ones of the control set. When selecting too many co-occurring topics, we may include less significant research areas or, alternatively, research areas that started to collaborate with the topic in question only after its emergence. Conversely, when selecting too few topics, the resulting graph may exclude some important ones. 

A second limitation is in the selection of the procreators. In this study, for each topic, we selected the most co-occurring topics, from its year of debut to 2014. We can argue that with such approach, we can fetch topics that not necessarily are considered its procreators. Indeed, as we already mentioned, each new emerging topic can have a different development pattern. And, if the debutant topic becomes mature enough to form new intense collaborations with other topics, those topics might also be part of the most co-occurring ones and be wrongly classified as ancestors. In addition, if a debutant topic helps to foster new areas, these new areas can also belong to the most co-occurring topics, since it is likely that they will have an intense collaboration, as part of the nurturing phase. To this end, considering the ancestors as only the topics which collaborated the most, can definitely be a limitation. A possible solution is to classify the relationship between the emerging topic and each most co-occurring topic by observing their pattern of collaboration, and then select only the topics that have a very closed relationship with the emerging topic in its first period of life. 

Lastly, the selection phase performed in our study cannot be reused in a system capable of automatically detecting embryonic topics, since it requires knowledge of the 

98 

set of topics with which the embryonic topic will co-occur in the future. However, this could be fixed by developing techniques that are able to select promising subgraphs according to their collaboration pace and density. The application of this technique in a realistic setting would however require a scalable method for identifying promising topic graphs. Indeed, the approach developed in our second study (see next chapter) generates an evolutionary graph in which: i) links are weighted according to the pace of collaboration between the two relevant topics and ii) community detection algorithms are applied to select portions of the network characterised by an intense collaboration between topics. We expect that this solution will be able to detect at a very early stage that “something” new is emerging in a certain portion of the topic graph, even if it may not be able to accurately define the topic itself. It would thus allow relevant stakeholders to react very quickly to developments in the research landscape. 

## **3.10 Conclusions** 

In this study, we hypothesised that research topics go through an embryonic stage, in which, while they are not yet consistently labelled or associated with a considerable number of publications, they can nonetheless be detected by analysing the dynamics between already existing topics. 

To confirm this hypothesis, we performed an experiment on 75 debutant topics in _Computer Science_ , which led to the analysis of a topic network including about 2000 topics extracted from a sample of 3 million papers in the 2000-2010 time interval. 

The results confirm that the creation of novel topics is anticipated by a significant increase in the pace of collaboration and density of the portions of the networks in which they will appear. These findings provide contributions of potential value to research in _Philosophy of Science_ . Firstly, they support our hypothesis that the 

99 

embryonic stage is part of the topic lifecycle and it can be measured numerically. Secondly, they bring new empirical evidence to fundamental theories in _Philosophy of Science_ , which are concerned with the evolution of scientific disciplines, e.g., Herrera et al. (2010), Kuhn (1970), Nowotny et al. (2013), and Sun et al. (2013). Lastly, they highlight that new topics tend to be born in an environment in which previously less interconnected research areas start to cross-fertilise and generate new ideas. This suggests that interdisciplinarity is one of the most significant forces that drives innovation forward, allowing researchers to integrate a diversity of expertise and perspectives, and yielding new solutions and new scientific visions. Hence, the results of our analysis could be used to support policies that promote interdisciplinary research. 

The next step is to exploit the dynamics discussed in this study to create a fully automatic approach for detecting embryonic topics. This approach will crawl the different topic networks and reveal areas within them exhibiting such dynamics. The aim is to produce a robust method to be used by researchers and companies alike for gaining a better understanding of where research is heading. In the next chapter, we present our second study that develops such an automatic approach, showing how we propose to solve the scalability issue and how we locate the dynamics within the networks. 

100 

# **Chapter 4** 

# **Second study: early detection of topics** 

## **4.1 Introduction** 

In the previous chapter, we described the first study aiming to discover some interesting dynamics between established research topics that could be used to forecast the emergence of a new research area. In addition, this study gave us new insights on how science evolves which are consistent with Kuhn’s vision of the scientific revolution. We explored these findings to design a second study aiming to effectively detect the emergence of new research topics. 

For the first study, we took advantage of some prior knowledge: we knew which research areas emerged and when (year of debut). We then selected some of their co-occurring topics, which could be considered as their ancestors, and performed an analysis to detect the most promising dynamics, i.e., pace of collaboration and network density prior to their emergence, which anticipated the emergence of new research areas. A representation of this pipeline can be found in Fig. 4.1. 

101 

The second study, instead, walks this flow backwards. Knowing that certain dynamics exist and can be measured, we aim to effectively detect the emergence of new research areas. In particular, the resulting algorithm crawls the different topic networks and locates clusters (i.e., groups of topics) where there is an overall increase of the pace of collaboration. 



**Figure 4.1:** Workflow for the first study in Chapter 3 (forward) and for this study (backward). 

However, this approach brings new challenges, such as ensuring its effective computability. In the first study, given a debutant topic, the analysis was located within small portions of the network containing its related topics, in the five years prior its emergence. Similarly, in this second study, we assume that the dynamics involving the development of a new research topic can be observed in the five years prior to its emergence. To this end, the designed algorithm will have to process five complete topic networks at once, each one representing one year. For instance, to discover the emerging topics in 2003, the algorithm will investigate dynamics that developed in the lustrum 1998-2002, as represented in Fig. 4.2. However, this poses several challenges because even the processing of a singles topic network, considering its dimension in terms of number of nodes and connections between nodes (see Section 3.2.3), is computationally expensive (Lancichinetti and Fortunato, 2009). Therefore, processing five topics networks at once can easily lead to scalability issues. In addition, as Fortunato (2010) points out, the analysis of dynamic networks (i.e., topic networks), in which nodes and links appear and disappear over time, is hard and in its infancy. 

102 



**Figure 4.2:** Representation of both input and output of the second study. On the left there are the topic networks that will be processed in search of interesting subnetworks, while on the right there are the matched debutant topics. The dashed circles within the topic networks represent clusters of interest that are analysed over time and can potentially lead to the emergence of new research topics. 

In this chapter, as part of our second study, we propose a way to effectively predict research trends. This approach is called _Augur_ , whose workflow is depicted in Fig. 4.3 and consists of three main stages: 

- Stage 1. **Creating Evolutionary Networks** . Augur takes in input the topic networks and converts them into evolutionary networks, which are static representations of the dynamicity of the topics networks that compress multiple topic networks into one (see Section 4.2); 

- Stage 2. **Clustering** . This involves locating within such evolutionary networks, areas or groups of topics that exhibit an increase of the pace of collaboration (see Section 4.3); 

- Stage 3. **Post-Processing** . This stage further enhances the outcome with information regarding active authors and relevant papers. This in- 

103 

formation can be useful for the user to make sense of the results (see Section 4.4). 

In brief, the aim of Augur is to return a set of clusters for a given year that could eventually lead to the emergence of new research areas in the following years. In addition, each cluster will be associated with additional information, such as active authors and relevant papers. This study alongside its results, which will be described and evaluated in the next chapter, have been presented at the 18th ACM/IEEE Joint Conference on Digital Libraries (Salatino et al., 2018a). 



**Figure 4.3:** Workflow of Augur. 

## **4.2 Evolutionary networks** 

The main objective of this study is to provide an algorithm that explores sequential topic networks and provides as output groups of topics exhibiting an increase in the pace of collaboration. A na¨ıve solution would start with identifying some interesting clusters (or subnetworks) from the topic network in _yeart−_ 4. This can be simply done either extracting all the 3-cliques, as already performed in the first study, or employing some clustering algorithm that can aggregate a larger set of topics based on their topology. Once all the clusters from that topic network ( _yeart−_ 4) have been 

104 

registered as initial set, the algorithm would proceed iteratively in the following networks ( _yeart−_ 3, _yeart−_ 2 and so on). This could be accomplished by matching clusters in different years and modifying the initial set of clusters depending on whether the topics contained in each cluster are increasing their collaboration or not. This approach is depicted in Fig. 4.2, where clusters are identified by blue dashed circles and matched with straight dashed lines along time. However, this approach poses several challenges: i) as already mentioned, processing five topic networks in one iteration is computationally expensive; ii) since topics are extremely dynamic and can develop new relationships in time, it is difficult to match the same cluster in two consecutive years — indeed also Fortunato (2010) argues that techniques for such analysis are still premature; and iii) the algorithm would need to take into account the possibility that a set of topics start their collaboration in the middle of the time-frame ( _yeart−_ 4, _yeart_ ), let’s say from the topic network _yeart−_ 2. In this section, we propose the notion of evolutionary network as a solution that can cope with all these challenges. 

An evolutionary network is a network that gathers information from different topic networks and uses the pace of collaboration to represent the gradual development of topics and their relationships over time. Positioning the cursor over a particular year, the evolutionary network will provide a view over a set of topics and their interaction in recent years. In the previous study, we observed that five years can be enough to observe the dynamics preceding the emergence of a new area. In this study we make a similar assumption and let the evolutionary network contemplate a similar timespan. For instance, the evolutionary network of the year 2000 will contain a snapshot of the interactions between topics in the years (1996, 2000), while the evolutionary network of 2001 will show the interaction of topics from 1997 to 2001, and so on. In brief, an evolutionary network will provide information on topics and how their collaboration evolved in the last five years and this helps to cope with the aforementioned challenges. In particular, considering that one evolutionary network can represent the interactions 

105 

of topics in a period of five years, the algorithm can work on one network at once rather than five. Indeed, the aim is to locate clusters of topics within the evolutionary network, where there is an overall increase in the pace of collaboration, rather than in the five topic networks. This approach allows us also to address the second challenge, since the clusters returned from the evolutionary graph will already represent the areas in which there is an increase of the pace of collaboration. Finally, since the evolutionary network takes into account the pace in which the relationships between topics evolved, topics that started a collaboration later in the timespan will also be part of the evolutionary network, so that the algorithm can process also their interaction. Here follows the formal representation of the evolutionary graph and how it is mined from the five topic networks that it includes. 

As any other network, an evolutionary network can also be mathematically represented by a graph as showed by Eq. 4.1. 



The evolutionary graph _G_<sup>_evol_</sup> _yeart_<sup>isthenafullyweightedgraphcomposedby</sup><sup>_V_</sup> _year_<sup>_evol_</sup> _t_ which is the set of vertices, _Eyear_<sup>_evol_</sup> _t_<sup>thesetofedgesthatconnectthosevertices,while</sup> _p_<sup>_evol_</sup> _yeart_<sup>and</sup><sup>_w_</sup> _year_<sup>_evol_</sup> _t_<sup>aretheweightsrespectivelyforthesetsofverticesandedges.How-</sup> ever, since the evolutionary network is generated taking into account five topic networks, there is a function that maps these topic networks (also represented by graphs, _G_<sup>_topic_</sup> _yeart_<sup>,asdefinedinSection3.2.3)intoanevolutionarynetwork,asshowedinEq.</sup> 4.2. 



106 

This mapping between the topic networks and the evolutionary networks is also depicted in Fig. 4.4. 

To ensure that all the topics and their interactions are included in the evolutionary network, both the set of vertex _Vyear_<sup>_evol_</sup> _t_<sup>andthesetofedges</sup><sup>_E_</sup> _year_<sup>_evol_</sup> _t_<sup>needtoincludeall</sup> nodes and edges of the five topic networks. To this end, the algorithm needs to select the unique set of different topics _Vyear_<sup>_topic_</sup> _t_<sup>within the topic networks, as well as the unique</sup> set of all edges _Eyear_<sup>_topic_</sup> _t_<sup>within the different topic networks.These sets will also include</sup> nodes that perhaps appeared only in one of the five topic networks and edges that connected two nodes only once out of five. Once the set _Vyear_<sup>_evol_</sup> _t_<sup>and</sup><sup>_E_</sup> _year_<sup>_evol_</sup> _t_<sup>havebeen</sup> populated, we can proceed in computing the sets _p_<sup>_evol_</sup> _yeart_<sup>and</sup><sup>_w_</sup> _year_<sup>_evol_</sup> _t_<sup>whichreportthe</sup> different values of the pace of collaboration. 



**Figure 4.4:** Representation of the evolutionary network. 

In the first study we defined the pace of collaboration as the rate at which the number of publications two topics share changes in time (see Section 3.6.1). More specifically, the pace of collaboration is the slope _α_ of the line _f_ ( _x_ ) = _αx_ + _β_ that best fits the different collaboration indices ( _µ_ ∆) along time. This line is computed using the linear least-squares regression. 

107 

To compute the link weights of the evolutionary network we use a similar approach. For each edge, we firstly compute the _strength of collaboration_ of all links, according to Eq. 4.3, and then we compute the _pace of collaboration_ , as showed in Eq. 4.4. 

In particular, given a link connecting node _u_ and node _v_ , with Eq. 4.3 we compute the strength of their collaboration ( ˆ _wu,v_<sup>_topic_)byfirstlynormalisingtheweightoftheir</sup> link ( _wu,v_<sup>_topic_)againstthenumberofpublicationsofbothnodes(</sup><sup>_p_</sup> _u_<sup>_topic_</sup> and _p_<sup>_topic_</sup> _v_ ), and then we compute the harmonic mean of these two values. A similar approach has been presented by Eq. 3.5 at page 80. 



Next, with Eq. 4.4, we compute the pace of collaboration ( _wu,v_<sup>_evol_</sup> _year_<sup>)astheslope</sup> of the line that fits the five measures (strength of collaboration) obtained from the same link in the five topics networks. 



In Eq. 4.4, _w_ ˆ _u,v_<sup>_topic_</sup> represents the mean value of the five weights, _<u>year</u>_ is the mean value of all the years the topics networks refer to _{yeart, yeart−_ 1 _, yeart−_ 2 _, yeart−_ 3 _, yeart−_ 4 _}_ , and _yeart−i_ is the instance value from that set. 

In case the instance of an edge is missing in one of the topic networks, perhaps because the two topics did not have any co-occurrence in that year, the strength of collaboration _w_ ˆ _u,v_<sup>_topic_</sup> _year−i_<sup>forthatyearwillbezero.</sup> 

For the sake of completeness, the evolutionary network includes the set of node weights _p_<sup>_evol_</sup> _yeart_<sup>.</sup> These weights report the pace of growth of each node computed according to Eq. 4.5. Also in this case we use the least-squared method. In particular, 

108 

the weight of a given _k-th_ vertex ( _p_<sup>_evol_</sup> _kyear_<sup>)istheslopeofthelinethatbestfitsthe</sup> weights of the same _k-th_ vertex in the different topic networks ( _p_<sup>_topic_</sup> _kyear−i_<sup>).</sup> 



In such equation, _p_<sup>_topic_</sup> _kyear−i_<sup>isthenumberofpublicationsthek-thtopicreceived</sup> in _yeart−i_ , while _p_<sup>_topic_</sup> _k_ is the mean value of all the weights of the same node in the different topic networks or the average value of publications received in that period of five years. In case the instance of a vertex is missing in a topic network ( _yeart−i_ ), implying that for such topic there are zero publications in that year, the weight _p_<sup>_topic_</sup> _kyear−i_ is zero. 

In brief, the evolutionary network _G_<sup>_evol_</sup> _yeart_<sup>canbeseenasastaticrepresentationor</sup> a snapshot of all the dynamics between topics in a period of five years. The network contains all the topics within the topic networks and reports whether or not these topics had a collaboration in this period. In addition, the node weight represents the increase in number of publications on a topic and the link weight the pace of collaboration between two topics. 

## **4.3 Cluster of established topics** 

The creation of evolutionary networks is the first phase of Augur. With it, we move from the domain of collaboration between topics to the domain of dynamics, so that we can focus our attention on detecting areas where there is this intense collaboration between topics. In this step, Augur clusters nodes that exhibit a strong collaboration pace. 

In Section 2.6 we described the concept of community and how the underlying community structure of a network can be detected. To this end, we performed some 

109 

experiments with several community detection algorithms available in literature (see evaluation in, Chapter 5), such as Fast Greedy, Clique Percolation Method and others. However, these algorithms failed to provide a good characterisation of the community structure within the evolutionary networks. Nonetheless, they allowed us to learn some interesting peculiarities of such networks. Indeed, this understanding allowed us to design the Advanced Clique Percolation Method, which extends the Clique Percolation Method (Palla et al., 2005), and works much better on this task. Before proceeding in its description (Section 4.3.2), we will briefly describe the standard Clique Percolation Method. 

### **4.3.1 Clique percolation method** 

The Clique Percolation Method (CPM) is a popular approach for analysing the community structure of networks and belongs to the family of fuzzy community detection algorithms. This approach has been enormously successful in many applications in many domains, such as the examination of social networks (Palla et al., 2007b; Gonz´alez et al., 2007), the analysis of cancer-related proteins in protein interaction networks (Jonsson and Bates, 2006; Jonsson et al., 2006), document clustering (Gao and Wong, 2006) and so on. 

CPM differs from other methods of clustering particularly on its definition of community. Indeed, the community (or _component_ , _k-clique community_ or _k-clique percolation cluster_ ) is defined as the union of all k-cliques that are connected and can be reached from each other across a set of adjacent _k-cliques_ (Everett and Borgatti, 1998; Batagelj and Zaversnik, 2003; Der´enyi et al., 2005). A _k-clique_ is a complete (i.e., fully connected<sup>1</sup> ) subgraph of _k_ vertices and the adjacency between two k- cliques is determined on whether they share _k-1_ nodes (hence, if they differ for only one node). The overall idea of community for the CPM is that it consists of several 

> 1k-cliques have been part also of the first study, in Chapter 3. Indeed, an example of 3-clique is in Fig. 3.6 at page 79. 

110 

complete subgraphs ( _k-cliques_ ) that tend to share many of their nodes. In particular, the Clique Percolation Method consists of two main steps: 

- Step 1. Locating _k-cliques_ within the network 

- Step 2. Creating the clique graph ( _k-clique adjacency graph_ ), in which the vertices represents the _k-cliques_ of the original graph, and there is an edge between two vertices when the two _k-cliques_ are adjacent 

Communities are then defined as the connected components of such graph. For instance, given the network depicted in Fig. 4.5, with _k_ = 3 the algorithm will locate the 3-cliques _{_ 1 _,_ 2 _,_ 3 _}_ , _{_ 1 _,_ 3 _,_ 4 _}_ , _{_ 4 _,_ 5 _,_ 6 _}_ , _{_ 5 _,_ 6 _,_ 7 _}_ , _{_ 5 _,_ 6 _,_ 8 _}_ , _{_ 5 _,_ 7 _,_ 8 _}_ and _{_ 6 _,_ 7 _,_ 8 _}_ . Then the algorithm creates the clique graph, using the clique adjacency matrix (Table 4.1), in which the cliques are connected between themselves when they share two ( _k1_ ) nodes (Everett and Borgatti, 1998). The resulting graph of _k-clique adjacency graph_ in Fig. 4.6, contains two connected components orange and green, which are the two final communities of the network, as reported in Fig. 4.7. In Code 2 there is the pseudocode for the Clique Percolation Method. 



**Figure 4.5:** Example of network. Our goal is to identify all cliques and create the clique graph. 

111 

**Table 4.1:** The overlap matrix. This matrix is viewed as an adjacency matrix whose nodes are cliques of the original network. The elements of the matrix indicate whether pairs of cliques are adjacent (share 2 nodes) or not in the graph. 

||**_{_1,2,3****_}_**|**_{_1,3,4****_}_**|**_{_4,5,6****_}_**|**_{_5,6,7****_}_**|**_{_5,6,8****_}_**|**_{_5,7,8****_}_**|**_{_6,7,8****_}_**|
|---|---|---|---|---|---|---|---|
|**_{_1,2,3****_}_**||1||||||
|**_{_1,3,4****_}_**|1|||||||
|**_{_4,5,6****_}_**||||1|1|||
|**_{_5,6,7****_}_**|||1||1|1|1|
|**_{_5,6,8****_}_**|||1|1||1|1|
|**_{_5,7,8****_}_**||||1|1||1|
|**_{_6,7,8****_}_**||||1|1|1||





**Figure 4.6:** Clique graph or _k-clique adjacency graph_ . The two connected components of this network map into the communities of the original network. 



**Figure 4.7:** The two communities shown in Fig. 4.6 are now mapped on the original network inFig. 4.5. 

112 

**Code 2:** Clique Percolation Method. **Input :** Evolutionary Network _network_ **Output:** Communities _comms_ cliques _←_ FindCliques(network, k=3); adj.mat _←_ matrix(length(cliques),init=0) ; `/* adjacency matrix */` **for** _i ←_ 1 **to** _length_ ( _cliques_ ) **do for** _j ←_ 1 **to** _length_ ( _cliques_ ) **do if** _SharedNodes(cliques[i],cliques[j]) == 2_ **then** `// k-1` adj.mat[i,j] _←_ 1 ; `/* adjacent cliques */` **end if end for end for** clique.graph _←_ GraphFromAdjacencyMatrix(adj.mat); components _←_ FindConnectedComponents(clique.graph); comms _←_ ConvertComponents(components); `/* converts components of cliques in components of topics: communities */` return(comms); 

As we will see in the evaluation chapter (Chapter 5) the Clique Percolation Method is not able to characterise the community structure of the evolutionary networks. In particular, there are two main limitations: 

- Limitation 1. This method does not take into account the link weights, treating them as either they exist or not; 

- Limitation 2. Some areas of the evolutionary networks appear to be particularly dense and the algorithm is unable to split such areas in further communities. 

The first one can be considered as a major weakness, as each link in the evolutionary network represents a different pace of collaboration between the two topics it connects. In the next section we will describe the Advanced Clique Percolation Method, which we developed to overcome these limitations. 

113 

### **4.3.2 Advanced Clique Percolation Method** 

The _Advanced Clique Percolation Method_ (ACPM) is a solution that aims to tackle the limitations of the algorithm described in the previous section. In the first instance, ACPM takes into account the link weights in a refined way, so that also the process of creating the clique graph and locating communities considers such weights. Secondly, this new algorithm redefines the concept of community, to handle the presence of very large communities within the network. 

The Advanced Clique Percolation Method consists of four steps: 

Step 1. Locating _k-cliques_ within the network 

Step 2. Measuring pace of collaboration per _k-cliques_ and filtering noise 

Step 3. Creating the _k-clique adjacency graph_ 

Step 4. Locating local maxima and extracting neighbourhoods 

In the following subsections, we will describe ACPM step-by-step and we will show how we integrated the link weights in Step 2 and how we redefined the concept of community in Step 4. In Code 3 is reported the pseudocode for the Advanced Clique Percolation Method. 

#### **Step 1: Locating k-cliques within the network** 

The first step is similar to the original method as the approach locates all the 3-cliques within the evolutionary network. At this stage, the algorithm explores the topology of the network and gathers together nodes that belong to triangles. In Code 3 this step is accomplished with the first line of code. 

114 

**Step 2: Measuring pace of collaboration per k-cliques and filtering noise** 

The standard clique percolation method works on binary networks (i.e., undirected networks with links without weights) and an arbitrary network can always be converted into a binary network, simply by inducing the graph that contains only those links whose weight is higher than the weight threshold _w_ . Indeed, the standard method uses the link weights only to filter them according to their value, so that it can create the binary network upon which locating the 3-cliques. However, we can argue that filtering the network using a static threshold is not an optimal solution. Considering that we want to promote 3-cliques that show intense activity of collaboration (high pace of collaboration), a link having weight below _w_ can be part of them and thus be still meaningful. 

The same research team that developed the Clique Percolation Method, proposed a new approach that shifts from filtering links to filtering _k-cliques_ based on their intensity (Farkas et al., 2007). After finding cliques, the approach computes the intensity of a clique as the geometric mean of the weights of its links. Then the community or weighted k-clique percolation cluster is considered as the set of adjacent k-cliques having an intensity greater of an intensity threshold _I_ (Onnela et al., 2005). In this way, a k-clique containing weak links (low weights) can be still part of the percolation cluster as long as it contains edges with large weights that help it to exceed the threshold _I_ . 

The Advanced Clique Percolation Method will then use a similar approach and will compute the intensity of 3-cliques after propagating all the links of the evolutionary network. However, rather than computing the geometric mean as done in (Onnela et al., 2005), the algorithm will compute the harmonic mean as already done for the first study in Chapter 3, so that the intensity matches with the pace of collaboration of the 3-clique. 

115 

To this end, for each retrieved clique, the algorithm computes its intensity or pace of collaboration as the harmonic mean of the link weights ( _Wab_ , _Wbc_ , _Wca_ , please refer to Fig. 3.6 at page 79), as showed in Eq. 4.6. 



Next, the algorithm filters some k-cliques that have very low value of pace of collaboration. In Code 3 this step is accomplished from line 2 to 6. 

#### **Step 3: Creating the k-clique adjacency graph** 

ACPM creates the k-clique adjacency graph _G_ = ( _V, E, W_ ). _V_ is the set of vertices representing the identified 3-cliques from the original graph, _E_ is the set of links connecting adjacent k-cliques that share _k-1_ vertices, and _W_ is the set containing the node weights (i.e, pace of collaboration of each clique computed using Eq. 4.6). This step is very similar to Step 2 of the standard clique percolation method (see page 111), with the only difference that ACPM propagates the link weights throughout the different steps. In Code 3 this step is accomplished from line 7 to 19. 

#### **Step 4: Locating local maxima and extracting neighbourhoods** 

In this final step, the algorithm identifies the communities within the evolutionary network. The standard clique percolation method defines communities as connected components of the _k-clique adjacency graph_ , and as we will see in the evaluation chapter (see Chapter 5), it returns very large communities. With ACPM we want to address this limitation by redefining the concept of community. 

When using the standard method, in the literature we can find some solutions that can help to cope with the presence of very large communities, such as those from Palla et al. (2005) and Farkas et al. (2007). However they appear to be unsuitable in the context of this work. 

116 

In particular, Palla et al. (2005) suggest to monitor how communities change, by trying different values of link weights _w_ and tuning the value _k_ for the dimension of cliques. Such analysis produces a similar effect to changing the resolution in a microscope. Indeed, increasing the threshold _w_ leads the communities to shrink and fall apart, as fewer cliques will be formed. Whereas, increasing the dimension of cliques _k_ makes the communities smaller, more cohesive and more fragmented. However, changing the values of _w_ and _k_ is not an optimal solution for two reasons. 

Firstly because, as already mentioned in Step 2, we want to promote 3-cliques that, while having some links with weight below _w_ , still show a high pace of collaboration. Therefore we cannot increase too much the value of _w_ . 

Secondly, if we increase the value of _k_ , communities become more granular, and this prevents smaller cliques from joining a community. By definition, a component (or _k-clique community_ ) contains all adjacent k-cliques and does not include cliques with smaller values of _k_ . For instance, in the network in Fig. 4.5, the node 9 belongs to the 2-clique _{_ 7 _,_ 9 _}_ but does not belong to any community simply because it is not part of any 3-cliques. In this way, increasing _k_ to 4 would mean not including all 3-cliques that do not belong to 4-cliques. Since we acknowledged from the first study (see Chapter 3) that all 3-cliques are important for the analysis of the dynamics of each triad of topics, we cannot raise the number of _k_ to 4. 

In Step 2, we computed the clique intensity (with Eq. 4.6). In the case of very large weighted communities, Farkas et al. (2007) suggest to increase the threshold _I_ and filter more 3-cliques based on their intensity. Indeed, a low intensity threshold allows a large number of k-cliques to participate in clusters, while increasing this threshold prevents the emergence of large modules that could mask the details of smaller communities. However, changing the values of _I_ is not an optimal solution for the following reason. 

117 

Differently from the standard method, the _k-clique adjacency graph_ (or clique graph) _G_ in ACPM is a weighted graph. Indeed, it contains the node weights representing the different values of pace of collaboration of 3-cliques. Therefore, we can imagine this clique graph as a large island with a complex terrain, as showed in Fig. 4.8a. The height of each point on the terrain is defined as the value of their intensity (or pace of collaboration). We can also imagine that the intensity threshold _I_ is the level of water around this island and the action of raising this threshold has the effect of leaving more portion of the landscape underwater. Indeed, as the water raises, more valleys get flooded and the main island splits into smaller islands, as showed in Fig. 4.8b. These new islands (or peaks) are groups of “closely related” vertices (k-cliques) that locally dominate according to the values of their pace of collaboration (Batagelj et al., 2006). However, it is also possible to raise the water high enough to further split the islands but at the same time we can submerge important pieces of landscape or peaks, as showed in Fig. 4.8c. We can argue that for the effective detection of new emerging topics, every peak can be relevant. 

In brief, we can use this threshold to filter out some background noise, such as all the k-cliques that have very low pace of collaboration and that can slow the computation of the algorithm. However, we cannot increase the threshold too much, as some important areas of the clique graph, which are relevant for the effective detection of new emerging areas, can fall below the threshold and be filtered out. 

So far, the state of the art has not provided any effective solution to further split these very large weighted communities. Hence, we need to investigate new solutions, such as redefining the concept of community. 

We are interested in communities as areas of the evolutionary network in which there is an intense collaboration between topics that eventually could lead to the emergence of new topics. As already mentioned, these peaks represent the areas of the network where a set of closely related topics (by means of k-cliques) are exhibit- 

118 









<!-- Start of picture text -->
(a) (b) (c)<br><!-- End of picture text -->

**Figure 4.8:** Approximative representation of the k-clique adjacency graph as island with complex terrain. The sea level represents the filter. With low tide, in (a) the returned network is almost similar to the original one. Increasing the level of the water, as in (b) the network splits in two components. With high tide, as in (c), the network further splits in more components but some of them might be covered. 

ing intense collaboration. We can certainly focus just on the peaks of the network. Therefore, once the algorithm creates the _k-clique adjacency graph_ we can proceed in locating all the peaks and selecting the topics with the most active collaboration, as showed in Fig. 4.9. 



**Figure 4.9:** Graphical representation of the k-clique adjacency graph. Rather than filtering with the sea level, we locate local maxima (peaks). 

In brief, with this fourth step, ACPM aims to identify the communities as peaks of the network. This consists of two main steps: 

119 

- locating the local maxima within the adjacency graph, which in turn consists of: 

   - converting the clique graph into an overlap matrix _M_ , 

   - locating local maxima in the matrix _M_ . 

- selecting their neighbourhoods which contain all the closely related topics that have an intense collaboration. 

Firstly, the algorithm converts the clique graph into an overlap matrix _M_ , according to Eq. 4.7. 



This overlapping matrix _M_ is similar to the adjacency matrix but instead of reporting ones<sup>2</sup> wherever there is a link between the _i-th_ and _j-th_ cliques, it reports the pace of collaboration of the _j-th_ clique ( _Wj_ ). In addition, in the main diagonal, when _j_ = _i_ , the matrix reports the pace of collaboration of _i-th_ clique ( _Wi_ ). To this end, each row _i_ of the matrix _M_ , reports at different positions the pace of collaboration of all the nodes to which the _i-th_ clique is connected, plus its pace of collaboration at position _i_ . In this way, we can analyse from the perspective of each clique (row) whether the clique itself is a maximum. 

Secondly, once the matrix M is created, the algorithm locates the maximum value in each row and its position. If the maximum is positioned in the main diagonal ( _i-th_ row, _i-th_ column) then the _i-th_ clique is a local maximum. This is because, since each row represent the connection that a given clique has, if it exhibits the highest value it means that among the nodes it is connected, it is the local maximum. 

> 2The adjacency matrix of a graph is a matrix with rows and columns labelled by graph vertices, with a 1 or 0 in position ( _Vi, Vj_ ) respectively if _Vi_ and _Vj_ are adjacent or not. 

120 

As the algorithm knows which cliques are considered local maxima, it can proceed with the extraction of their neighbourhoods. To extract the neighbourhood of a given local maximum we can select their ego network. The ego network is a network consisting of a central node ( _ego_ ), the nodes it is directly connected ( _alters_ ), and the ties between them (Freeman, 1982). In the context of this work, an ego network consists of the induced subgraph containing a given local maximum clique and the cliques that are directly connected to it. The size of the neighbourhood or ego network is given by the “order”. When the order is 0, the ego network includes only the ego node. When the order is 1, the ego network includes the ego node plus its immediate neighbours. ACPM extracts the ego network with order 2, meaning that it will contain the ego node, the immediate neighbours and the neighbours of neighbours, and all the links between these cliques. This is because using order 1 might not allow us to observe the phenomenon in its completeness, since we are extracting the local maximum clique and its immediate alters. Using order 2, instead, slightly broadens this space that might contain more nodes and can allow us to locate the topics that are exhibiting an increase of the pace of collaboration. 

As output, ACPM returns the ego networks of cliques converting them into clusters of topics. In Code 3 this step is accomplished from line 19 to 31. 

#### **Difference between CPM and ACPM** 

In brief, the most important differences between CPM and ACPM is that the newly designed approach gives more value to the link weights, rather than simply filtering the links based on a threshold. In addition, the whole concept of community is redefined. Instead of considering communities as connected components of the k- clique adjacency graph that in many occasions can appear very large, it considers communities as the peaks of the network characterised as composition of local areas exhibiting an intense collaboration between topics. 

121 

In the next section, we describe the final result of Augur, i.e. the actual result that the user receive as outcome. In particular, we describe how we post-processed the communities to retrieve the final set of clusters with their topics. In addition, to help the user to understand the results, the algorithm will provide, for each cluster, some relevant authors and papers. 

122 

- **Code 3:** Advanced Clique Percolation Method. **Input :** Evolutionary Network _network_ , Threshold _threshold_ **Output:** Communities _comms_ 

- **1** cliques _←_ FindCliques(network, k=3); 

- **2 for** _i ←_ 1 **to** _length_ ( _cliques_ ) **do 3** poc.cliques[i] _←_ PaceOfCollaboration(cliques[i]) 

- **4 end for** 

- **5** cliques _←_ cliques[which(poc.cliques _>_ threshold)]; 

- **6** poc.cliques _←_ poc.cliques[which(poc.cliques _>_ threshold)]; 

- **7** m _←_ matrix(length(cliques), init=0) `// overlap mat. initialized with 0` **8** adj.mat _←_ matrix(length(cliques), init=0) `// adjacency matrix` 

- **9 for** _i ←_ 1 **to** _length_ ( _cliques_ ) **do** 

- **10 for** _j ←_ 1 **to** _length_ ( _cliques_ ) **do 11 if** _(i̸_ = _j)_ & _(SharedNodes(cliques[i],cliques[j])_ == _2)_ **then** 

- **12** adj.mat[i,j] _←_ 1 ; `/* adjacent cliques */` **13** m[i,j] _←_ poc.cliques[j] `// according to Eq. 4.7` **14 else if** _j_ == _i_ **then 15** m[i,j] _←_ poc.cliques[i]; 

- **16 end if** 

- **17 end for** 

- **18 end for** 

- **19** clique.graph _←_ GraphFromAdjacencyMatrix(adj.mat); 

- **20** pos.max _←_ MaxPosition(m, mod=”rowwise”) `// find position of max vals` 

- **21** k _←_ 1; 

- **22 for** _i ←_ 1 **to** _length_ ( _pos.max_ ) **do** 

- **23 if** _pos.max[i] == i_ **then 24** local.maxima[k] _←_ i; 

- **25** k _←_ k+1; 

- **26 end if** 

- **27 end for** 

- **28 for** _i ←_ 1 **to** _length_ ( _local.maxima_ ) **do** 

- **29** components[i] _←_ EgoNetwork(clique.graph, local.maxima, order = 2); 

- **30 end for** 

- **31** comms _←_ ConvertComponents(components); `/* converts components of cliques in components of topics: communities */` 

- **32** return(comms); 

123 

## **4.4 From cluster of topics to embryonic topics** 

In the previous sections, we devoted our attention to the main phases of Augur, which are the creation of the evolutionary networks and the clustering of these networks, using the Advanced Clique Percolation Method. However, the results are still far from being conclusive. Indeed, the selection of ego networks from local maximum as community, can draw in links that are not necessarily high in pace of collaboration. To this end it is important to further post-process the results of the previous step. 

In addition, to support the user in making sense of such results, Augur also provides a set of active papers and relevant authors associated to each community. 

### **4.4.1 Cluster aggregation and main topics** 

Given an evolutionary network, the Advanced Clique Percolation Method returns several communities whose topics are involved in an intense collaboration. These communities have been extracted locating the local maxima within the clique graph and then returning their ego network. As already mentioned, the dimension of the ego network strongly depends on the order value, which has been set to 2. However, in this case, the returned communities may contain links of the evolutionary network that not necessarily have high pace of collaboration. Indeed, regardless of its weight, if a link is placed nearby a local maximum it will become part of the community. Furthermore, in very dense zones of the evolutionary network, retrieving an ego networks of order 2 can lead to communities of topics that go from 50 to 200, which is arguably a very large dimension for a community. Therefore, Augur needs to further process these results by removing less significant nodes. 

To this end, we ranked the links within each community according to their pace of collaboration and we observed that their values follow a long-tailed distribution. 

124 

Observing these distributions across all the retrieved clusters, we found that, on average, the pace of collaboration within a cluster significantly drops after 15 links. Therefore, for each community, Augur ranks the links by their weights in descending order and selects the first 15, which potentially embody the most active collaborations between topics. In this way the topics of the final clusters will be the topics that are connected by the selected 15 links. However, since ACPM returns overlapping communities, it can happen that two (or more) clusters share a subset of their topics simply because their mutual topics had the most active collaborations in both communities. Therefore, before returning the result, Augur checks all the clusters removing duplicates and merging clusters that have Jaccard similarity greater than 0.7. An empirical analysis suggested that using 0.7, the two compared sets can be considered almost similar. 

In Code 4 there is the pseudocode for filtering communities. 

**Code 4:** Algorithm for <u>post-processing</u> the clusters of topics. **Input :** List of returned communities _comms_ **Output:** Clusters of topics _clusters_ k _←_ 1; **foreach** _community in comms_ **do** links _←_ GetLinks(community); links _←_ sort(links, descendig = true); links _←_ links[1:15] `// select the first 15 links` clusters[k][topics] _←_ TopicsInLinks(links); clusters[k][links] _←_ links; k _←_ k + 1; **end foreach** 

clusters _←_ RemoveDuplicates(clusters); clusters _←_ MergeClusters(clusters, sim=0.7) `// with similarity above 0.7 /* The result contains information about the most important topics and links that connect these topics */` return(clusters) 

125 

### **4.4.2 Active authors** 

To help the user in making sense of the returned cluster of topics, Augur provides a set of relevant authors. Augur performs an analysis on the five years prior to the detection of the cluster and identifies the authors that are actively publishing in as many topics as possible within the cluster. For instance, if ACPM is identifying the community structure within the evolutionary network of 2001, the analysed topics networks will range from 1997 to 2001. The most active authors for such communities will be selected in the same period. 

Given a cluster in _yeart_ , its most active authors are evaluated based on: 

- **The number of topics and links within the community he or she is actively publishing from** _yeart−_ 4 **to** _yeart_ **.** From Rexplore, it is possible to select the list of authors that were publishing in a topic in a particular time range ( _yeart−_ 4, _yeart_ ). Since an author can belong to different topics, for each author we counted the number of topics he or she was actively publishing in that period. Moreover, we also counted the number of links within the community he or she was part of. For instance, if in that period, an author was active in five research areas of the community, the algorithm will consider him or her as belonging to five nodes and also count the number of links that connect these nodes in the community. This is because an author can be considered more central and active if he or she belongs to as many links as possible within the community (especially those with the highest pace of collaboration). 

- **Cumulative weight according to the link weights of the evolutionary network.** Within the community, different links can have different weights based on the pace of collaboration of the two topics they connect. We can argue that authors belonging to the topics with highest pace of collaboration can be 

126 

the most active. Therefore, for each author, we selected the links connecting the topics, in which he or she published, and we summed up all the link weights. 

- **Number of publications until** _yeart_ **.** We selected for each author the number of papers he or she had published until _yeart_ . This number has been normalised with the number of topics he or she was publishing. 

- **Topics of the community he or she is publishing from** _yeart−_ 4 **to** _yeart_ **.** Information about the topics within the community the author is publishing in the time range ( _yeart−_ 4, _yeart_ ). 

The final output consists of a ranking of the authors based on the number of associated topics (first parameter), then according to the cumulative weight (second parameter). The other two parameters can support the user in identifying other important authors more comprehensively. Code 5 shows the pseudocode for extracting the active authors. 

127 

**Code 5:** Algorithm for selecting the most active authors. **Input :** List of clusters _clusters_ , years in which the clusters have been found _years_ **Output:** List of active authors _inf.authors_ **for** _i ←_ 1 **to** _length_ ( _clusters_ ) **do** topics _←_ clusters[i][topics] `// see Code 4` links _←_ clusters[i][links]; year _←_ years[i] `// year when the cluster was discovered` **foreach** _topic in topics_ **do** authors[topic] _←_ RetrieveAuthors(topic,from=(year-5), to=year); **end foreach** inf.authors[names] _←_ unique(authors); inf.authors[num.topics] _←_ CountTopics(inf.authors[names],topics); inf.authors[num.links] _←_ CountLinks(inf.authors[names],links); inf.authors[cum.weight] _←_ SumWeights(inf.authors[num.links], links); inf.authors[num.publications] _←_ RetrievePublications(inf.authors[names],from=(year-5), to=year); inf.authors[topics] _←_ GetTopics(inf.authors[names],topics); inf.authors _←_ sort(inf.authors, by=(num.topics, num.weight)) **end for** return(inf.authors) 

### **4.4.3 Relevant papers** 

Alongside the most active authors, for a given cluster, Augur provides also a set of relevant papers. These papers are important research outputs that are laying the basis of the new potential area. As per the active authors, also the relevant papers are analysed in the same period of analysis of the evolutionary network that generated such cluster. 

In particular, for a set of topics within the cluster at _yeart_ , the relevant papers are evaluated according to: 

- **The number of topics in which they appear.** From Rexplore, it is possible to select all the papers published within a topic in a time period ( _yeart−_ 4, _yeart_ ). 

128 

Since a paper can describe content belonging to different topics, for each paper we counted the number of topics it is associated with. We then retained the papers that appear at least in two topics. 

- **Cumulative weight according to the link weights of the evolutionary network.** As in the case of active authors, we can argue that the papers belonging to the topics with the highest pace of collaboration can be the most relevant. Therefore, for each paper, we observed the links connecting the topics associated to the paper, and we summed up all their weights. 

- **Weight based on the authors that wrote the paper.** This value considers the number of citation the authors that wrote the paper received at the time the paper was written. This value has then been normalised by the number of its authors. The idea is that a particular paper written by a senior researcher, can push the boundaries towards a new interdisciplinary field. 

- **Number of citations.** Rexplore reports the number of citations a paper received over time. To this end, we summed the number of citations each paper received from the year it has been published (within the range ( _yeart−_ 4, _yeart_ )) until _yeart_ . 

The final output consists of a ranking of relevant publications based on the number of topics they appear (first parameter), then according to the cumulative weight (second parameter). The other parameters can support the user in identifying other important papers more comprehensively. Code 6 shows the pseudocode for selecting the relevant papers. 

129 

**Code 6:** Algorithm for selecting the most relevant <u>papers.</u> **Input :** List of clusters _clusters_ , years in which the clusters have been found _years_ **Output:** List of relevant papers _inf.papers_ **for** _i ←_ 1 **to** _length_ ( _clusters_ ) **do** topics _←_ clusters[i][topics] `// see Code 4` links _←_ clusters[i][links]; year _←_ years[i] `// year when the cluster was discovered` **foreach** _topic in topics_ **do** papers[topic] _←_ RetrievePapers(topic,from=(year-5), to=year); **end foreach** inf.papers[title] _←_ unique(papers); inf.papers[num.topics] _←_ CountTopics(inf.papers[title],topics); inf.papers[num.links] _←_ CountLinks(inf.papers[title],links); inf.papers[cum.weight] _←_ SumWeights(inf.papers[num.links], links); inf.papers[authors] _←_ GetInfoAboutAuthors(inf.papers[title]); inf.papers[num.citation] _←_ RetrieveCitations(inf.papers[title], until=year); inf.papers _←_ sort(inf.papers, by=(num.topics, num.weight)) **end for** return(inf.papers) 

## **4.5 Conclusions: from the approach to the evalu-** 

## **ation** 

In this chapter we introduced Augur, a new framework for the early detection of topics, and we discussed its main components: the evolutionary network and the Advanced Clique Percolation Method (see Fig. 4.3). In particular, thanks to the insights gained from the first study in Chapter 3, we designed the evolutionary network as a way to represent our input data. This strategy allowed us to address the scalability issue associated with the simultaneous computation of several large topic networks. 

In addition, we designed the Advanced Clique Percolation Method, a novel community detection algorithm that could exploit the peculiarities of the evolutionary network and could also cope with the presence of very large communities. 

130 

The next chapter is devoted to the evaluation of Augur, which has a twofold purpose: i) assess its validity, and ii) evaluate the effectiveness of the Advanced Clique Percolation Method against other community detection algorithms, such as Fast Greedy (Clauset et al., 2004), Leading Eigenvector (Newman, 2006a), Fuzzy C-Means (Bezdek, 1981) and the standard Clique Percolation Method (Palla et al., 2005). 

131 

# **Part III** 

# **Evaluation and Conclusion** 

132 

# **Chapter 5** 

# **Evaluation of Augur** 

## **5.1 Introduction** 

In this chapter, we evaluate _Augur_ and other alternative approaches on a gold standard of historical data. In particular, we want to measure to what extent the clusters produced by our approach are effective indicators of the emergence of new topics. As we will see, the approach that provides better results, in terms of precision and recall, is the Advanced Clique Percolation Method. 

More specifically, in the sections that follow: there will be a description of how the evaluation was designed (Section 5.2); and a description of the gold standard (Section 5.3); in particular how it was compared with the returned clusters and the results obtained from the different clustering algorithms with respect to the adopted measures (Section 5.4). We will then see how these results have been improved by means of appropriate filters (Section 5.5) and semantically enhanced (Section 5.6). Finally, we will discuss the obtained results in more detail (Section 5.7). 

The results presented in this chapter have been published at the 18th ACM/IEEE Joint Conference on Digital Libraries (Salatino et al., 2018a). 

133 

The data collected during the evaluation and the gold standard are available at `http://doi.org/10.21954/ou.rd.8281010` 

## **5.2 From the clusters to the evaluation** 

We evaluated Augur by selecting topic networks from the year 1995 to 2009, which yielded 11 evolutionary networks. Table 5.1 reports the complete mapping between topic networks and evolutionary networks. For instance, the evolutionary network of the year 2005 takes into account the topic networks in the years 2001-2005. 

**Table 5.1:** Mapping between _topics networks_ and _evolutionary graphs_ . 

|**Topic Networks of**<br>**the Year**|**Evolutionary**<br>**Graphs of the**<br>**Year**|
|---|---|
|1995-1999|1999|
|1996-2000|2000|
|1997-2001|2001|
|1998-2002|2002|
|1999-2003|2003|
|2000-2004|2004|
|2001-2005|2005|
|2002-2006|2006|
|2003-2007|2007|
|2004-2008|2008|
|2005-2009|2009|



Given the evolutionary networks, we run different community detection algorithms, including the Advanced Clique Percolation Method, to produce the set of clusters that will be then evaluated against the gold standard. Specifically, the evaluation aims to answer the question: “ **How many clusters returned each year by the algorithm effectively indicate a new emerging area?** ” 

To answer this question, it is important to understand how many of the returned clusters, for a given algorithm, map to the ancestors of emerging topics. 

134 

In the first study (see Section 3), we analysed the emergence of a debutant topic using the network of its _n_ most co-occurring topics in the five years prior its emergence. For example, for a topic emerging in 2006, we would analyse the networks from year 2001 to 2005. In the context of this study, instead, we need to reverse this concept and, for instance, if we are analysing topic networks from 2001 to 2005 (evolutionary network of 2005), we can expect that those areas exhibiting such dynamics will lead to the emergence of a new topic in the following year, or at most two years. Indeed, for this evaluation, we will compare the clusters obtained in a given year with the debutant topics of the following two years. To this end, for the gold standard, we included all the topics that emerged in the period 2000-2011. Table 5.2 reports the mappings between the clusters and the debutant topics. As an example, the clusters obtained from the evolutionary network of the 2005, will be compared with the topics that emerged in the years 2006 and 2007. 

**Table 5.2:** Mapping the _evolutionary graphs_ and their clusters with the debutant topics in the subsequent years. For instance, the clusters obtained from the evolutionary network of the 2005 will be compared with the topics emerged in the years 2006 and 2007. 

|**Evolutionary Graph**<br>**and Clusters of the**<br>**Year**|**Debutant Topics of the**<br>**Year**|
|---|---|
|1999|2000-2001|
|2000|2001-2002|
|2001|2002-2003|
|2002|2003-2004|
|2003|2004-2005|
|2004|2005-2006|
|2005|2006-2007|
|2006|2007-2008|
|2007|2008-2009|
|2008|2009-2010|
|2009|2010-2011|



135 

In general, the evaluation consists of finding the match between clusters and debutant topics. This process can also be seen as “labelling” the clusters, in which the cluster receives a label with the name of the topic that is potentially nurturing. 

However, before proceeding with the evaluation, it is important to produce the gold standard, containing the topics that emerged in the year 2000-2011, as reported in Table 5.2. 

In the next section, we will show how we created the gold standard so that we could evaluate both Augur and the different clustering algorithms. 

## **5.3 Gold Standard** 

Very often an evaluation is carried out to compare the results of a given algorithm against a set of results determined a priori to be correct, also known as gold standard. In the context of this work, the results that represent the truth are the debutant topics that emerged from 2000 to 2011. 

This information is already available within the Rexplore database since for each topic, there is information about the year of debut. However, only knowing the emerging topics and their year of debut might not be enough for evaluating the clusters. A domain expert can analyse the interaction of some topics in a certain year and suggest, based on his or her judgement, that such interaction might lead to the emergence of one of the topics beheld by the gold standard. Therefore, the evaluation would need several domain experts with different areas of expertise. This process cannot be achieved in an automatic way, unless we enrich the debutant topics with additional information. 

To automatise the evaluation we need to associate to each debutant topic a set of ancestors, which will be matched against the retrieved clusters. 

136 

In brief, the gold standard designed for this evaluation consists of gathering together the list of emerging topics with their year of debut, as we will see in Section 5.3.1. Then in Section 5.3.2, we will describe how we selected the ancestors for each debutant topic. 

### **5.3.1 Debutant topics** 

The Rexplore corpus is very diverse. It integrates entities of different dimensions such as topics, authors, papers and much more, through different semantic relationships. With this wide variety of interconnections, for a given a topic, one can easily retrieve the number of published papers per year, the number of publishing authors, the year of debut and so on. In particular, Rexplore computes the year of debut for a topic as the year in which the label of that topic has been used for the first time as keyword in a paper. For example, the label of the topic _Cloud Computing_ , according to the corpus in the database, made its first appearance in the year 2006. 

Since the scope of this doctoral work is confined within the _Computer Science_ , to build the gold standard, we initially filtered the set of topics covered by Rexplore. 

Rexplore contains 21772 keywords that made their debut between the years 1990 and 2012, and they cover areas within fields like _Chemistry_ , _Genetics_ , _Biology_ and so on. All these keywords are scattered along time according to the histogram in Fig. 5.1. To filter this large and diverse set of keywords we used the Computer Science Ontology which allowed us to remove both the keywords that do not represent topics and those that do not belong to the _Computer Science_ field. 

After filtering, we then retrieved all the emerging topics that have their year of debut into the range 2000-2011, according to Table 5.2. To minimise the noise that can be caused by the spurious occurrence of the label associated with a topic in the literature, we use the concept of soft debut, in which a topic makes its debut only when it has reached at least 5 publications. As an example, the topic Deep Learning 

137 



**Figure 5.1:** Histogram reporting the number of keywords that had their first appearance (hard debut) in the years between 1990 and 2012. 

makes its first appearance in 2003, and reached five publications in 2005. In this way, we can be more certain that a new label recognised by multiple authors was introduced. We thus computed the soft debut of each topic. After analysing the difference between the original debut (herein labelled hard debut) and the soft debut, it appears that most of the topics have their soft debut at most two years after their hard debut. 

In Fig. 5.2, it is reported a histogram of all the 1,408 topics emerged within the field of _Computer Science_ from 2000 to 2011. 

Unfortunately, the number of debutant topics drastically decreases in the second part of the analysed period. This is probably due to some missing data in our dataset. We still included the years after 2006 in the analysis for the sake of completeness, however this issue prevents us from trusting the results of the evaluation for years 

138 

after 2006. As future work, we plan to analyse other scholarly datasets to provide a gold standard that will cover also more recent years. 



**Figure 5.2:** Histogram reporting the number of topics that had their soft debut in the years between 2000 and 2011. 

Knowing all the debutant topics under the field of _Computer Science_ that emerged in the period between 2000 and 2011, we can proceed in enhancing them with their ancestors as described in the next section. 

### **5.3.2 Extraction of related topics** 

The extraction of related topics is inspired by the selection phase designed in the first study, and described in Section 3.5 at page 75. For each debutant topic, the algorithm aims to select a set of topics, considered its ancestors, that could potentially have helped it to arise as a result of a multidisciplinary interaction. 

In the first study, the main assumption was that a new topic will continue to collaborate with its ancestors for a certain time after its emergence, and the algorithm 

139 

locates these ancestors by selecting the _n_ most co-occurring topics. However, in the closing notes of Chapter 3, we pointed out some drawbacks of this approach. We can argue that for a given topic, selecting the most co-occurring topics, from the year of debut until now, can lead to topics that are not necessarily its ancestors. 

Indeed, if the debutant topic becomes mature enough to form new intense collaborations with other topics, those topics might also be part of the most co-occurring ones and be wrongly classified as ancestors. In addition, if the debutant topic helps to foster new areas, those new areas can also belong to the most co-occurring topics since it is likely that they will have an intense collaboration, as part of the nurturing phase. 

To this end, when generating our gold standard, we consider as ancestors the top 25 topics, which mostly collaborated with the debutant topic during its initial five years of activity, and were already existing when the debutant topic emerged. 

In practice, given a debutant topic, the algorithm firstly selects all the co-occurring topics in its first five years of activity, which are also older than the debutant topic. Then, for each co-occurring topic, we observe its _intensity of collaboration_ by computing the distance between the amount of papers the debutant topics received in the first five years and the amount of papers in which the debutant topics and the related topic appear together. In this way, the algorithm can locate those topics that mostly collaborated with the debutant topic in its first five years of life. 

In detail, considering _⃗Pdt_ (paper vector of the debutant topic) the non-zero vector containing the amount of papers published in the emerging topic in the first five years of activity, and _⃗Cdt,rt_ (collaboration vector of the debutant topic and its related topic) the vector containing the amount of papers the two topics appear together in the same five years, the intensity of collaboration _IoC_ ( _⃗Pdt,⃗Cdt,rt_ ) between a debutant topic and a related topic is the Euclidean distance between these two vectors, as defined in Eq. 

140 

5.1. 



If the distance between the collaboration vector and the paper vector of the debutant topics is close to zero, it means that the debutant topic and the related topic had a very intense relationship in the first five years of life of the debutant topic and that the related topic had a major role in shaping the debutant topic. Therefore, we can consider this related topic as ancestor. 

By contrast, if the distance between the collaboration vector and the paper vector is near to one, it means that the debutant topic in its first five years of life had a very mild relationship with the related topic and the latter had a minor role in shaping the debutant topic. 

Accordingly, after performing all the intensities of collaboration between the debutant topic and all the retrieved co-occurring topics, the algorithm ranks them in ascending order based on the Euclidean distance. For the evaluation, we selected the first 25 meaningful topics that were influential for the debutant topic. In Table 5.3 we report a sample of ancestors extracted for the topic _Semantic Search_ debuting in 2003. Code 7 instead reports the pseudocode that describes this process. 

The result of this process is a gold standard that contains topics in the _Computer Science_ between 2000-2011 and their ancestors. 

141 

**Code 7:** Extracting the ancestors of debutant topics. **Input :** List of Debutant Topics _deb.topics_ **Output:** List of ancestors _ancestors_ 

**foreach** _topic in deb.topics_ **do** year _←_ GetYearOfSoftDebut(topic); related.topics _←_ SelectCoOccurringTopics(topic, from=year, to=year+5); p.dt _←_ NumberOfPapers(topic, from=year, to=year+5); **foreach** _rt in related.topic_ **do** c.dt.rt _←_ NumCoOccurringPapers(topic, rt, from=year, to=year+5); ioc[rt] _←_ sqrt(sum((p.dt _−_ c.dt.rt)<sup>2</sup> )); `/* Euclidean distance */` **end foreach** temp.ancestors _←_ sort(related.topic, values=ioc, increasing=TRUE); ancestors[topic] _←_ temp.ancestors[1:25]; `/* keep only the best 25 */` **end foreach** return(ancestors); 

**Table 5.3:** Example of ancestors extracted form the _Semantic Search_ topic debuting in 2003. 

|**Debutant Topic**|Semantic Search|
|---|---|
|**Soft debut**|2003|
||data mining<br>database systems<br>information retrieval<br>internet<br>knowledge based systems<br>metadata|
|**some ancestors**|multimedia systems|
|**(alphabetical**<br>**order)**|natural language processing systems<br>ontology<br>query processing<br>search engines<br>semantic web<br>semantics<br>web services<br>world wide web|



142 

## **5.4 Labelling the clusters** 

As already mentioned, Augur returns a set of clusters that each year are extracted from the evolutionary networks. Each cluster contains a “team of topics” that should lead to the emergence of a new area in the near future. 

The aim of this evaluation is to compare and match the returned clusters in each year with the debutant topics in the next two years, as reported in Table 5.2. However, as previously mentioned, comparing the emerging topics with the clusters, using only their label, is not feasible. For this reason, the debutant topics have been supplied with information regarding their ancestors, so that the algorithm can match the topics in each cluster against the ancestors of each debutant topic. 

This is consistent with the aim of the evaluation, because the topics within the clusters will eventually lead to the emergence of a new topic, while the ancestors of a debutant topic, by definition, are the topics that bred this new topic and helped it to arise. Therefore, if the topics in the cluster are analogous to the ancestors of a debutant topics, we can assume that the cluster is correctly forecasting the debutant topic. 

The algorithm that runs the evaluation, henceforth also called _evaluator_ , compares the clusters and the debutant topics in an _all-vs-all_ fashion. The algorithm computes the Jaccard Index between the _i-th_ cluster _Ci_ and the ancestors of the _k-th_ debutant topic _Dk_ , showed in Table 5.4, using Eq. 5.2. However, considering only the syntactical representation of topics is restrictive. Indeed, a topic can have more than one label referring to it. Therefore, if the cluster _Ci_ and the debutant topic _Dk_ contain the same topic but with different labels, the equation will fail to match the topic. 

To tackle this problem, we semantically enhanced the equation by employing the Computer Science Ontology. Particularly, Eq. 5.2 includes also the topics which have a _same-as_ relationship with the topics appearing in the cluster. 

143 

**Table 5.4:** Example of cluster _Ci_ returned by Augur and ancestors _Dk_ of the topic _Resource Description Framework_ available in the gold standard. 

|**Cluster** _Ci_|query languages, information retrieval, artificial intelligence,<br>world wide web, management information systems, relational<br>database systems, computational geometry, image analysis, data<br>reduction, knowledge acquisition, three dimensional computer<br>graphics, membership functions, graph theory, theorem proving,<br>vectors|
|---|---|
|**Ancestors**<br>**of debutant**<br>**topic** _Dk_|query languages, information retrieval, artificial intelligence,<br>world wide web, management information systems, natural lan-<br>guage processing systems, multi agent systems, expert systems,<br>xml, search engines, semantics, metadata, intelligent agents, in-<br>teroperability, html, algorithms, data communication systems,<br>security of data, schemas, linguistics, resource allocation, con-<br>straint theory, software agents, network protocols, websites|









We enhanced the clusters, so that even if a topic in _Ci_ does not have a syntactic match with an ancestor of a debutant topic in _Dk_ , its _related-equivalent_ in _SAi_ might have it. This works also in the opposite direction, if we had enhanced _Dk_ , so that even if one ancestor was not matching a topic in a cluster _Ci_ , one of its _relatedequivalent_ could have helped to match. However, we did not enhance both _Ci_ and _Dk_ simultaneously, to avoid that the same topic could match multiple times. In addition, we did not include _SAi_ in the denominator, because although the _SAi_ topics have been merged with the _Ci_ , they actually play the role of substitutes for the actual topics in the cluster. 

The similarity index _J_ ( _Ci, Dk, SAi_ ) between the clusters and the debutant topics falls in the range 0 to 1. If similarity is very near 0 the two sets share only few topics, 

144 

while for values of 0.1 to 0.4 there is already a good number of matching topics. When the similarity is near 1, that the two sets are almost identical. We consider a positive match between a debutant topic and a cluster only when their similarity is above a threshold _t_ , as stated as follow: 



The similarity threshold _t_ cannot be defined a priori and indeed its detection will be part of the evaluation. The algorithm that runs the comparisons between the set of clusters _C_ and the set of ancestors of debutant topics _D_ , will track all the different similarities into a similarity matrix (R<sup>_|C|×|D|_</sup> ). In this way, we can compute the performance for varying values of similarity. The algorithm will iteratively set a threshold and then compute the values of precision and recall based on the matched clusters and the matched debutant topics. Eventually, we would like to earn some insights on the similarity threshold that guarantees the significance of the match and that keeps high the performance of Augur. Code 8, describes the general workflow for the process of evaluation. 

In the next section, we will define the values of precision and recall employed to assess the performance of Augur. Then we will compare five alternative clustering algorithms: (i) Fast Greedy Algorithm, (ii) Leading Eigenvector Algorithm, (iii) Fuzzy C-Means, (iv) Clique Percolation Method, and (v) Advanced Clique Percolation Method. 

145 

**<u>Code 8:</u>** <u>Process of evaluation.</u> **Input :** List of Debutant Topics _deb.topics_ , list of Clusters _set.clusters_ , list of years _years_ **Output:** _precision_ and _recall_ along time **foreach** _year of years_ **do** clusters _←_ GetClustersOfYear(set.clusters, year); topics _←_ GetDebutantTopics(deb.topics, year+1, year+2); `/* in the two following years */` **foreach** _cl in clusters_ **do** same.as _←_ GetSameAsOfCluster(cl); **foreach** _tp of topics_ **do** ancestors _←_ GetAncestorsOfTopic(tp); sim.matrix[cl,tp] _←_<sup>_|_(</sup><sup>_cl ∪same.as_)</sup><sup>_∩ancestors|_</sup> ; `/* Jaccard Index` _|cl ∪ ancestors|_ `in Eq. 5.2 */` **end foreach end foreach for** _i ←_ 0 **to** 1 **by** 0 _._ 001 **do** temp.mat _←_ BinarizeSimilarityMatrix(threshold=i); temp.precision[i] _←_ GetMatchedClusters(temp.mat)/length(clusters) ; temp.recall[i] _←_ GetMatchedTopics(temp.mat)/length(topics) ; **end for** precision[year] _←_ temp.precision; recall[year] _←_ temp.recall; **end foreach** 

```
/*Nowprecisionandrecall,eachyear,arearrayscontaining
valuesofprecisionandrecallvaryingwiththedifferent
similarityvalues.
```

```
*/
```

### **5.4.1 Measures of performance** 

Precision and Recall are often used to evaluate the performance in tasks such as information retrieval and pattern recognition. To evaluate the clusters returned by Augur, we will also consider precision and recall. In this section, we will provide a definition of these measures taking into account the number of returned clusters, the amount of debutant topics and the number of matches between these two sets. 

146 

If we assume that there is a _one-to-one_ relationship between clusters and ancestors of debutant topics, so that every retrieved cluster has only one corresponding emerging topic and vice versa, we can define precision and recall using the confusion matrix in Table 5.5. 

**Table 5.5:** Confusion matrix for a binary classifier. 

|||Clus<br>Retrieved|ters<br>Not Retrieved|
|---|---|---|---|
|Debutant|Identified|True Positive|False Negative|
|topics|Not<br>Identified|False Positive|True Negative|



Comparing the set of clusters against the set of debutant topics leads to four different cases: 

- _true positives_ represent the number of clusters that have been matched with the debutant topics; 

- _false positives_ represent the retrieved clusters that have not been matched with any topic; 

- _false negatives_ are the debutant topics that do not have any matched cluster; 

- although not quantifiable, the _true negatives_ represent the amount of not found cluster that effectively do not correspond to any debutant topic. 

The values of precision and recall are respectively described in Eq. 5.3 and Eq. 

5.4. 

147 





However, the _one-to-one_ relationship between clusters and ancestors of debutant topics is a stretched assumption. Indeed, we can argue that a cluster can foster the emergence of more than one new topic and similarly two or more different clusters can share the same subset of ancestors that match the same debutant topic. Therefore, precision and recall, respectively defined in Eq. 5.3 and Eq. 5.4 are not suitable to assess the validity of the approach. 

Since there is a _many-to-many_ relationship between clusters and topics, as represented in Fig. 5.3, to evaluate this system it is important to observe this relationship from different angles (matched clusters, and matched debutant topics) and focus on the following two specific questions: 

1. **How good is our system in identifying portion of topic networks (clusters) that eventually will lead to the emergence of new topics? (perspective of the cluster)** 

148 

2. **How good is our system in identifying debutant topics that have been matched with clusters? (perspective of the debutant topics)** 



**Figure 5.3:** Graphical explanation of the _many-to-many_ relationship between clusters and debutant topics. Since the number of matched cluster can be different from the matched debutant topics, the value of precision and recall need to take into account this difference. 

Those two questions shape the definition of true positive mentioned above giving it a dual definition. Taking into account the first question it is possible to define the true positives as the clusters that have been matched with debutant topics. Considering the second question, instead, the true positives are the number of debutant topics that have been matched with the retrieved clusters. In a _one-to-one_ relationship, these two quantities can have the same value, while in a _many-to-many_ this is not the case. 

Therefore, we define **precision** as the fraction of clusters that have been successfully matched with debutant topics (also known as _correctness_ ), and **recall** as 

149 

the fraction of topics that have been successfully matched by clusters (also known as _completeness_ ), as defined in Eq. 5.5 and Eq. 5.6. 





The symbol ⋉ is called _left semijoin_ and the result of _{retrieved clusters}_ ⋉ _{debutant topics}_ is the set of the clusters for which there is a match with the debutant topics. Similarly, the sign ⋊ is called _right semijoin_ and the result of _{retrieved clusters}_ ⋊ _{debutant topics}_ is the set of debutant topics that received a match from the clusters. 

Since, the gold standard and the tools to evaluate are now both available, we can proceed in assessing the validity of Augur and of some community detection algorithms. 

### **5.4.2 Description of the main community detection algorithms** 

In the previous chapter, we introduced the concept of community detection as a way to perform clustering over networks. In addition, we talked about some algorithms that are available in the literature, which can be classified according to two main families: 

- a _crisp_ community detection algorithm produces mutually exclusive clusters; 

150 

- a _fuzzy_ algorithm provides overlapping communities so that a node can belong to more than one cluster. 

As already anticipated, crisp algorithms are not suitable for the purpose of this work as it is expected that a topic can lead to the emergence of more than one other topic. However, for the sake of completeness, we tested them and indeed their results allowed us to gain a better understanding of evolutionary networks. In particular, for the family of crisp community detection algorithms, we used Fast Greedy (Clauset et al., 2004) and Leading Eigenvector (Newman, 2006a). Instead, as fuzzy community detection algorithms, we evaluated Fuzzy C-Means (Bezdek, 1981), the Clique Percolation Method (Palla et al., 2005) and the Advanced Clique Percolation Method proposed in this thesis. 

In the following sections, we describe the results we obtained from all the tested algorithms. In Table 5.6 we report all the employed algorithms with information about their implementation and the section describing their results. 

**Table 5.6:** List of the community detection algorithms used for the evaluation. 

|**Algorithm**|**Refercence**|**Implementation**<br>**used**|**Results**|
|---|---|---|---|
|Fast Greedy|Clauset et al. (2004)|R: iGraph|Section 5.4.3|
|Leading Eigenvector|Newman (2006a)|R: iGraph|Section 5.4.4|
|Fuzzy C-Means|Bezdek (1981)|R: e1071|Section 5.4.5|
|Clique Percolation<br>Method|Palla et al. (2005)|R: developed from<br>scratch|Section 5.4.6|
|Advan. Clique<br>Percolation Method|Salatino et al. (2018a)<br>and this work|R: developed from<br>scratch|Section 5.4.7|



151 

### **5.4.3 Results with Fast Greedy Algorithm** 

We adopted the implementation of the Fast Greedy algorithm available within the iGraph<sup>1</sup> package for R, which is the most comprehensive package for _Network Science_ . The algorithm takes as input the 11 evolutionary networks, according to Table 5.2 at page 135, and returns several communities along a time dimension. In Table 5.7, are reported the number of communities returned for each year and we can observe that, as a consequence of the constant widening of evolutionary networks over time, the algorithm returns an almost ever increasing number of communities. Another interesting phenomenon is that the sizes of the communities returned each year by the algorithm have a long-tailed distribution, as showed in Fig. 5.4. In particular, there is a small number of communities with a substantial number of topics and a large number of communities with just a few topics. In Table 5.7, we also reported the dimension of the first ten communities to highlight this phenomenon along time. 

**Table 5.7:** Number of communities and the size of the first ten communities using the Fast Greedy algorithm over the different evolutionary networks 

|**Year**|**# communities**|**Dimension of the first 10 communities**|
|---|---|---|
|1999|50|355, 329, 306, 180, 170, 159, 116, 87, 86, 84|
|2000|52|372, 370, 264, 246, 226, 150, 138, 100, 77, 66|
|2001|38|475, 447, 421, 221, 199, 196, 110, 107, 65, 29|
|2002|51|422, 402, 345, 326, 296, 198, 165, 142, 34, 33|
|2003|62|540, 452, 439, 363, 282, 228, 134, 84, 51, 39|
|2004|65|878, 584, 474, 309, 249, 243, 166, 121, 26, 19|
|2005|102|1179, 571, 523, 350, 268, 121, 121, 104, 55, 44|
|2006|98|1098, 565, 518, 493, 462, 323, 256, 195, 124, 67|
|2007|106|1193, 965, 713, 538, 369, 221, 169, 109, 101, 91|
|2008|152|1918, 1183, 856, 758, 639, 470, 370, 285, 166, 152|
|2009|164|1835, 1305, 1295, 1130, 815, 669, 380, 361, 273, 268|



Once the algorithm completed the processing the evolutionary networks and returned the clusters, the next step was to evaluate these clusters against the ancestors of the actual debutant topics. The evaluator then compared the clusters and the 

> 1 `http://igraph.org/r/doc/cluster_fast_greedy.html` 

152 



**Figure 5.4:** Distribution of the community sizes obtained from the Fast Greedy algorithm in the different years. 

debutants in an _all-vs-all_ fashion, creating a matrix of similarity. Then, from this similarity matrix it becomes possible to define the minimum value of similarity above which they are considered similar. 

As already mentioned, using a low similarity value (near 0), it means that a cluster and a debutant topic will be considered similar even with few mutual topics. A very high similarity value (near 1) means that a cluster must contain almost all and exclusively the ancestors of a debutant topic to be considered a match. However, to choose a suitable similarity threshold, we need to consider the minimum value in which the match is considered meaningful and at the same time it maximises precision and recall. In Fig 5.5, we report, for each year, all the values of precision and recall depending on the different values of similarity. The lines of precision and recall for a particular year are identified by the same colour. As it can be seen from the figure, regardless of the value of similarity, the precision is always low while the recall is very 

153 

high for similarity values near 0 but then it quickly drops when we attempt to increase it. According to these results we can understand that because of low precision only a small portion of the returned clusters matched the debutant topics. Increasing the value of similarity worsen the situation since fewer and fewer clusters could match debutant topics. Regarding the recall, we can see that using a low similarity value, almost all the debutant topics were matching the returned clusters, most certainly because only a few mutual topics are needed to consider the two parts similar, and then everything almost matches with everything else. If we increase the similarity value, fewer debutant topics get matched and then the recall drastically decreases. 

An interesting phenomenon highlighted from Fig. 5.5 is that the values of precision and recall depend from the year of analysis. We can see that, although poor, the best performance comes from the evolutionary networks of 1999 to 2001 and then they decrease along time. This can be justified by the fact that there are fewer and fewer debutant topics that can be matched by the retrieved clusters in the last part of the analysed period, as reported in Fig. 5.5. Thus, even if the results appear to be very poor, they do provide interesting insights. 

In conclusion, as the results suggest, the Fast Greedy algorithm is not suitable for the aim of this work as it does not provide good results in terms of precision and recall. 

### **5.4.4 Results with Leading Eigenvector Algorithm** 

The Leading Eigenvector, as the Fast Greedy, is also implemented in the iGraph<sup>2</sup> package for R. The algorithm iteratively processes the 11 evolutionary networks, returning, for each year, a set of clusters. Table 5.8 reports the number of communities the algorithm is able to locate within the different networks, as well as the size of the first ten communities. From the table, we can observe that also this algorithm 

> 2 `http://igraph.org/r/doc/cluster_leading_eigen.html` 

154 



**Figure 5.5:** Results in terms of precision and recall obtained from evaluating the Fast Greedy algorithm against the gold standard. 

returns communities whose size resembles a long-tailed distribution. In particular, for years like 1999, 2000, 2006, 2007, 2008 and 2009 the algorithm returns one or two large communities and some other very small ones. 

We ran the evaluator over the obtained clusters and Fig. 5.6 reports the values of precision and recall depending on the different values of similarity. As we can see, also this approach does not provide valuable results as the precision is below 0.4 regardless of the similarity value and the recall decreases as soon as the value raises. These values of precision and recall are comparable to the results obtained using the Fast Greedy algorithm, mostly because both these algorithms form few giant communities and many other small ones. This phenomenon mainly happens in networks with high number of nodes and edges, because Fast Greedy and the Leading Eigenvector respectively tend to merge and split the communities, trying to optimise a quality function called modularity. In optimising the modularity function 

155 

**Table 5.8:** Number of communities and the size of the first ten communities using the Leading Eigenvector algorithm over the different evolutionary networks 

|**Year**|**# communities**|**Dimension of the first 10 communities**|
|---|---|---|
|1999|14|2187, 3, 2, 2, 2, 2, 2, 2, 2, 2|
|2000|14|2069, 169, 3, 2, 2, 2, 2, 2, 2, 2|
|2001|11|1279, 421, 237, 207, 190, 72, 2, 2, 2, 2|
|2002|36|567, 553, 369, 347, 279, 207, 100, 49, 6, 6|
|2003|15|1661, 765, 306, 44, 36, 4, 3, 2, 2, 2|
|2004|25|908, 514, 406, 387, 380, 324, 244, 26, 21, 14|
|2005|22|1337, 609, 564, 470, 351, 254, 106, 3, 2, 2|
|2006|22|4286, 177, 2, 2, 2, 2, 2, 2, 2, 2|
|2007|17|5183, 4, 2, 2, 2, 2, 2, 2, 2, 2|
|2008|12|7866, 3, 2, 2, 2, 2, 2, 2, 2, 2|
|2009|24|7684, 1448, 691, 2, 2, 2, 2, 2, 2, 2|



they force small communities into larger ones, offering a misleading characterisation of the underlying community structure (Lancichinetti and Fortunato, 2011). This is a well-known problem in the literature, which pushed the community of scholars to move towards alternative solutions that could work on real-world complex networks (Holmstr¨om et al., 2009; Botta and Del Genio, 2016). 

In conclusion, even if modularity offers a first-principle understanding of community structure, an algorithm based on its maximisation cannot provide a good characterisation. It is also worth to remember that both Fast Greedy and Leading Eigenvector belong to the crisp family of community detection algorithm. Although they helped to move the first steps towards the effective detection of emerging trends, these algorithms cannot characterise the community structure of our networks, given that a topic can foster the emergence of more than one other topic. In the next sections we will show the results we obtained using some fuzzy community detection algorithms. 

156 



**Figure 5.6:** Results in terms of precision and recall obtained from evaluating the Leading Eigenvector algorithm against the gold standard. 

### **5.4.5 Results with Fuzzy C-Means** 

Fuzzy C-Means is one of the most famous and widely adopted algorithms for clustering data and, as the name suggests, it belongs to the fuzzy family. An implementation of this algorithm is available in the e1071<sup>3</sup> package for R. The required arguments include the input matrix, the number of clusters and the degree of fuzzification. The input matrix contains information about the evolutionary networks, from which the algorithm will find the clusters. It is structured as matrix, where rows correspond to observations (i.e., topics in the evolutionary network) and columns to variables (i.e., topics to which it is connected). The degree of fuzzification or fuzziness coefficient can be any real number greater than 1<sup>4</sup> and will be set to 2, as commonly done when the domain is not well known (Hathaway and Bezdek, 2001). Lastly, the number of 

> 3https://www.rdocumentation.org/packages/e1071/versions/1.6-8/topics/cmeans 

> 4With m=1, the membership of a node (topic) to a cluster will converge to either 0 or 1, which 

> denotes a crisp partitioning. 

157 

clusters is the number of clusters we expected as output from the algorithm. This value is not known a priori but the state of the art offers several methods that can help to determine it, such as the elbow method. Since each evolutionary network can contain a different number of communities, these networks need to be individually analysed to determine their number of clusters. 

The elbow criterion is a visual method and consists in running the clustering algorithm with a constantly increasing number of clusters, as showed in Code 9. For each run, we calculate the sum of squared errors of prediction (SSE)<sup>5</sup> and plot it against the number of clusters. If the line curves like an arm, the parameter is set to the minimum number of clusters in which the SSE starts to asymptotically decrease towards 0. This is typically located at the elbow of the curve. However, this method is computationally expensive since one needs to actually run the C-means algorithm several times trying different number of clusters. According to the number of debutant topics per year (see Fig. 5.2), it is reasonable to have a range of clusters that goes from 5 to 200. However, since each evolutionary network is a very large data sample and the execution of one single instance of C-Means is quite expensive, at each run we increased the number of cluster by 5. 

> 5The sum of squared errors of prediction measures quantitatively the discrepancy between the actual data and the predicted model. 

158 

**Code 9:** Counting the number of clusters within the evolutionary networks using the Elbow Method with Fuzzy C-Means. 

**Input :** List of Evolutionary Networks _evolutionary.networks_ , list of years _years_ 

**Output:** Number of clusters _num.clusters_ along time 

**foreach** _year of years_ **do** 

ev.network _←_ GetEvolutionaryNetworkOfYear(evolutionary.networks, year); mat _←_ AsAdjacencyMatrix(ev.network) `// Graph into adjacency matrix` i _←_ 1; 

**for** _cl ←_ 5 **to** 200 **by** 5 **do** 

fclust.obj _←_ cmeans(mat,clusters=cl,m=2) `// m = degree of fuzzif.` 

`/*` _fclust.obj_ `contains the memberships, the centroids and the value of the objective function (SSE) */` sse[i] _←_ GetWithinError(fclust.obj); x[i] _←_ cl; i _←_ i + 1; 

**end for** 

plot(x, sse); 

- `/* The position of the ‘‘elbow’’ in the plot determines the number of clusters in that particular year */` 

#### **end foreach** 



**Figure 5.7:** Sum of squared error in prediction (SSE) obtained from evaluating the Fuzzy C-Means with different number clusters (from 5 to 200) over the different evolutionary networks. We can see that for all the evolutionary networks the elbow is located at 25. 

We run the method showed in Code 9 and we reported in Fig. 5.7 all the different SSEs, based on the year and the number of clusters in which the Fuzzy C-Means 

159 

algorithm has been trained. From the figure we can observe a common pattern: with 5 clusters the SSE for each evolutionary network is around 0.45 and it exponentially decreases towards 0.01 for 200 clusters. In addition, we can observe that for all the different evolutionary networks, the SSE curves start to bend around 25. Hence, we ran the Fuzzy C-Means over the different evolutionary networks using 25 as number of clusters. 

As output, the algorithm returns a membership matrix where rows correspond to the different topics and 25 columns corresponding to the clusters. This matrix reports the likelihood of each topic to belong to a particular cluster. 

To retrieve the final cluster set, for a given cluster, we selected all topics having likelihood (of belonging to it) above a particular threshold (0.04 or _chance level_ 1/25). Instead, if for a particular cluster, all the likelihoods were below or equal to such threshold we selected the first 25 topics. 

Table 5.9 reports the number of communities (as already mentioned, set to 25), as well as the size of the first ten communities. We can observe that also the Fuzzy C- Means fails to characterise the different clusters within the different networks, because for each year it provides one large community and some little ones. Also, the fact that all these little communities have 25 topics, means that some of the topics found in a cluster, are likely to be there by chance. 

Using these clusters, we ran the evaluator and Fig. 5.8 reports the values of precision and recall depending on the different values of similarity. Overall, we can observe very low values of precision and recall, dropping to zero when the similarity threshold reaches around 0.01. We can find an exception in the year 2000, in which the precision stays around 0.96 for initial values of similarity thresholds and then it collapse when it reaches 0.0638. This phenomenon is due to the fact that all the 24 small communities were containing three similar topics (“telecommunication links”, “telecommunication networks”, “channel capacity”) that found a match with the an- 

160 

cestors of _Network Coding_ boosting the precision value. When the similarity threshold increases over 0.0638, the precision decreases because we cannot find matches that exceed such threshold. 

**Table 5.9:** Number of communities and the size of the first ten communities using the Fuzzy C-Means algorithm over the different evolutionary networks. 

|**Year**|**# communities**|**Dimension of the first 10 communities**|
|---|---|---|
|1999|25|681, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2000|25|728, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2001|25|885, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2002|25|922, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2003|25|1050, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2004|25|1381, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2005|25|1507, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2006|25|1791, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2007|25|2082, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2008|25|3443, 25, 25, 25, 25, 25, 25, 25, 25, 25|
|2009|25|3853, 25, 25, 25, 25, 25, 25, 25, 25, 25|





**Figure 5.8:** Results in terms of precision and recall obtained from evaluating the Fuzzy C-Means against the gold standard. 

161 

### **5.4.6 Results with Clique Percolation Method** 

The Clique Percolation Method, is another algorithm that falls in the family of fuzzy community detection algorithms. Among all the packages that allow to perform network analysis in _R_ there was not an implementation of the Clique Percolation Method. After developing a version<sup>6</sup> based on the work of Palla et al. (2005), we ran the algorithm over the 11 evolutionary networks, which returned the communities summarised in Table 5.10. From the same table, we can observe that also this algorithm returns communities whose size resembles a long-tailed distribution. In particular, we can see that, for each year, there is one big blob of topics, which in most of the cases is over 1 000 topics and in some cases over 4 000 topics. All other communities have at most 11 topics. 

**Table 5.10:** Number of communities and the size of the first ten communities using the Clique Percolation Method algorithm over the different evolutionary networks. 

|**Year**|**# communities**<br>**Dime**|**nsion of **|**the first 10 communities**|
|---|---|---|---|
|1999|68<br>966, 1|1, 11, 9, 7|, 6, 5, 5, 4, 4|
|2000|54<br>1124,|7, 6, 5, 5,|4, 4, 4, 4, 4|
|2001|31<br>1302,|4, 4, 4, 4,|4, 4, 4, 3, 3|
|2002|26<br>1454,|5, 4, 4, 4,|4, 4, 3, 3, 3|
|2003|40<br>1554,|6, 6, 6, 5,|5, 4, 4, 4, 4|
|2004|22<br>1783,|7, 6, 4, 4,|3, 3, 3, 3, 3|
|2005|48<br>1793,|5, 5, 4, 4,|4, 4, 4, 4, 4|
|2006|67<br>2042,|8, 5, 5, 5,|5, 5, 5, 4, 4|
|2007|83<br>2541,|5, 5, 5, 4,|4, 4, 4, 4, 4|
|2008|74<br>4492,|7, 5, 4, 4,|4, 4, 4, 4, 4|
|2009|88<br>6031,|6, 5, 5, 5,|5, 5, 4, 4, 4|



Observing in more detail the large communities that the algorithm returned over time, it is possible to see that all the topics belong to the _Computer Science_ field. This means that the _Computer Science_ field is so tight on a clique level that the algorithm is unable to split it in further subnetworks. We can better appreciate this phenomenon through Fig. 5.9. This figure shows the evolutionary network of year 2000 divided 

> 6This version is available in my personal Github repository: `https://github.com/ angelosalatino/CliquePercolationMethod-R` . 

162 

in 54 communities or connected components as per the definition of community for the CPM. From the figure, we can see that there is one very large community and many other smaller ones. The largest community, which contains all the subareas of _Computer Science_ , is composed by 1 124 topics and 10 939 edges. The average degree of the nodes is 19.46, meaning that on average each topic is connected with at least 19 other topics. In addition, the subnetwork is composed by 27 064 3-cliques with an average of 72 cliques per topic, and each couple of cliques shares two topics. Also, the average path length (also known as _degree of separation_ ) of the network is 3.04, which means that on average two topics are separated by only 2 topics. All these characteristics suggest that this particular area of the evolutionary graph contains a high density of ties, to the extent that the Clique Percolation Method is unable to split it in further subnetworks. In Table 5.11, we report some other statistics that point out the characteristics of both the evolutionary network of year 2000 and its main community of _Computer Science_ , also suggesting their dense nature. In particular, while the main community of _Computer Science_ contains half of the nodes, it also contains 82% of the total number of links. Also, the diameter between the network and the community drastically reduces from 20.67 to 8.95, making it quite tight-knit. **Table 5.11:** Some statistics for the evolutionary network of year 2000 and its largest community of _Computer Science_ . 

|**Network**<br>**parameter**|**Evolutionary**<br>**Network (of**<br>**2000)**|**Computer**<br>**Science**<br>**community**|
|---|---|---|
|_Nodes_|2263|1124 (49.6 %)|
|_Edges_|13327|10939 (82 %)|
|_Avg degree_|11.77|19.46|
|_Avg clustering coeff._|0.163|0.198|
|_Max degree_|184|160|
|_Diameter_|20.67|8.95|



163 



**Figure 5.9:** Evolutionary graph of the year 2000 split into communities using the Clique Percolation Method. The largest community counts 1124 topics and 10393 edges. 

For the sake of completeness, the returned clusters have been evaluated against the debutant topics whose results are reported in Fig 5.10. From the figure, we can observe that both precision and recall exhibit the same patterns of the previously tested approaches. In brief, the Clique Percolation Method appears to not be suitable for clustering evolutionary networks. As showed, it tends to split these networks in a set of one very large community and several other small communities. This is mostly due 

164 

to the fact that the evolutionary network appears to be very dense in specific area and then all the topics within this area are gathered together. Indeed, this phenomenon was already observed running the Fast Greedy and Leading Eigenvector methods, which while trying to optimise the modularity function, merge smaller communities into bigger ones. 

Another limitation of the Clique Percolation Method is that it does not take advantage of the weights of the networks as the other algorithms do. 



**Figure 5.10:** Results in terms of precision and recall obtained from evaluating the Clique Percolation Method against the gold standard. 

In conclusion, the Clique Percolation Method as well as the Fast Greedy, Leading Eigenvector and Fuzzy C-Means methods, are not providing high values of precision and recall at high values of similarity. However, it is worth mentioning that these algorithms helped us to understand the structure and peculiarities of the evolutionary network: it is very dense and some algorithms do not take advantage of the link weights. 

165 

### **5.4.7 Results with Advanced Clique Percolation Method** 

The Advanced Clique Percolation Method (ACPM) is a newly developed community detection algorithm and, as the name suggests, it is inspired by the Clique Percolation Method. In particular, this new version takes into account the weights of the network and redefines the concept of community, as explained in Section 4.3.2. In Table 5.12 are reported the number of communities this algorithm returned each year, as well as the size of the first ten communities sorted in descending order. As we can see, the algorithm is returning communities with a more reasonable size (around 20 topics) compared to the communities retrieved with the Clique Percolation Method, Fast Greedy and so on. Figure 5.11 reports more extensively the sizes of the first 100 communities, in which we can observe how the distributions are less long-tailed and more uniform. 

**Table 5.12:** Number of communities and the size of the first ten communities using the Advanced Clique Percolation Method algorithm over the different evolutionary networks. 

|**Year**|**# communities**<br>**Dimension o**|**f the fi**|**irst 10 communities**|
|---|---|---|---|
|1999|238<br>37, 27, 26, 24,|24, 24,|24, 23, 23, 22|
|2000|201<br>26, 25, 25, 23,|23, 22,|22, 22, 21, 21|
|2001|174<br>25, 24, 23, 21,|21, 21,|21, 21, 20, 20|
|2002|228<br>28, 25, 25, 24,|24, 23,|23, 22, 22, 22|
|2003|159<br>28, 25, 25, 25,|24, 23,|21, 21, 21, 21|
|2004|130<br>29, 23, 23, 23,|22, 22,|22, 21, 21, 21|
|2005|168<br>26, 25, 23, 23,|22, 22,|21, 21, 21, 21|
|2006|110<br>22, 21, 20, 20,|20, 19,|18, 18, 18, 18|
|2007|103<br>25, 24, 23, 22,|22, 21,|21, 20, 20, 20|
|2008|167<br>24, 22, 22, 21,|21, 21,|20, 20, 20, 19|
|2009|177<br>22, 22, 20, 19,|19, 19,|18, 18, 18, 18|



These new distributions of size of communities suggests that the algorithm managed to split the area of _Computer Science_ in further sub areas. Figure 5.12 shows the evolutionary network of the year 2000, which is split into 201 communities. Differently form Fig. 5.9, we can see that all the topics that where gathered within 

166 



**Figure 5.11:** Distribution of the community sizes obtained from the Advanced Clique Percolation Method in the different years. 

the large bubble of _Computer Science_ are now spread out into several communities. However, since the Advanced Clique Percolation Method falls into the fuzzy community detection algorithms, the same topic can appear into more than one community. This means that it can actively hold several partnerships and eventually lead to the emergence of more than one new area. 

All the communities that the algorithm returned each year were evaluated against the gold standard, as already performed in the previous tests. The results of the evaluation are reported in Fig 5.13. Comparing them to the results obtained with the Clique Percolation Method and by extension also with the other approaches, we can observe that for ACPM the overall values of precision increase and also they stay up until almost 0.1 of similarity value. The values of recall instead are fairly good and are no longer affected by this quick fall. However, although we see a general improvement in both precision and recall we cannot be completely satisfied by these 

167 



**Figure 5.12:** Evolutionary graph of the year 2000 split into communities using the Advanced Clique Percolation Method. 

168 

results. The values for precision are still very low and the algorithm needs to be further improved in order to return better results. 



**Figure 5.13:** Results in terms of precision and recall obtained from evaluating the Advanced Clique Percolation Method against the gold standard. 

To further improve the algorithm we analysed the communities more qualitatively. We realised that in some communities, most of the topics were not sub areas of _Computer Science_ . This impacts precision (see Eq. 5.5), because these communities containing _non-Computer Science_ topics where unsuccessfully compared against the ancestors of debutant topics with the _Computer Science_ area. To cope with this problem, we filtered the communities semantically. 

169 

## **5.5 Applying semantic filters** 

In order to improve the results and thus remove the communities where most of the topics do not belong to _Computer Science_ , we developed a filter. This filter selects communities for which least 30% of their topics are found in the Computer Science Ontology. This filtering process is part of the _post-processing_ phase, highlighted in the workflow in Fig. 4.3, at page 104. As a result, we remove all the communities that can never match with the debutant topics and eventually improve the values of precision. Indeed, thanks to this filter, the results obtained from all the approaches show an improvement in terms of precision and recall. Table 5.13 reports the number of communities returned by all the analysed approaches, both before and after applying the semantic filter. On average (along the different years), when applying this filter to Fast Greedy, we reduce the number of clusters by 37%. When filtering the clusters of Leading Eigenvector, they are reduced by 41%, and by 52%, 43% and 37% for the Fuzzy C-Means, Clique Percolation Method and its Advanced version, respectively. 



**Figure 5.14:** Results in terms of precision and recall obtained from evaluating the Fast Greedy against the gold standard after filtering the communities semantically. 

All the communities that succeeded the filtering phase were then evaluated against the gold standard. In Fig. 5.14, 5.15, 5.16, 5.17, 5.18 are reported the new values 

170 

**Table 5.13:** Listing the number of communities obtained using the Fast Greedy (FG), Leading Eigenvector (LE), Fuzzy C-Means (FCM), Clique Percolation Method (CPM) and Advanced Clique Percolation Method (ACPM), before (# comm.) and after filtering (# comm. filt.). Below the table is reported the average percentage difference between the initial value of community and the final number of communities after filtering. 

||F|G|L|E|FC|M|CP|M|AC|PM|
|---|---|---|---|---|---|---|---|---|---|---|
|Years|#<br>comm.|#<br>comm.<br>filt.|#<br>comm.|#<br>comm.<br>filt.|#<br>comm.|#<br>comm.<br>filt.|#<br>comm.|#<br>comm.<br>filt.|#<br>comm.|#<br>comm.<br>filt.|
|1999|50|26|14|5|25|25|68|32|238|121|
|2000|52|29|14|7|25|25|54|22|201|103|
|2001|38|23|11|9|25|25|31|12|174|98|
|2002|51|28|36|18|25|1|26|14|228|118|
|2003|62|44|15|10|25|1|40|25|159|83|
|2004|65|45|25|17|25|1|22|17|130|70|
|2005|102|73|22|16|25|1|48|33|168|91|
|2006|98|68|22|15|25|25|67|45|110|81|
|2007|106|76|17|10|25|25|83|39|103|94|
|2008|152|101|12|6|25|1|74|42|167|129|
|2009|164|96|24|11|25|1|88|58|177|146|
|%diff||37%||41%||52%||43%||37%|



of precision and recall with different values of similarity, obtained each year from all the tested approaches. Table 5.14, for the sake of comparison, provides an index of the figures reporting the results for the various methods, before and after applying the filter. Indeed, comparing these results with the ones obtained without filtering, we can observe an improvement in precision while the values of recall are equivalent. Looking at the definitions of precision and recall, described in Section 5.4.1, these results suggest that we managed to keep all the communities that were matching with the debutant topics and we also managed to remove all those communities that were having a negative impact on the values of precision. 

171 

**Table 5.14:** Figures comparison for each approach before and after applying the filter. 

|**Method**|**Before filtering**|**After filtering**|
|---|---|---|
|FG|Figure 5.5 at p. 155|Figure 5.14 at p. 170|
|LE|Figure 5.6 at p. 157|Figure 5.15 at p. 172|
|FCM|Figure 5.8 at p. 161|Figure 5.16 at p. 173|
|CPM|Figure 5.10 at p. 165|Figure 5.17 at p. 173|
|ACPM|Figure 5.13 at p. 169|Figure 5.18 at p. 174|





**Figure 5.15:** Results in terms of precision and recall obtained from evaluating the Leading Eigenvector against the gold standard after filtering the communities semantically. 

In conclusion, applying a semantic filter we observed a substantial improvement in the results, because it allows us to remove some outlier communities. Nonetheless we would like to investigate whether it is possible to further improve these results and in the next section we will show how these results have been further improved and how semantics keeps playing an important role in these enhancements. At this stage an improvement of the results means to let both precision and recall be high also for higher values of similarity. 

172 



**Figure 5.16:** Results in terms of precision and recall obtained from evaluating the Fuzzy C-Means against the gold standard after filtering the communities semantically. 



**Figure 5.17:** Results in terms of precision and recall obtained from evaluating the Clique Percolation Method against the gold standard after filtering the communities semantically. 

173 



**Figure 5.18:** Results in terms of precision and recall obtained from evaluating the Advanced Clique Percolation Method against the gold standard after filtering the communities semantically. 

174 

## **5.6 Semantic enhancement** 

We already observed in several cases that the adoption of semantics, e.g., taking advantage of the Computer Science Ontology, can help to improve the results. The ontology provided all the topics with _same-as_ relationships, so that we could produce a better match between clusters and debutant topics (see Eq. 5.2) and it also helped to filter the communities. With the aim of understanding whether the current results, showed in Fig. 5.14, 5.15, 5.16, 5.17, can be further improved, both clusters and the ancestors of the debutant topics have been enhanced using the _skos:broaderGeneric_ relationship within the Computer Science Ontology. This enhancement consists of merging clusters and debutant topics with their _super-areas_ . For instance, enhancing a set _Zx_ , which can be either a cluster or the ancestors of a debutant topic, consists of selecting all the super-areas of its topics and including them into the original set, as showed in Eq. 5.7. 





_enhanced_ ( _Zx_ ) = _topics_ ( _Zx_ ) _∪ SuperAreas_ ( _topics_ ( _Zx_ )) 

Given the possibility of enhancing both clusters and ancestors with their superareas, we tested all the possible strategies: 

Approach 1. Enhancement of clusters with super-areas against only the ancestors of debutant topics, labelled also as **(C** _∪_ **Sup) vs. D** 

Approach 2. Enhancement of debutant topics with super-areas against topics in the cluster, **C vs. (D** _∪_ **Sup)** 

Approach 3. Enhancement of clusters with super-areas against enhancement of debutant topics with super-areas, **(C** _∪_ **Sup) vs. (D** _∪_ **Sup)** 

175 

After enhancing both sets of clusters and debutant topics, we ran the different evaluations according to the previous three configurations. To this end, the similarity measure, defined in Eq. 5.2 at page 144, needs to be revisited so that it can consider these new enhanced sets. Equation 5.8 defines the new similarity measure, which combines clusters and debutant topics with their respective enhancements. It computes the Jaccard similary between the two enhanced sets: ( _Ci ∪ SAi ∪ ECi_ ) and ( _Dk ∪ EDk_ ). The first enhanced set includes the topics of the original cluster _Ci_ , their _same-as_ topics _SAi_ and their super-areas in _ECi_ . Instead, the second enhanced set includes the ancestors of the debutant topics _Dk_ and their super-areas _EDk_ . This new similarity measure is more comprehensive as it can suit all three approaches. 

In particular, when we test the first approach, we do not enhance the ancestors of debutant topic, therefore _EDk_ = _∅_ . Whereas, for the second approach _ECi_ = _∅_ , as we do not enhance the clusters. In addition, we can also observe that when there are no enhancements, i.e., _ECi_ = _EDk_ = _∅_ , Eq. 5.8 is similar to Eq. 5.2. We did not include the _same-as_ topics of the cluster _SAi_ in the denominator for the same reasons ponted out when describing Eq. 5.2. 









_EDk → enhancement of k_ - _th Debutant topic_ 



We compared the results obtained from the three different strategies, including 

also the results obtained when applying semantic filtering (Section 5.5). In Fig. 5.19, 5.20, 5.21, 5.22 and 5.23 are reported the results in terms of precision and recall for 

176 

the year 1999 for the five community detection algorithms. Each subplot reports four lines, three of different strategies and one, coloured in blue, that reports the results of the unchanged clusters and debutant topics. The results for Advanced Clique Percolation Method are reported in Fig. 5.18, for the other four algorithms in Fig. 5.14, 5.15, 5.16 and 5.17. 



**Figure 5.19:** Results in terms of precision and recall obtained from evaluating the Fast Greedy in year 1999 with different solution of semantic enhancement. 



**Figure 5.20:** Results in terms of precision and recall obtained from evaluating the Leading Eigenvector in year 1999 with different solution of semantic enhancement. 

177 



**Figure 5.21:** Results in terms of precision and recall obtained from evaluating the Fuzzy C-Means in year 1999 with different solution of semantic enhancement. 



**Figure 5.22:** Results in terms of precision and recall obtained from evaluating the Clique Percolation Method in year 1999 with different solution of semantic enhancement. 

From all these graph charts we can acknowledge that the adoption of the Computer Science Ontology to enhance the cluster and the debutant topics improved the results. Focusing on the results of the Advanced Clique Percolation Method in Fig. 5.23, choosing a similarity value of 0.1, for the _unchanged_ approach (blue line), the precision is around 0.7 and the recall 0.5. Whereas, at the same similarity value, the new 

178 



**Figure 5.23:** Results in terms of precision and recall obtained from evaluating the Advanced Clique Percolation Method in year 1999 with different solution of semantic enhancement. 

strategies have higher values of precision with a peak around 0.85, as well as high values of recall that reaches 0.77 for the third strategy (red line). A similar behaviour occurs for the results of other algorithms, such as the ones for Fast Greedy in Fig. 5.19. 

In general, we can see that all these approaches provide improved results that also appear to be far from the ones obtained with the unchanged approach (blue line). However, approach 3 (red line), which compares enhanced clusters and enhance debutant topics, provides even better results. Indeed, for all the tested algorithms, we can see that, for equal values of similarity, the third strategy has always higher values of precision and recall. 

Performing this evaluation in the years from 2000 to 2009, we observed a similar behaviour for all the five community detection algorithms. For instance, in Fig. 5.24 are reported the values of precision and recall for year 2000 for the Advanced Clique Percolation Method. 

As we can see, the different approaches perform in a similar way and approach 3 outperforms the others. In a similar way, the approach 3 outperforms the other 

179 



**Figure 5.24:** Results in terms of precision and recall obtained from evaluating the Advanced Clique Percolation Method in year 2000 with different solution of semantic enhancement. 

approaches in all the remaining years (2001-2009) and it also does it for the other four community detection algorithms. 

Since the third approach is performing better than others, in Fig. 5.25 are reported the values of precision and recall of its application on the Advanced Clique Percolation Method during the period of analysis (1999-2009). 

From the results, we can observe that from year 1999 to 2005 the values of precision and recall are quite high. Indeed, for a similarity value of 0.2, for those years, the values of precision go from 0.6 to 0.72, while the values of recall go from 0.36 to 0.55. However, those results start to gradually decrease for the years 2006 to 2009. We can see that for year 2006, for a similarity value of 0.2, the precision is 0.3 while the recall is 0.28. For the years from 2007 to 2009 the different values of precision are below 0.2 and values of recall are between 0.2 and 0.3. 

This decrease in performance can be justified by the fact that while the number of clusters returned from the evolutionary networks keeps growing over time, the number of debutant topics is decreasing, as showed in Fig. 5.26. 

180 



**Figure 5.25:** Results in terms of precision and recall obtained from evaluating the Advanced Clique Percolation Method after enhancing both clusters and debutant topics with their super-areas. 



**Figure 5.26:** Comparison between the amount of debutant topics and cluster, retrieved each year. 

In Fig. 5.27, 5.28, 5.29, 5.30, are reported the new values of precision and recall with different values of similarity, when using the third approach respectively Fast Greedy, Leading Eigenvector, Fuzzy C-Means and Clique Percolation Method. If we compare these results with those obtained when applying semantic filtering only (see Section 5.5) we can observe, for all approaches, an increase of performance in both 

181 

precision and recall. In Table 5.15 are reported the different indexes of figures showing the results across different sections: only clustering (Section 5.4), applying semantic filtering (see Section 5.5) and this semantic enhancement. 

**Table 5.15:** Figures comparison for each approach, when using only the clustering techniques, when applying semantic filtering and when enhancing semantically the set of clusters and debutants. 

|**Method**|**Only clustering**|**Semantic filtering**|**Semantic Enhancement**|
|---|---|---|---|
|FG|Figure 5.5 at p. 155|Figure 5.14 at p. 170|Figure 5.27 at p. 182|
|LE|Figure 5.6 at p. 157|Figure 5.15 at p. 172|Figure 5.28 at p. 183|
|FCM|Figure 5.8 at p. 161|Figure 5.16 at p. 173|Figure 5.29 at p. 184|
|CPM|Figure 5.10 at p. 165|Figure 5.17 at p. 173|Figure 5.30 at p. 184|
|ACPM|Figure 5.13 at p. 169|Figure 5.18 at p. 174|Figure 5.25 at p. 181|





**Figure 5.27:** Results in terms of precision and recall obtained from evaluating the Fast Greedy after enhancing both clusters and debutant topics with their super-areas. 

In brief, by observing the results, we can see that applying semantic filters and enhancing both the topics in the communities and the ancestors of debutant topics boost the performance of each approach, with the Advanced Clique Percolation Method outperforming the other four tested algorithm. 

182 



**Figure 5.28:** Results in terms of precision and recall obtained from evaluating the Leading Eigenvector after enhancing both clusters and debutant topics with their super-areas. 

Table 5.16, 5.17 and 5.18 provide another perspective on the obtained results. They show the results with a fixed similarity threshold, Table 5.16 for similarity threshold equal to 0.1, Table 5.17 for 0.15, and Table 5.18 for 0.2. As we can see the ACPM algorithm, for a given similarity threshold outperforms the other four algorithms. A noticeable outlier in Table 5.16 and 5.17 is in the results of Fuzzy C- Means (FCM) in the year 2000, where we can find 0.96 of precision. This aberration is due to three topics that were constantly encountered, which were matching the ancestor of a debutant topic, as explained in Section 5.4.5. 

183 



**Figure 5.29:** Results in terms of precision and recall obtained from evaluating the Fuzzy C-Means after enhancing both clusters and debutant topics with their superareas. 



**Figure 5.30:** Results in terms of precision and recall obtained from evaluating the Clique Percolation Method after enhancing both clusters and debutant topics with their super-areas. 

184 

**Table 5.16:** Values of Precision and Recall for the five approaches along time, at similarity value of 0.1. In bold the best results. 

|||FG||LE|F|CM|C|PM|**AC**|**PM**|
|---|---|---|---|---|---|---|---|---|---|---|
|Years|Pr|Re|Pr|Re|Pr|Re|Pr|Re|**Pr**|**Re**|
|1999|.27|.11|.00|.00|.00|.00|.06|.01|**.86**|**.76**|
|2000|.21|.07|.14|.02|.96|.01|.05|.00|**.78**|**.70**|
|2001|.13|.04|.11|.01|.00|.00|.17|.00|**.77**|**.72**|
|2002|.14|.04|.11|.01|.00|.00|.29|.01|**.82**|**.80**|
|2003|.09|.02|.20|.02|.00|.00|.08|.02|**.83**|**.79**|
|2004|.11|.05|.06|.00|.00|.00|.00|.00|**.84**|**.68**|
|2005|.07|.11|.06|.01|.00|.00|.00|.00|**.71**|**.66**|
|2006|.01|.01|.07|.01|.00|.00|.00|.00|**.43**|**.51**|
|2007|.01|.08|.00|.00|.00|.00|.00|.00|**.28**|**.44**|
|2008|.01|.04|.00|.00|.00|.00|.00|.00|**.15**|**.33**|
|2009|.00|.00|.00|.00|.00|.00|.00|.00|**.09**|**.76**|



**Table 5.17:** Values of Precision and Recall for the five approaches along time, at similarity value of 0.15. In bold the best results. 

|||FG||LE|F|CM|C|PM|**AC**|**PM**|
|---|---|---|---|---|---|---|---|---|---|---|
|Years|Pr|Re|Pr|Re|Pr|Re|Pr|Re|**Pr**|**Re**|
|1999|.12|.06|.00|.00|.00|.00|.03|.00|**.81**|**.65**|
|2000|.14|.02|.00|.00|.96|.01|.00|.00|**.75**|**.55**|
|2001|.04|.00|.00|.00|.00|.00|.17|.00|**.73**|**.63**|
|2002|.07|.01|.00|.00|.00|.00|.29|.01|**.81**|**.70**|
|2003|.07|.01|.20|.01|.00|.00|.08|.02|**.80**|**.73**|
|2004|.07|.03|.06|.00|.00|.00|.00|.00|**.74**|**.58**|
|2005|.05|.04|.00|.00|.00|.00|.00|.00|**.68**|**.59**|
|2006|.00|.00|.00|.00|.00|.00|.00|.00|**.35**|**.38**|
|2007|.00|.00|.00|.00|.00|.00|.00|.00|**.24**|**.36**|
|2008|.00|.00|.00|.00|.00|.00|.00|.00|**.14**|**.25**|
|2009|.00|.00|.00|.00|.00|.00|.00|.00|**.07**|**.59**|



185 

**Table 5.18:** Values of Precision and Recall for the five approaches along time, at similarity value of 0.2. In bold the best results. 

|||FG||LE|F|CM|C|PM|**AC**|**PM**|
|---|---|---|---|---|---|---|---|---|---|---|
|Years|Pr|Re|Pr|Re|Pr|Re|Pr|Re|**Pr**|**Re**|
|1999|.08|.03|.00|.00|.00|.00|.03|.00|**.64**|**.41**|
|2000|.03|.00|.00|.00|.00|.00|.00|.00|**.57**|**.33**|
|2001|.04|.00|.00|.00|.00|.00|.17|.00|**.63**|**.44**|
|2002|.04|.00|.00|.00|.00|.00|.07|.01|**.70**|**.50**|
|2003|.02|.00|.20|.01|.00|.00|.08|.02|**.70**|**.51**|
|2004|.04|.02|.06|.00|.00|.00|.00|.00|**.66**|**.42**|
|2005|.04|.02|.00|.00|.00|.00|.00|.00|**.56**|**.43**|
|2006|.00|.00|.00|.00|.00|.00|.00|.00|**.30**|**.28**|
|2007|.00|.00|.00|.00|.00|.00|.00|.00|**.15**|**.28**|
|2008|.00|.00|.00|.00|.00|.00|.00|.00|**.12**|**.17**|
|2009|.00|.00|.00|.00|.00|.00|.00|.00|**.03**|**.24**|



186 

## **5.7 Discussion** 

Throughout this chapter, we analysed the different steps that we have undertaken to assess the validity of Augur and the other clustering algorithms. We started with a number of community detection algorithms that were available in the state of the art. We saw that they do not provide good results but, at the same time, they allowed us to understand the specialities of the evolutionary networks we were dealing with. Hence, we realised that we needed a new approach, which could take into account all the characteristics of the networks, e.g., weights, and could also cope with the fact the networks appear to be very dense in certain areas. The Advanced Clique Percolation Method provided good results, and we succeeded in improving them further by means of semantic filtering and semantic enhancement techniques. These allowed us to increase precision and recall at higher values of similarity. 

Nonetheless, there are still some issues that need to be further investigated. Specifically, the sections that follow seek to explore the following questions: 

- What is the appropriate value of similarity for a match? 

- Why precision and recall decrease in the last years of the analysed decade? 

- What else can be done to improve the results? 

We will discuss these aspects to better assess the validity of Augur. 

### **5.7.1 When does a cluster match a debutant topic?** 

The aim of the evaluation is to determine the effectiveness of Augur in returning a set of clusters containing topics that are increasing their degree of collaboration over time, which will eventually lead to the emergence of a new research area. In brief, to evaluate such effectiveness, we performed the following steps: 

187 

- run the five community detection algorithms on the evolutionary networks form 1999 to 2009, according to Table 5.1; 

- for each approach, compare the clusters returned each year with the ancestors of areas that actually emerged in the following two years (see Table 5.2 at page 135) for different similarity values. 

Throughout this chapter, the results in terms of precision and recall of each approach, have been presented as a function of the similarity value. In particular, observing the results we obtained for the last approach (see Fig. 5.25), a similarity value that offers a good balance in performance and is also valid across the years is being considered 0.2. Given this value, precision stays high (0.6-0.71) for the years from 1999 to 2005, while recall is in the range 0.43 to 0.63. 

Table 5.19 reports two comparisons between communities and ancestors of debutant topics that are considered similar because their similarity is above 0.2. In both cases the clusters match with the _Semantic Search_ topic. This phenomenon, in which two or more clusters can match the ancestors of a specific debutant topic, is recurrent in the results and will be further investigated in the next section, while here we will focus on the chosen similarity value. 

From the table, we can see that 14 out of 19 topics within the first cluster (marked in bold) match ancestors (also marked in bold) of the topic _Semantic Search_ , which debuted in 2003. The similarity value between the community and the debutant topic is 0.425. A topic marked in bold and appearing in only one set (either cluster or ancestors fo debutant topic), matched thanks to the semantic enhancement. 

For the second community, instead, 16 out of 19 topics in the cluster matched the ancestors of _Semantic Search_ and their similarity stands at 0.413. According to these results it seems that a cluster covers particularly well the debutant topics with a similarity above 0.4. So far we observed similarities between clusters and debutant 

188 

topics that double the chosen similarity value of 0.2. **So, what can be said when there is a match with similarity of 0.2?** 

**Table 5.19:** Matchings between cluster and debutant topics with similarity measure over 0.2. In this case the two clusters match the same debutant topic: _Semantic Search_ 

|**Cluster**|**Ancestors of debutant topic**|**Debutant**<br>**topic**|
|---|---|---|
|**world wide web**, **query**<br>**languages**,<br>**metadata**,<br>**content based retrieval**,<br>**information**<br>**retrieval**,<br>**search**<br>**engines**,<br>**xml**,<br>**information**<br>**systems**,<br>**information**<br>**retrieval**<br>**systems**,<br>**servers**,<br>**digi-**<br>**tal**<br>**libraries**,<br>**indexing**<br>**(of**<br>**information)**,<br>**text**<br>**processing**,<br>**electronic**<br>**commerce**,<br>multi<br>agent<br>systems, intelligent agents,<br>information<br>management,<br>web browsers, classification<br>(of information)|**world wide web**, **query lan-**<br>**guages**,<br>**metadata**,<br>**content**<br>**based retrieval**, **information**<br>**retrieval**,<br>**search**<br>**engines**,<br>**xml**, **information systems**, **in-**<br>**formation retrieval systems**,<br>**search**<br>**engine**,<br>**hypertext**<br>**systems**,<br>**query**<br>**processing**,<br>**natural language processing**<br>**systems**, safety devices, seman-<br>tics,<br>mathematical expressions,<br>enabling technologies, websites,<br>human computer interaction, so-<br>cial networking (online), current<br>system, ontology, tools, internet,<br>telecommunication equipment|Semantic Search<br>(debuting<br>in<br>2003<br>and<br>ac-<br>cording<br>to<br>Eq.<br>5.8<br>the<br>value<br>of<br>similarity<br>is<br>0.425)|
|**world wide web**, **query**<br>**languages**,<br>**metadata**,<br>**content based retrieval**,<br>**information**<br>**retrieval**,<br>**search**<br>**engines**,<br>**xml**,<br>**information**<br>**retrieval**<br>**systems**, **servers**, **client**<br>**server**<br>**computer**<br>**sys-**<br>**tems**,<br>**digital**<br>**libraries**,<br>**indexing**<br>**(of**<br>**infor-**<br>**mation)**,<br>**html**,<br>**text**<br>**processing**,<br>**network**<br>**protocols**,<br>**electronic**<br>**commerce**, java program-<br>ming language, information<br>management, web browsers|**world wide web**, **query lan-**<br>**guages**,<br>**metadata**,<br>**content**<br>**based retrieval**, **information**<br>**retrieval**,<br>**search**<br>**engines**,<br>**xml**,<br>**information**<br>**retrieval**<br>**systems**,<br>**search**<br>**engine**,<br>**hypertext**<br>**systems**,<br>**query**<br>**processing**, **natural language**<br>**processing**<br>**systems**,<br>safety<br>devices, semantics, mathematical<br>expressions,<br>enabling technolo-<br>gies, websites, human computer<br>interaction,<br>social<br>networking<br>(online),<br>information<br>systems,<br>current system, ontology, tools,<br>internet,<br>telecommunication<br>equipment|Semantic Search<br>(value of similar-<br>ity is 0.413)|



189 

In Table 5.20, we report two comparisons between clusters and debutant topics with values of similarity just above 0.2. As we can see, in the first comparison 6 of the 15 topics in the cluster match the ancestors of _Resource Description Framework_ with a similarity measure of 0.21. However, looking at the list of topics within the cluster, among those that did not match there are topics that could be considered very far from the debutant topic. In particular, _Three Dimensional Computer Graphics_ , _Theorem Proving_ , and _Image analysis_ are unrelated to the first topics that match _Resource Description Framework_ . Looking at the network in Fig. 5.31, we can actually observe the existence of two different sections that are grouped together, the topics that matched (and coloured in red) and the ones that did not match (coloured in blue). We can observe that since there are many links that cross the two groups, the algorithm is unable to split this cluster in the two parts. Nonetheless, the results are still valuable. With a similar value of similarity, the second cluster matches 5 of 9 topics with the ancestors of debutant topics. These results suggest that with only 5 topics, the match between the two sets is still significant. A future improvement of Augur would be the refinement of the Advanced Clique Percolation Method so that it can further split the network in Fig. 5.31 in further subnetworks. 

Table 5.19, reports a case in which two (or in some other cases more) communities match the same debutant topic. Analysing qualitatively the matches between clusters and debutant topics, we realised that, as two or more communities can match the same debutant topic, in a similar way one community can match more than one debutant topic, making the relationship between the clusters and debutant topics _many-to-many_ . In brief, this qualitative analysis over the matches between clusters and ancestors of debutant topics allows us to observe that with a similarity of 0.2, we have significant matches (see Table 5.20). However, these results pose a new question 

> 7According to Wikipedia ( `https://en.wikipedia.org/wiki/Resource_Description_ Framework` ) the topic _Resource Description Framework_ debuted in 1997. However, in our dataset, the first paper tagged with this keyword appears in the year 2000. 

190 

**Table 5.20:** Matchings between cluster and debutant topics with similarity measure just above 0.2. 

|**Cluster**|**Ancestors of debutant topic**|**Debutant**<br>**topic**|
|---|---|---|
|**query languages**, **infor-**<br>**mation retrieval**, **artifi-**<br>**cial**<br>**intelligence**,<br>**world**<br>**wide web**, **management**<br>**information systems**, **re-**<br>**lational**<br>**database**<br>**sys-**<br>**tems**, computational geom-<br>etry, image analysis, data<br>reduction,<br>knowledge<br>ac-<br>quisition, three dimensional<br>computer graphics,<br>mem-<br>bership<br>functions,<br>graph<br>theory,<br>theorem<br>proving,<br>vectors|**query languages**, **information**<br>**retrieval**,<br>**artificial**<br>**intel-**<br>**ligence**,<br>**world**<br>**wide**<br>**web**,<br>**management**<br>**information**<br>**systems**,<br>**natural**<br>**language**<br>**processing**<br>**systems**,<br>**multi**<br>**agent**<br>**systems**,<br>**expert**<br>**sys-**<br>**tems**,<br>**xml**,<br>**search**<br>**engines**,<br>semantics,<br>metadata,<br>intelli-<br>gent<br>agents,<br>interoperability,<br>html,<br>algorithms,<br>data<br>com-<br>munication<br>systems,<br>security<br>of<br>data,<br>schemas,<br>linguistics,<br>resource<br>allocation,<br>constraint<br>theory, software agents, network<br>protocols, websites|Resource<br>De-<br>scription Frame-<br>work<br>(debuting<br>in<br>2000<sup>7</sup><br>and<br>according to Eq.<br>5.8<br>the<br>value<br>of<br>similarity<br>is<br>0.21)|
|**database systems**, **data**<br>**mining**, **data structures**,<br>**world wide web**, **knowl-**<br>**edge engineering**, learn-<br>ing systems, genetic algo-<br>rithms,<br>multilayer<br>neural<br>networks, decision theory|**database systems**, **data min-**<br>**ing**, **data structures**, **world**<br>**wide web**, **knowledge engi-**<br>**neering**,<br>**information**<br>**analy-**<br>**sis**, **semantic web**, semantics,<br>ontology,<br>information<br>systems,<br>knowledge management, knowl-<br>edge representation, management<br>information systems, mathemati-<br>cal models, information technol-<br>ogy, computer aided software en-<br>gineering, metadata, natural lan-<br>guage processing systems, tax-<br>onomies, knowledge based sys-<br>tems, software engineering, infor-<br>mation retrieval, research, data<br>processing, formal languages|Ontology<br>Engi-<br>neering<br>(debut-<br>ing in 2002 and<br>according to Eq.<br>5.8<br>the<br>value<br>of<br>similarity<br>is<br>0.21)|



191 



**Figure 5.31:** Community extracted from the evolutionary network of year 1999 that matches with _Resource Description Framework_ debuting in 2000. Red nodes are the matched topics, blue nodes are the unmatched topics. 

on why there is this _many-to-many_ relationship between clusters and debutant topics, which will be addressed in the next section. 

### **5.7.2 Why clusters can match more than one debutant topic** 

### **and vice versa?** 

The relationship between clusters and debutant topics is _many-to-many_ . Indeed, our evaluation metrics (see Section 5.4.1) were designed to capture such phenomenon. An 

192 

example in which two communities match the same debutant topic, _Semantic Search_ , is reported in the previous section (Table 5.19). An example, instead, in which the same community match two debutant topics, like _Lexical Resources_ and _Ontology Learning_ , is reported in Table 5.21. 

The reason why two communities can match the same debutant topic is because even if the communities are different, they can share a good portion of topics, like a signature. Observing the two communities in Table 5.19, the topics that match with the ancestor of _Semantic Search_ (marked in bold) are very alike. Indeed, using Eq. 5.8, the similarity between those two clusters is 0.733. 

If we consider how those communities have been extracted (see Section 4.3.2), we can see that the reason why there are very similar clusters, like the ones in the example, is because two local maxima in the evolutionary network are very close to each other. This is reasonable since the _Computer Science_ environment is very wellknit and highly dynamic. Two topics not so far apart can be the centre of two different movements, but because they are not so far apart, when the algorithm extracts one’s neighbourhood, the other maximum with part of its community gets dragged in. This is logical as we are looking for overlapping communities, since the assumption is that one topic can foster the emergence of more than one new research area. However, this could be seen as a resolution issue when extracting the neighbourhoods of local maxima. If the resolution is very low, the cluster might not include some important topics and eventually fail to match any of the ancestors of debutant topics, leading to low precision. On the contrary, if the resolution is very large the cluster will include many topics and then it will match almost every debutant topic. 

Figure 5.32 depicts the network which combines the two communities. The nodes in red are those which match the ancestors of the debutant topics, while the nodes in green and blue are those belonging to the respective communities that did not match. 

193 

As we can see, the two communities share many topics and very likely the two local maxima that generated them were not so far from each other. 



**Figure 5.32:** Community extracted from the evolutionary network of year 2003 that matches with _Lexical Resources_ and _Ontology Learning_ , respectively debuting in 2005 and 2004. Red nodes are the matched topics, while blue and green nodes are the topics that did not match with the ancestors of the two debutant topics. 

Lets explore now the issue of **why one or more debutant topics can be matched by the same cluster?** As we can see in the first row of Table 5.21, 15 of 18 topics (marked in bold) of a community extracted from the evolutionary network of the year 2003 matched the ancestors of _Lexical Resources_<sup>8</sup> with a similarity measure of 0.393. In the second row, instead, 13 of the 18 topics in the same cluster matched 

> 8 `https://en.wikipedia.org/wiki/Lexical_resource` 

194 

the ancestors of _Ontology Learning_ with 0.348 as similarity measure. The two topics debuted respectively in the years 2005 and 2004, and while it may seem obvious that the community is pushing the emergence of new research areas in two different years, there are other communities that can match more than two topics in the same year. 

**Table 5.21:** Example of matching between one clusters and multiple debutant topics. 

|**Cluster**|**Ancestors of debutant topic**|**Debutant**<br>**topic**|
|---|---|---|
|**world wide web**, **query**<br>**languages**,<br>**natural**<br>**language processing sys-**<br>**tems**, **database systems**,<br>**artificial**<br>**intelligence**,<br>**information**<br>**retrieval**<br>**systems**,<br>**information**<br>**retrieval**,<br>**syntactics**,<br>**computer programming**<br>**languages**,<br>**metadata**,<br>**xml**,<br>**multi**<br>**agent**<br>**sys-**<br>**tems**,<br>**servers**,<br>**search**<br>**engines**,<br>**information**<br>**management**,<br>electronic<br>commerce, software agents,<br>intelligent agents|**world wide web**, **query lan-**<br>**guages**,<br>**natural**<br>**language**<br>**processing systems**, **database**<br>**systems**,<br>**artificial**<br>**intelli-**<br>**gence**, **information retrieval**<br>**systems**,<br>**information**<br>**re-**<br>**trieval**, **syntactics**, **semantic**<br>**web**, **natural language pro-**<br>**cessing**,<br>**text**<br>**processing**,<br>**wordnet**, **computational lin-**<br>**guistics**,<br>semantics,<br>ontology,<br>linguistics,<br>information<br>theory,<br>international conferences,<br>word<br>processing, terminology, natural<br>languages,<br>lexical<br>semantics,<br>algorithms,<br>thesauri,<br>semantic<br>relations|Lexical<br>Re-<br>sources<br>(debut-<br>ing in 2005 and<br>according to Eq.<br>5.8<br>the<br>value<br>of<br>similarity<br>is<br>0.393)|
|**world wide web**, **query**<br>**languages**,<br>**natural**<br>**language**<br>**processing**<br>**systems**,<br>**artificial**<br>**in-**<br>**telligence**,<br>**information**<br>**retrieval**,<br>**information**<br>**management**,<br>**search**<br>**engines**, **computer pro-**<br>**gramming**<br>**languages**,<br>**metadata**,<br>**syntactics**,<br>**xml**,<br>**servers**,<br>**multi**<br>**agent systems**, database<br>systems,<br>electronic<br>com-<br>merce, information retrieval<br>systems,<br>software<br>agents,<br>intelligent agents|**world wide web**, **query lan-**<br>**guages**,**natural language pro-**<br>**cessing systems**, **artificial in-**<br>**telligence**,<br>**information**<br>**re-**<br>**trieval**, **information manage-**<br>**ment**,<br>**search**<br>**engines**,<br>**web**<br>**services**, **semantic web**, **natu-**<br>**ral language processing**,**com-**<br>**putational linguistics**, **learn-**<br>**ing systems**, ontology, seman-<br>tics, taxonomies, education, in-<br>formation theory, knowledge ac-<br>quisition,<br>learning<br>algorithms,<br>data mining, linguistics, interna-<br>tional conferences, ontology engi-<br>neering, domain ontologies, tech-<br>nology|Ontology Learn-<br>ing (debuting in<br>2004 and accord-<br>ing to Eq.<br>5.8<br>the value of sim-<br>ilarity is 0.348)|



195 

This can be justified by the fact that two debutant topics can share some parts of their “DNA” as they can have similar ancestors. As a result the community that contains this shared part will match both debutant topics. Indeed, _Ontology Learning_ and _Lexical Resources_ do share many ancestors, and according to Eq. 5.8, their similarity, in terms of shared ancestors, is 0.515. This means that the two debutant topics are more similar between themselves than each of them is to the cluster. 

Further, from this analysis it emerged that a cluster extracted from the evolutionary network of year 2004 matched over 40 debutant topics within the years 2005 and 2006. This cluster, whose network is depicted in Fig. 5.33, contains 10 topics: _Network Protocols_ , _Security_ , _Security Of Data_ , _Cryptography_ , _Authentication_ , _Wireless Telecommunication Systems_ , _Servers_ , _Public Key Cryptography_ , _Data Privacy_ , _Network Security_ . The debutant topics that have been matched with this community are all related to the _Security_ field, and are: 

_Secure Data_ (with similarity = 0.452), _Authenticated Key Exchange_ (0.449), _Symmetric Keys_ (0.449), _Man In The Middle Attacks_ (0.441), _Bilinear Pairing_ (0.433), _Keys (for Locks)_ (0.433), _Identity Based Cryptography_ (0.425), _Key Pre-Distribution_ (0.424), _Key Establishments_ (0.424), _Bilinear Map_ (0.417), _Anonymous Authentication_ (0.417), _Improved Scheme_ (0.400), _Security Challenges_ (0.391), _Security Frameworks_ (0.391), _Sensitive Datas_ (0.382), _Various Attacks_ (0.382), _Heterogeneous Sensor Networks_ (0.364), _Forgery Attacks_ (0.351), _Unforgeability_ (0.351), _Rfid Systems_ (0.333), _Homomorphic-Encryptions_ (0.333), _Encrypted Data_ (0.324), _Phishing_ (0.324), _Secret Information_ (0.324), _Diffie-Hellman Assumption_ (0.315), _Malicious Activities_ (0.296), _Privacy Issue_ (0.275), _Phishing Attacks_ (0.275), _Side-Channel Analysis_ (0.270), _Sybil Attack_ (0.265), _Rfid Applications_ (0.265), _Cyber-Attacks_ (0.260), _Biometric Data_ (0.260), _Trojans_ (0.260), _Public-Key Encryption Scheme_ (0.256), _Malicious Nodes_ (0.254), _Malwares_ (0.250), _Private Data_ (0.242), _Hash Value_ (0.239), _Malicious Software_ (0.237), _Privacy Preservation_ (0.229), _Secret Mes-_ 

196 

_sages_ (0.229), _Sql Injection_ (0.216), _K-Anonymity_ (0.206), _Network Attack_ (0.206), _Privacy Requirements_ (0.206). In this case, we can observe a common movement in an area that can spawn multiple related topics. 



**Figure 5.33:** Community of topics extracted in the evolutionary network of year 2004 that matched with more 40 debutant topics in the following two years. 

### **5.7.3 To what extent the number of ancestors can influence the performance of Augur?** 

When extracting the ancestors of each debutant topic, in Section 5.3.2, we selected the first 25 meaningful topics. In this analysis we want to understand whether the number of ancestors for a debutant topic can influence the results. To this end, the debutant topics have been recomputed and enhanced with a different number of ancestors. The selection of 25 ancestors may already seem excessive and further increasing this number would mean increasing the chances of drawing some topics 

197 

that not should necessarily be considered ancestors (see Section 3.9). Therefore, we reduced the number of ancestors to 20 and 15. 

We performed this analysis only with the clusters of the Advanced Clique Percolation Method, as it outperformed the other four community detection algorithms. These clusters have been evaluated against these two newly computed sets of debutant topics and the results are reported in Fig. 5.34 and Fig. 5.35. We can see that reducing the number of ancestors slightly affects the value of precision and recall, but they are still good results. This suggests that using 25 ancestors for each debutant topic is a good solution. 



**Figure 5.34:** Results in terms of precision and recall obtained from evaluating the Advanced Clique Percolation Method against the gold standard with 15 ancestors. Both clusters and debutant topics have been enhanced with their super-areas. 

198 



**Figure 5.35:** Results in terms of precision and recall obtained from evaluating the Advanced Clique Percolation Method against the gold standard with 20 ancestors. Both clusters and debutant topics have been enhanced with their super-areas. 

### **5.7.4 What else can be said regarding the decrease of performance in the last period of analysis?** 

Throughout this chapter, we have seen in many occasions that the performances were decreasing in the last period of analysis. In particular, both precision and recall were affected because fewer and fewer clusters could be effectively matched with the ancestors of debutant topics. The main reason is certainly the lack of data, as showed in Fig. 5.2 on page 139. During the period of analysis, we have a constantly increasing number of clusters while the number of emerging areas substantially decreases after 2006. In the year 2010 only 12 topics emerge and even fewer in the following years. The reasons of this decrease in the number of debutant topics are uncertain. One might argue that maybe the corpus does not contain enough data that cover those years, but actually, as showed in Fig. 5.36, the number of papers keeps increasing year by year, while debutant topics decrease. Although it is hard to believe that, 

199 

in reality, the number of debutant topics decreases over time, in particular with the observed rate, **what else can be said for the clusters that did not find a match because of the lack of emerging topics?** 



**Figure 5.36:** Comparison between the constant increase of published papers and the decrease of emerging topics each year. 

Comparing the set of clusters against the set of debutant topics, leads to four different cases, as reported in Section 5.4.1. 

Here we want to focus our attention to the case in which clusters do not match debutant topics: the _false positives_ . 

A cluster embodies certain dynamics, topics that are tightening their relationships and their collaboration is becoming more intense. The debutant topic is the result of this close relationship and serves as a label for this intense multidisciplinary activity. However, we can argue that is not always guaranteed that an increased collaboration will always lead to the emergence of a new area. It might be the case that two or more topics are increasing their collaboration towards a particular common aim that eventually will not turn into a new area. Nonetheless, this collaboration can still be meaningful and relevant for the stakeholders. Hence, it might be the case that _even if the cluster does not match any debutant topic, it can still provide important information_ . 

200 

To this end, we performed a more qualitative investigation over these specific communities to asses if Augur was detecting community of topics that would keep growing and influence the research landscape. For each cluster (at year _t_ ), we extracted the portion of network containing the topics that generated the cluster (from the evolutionary network at year _t_ ) and also the same portion of network in the following year (from the evolutionary network at year _t+1_ ), to understand how these communities developed in time. This analysis allowed me to classify those clusters in four further categories: 

- Category 1. **Strengthening Ties** : The links that those two networks share are increasing their intensity in year _t+1_ , meaning that the topics of this cluster are still increasing their pace of collaboration over time 

- Category 2. **Network Expansion** : The network at year _t+1_ introduces new links between the topics, compared to the network at year _t_ , meaning that the network is growing in terms of its relationships 

- Category 3. **Strengthening Ties and Network Expansion** : The network _t+1_ exhibits a growth in terms of new links and also the old links are increasing in intensity 

- Category 4. **No development** : The network at year _t+1_ is not showing any development compared to the network at year _t_ . 

In Fig. 5.37, we reported a bar chart that shows how the unmatched cluster can be classified according to the previous categories, yearly. In general, we can see that almost 72% of the unmatched clusters are amplifying and/or expanding their relationships. The rest remains undeveloped. In accordance to Fig. 5.25, in the year 2006 when precision starts to fall, there are more clusters that are unmatched. However, even if these clusters cannot be labelled with emerging topics, we can see that for most 

201 

of them, their inner topics are still involved in this process of development. Indeed, for the year 2006, there are 39 active clusters against 4. In year 2007, 56 unmatched clusters will further develop in the next year against 12. In 2008 and 2009 the clusters that remain undeveloped increase but their counterpart is still high. Indeed, in year 2008 there are 61 developing clusters against 46 “static” ones and in 2009 there are 91 developing clusters against 39. In conclusion, even if there is not enough data in the last period of analysis, in terms of emerging topics, to support the evaluation in matching clusters, we can still observe that most of the unmatched clusters continue to develop with their topics either amplifying their relationships, or embracing new ones, or both. 

For the sake of curiosity, we conducted a similar analysis over the matched clusters. All the clusters have been analysed and categorised according to the four groups previously mentioned. From Fig. 5.38, we can observe that 79% of clusters continue their development in the following year, while 21% of them remain undeveloped. From the bar chart, we can observe that, over time, the most prominent form of development is that the inner topics create new relationships: 42.6% (violet bar), while 19% of clusters are both strengthening their relationships and expanding the network (green bar). Instead, just 3.5% of clusters are strengthening their ties only (orange bar). This can be justified by the fact that, as a new area emerges, the topics in the cluster reduce their collaboration as they now might focus on the new area. Nonetheless, new collaborations between these topics can still be established. From the bar chart, we can also observe the presence of some clusters that did not show any development in the following year (pink bar). For this particular subset of clusters, it might be the case that the new topic is drastically changing the dynamics of the clusters. Since a new topic just stemmed out, most of the topics in the cluster can start to collaborate more with the newborn rather than continuing to collaborate 

202 

with their peers. In other words, the emerging topic is draining the degree of their collaboration. 





**Figure 5.37:** Differences in how the unmatched clusters, obtained in a certain year, develop in the following year. A cluster can strengthen its ties, expand its network, both expand its network and strengthen its ties, or not developing. 

203 





**Figure 5.38:** Differences in how the matched clusters, obtained in a certain year, develop in the following year. A cluster can strengthen its ties, expand its network, both expand its network and strengthen its ties, or not developing. 

### **5.7.5 Why are there still unmatched debutant topics?** 

From the results reported in Fig. 5.25, we observed that the values of recall fluctuate between 0.3 and 0.8 and they also tend to decrease in the last period of analysis. This means that some of the emerging topics do not match the returned clusters. Table 5.22 reports, for each year, the number of debutant topics that received a match and 

204 

also those which did not. Understanding the reasons why there are still unmatched debutant topics allows us to understand how we can further improve Augur and perhaps can tell us more about the dynamic of debutant topics. 

**Table 5.22:** Number of matched and unmatched debutant topics in the years from 2000 to 2011 

|**Year**|**Matched**<br>**Debutant**<br>**topics**|**Non-matched**<br>**debutant**<br>**topics**|
|---|---|---|
|2000|122|27|
|2001|165|29|
|2002|184|37|
|2003|179|37|
|2004|123|14|
|2005|206|35|
|2006|110|24|
|2007|44|16|
|2008|16|11|
|2009|5|7|
|2010|9|3|
|2011|4|1|



The reasons why a debutant topic is left unmatched can be twofold. The first possibility is that for such debutant topic we were unable to find its right ancestors. The second possibility is instead that Augur fails to locate the clusters that could eventually match the ancestors of the debutant topics. 

To verify the first hypothesis, we manually checked the ancestors of some unmatched debutant topics and see whether there were unrelated topics. Here, we observed that the ancestors appear to be accurate and related to the debutant topic in question. For example, the ancestors of the unmatched topic _Wearable Devices_ , which appear to be reasonable, are _Wearable Computers_ , _Mobile Computing_ , _Sensors_ , _Wearable Computing_ , _Pervasive Computing_ , _Human Engineering_ , _Ubiquitous Computing_ , _Algorithms_ , _Kinematics_ , _Forecasting_ , _Patient Monitoring_ , _Data Acquisition_ , _Data Processing_ , _Computer Operating Systems_ , _Tracking (position)_ , _Biomedical_ 

205 

_Equipment_ , _Social Interactions_ , _Sensor_ , _Accelerometer_ , _Potential Applications_ , _Wireless Telecommunication Systems_ , _Textiles_ . Given such evidence we can reject the first hypothesis. 

To verify the second hypothesis, we computed the overall pace of collaboration of each network of ancestors, related to both matched and unmatched debutant topics. 

In particular, for each debutant topic, we selected the portion of network containing their ancestors in the year priors to their debut. Then we computed the overall pace of collaboration. Since each link of the network expresses the pace of collaboration between the two nodes (see Section 4.2), computing the overall pace of collaboration for this portion of the network involves computing the average of the weights of all the links. Finally, we collected and then compared the pace of collaboration for the two groups, matched and unmatched debutant topics. In Fig. 5.39 are reported the two distributions of pace of collaboration obtained from the networks of both matched and unmatched debutant topics. Specifically, the line charts report the frequency (in percentage) of the pace of collaboration computed from the networks, related to the two groups. In general, we can see that more than 50% of the unmatched debutant topics (red line) have pace of collaboration smaller than 0. By contrast, more than 75% of the matched debutant topics (blue line) have pace of collaboration greater than 0. The mean value of pace of collaboration obtained from networks associated to unmatched topics is 0.02, while the mean value of pace of collaboration of the other group is 0.29. 

We analysed the pace of collaboration because Augur returns the communities that exhibit high values of pace of collaboration. If a portion of network, similar to the one containing the ancestors of a debutant topic, has a low value of pace of collaboration, it might be concealed by areas that exhibit higher values. Considering that this analysis allowed us to acknowledge that the pace of collaboration associated to the unmatched debutant topics is in general lower than the pace of collaboration associated to the 

206 



**Figure 5.39:** Distributions of pace of collaboration valued from the networks of ancestors of both matched and unmatched debutant topics. 

other group, we can conclude that the reason why there are still unmatched debutant topics is because Augur is not returning all the needed clusters. This can be due to the fact that their ancestors have a low pace of collaboration or because some topics may indeed come into existence more abruptly as new technologies or emerge through new discoveries. 

### **5.7.6 Can authors support the identification of emerging areas?** 

The evaluation so far consisted of verifying which of the returned clusters can match one of the emerging topics. This match was performed between the topics of each cluster and the ancestors of the debutant topics. 

However, another source of information that could be employed is the _authors_ . Indeed, Augur crawls the different evolutionary networks and, for each of them, returns a set of clusters, containing topics that exhibit an increase in the pace of collabora- 

207 

tion, as well as a set of authors that are considered active (see Section 4.4.2). The latter information can be used during the evaluation as a way to confirm the matches between the clusters and the debutant topics. The idea is that, given a cluster, the active authors are the most active authors in that particular set of topics. They are the leaders of this dense collaboration between the different topics and potentially they will also be the first people to publish in this brand-new area fostered by this multidisciplinarity. 

Based on this assumption, enriching the gold standard with authors who were the first to publish in a debutant topic, might help to further evaluate the clusters obtained from the different evolutionary networks. Practically, for a given debutant topic, the algorithm will select the authors that have published the highest number of publications, in the first five years of its life. 

In brief, the algorithm for extracting the main authors firstly selects all the authors that published in that topic, within its first five years, and then it ranks them based on the number of publications and selects the first 100, as showed in Code 10. However, the threshold of 100 authors can be reconsidered during the analysis. 

208 

**Code 10:** Extracting main authors of debutant topic. **Input :** List of Debutant Topics _deb.topics_ **Output:** List of Authors _authors_ **foreach** _topic in deb.topics_ **do** year _←_ GetYearOfSoftDebut(topic); related.authors _←_ SelectAuthorsInTopics(topic, from=year, to=year+5); **foreach** _author in related.author_ **do** papers.author[author] _←_ NumPapersPublishedInTopic(topic, author, from=year, to=year+5); **end foreach** temp.authors _←_ sort(related.author, values=papers.author, decreasing=TRUE); authors[topic] _←_ temp.authors[1:100]; `/* keep only the first 100 */` **end foreach** return(authors); 

We performed a quantitative analysis, in which we employed the authors to confirm the matches between clusters and ancestors. In particular, for each match between clusters and debutant topics, the algorithm evaluated the similarity, using the Jaccard Index, between active authors (described in Section 4.4.2) and the authors associated to the debutant topics. Observing the results, we realised that these results could not bring any contribution as the similarity values were below 0.01. This is justified by the fact that the sets of authors can be very large and if there are only few mutual authors, then the similarity between the two sets can be very low. 

The reason for this problem is because we are comparing the similarities obtained from two different kinds of information that are carried by topics and authors. Topics are more coarse-grained, as they can be seen as categories for a collection of papers written on such topics. On the contrary, authors can be seen as single data points and are more fine-grained. Hence, the question of whether authors can help the identifications of emerging areas, cannot be answered without further work. 

209 

### **5.7.7 How does the final result look like?** 

The final result is the information that the user receives from Augur, which aims to alert him or her to the emergence of a new area and provide sufficient detail to allow him/her to understand the key elements of the topic dynamic. 

Here follows an example of a cluster produced by Augur from the topic networks in the period 1998-2002. The cluster contains topics, such as, _World Wide Web_ , _Query Languages_ , _Metadata_ , _Content Base Retrieval_ , and _Search Engines_ , which exhibit a strong increment in their pace of collaboration in the period under analysis and match the ancestors of _Semantic Search_ , a topic that debuted in 2003. Therefore, we considered this cluster as correctly predicting _Semantic Search_ (with a similarity of 0.38). _Semantic Search_ aims to improve search accuracy by understanding the contextual meaning of the query terms and combines research in semantic technologies and information retrieval. In Table 5.23, we report in bold the direct ancestors of _Semantic Search_ , but, even among the other ones, we find many topics conducive to _Semantic Search_ or that produced technologies adopted by this field, such as _Text Processing_ , _Electronic Commerce_ , _Digital Libraries_ , and _Web Browser_ . In Fig. 5.40 we show its network representation. 

This is an exemplary case of the dynamics exploited by Augur, in which some topics, previously less connected, started to collaborate and moulded a novel research area that inherited their domains (e.g., _Information Retrieval_ , _Digital Libraries_ ), formats (e.g., _Xml_ ), software (e.g., _Search Engines_ ), and applications (e.g., _Contentbased Retrieval_ ). As part of the making sense process, in Table 5.24 we also show the top 10 authors (top) and the top 5 papers (bottom) relevant to this cluster. 

210 

**Table 5.23:** Example of output produced by Augur. The cluster associated with the emergence of the _Semantic Search_ topic (in bold the topics that match its ancestors). 

**Topics within the cluster world wide web, query languages, metadata, content-based retrieval, information retrieval, search engines, xml, information systems, information retrieval systems** , multi agent systems, intelligent agents, servers, digital libraries, electronic commerce, text processing, information management, indexing, web browsers, classification 



**Figure 5.40:** Network representation of the same cluster in Table 5.23 extracted from the evolutionary network of year 2002. 

211 

**Table 5.24:** Example of output produced by Augur. On top, there are the top 10 active authors. At the bottom, the top 5 papers. 

- **Active Authors Relevant Papers** • W. Bruce Croft, • A Sheth et al. “ _Managing semantic content for the_ • Dieter Fensel, _Web_ ” (2002) • Dan Suciu, • RWP Luk et al. “ _A survey in indexing and search-_ • William W. Cohen, _ing XML documents_ ” (2002) • Berthier Ribeiro-Neto, • J Kahan et al. “ _Annotea: An open RDF infras-_ • Clement T. Yu, _tructure for shared Web annotations_ ” (2002) • James Allan, • R Manmatha et al. “ _Modeling score distributions_ • Justin Zobel, _for combining the outputs of search engines_ ” (2001) • Dragomir R. Radev, • S Dagtas et al. “ _Models for motion-based video_ • Victor Vianu _indexing and retrieval_ ” (2000) 

## **5.8 Final remarks** 

In this chapter, we evaluated Augur on a gold standard of 1,408 debutant topics, which emerged in the 2000-2011 timeframe, and we compared the results of the Advanced Clique Percolation Method against four alternative approaches: Fast Greedy, Leiden Eigenvector, Fuzzy C-Means, and Clique Percolation Method. In particular, we initially designed an evaluation framework, defining how we compared the clusters of topics obtained from each evolutionary network, against the topics debuting in the following two years. Then, we designed our gold standard that included the selection of 1408 debutant topics, and the extraction of their foster ancestors. At this stage, we firstly evaluated the results obtained by the five clustering algorithms on the gold standard using the similarity index showed in Eq. 5.2. The ACPM provided interesting results, however there still was room for improvement. To this end, initially we applied a semantic filter to further clean the results obtained by the different algorithms, and then we applied a more comprehensive similarity index (see Eq. 5.8). This new index take fully advantage of the Computer Science Ontology by enhancing both clusters and ancestors of debutant topics with their broader topics. The final 

212 

results show that our approach outperforms state of the art solutions and is able to successfully identify clusters that will lead to the emergence of new topics in the two following years. 

While these results are satisfactory, our analysis presents some limitations that can be object of future work. In the first instance, the gold standard does not cover well the years after 2007. Indeed, as discussed in Section 5.7.4 the number of debutant topics gradually decreases after 2007. We thus intend to consider more up-to-date scholarly datasets and produce a more comprehensive version of the gold standard that could be adopted by the scholarly community to further study this task. 

Another limitation of Augur is that, in its current version, it only focuses on the pace of collaboration between topics and network density. We can argue that relying on only two indicators may not be enough to fully understand and detect the complex dynamics behind the creation of a topic. One way to further improve the results, could be to add other relevant entities, such as authors, venues and so on. This may enable the possibility to investigate other kinds of dynamics that could be associated with the emergence of new research areas, such as the patterns of collaboration between prominent authors, the dynamics of citations networks, or changes in the topic distributions of high-tier scientific venues. 

213 

# **Chapter 6** 

# **Conclusion** 

The main goal of this dissertation was to develop an approach for detecting emerging topics at the embryonic stage, i.e., when they have not yet been labelled or associated with a considerable number of publications. In a first study, we focused on understanding the dynamics that can drive the emergence of a new research topic (Chapter 3). The results showed a strong correlation between the pace of collaboration in a topic network and the emergence of new research topics a few years later. We then created Augur, a system for detecting areas of the network of topics characterised by these dynamics (Chapter 4). Augur uses the Advanced Clique Percolation Method (ACPM) for analysing the topics involved in these dynamics and clustering them. The output is a number of clusters of topics, each of which has a strong probability to be associated with an emerging new topic. These are then further characterised by providing a list of significant authors and publications. We evaluated Augur and ACPM versus four alternative community detection algorithms on a gold standard of 1,408 debutant topics in the 2000-2011 timeframe. The results show that Augur outperforms state-of-the-art solutions and is able to successfully identify a high percentage of clusters that will produce new topics in the two following years. 

214 

## **6.1 Overview of contributions and major findings** 

In Chapter 1, we introduced six research questions that drove this doctoral work. We will now analyse the answers of these questions and restate our contributions. 

**Research Question 1:** Is it possible to precisely define the notion of established topic? (Section 1.3.1) 

To answer this question, we performed an analysis of the body of research in order to explore some ideas in relation to the problem. In Section 2.2, we analysed the stages that a research topic goes through. In Chapter 3, we attempted to determine how a topic can be considered established, from a practical point of view. Even though in principle we could use a more exhaustive list of metrics to define when a topic is considered established, we focused on the age of the topic, the number of relevant papers that it are published each year, and the fact that it is covered in CSO. 

This understanding proved to be very valuable, as in our first study, we were then able to compare the dynamics associated with established topics against the dynamics involving recently emerged ones. 

**Research Question 2:** How early in the topic lifecycle is it possible to identify an emerging topic? (Section 1.3.2) 

In Section 2.2, we analysed the different stages which a new research topic goes through before becoming established on the basis of our first hypothesis, which states “ _before emerging, new topics face an embryonic stage in which researcher are already involved in several activities_ ”. In the literature, we found enough evidence that would suggest the existence of an embryonic stage. In this particular stage, a topic has not yet been explicitly labelled and recognised by a research community, but it is already taking shape, as evidenced by the fact that researchers from a variety of fields are 

215 

forming new collaborations, producing new work, and starting to define the challenges and the paradigms associated with the emerging new area. 

In Chapter 3, we performed an analysis in which we observed the dynamics leading to the emergence of new research topics. 

In this analysis, we found a correlation between the collaboration pace of existent topics and the emergence of new emerging topics in the near future (p-value _<_ 0.0001). In addition, because at the time of performing the analysis the emerging topics did not exist yet, we were able then to analyse their emergence within their embryonic stage. 

In brief, based on the evidence collected in this work, we can say that it is possible to do better than the current approaches available in the literature, which detect new topics from the early stage onwards, by forecasting their emergence already at the embryonic stage. 

**Research Question 3:** What are the indicators that can be exploited to predict the emergence of new topics? (Section 1.3.3) 

This question has been driven by our second hypothesis: _the emergence of a new research topic is anticipated by specific dynamics between pre-existing topics._ 

In Chapter 3, we compared the sections of the co-occurrence networks where new topics are about to emerge with a control group of subgraphs associated with established topics. These graphs were analysed by using two novel approaches that integrate both statistics and semantics. The results provide evidence that the emergence of a novel research topic can be anticipated by a significant increase in the pace of collaboration between relevant research areas, which can be seen as the “ancestors” of the new topic. In particular, we identified two indicators that are correlated with the emergence of new research topics: 

- pace of collaboration, Eq. 3.7, p-value = 4 _._ 64 _×_ 10<sup>_−_45</sup> 

216 

• network density, Eq. 3.9, p-value = 6 _._ 43 _×_ 10<sup>_−_16</sup> 

In other words, the development of new topics seems to be encouraged by the cross-fertilisation of established research areas. Of course there may well exist other patterns, which could help to forecast the emergence of a new research area; a hypothesis that we plan to explore in future work. 

**Research Question 4:** Is it possible to develop an effective computational method that can support this prediction task? (Section 1.3.4) We hypothesised that it is possible to develop an automatic approach for detecting new emerging topics at their embryonic stage by analysing the dynamics of existing topics (i.e., observing their patterns of collaboration). 

To test this hypothesis, we performed a second study which led to the development of Augur. As described in Chapter 4, we aimed at effectively detecting the emergence of new research areas by analysing topic networks and identifying clusters associated with an overall increase of the pace of collaboration between research areas. 

The evaluation discussed in Chapter 5 showed that Augur is able to detect with high precision the topics that will emerge a few years later. In particular, from Table 5.17, at page 185, we can see how in the years from 1999 to 2005, ACPM yields values of precision around 0.8 and values of recall around 0.7, outperforming the other four algorithms. Indeed, other algorithms such as FG, LE, and FCM do not exceed 0.15 in precision and 0.5 in recall. Only the Clique Percolation Method is able to partially exceed these values with precision nearly 0.3, but a low recall. 

These results allow us to affirm: 

- that the ACPM algorithm, designed to identify clusters from evolutionary networks, outperforms other state-of-the-art algorithms (i.e., FG, LE, FCM and CPM) for forecasting the emergence of new research topics; 

217 

- that is possible to develop a computational method for predicting the emergence of new topics at their early stage and forecast their emergence. 

**Research Question 5:** Are there commonalities between our approach to predicting the emergence of new topics and epistemological theories of research dynamics? (Section 1.3.5) 

Thomas Kuhn (1970) stated that science proceeds within certain paradigms or, in other words, sets of concepts or thought patterns. When some paradigms cannot cope with certain problems, a paradigm shift can lead to the emergence of a new scientific discipline. Other theories mention that different communities of researchers can be engaged in an exchange of tools, methodologies and theories, leading then to the emergence of a new research area (Surowiecki, 2005; Becher and Trowler, 2001). All these theories support the idea that a new topic comes into existence even before it is explicitly labelled and recognised by a research community. In this phase, the topic is already taking shape, as researchers from a variety of fields are forming new collaborations and producing new work, starting to define the challenges and the paradigms associated with the emerging new area. 

This doctoral work has many commonalities with what historians of Science and philosophers have been arguing in the last 60 years. Indeed, in designing and developing an approach for the detection of new emerging topics, we have been significantly influenced by these theories. In our first study, we observed that within the embryonic stage of topics, their related topics (i.e., their ancestors) are intensifying their activity of collaboration (p-value = 4 _._ 64 _×_ 10<sup>_−_45</sup> ) as well as establish new collaborations (pvalue = 6 _._ 43 _×_ 10<sup>_−_16</sup> ). These findings suggest that an interdisciplinary environment is the driving force for the creation of novel research topics. 

218 

These findings bring new empirical evidence to the relevant theories in _Philosophy of Science_ , highlighting the important role of multidisciplinarity in the creation of new research topics. 

**Research Question 6:** What evaluation mechanisms are appropriate for this task? (Section 1.3.6) 

This question focused on how to make sure that the induced clusters (i.e., groups of topics) could be validated and evaluated as valid fertile areas that are fostering the emergence of a new ones. In order to answer this question, we faced several challenges, including developing a gold standard and defining the right evaluation measures. In particular, for the gold standard, only knowing the topics that emerged in a particular period, does not provide enough information to evaluate the results of Augur, or at least to do so automatically. Therefore, we associated these emerging topics with their ancestors that eventually would provide the match for the topics found in clusters. 

The second challenging task was to define the evaluation measures to assess the validity of Augur. In Section 5.7.2 we discussed that a cluster can potentially match multiple debutant topics, and vice versa (see also Fig. 5.3 at page 149). This _manyto-many_ relationship prevents us to adopt the standard values of precision and recall. For this reason, in Section 5.4.1, we redefined precision (Eq. 5.3) as the fraction of clusters that have been successfully matched with debutant topics, and recall (Eq. 5.4) as the fraction of topics that have been successfully matched by the clusters. 

Another aspect that we investigated is the semantic similarity between the clusters and the ancestors of debutant topics. To investigate similarity between these two sets we relied on the Jaccard index. This index matches the samples within two sets in a syntactic way and thus it discards any semantics. Hence, in Eq. 5.2 and Eq. 5.8 we proposed an enhanced version of the Jaccard index which considers also the semantic 

219 

component. In the first instance, we enhanced the set of clusters with the relevant same-as relations. In this way, an ancestor can match either a topic in the cluster or other topics in a same-as relation with it. To this end, Eq. 5.8, we developed a more semantic index. In particular, both clusters and ancestors of debutant topics are enhanced with their super-areas, with the assumption that if the two sets share many of their super-areas it is very likely that they belong to the same sample. 

Using the semantic enhanced index of Eq. 5.8, we were able to improve the matching process between sets of clusters generated by Augur and ancestors of debutant topics, so that the ACPM was able to reach excellent results, up to a precision of 0.8 and recall of 0.76 in the same period. 

## **6.2 Limitations of the study and future directions** 

In this section, we will discuss some limitations of this doctoral work and discuss future work. 

### **6.2.1 Gold standard** 

One of the main issues we faced when evaluating Augur, was that towards the end of the analysed period the number of debutant topics in our dataset decreases drastically (see Figure 5.2 at page 139). For the sake of completeness, we also included in the analysis the topics emerged in the years after 2006, however this issue prevents us from fully trusting the results of the evaluation for the years in that period. As future work, we plan to acquire more up-to-date scholarly datasets and to produce a more comprehensive version of the gold standard. 

220 

### **6.2.2 Evolutionary network** 

The evolutionary network is a key component of Augur’s framework. It structures the data so that they can be easily processed in the following step of the process. In particular, we create semantic enhanced topic networks from publication metadata, and then we convert them into evolutionary networks, which track the pace of collaboration between research topics over a period of five years. All the assumptions that we made when designing these evolutionary networks, such as number of years and how to measure the pace of collaboration, derive from the results of the first study (Chapter 3). In future work, we intend to explore other configurations with the aim of further improving the performances of Augur. In particular, we plan to investigate the following questions: what is the number of consecutive topic networks that can be merged to have a good estimate of the pace of collaboration between topics? What is the best function that allows to approximate the pace of collaboration between research topics? How does this approximation function change according to the amount of network to process? 

### **6.2.3 Clustering Algorithm** 

The second phase of Augur is the identification of areas exhibiting an intense activity of collaboration, which eventually leads to the emergence of new research topics. To this end, we developed the Advanced Clique Percolation Method with the aim of detecting clusters of topics that exhibit a significant increase in collaboration pace. We designed ACPM to address the inability of the standard Clique Percolation Method to deal with very dense networks. Since the retrieved clusters necessitate post-processing (by going through the third stage), as a future work we should also aim at improving this clustering phase. This implies either improving ACPM or seeking new solutions for clustering the evolutionary networks. The field of _Network Science_ is constantly growing with new techniques to analyse large and dense networks, which may be 

221 

relevant here. Furthermore, we can explore other community detection algorithms and eventually extend them, as we did for CPM, to try and improve the performance of Augur. 

### **6.2.4 Post processing and sense making** 

In the third and final stage of Augur, we filter the set of clusters and we enhance them with information regarding active authors and relevant papers. This information supports users in making sense of the results. Work to improve this stage will focus on understanding qualitatively the kind of information that can better support the user in making sense of the results. By definition, the set of authors returned by Augur comprise researchers are engaged in the formation of the new topic, whereas the resulting papers are important research outputs that are laying the basis of this new area. We believe that it would be interesting to explore whether other information can be provided to the user, to assist him or her in making sense of the dynamics associated with the emergence of a new area. 

### **6.2.5 Trying different windows of years** 

In Chapter 5, we designed the evaluation of Augur, aiming at investigating its ability to forecast the emergence of new research topics in the two years following the year of analysis. As showed in Table 5.2 (at page 135), an analysis performed in the year 2000, would allow us to detect topics emerged in the years 2001 and 2002. This choice was determined by the results obtained in the first study. For a particular emerging topic, we analysed the relationship between its ancestors in the five years prior its emergence. In Augur, we also used five sequential topic networks for detecting emerging topics in the following year. However, we estimated that with such amount of consecutive topic networks there would be enough information to forecast topics also in the following second year. In future work we plan to explore how far in the 

222 

future is possible to have accurate forecasting and to what extent the performance of Augur changes over a larger timeframe. 

### **6.2.6 Testing new version of CSO** 

In June 2018, our research team released a new version of CSO (Salatino et al., 2018b). This new version was produced by running Klink-2 on a up-to-date corpus of publications, and it contains about 26K topics and 226K relationships (see Section 2.1.1). Compared to the previous version, this new version is more fine-grained and comprehensive in terms of relationships. 

In the studies presented in this dissertation, including the development of Augur, we heavily relied on the Computer Science Ontology in several stages, such as (i) creation of the semantic enhanced topic networks, (ii) creating the evolutionary networks, (iii) filtering clusters, and (iv) semantic enhancement in the evaluation. 

In the future we plan to evaluate whether the use of a more comprehensive and robust ontology allows us to improve the performance of Augur. 

In particular, in Chapter 5, we used Eq. 5.8 to measure the semantic similarity between a given cluster and ancestors of debutant topics. It will be interesting to observe how this measure changes when adopting the new version of the ontology. 

### **6.2.7 Introducing further dynamics** 

Another limitation of Augur is that in this current version, it only focuses on the pace of collaboration between topics. It is possible that using only this indicator might not be enough to fully understand and detect the complex dynamics behind the creation of a topic. Augur uses information coming from authors and papers to support the user in making sense of the given results, however this information is not actually used in the process associated with the early detection of emerging topics. 

223 

We believe that taking in consideration other entities, like authors and venues, may further improve Augur performances. This will enable the possibility to investigate other kinds of dynamics that could be associated with the emergence of new research areas, such as the patterns of collaboration between prominent authors, the dynamics of citations networks, or the change in the topic distributions of high-tier scientific venues. 

The introduction of these new dynamics would require performing new studies like the ones presented in this dissertation. There should be a first study, similar to the one proposed in Chapter 3, to understand how a particular dynamic correlates with the emergence of new research area. Then, there should be a second study to analyse how to explore this new dynamic to effectively detect the emergence of new research topics. Eventually, there should be a third study to understand how to integrate the new findings within Augur. 

### **6.2.8 Scope** 

At the moment, Augur works within the domain of _Computer Science_ . This limitation is due to two main reasons. Firstly, because of the limited availability of scholarly metadata at our disposal. The Rexplore dataset is not as comprehensive for other fields as it is for _Computer Science_ . The second reason is that the ontology (CSO) we adopted to define our topics also covers only the field of _Computer Science_ . In order to broaden the scope of Augur we need both to seek new scholarly datasets and topic ontologies for other disciplines. This is partially achievable in some fields like Medicine and Physics. For instance, in the field of Medicine, we can use Medline<sup>1</sup> as scholarly dataset and the Medical Subject Heading<sup>2</sup> (MeSH) for defining topics. Indeed, we are currently planning to adopt Augur to work in this domain, since both resources are available. In the field of Physics, instead, we can use the Physics Subject 

> 1Medline/PubMed data `https://www.ncbi.nlm.nih.gov/pubmed/` 

> 2Medical Subject Heading `https://meshb.nlm.nih.gov/` 

224 

Headings<sup>3</sup> (PhySH) as vocabulary for subject areas and arXiv<sup>4</sup> for the corpus. In this case, however, there are other challenges to face, because for instance the arXiv corpus does not store metadata and therefore they must be parsed from the _pdf_ files. 

Since the design of Augur was based on robust epistemological theories, we are confident that it will achieve satisfactory results also in other scientific fields. However, given that _Computer Science_ is a highly dynamic area compared to other scientific fields, we expect that some parameters of the system will need to be attuned. 

In brief, here we list a few necessary requirements in order to adopt Augur in other fields of Science: 

- **Ontology or research topics** , this is important as it will be used as glossary of topics and therefore support the definition of research topic in the investigated field; 

- **Corpus of scientific articles** , covering the new field, upon which performing the analysis. As in Rexplore, for each paper, the corpus should contain information about either keywords or topics and the year of publication. This information is required for creating the semantic enhanced topic network from which building the several evolutionary networks, and extracting the clusters of collaborating topics. If topics are not available, there is a need for a further step which extracts topics from papers using their metadata, such as title and abstract or full-content; 

- **Tuning of parameters** , since the parameters of Augur are domain dependent, and need to be adjusted to accommodate the explored field. These parameters include the number of links that define the cluster, the similarity measure used to merge similar clusters, and others showed in Chapter 4. 

> 3Physics Subject Headings `https://physh.aps.org/` 

> 4arXiv Physics `https://arxiv.org/archive/physics` 

225 

Another factor that should be taken into account when exploring the dynamics in other fields is their publishing behaviour. Each field possesses its own publishing preferences. For instance, journal or conference articles are poor vehicles of communication in the field of _Social Science_ as they are not suitable to discuss complex issues. Hence preferring books. However, many other fields investigating narrow area of study, with discrete and separable problems, e.g., _Physics_ , _Medicine_ , _Engineering_ , and others, predominantly use articles. We do not have enough evidence to claim how the behaviour of Augur could be affected by this factor. 

### **6.2.9 Scalability** 

It is also worth discussing a possible scalability issue that could arise while processing different topic networks. 

As reported in Table 5.11 the evolutionary network of the year 2000 consists of 2263 nodes and 13327 links, and both these numbers tended to grow over time. Indeed, the evolutionary network of the year 2009 consists of 9865 nodes and 99660 links. However, the computational time to process each one of these networks did not exceed 3-4 hours. Working in other domains of science can lead to process larger networks affecting the scalability. For instance, speaking with colleagues at Chan Zuckerberg Initiative, in which they investigate trends in the field of _Medicine_ , they deal with keyword networks containing more than 15K unique keywords, which poses real challenges in processing them. 

We are currently evaluating Augur on a more recent data using Microsoft Academic Search with number of nodes and link about three times larger than our previous evolutionary networks. Processing such large evolutionary network takes around 24 hours. 

226 

We are thus confident that scalability should not be an issue when applying Augur on other research areas. 

### **6.2.10 Human-based evaluation** 

In Chapter 5 we evaluated Augur on a gold standard of historical data, and in order to do so, we first we designed an evaluation framework, which defines when a returned cluster matches the ancestors of a debutant topic. Then, we extracted the gold standard. These two steps allowed us to evaluate Augur both in an automatic and a quantitative way. However, it may be possible to evaluate Augur more qualitatively with the support of domain experts. 

A domain expert can analyse the interaction of some topics in a certain year and suggest, based on his or her judgement, that such interaction might lead to the emergence of new topics. However, to pursue such evaluation we would need several domain experts with different areas of expertise analysing the different clusters returned by Augur. This was not attainable within the timescale provided for this research. Indeed, this would have required a set of time consuming activities such as: (i) finding available domain experts for each relevant topic, (ii) understanding their domain of expertise, (iii) selecting candidate clusters that could fit his or her expertise, (iv) engaging with the experts during the process of evaluation, and (v) making sure the experts complete the evaluation with high quality. 

In the future, we plan to run a user study in which we will collect the opinion of several domain experts, including senior editors at Springer Nature, regarding the results obtained by Augur. 

227 

## **6.3 Concluding remarks** 

In this dissertation we presented the work of three years of research on the early detection of new research topics. This problem has been analysed from different angles, putting us in front of several challenges, that made this doctoral work particularly interesting and rewarding. 

We firstly analysed the literature and formulated the set of hypotheses discussed in Section 1.4. We then conducted an empirical study which aimed at uncovering some of the patterns that can lead to the emergence of new research topics. As discussed in Chapter 3, we initially analysed the relationship between an emerging topic and the collaboration between already existing topics, and how the development of the latter can influence the former. This understanding allowed us to design Augur, an approach to detecting research topics in their embryonic stage, as described in Chapter 4 and evaluated in Chapter 5. Augur yielded excellent results and outperformed alternative approaches. 

This doctoral work opens up several interesting research directions and we look forward to further developing the techniques presented here. 

228 

# **Bibliography** 

- Abrahamson, E. (1996). Management fashion. _Academy of management review_ , 21(1):254–285. 

- Afzal, Z., Tsatsaronis, G., Doornenbal, M., Coupet, P., and Gregory, M. (2016). Learning domain labels using conceptual fingerprints: An in-use case study in the neurology domain. In _Knowledge Engineering and Knowledge Management: 20th International Conference, EKAW 2016, Bologna, Italy, November 19-23, 2016, Proceedings 20_ , pages 731–745. Springer. 

- Ahn, Y.-Y., Bagrow, J. P., and Lehmann, S. (2010). Link communities reveal multiscale complexity in networks. _Nature_ , 466(7307):761. 

- Alghamdi, R. and Alfalqi, K. (2015). A survey of topic modeling in text mining. _I. J. ACSA_ , 6(1):147–153. 

- Allan, J., Carbonell, J. G., Doddington, G., Yamron, J., and Yang, Y. (1998). Topic detection and tracking pilot study final report. 

- Arenas, A., Diaz-Guilera, A., and P´erez-Vicente, C. J. (2006). Synchronization reveals topological scales in complex networks. _Physical review letters_ , 96(11):114102. 

- ˚Astr¨om, F. (2007). Changes in the lis research front: Time-sliced cocitation analyses of lis journal articles, 1990–2004. _Journal of the Association for Information Science and Technology_ , 58(7):947–957. 

229 

- Baldwin, C., Hughes, J., Hope, T., Jacoby, R., and Ziebland, S. (2003). Ethics and dementia: mapping the literature by bibliometric analysis. _International journal of geriatric psychiatry_ , 18(1):41–54. 

- Barab´asi, A.-L., Gulbahce, N., and Loscalzo, J. (2011). Network medicine: a networkbased approach to human disease. _Nature reviews. Genetics_ , 12(1):56. 

- Batagelj, V., Kejˇzar, N., Korenjak-Cerne,<sup>ˇ</sup> S., and Zaverˇsnik, M. (2006). Analyzing the structure of us patents network. _Data science and classification_ , pages 141–148. 

- Batagelj, V. and Zaversnik, M. (2003). Short cycles connectivity. _arXiv preprint cs/0308011_ . 

- Baumes, J., Goldberg, M. K., Krishnamoorthy, M. S., Magdon-Ismail, M., and Preston, N. (2005). Finding communities by clustering a graph into overlapping subgraphs. _IADIS AC_ , 5:97–104. 

- Becher, T. and Trowler, P. (2001). _Academic tribes and territories: Intellectual enquiry and the culture of disciplines_ . McGraw-Hill Education (UK). 

- Berners-Lee, T. and Fischetti, M. (1999). _Weaving the Web: The original design and ultimate destiny of the World Wide Web by its inventor_ . DIANE Publishing Company. 

- Berners-Lee, T., Hendler, J., Lassila, O., et al. (2001). The semantic web. _Scientific american_ , 284(5):28–37. 

- Bettencourt, L. M., Kaiser, D. I., and Kaur, J. (2009). Scientific discovery and topological transitions in collaboration networks. _Journal of Informetrics_ , 3(3):210–221. 

230 

- Bezdek, J. C. (1981). _Pattern Recognition with Fuzzy Objective Function Algorithms_ . Kluwer Academic Publishers, Norwell, MA, USA. 

- Blatt, M., Wiseman, S., and Domany, E. (1996). Superparamagnetic clustering of data. _Physical review letters_ , 76(18):3251. 

- Blei, D. M. (2012). Probabilistic topic models. _Communications of the ACM_ , 55(4):77–84. 

- Blei, D. M. and Lafferty, J. D. (2006). Correlated topic models. In Weiss, Y., Sch¨olkopf, P. B., and Platt, J. C., editors, _Advances in Neural Information Processing Systems 18_ , pages 147–154. MIT Press. 

- Blei, D. M., Ng, A. Y., and Jordan, M. I. (2003). Latent dirichlet allocation. _Journal of machine Learning research_ , 3(Jan):993–1022. 

- Blondel, V. D., Guillaume, J.-L., Lambiotte, R., and Lefebvre, E. (2008). Fast unfolding of communities in large networks. _Journal of statistical mechanics: theory and experiment_ , 2008(10):P10008. 

- Boccaletti, S., Ivanchenko, M., Latora, V., Pluchino, A., and Rapisarda, A. (2007). Detecting complex network modularity by dynamical clustering. _Physical Review E_ , 75(4):045102. 

- Bolelli, L., Ertekin, c., and Giles, C. L. (2009). Topic and trend detection in text collections using latent dirichlet allocation. In _Proceedings of the 31th European Conference on IR Research on Advances in Information Retrieval_ , ECIR ’09, pages 776–780, Berlin, Heidelberg. Springer-Verlag. 

- B¨orner, K. (2010). _Atlas of Science: Visualizing what We Know_ . MIT Press. 

- B¨orner, K., Huang, W., Linnemeier, M., Duhon, R. J., Phillips, P., Ma, N., Zoss, A. M., Guo, H., and Price, M. A. (2010). Rete-netzwerk-red: analyzing and 231 

visualizing scholarly networks using the network workbench tool. _Scientometrics_ , 83(3):863–876. 

- Botta, F. and Del Genio, C. I. (2016). Finding network communities using modularity density. _Journal of Statistical Mechanics: Theory and Experiment_ , 2016(12):123402. 

- Boyack, K., B¨orner, K., and Klavans, R. (2008). Mapping the structure and evolution of chemistry research. _Scientometrics_ , 79(1):45–60. 

- Boyack, K. W. and Klavans, R. (2014). Creation of a highly detailed, dynamic, global model and map of science. _Journal of the Association for Information Science and Technology_ , 65(4):670–685. 

- Boyack, K. W., Klavans, R., and B¨orner, K. (2005). Mapping the backbone of science. _Scientometrics_ , 64(3):351–374. 

- Boyack, K. W., Mane, K., and Borner, K. (2004). Mapping medline papers, genes, and proteins related to melanoma research. In _Information Visualisation, 2004. IV 2004. Proceedings. Eighth International Conference on_ , pages 965– 971. IEEE. 

- Brandes, U., Delling, D., Gaertler, M., Gorke, R., Hoefer, M., Nikoloski, Z., and Wagner, D. (2008). On modularity clustering. _IEEE transactions on knowledge and data engineering_ , 20(2):172–188. 

- Braun, T., Schubert, A. P., and Kostoff, R. N. (2000). Growth and trends of fullerene research as reflected in its journal literature. _Chemical reviews_ , 100(1):23–38. 

- Burt, R. S. (2000). The network structure of social capital. _Research in organizational behavior_ , 22:345–423. 

232 

- Callon, M., Courtial, J.-P., and Laville, F. (1991). Co-word analysis as a tool for describing the network of interactions between basic and technological research: The case of polymer chemsitry. _Scientometrics_ , 22(1):155–205. 

- Callon, M., Courtial, J.-P., Turner, W. A., and Bauin, S. (1983). From translations to problematic networks: An introduction to co-word analysis. _Information (International Social Science Council)_ , 22(2):191–235. 

- Cameron, D., Aleman-Meza, B., Arpinar, I. B., Decker, S. L., and Sheth, A. P. (2010). A taxonomy-based model for expertise extrapolation. In _Semantic Computing (ICSC), 2010 IEEE Fourth International Conference on_ , pages 333–340. IEEE. 

- Cano-Basave, A. E., Osborne, F., and Salatino, A. A. (2016). Ontology forecasting in scientific literature: Semantic concepts prediction based on innovationadoption priors. In Blomqvist, E., Ciancarini, P., Poggi, F., and Vitali, F., editors, _Knowledge Engineering and Knowledge Management_ , pages 51–67, Cham. Springer International Publishing. 

- Capocci, A., Servedio, V. D., Caldarelli, G., and Colaiori, F. (2005). Detecting communities in large networks. _Physica A: Statistical Mechanics and its Applications_ , 352(2):669–676. 

- Cataldi, M., Di Caro, L., and Schifanella, C. (2010). Emerging topic detection on twitter based on temporal and social terms evaluation. In _Proceedings of the tenth international workshop on multimedia data mining_ , page 4. ACM. 

- Chang, J. and Blei, D. M. (2010). Hierarchical relational models for document networks. _The Annals of Applied Statistics_ , 4(1):124–150. 

- Chavalarias, D. and Cointet, J.-P. (2013). Phylomemetic patterns in science evolutionthe rise and fall of scientific fields. _PloS one_ , 8(2):e54847. 

233 

- Chen, B., Tsutsui, S., Ding, Y., and Ma, F. (2017). Understanding the topic evolution in a scientific domain: An exploratory study for the field of information retrieval. _Journal of Informetrics_ , 11(4):1175–1189. 

- Chen, C. (2006). Citespace ii: Detecting and visualizing emerging trends and transient patterns in scientific literature. _Journal of the Association for Information Science and Technology_ , 57(3):359–377. 

- Chen, C., Chen, Y., Horowitz, M., Hou, H., Liu, Z., and Pellegrino, D. (2009). Towards an explanatory and computational theory of scientific discovery. _Journal of Informetrics_ , 3(3):191–209. 

- Chen, C., Hu, Z., Liu, S., and Tseng, H. (2012). Emerging trends in regenerative medicine: a scientometric analysis in citespace. _Expert opinion on biological therapy_ , 12(5):593–608. 

- Clark, B. R. (1962). _Faculty culture_ . Center for the Study of Higher Education, University of California. 

- Clauset, A., Newman, M. E., and Moore, C. (2004). Finding community structure in very large networks. _Physical review E_ , 70(6):066111. 

- Coleman, J. S. et al. (1964). Introduction to mathematical sociology. _Introduction to mathematical sociology._ 

- Coulter, N., Monarch, I., and Konda, S. (1998). Software engineering as seen through its research literature: A study in co-word analysis. _Journal of the Association for Information Science and Technology_ , 49(13):1206–1223. 

- Courtial, J. P. (1994). A coword analysis of scientometrics. _Scientometrics_ , 31(3):251– 260. 

234 

- Cowan, R. and Jonard, N. (2004). Network structure and the diffusion of knowledge. _Journal of economic Dynamics and Control_ , 28(8):1557–1575. 

- Dai, X.-Y., Chen, Q.-C., Wang, X.-L., and Xu, J. (2010). Online topic detection and tracking of financial news based on hierarchical clustering. In _Machine Learning and Cybernetics (ICMLC), 2010 International Conference on_ , volume 6, pages 3341–3346. IEEE. 

- Davis, J. A. and Leinhardt, S. (1967). The structure of positive interpersonal relations in small groups. 

- Decker, S. L. (2007). _Detection of bursty and emerging trends towards identification of researchers at the early stage of trends_ . PhD thesis, uga. 

- Deerwester, S., Dumais, S. T., Furnas, G. W., Landauer, T. K., and Harshman, R. (1990). Indexing by latent semantic analysis. _Journal of the American society for information science_ , 41(6):391. 

- Der´enyi, I., Palla, G., and Vicsek, T. (2005). Clique percolation in random networks. _Physical review letters_ , 94(16):160202. 

- Di Caro, L., Guerzoni, M., Nuccio, M., and Siragusa, G. (2017). A bimodal network approach to model topic dynamics. _arXiv preprint arXiv:1709.09373_ . 

- Ding, Y. (2011). Community detection: Topological vs. topical. _Journal of Informetrics_ , 5(4):498–514. 

- Ding, Y., Chowdhury, G. G., and Foo, S. (2001). Bibliometric cartography of information retrieval research by using co-word analysis. _Information processing & management_ , 37(6):817–842. 

235 

- Donetti, L. and Munoz, M. A. (2004). Detecting network communities: a new systematic and efficient algorithm. _Journal of Statistical Mechanics: Theory and Experiment_ , 2004(10):P10012. 

- Dourisboure, Y., Geraci, F., and Pellegrini, M. (2007). Extraction and classification of dense communities in the web. In _Proceedings of the 16th international conference on World Wide Web_ , pages 461–470. ACM. 

- Duvvuru, A., Kamarthi, S., and Sultornsanee, S. (2012). Undercovering research trends: Network analysis of keywords in scholarly articles. In _Computer Science and Software Engineering (JCSSE), 2012 International Joint Conference on_ , pages 265–270. IEEE. 

- Duvvuru, A., Radhakrishnan, S., More, D., Kamarthi, S., and Sultornsanee, S. (2013). Analyzing structural & temporal characteristics of keyword system in academic research articles. _Procedia Computer Science_ , 20:439–445. 

- Eichmann, D., Ruiz, M., Srinivasan, P., Street, N., Culy, C., and Menczer, F. (1999). A cluster-based approach to tracking, detection and segmentation of broadcast news. In _Proceedings of the DARPA Broadcast News Workshop_ , pages 69–76. 

- Elio, R., Hoover, J., Nikolaidis, I., Salavatipour, M., Stewart, L., and Wong, K. (2011). About computing science research methodology. 

- Eppstein, D., L¨offler, M., and Strash, D. (2010). Listing all maximal cliques in sparse graphs in near-optimal time. In _International Symposium on Algorithms and Computation_ , pages 403–414. Springer. 

- Erten, C., Harding, P. J., Kobourov, S. G., Wampler, K., Yee, G., et al. (2004). Exploring the computing literature using temporal graph visualization. In _Visualization and Data Analysis_ , pages 45–56. 

236 

- Evans, T. and Lambiotte, R. (2009). Line graphs, link partitions, and overlapping communities. _Physical Review E_ , 80(1):016105. 

- Everett, M. G. and Borgatti, S. P. (1998). Analyzing clique overlap. _Connections_ , 21(1):49–61. 

- Farkas, I., Abel,<sup>´</sup> D., Palla, G., and Vicsek, T. (2007). Weighted network modules. _New Journal of Physics_ , 9(6):180. 

- Faust, K. (2010). A puzzle concerning triads in social networks: Graph constraints and the triad census. _Social Networks_ , 32(3):221–233. 

- Flake, G. W., Lawrence, S., Giles, C. L., and Coetzee, F. M. (2002). Self-organization and identification of web communities. _Computer_ , 35(3):66–70. 

- Fortunato, S. (2010). Community detection in graphs. _Physics reports_ , 486(3):75–174. 

- Fowler, J. H. (2006). Legislative cosponsorship networks in the us house and senate. _Social Networks_ , 28(4):454–465. 

- Fowler, J. H. and Jeon, S. (2008). The authority of supreme court precedent. _Social networks_ , 30(1):16–30. 

- Freeman, L. (2004). The development of social network analysis. _A Study in the Sociology of Science_ , 1. 

- Freeman, L. C. (1982). Centered graphs and the structure of ego networks. _Mathematical Social Sciences_ , 3(3):291–304. 

- Fried, D. and Kobourov, S. G. (2014). Maps of computer science. In _Visualization Symposium (PacificVis), 2014 IEEE Pacific_ , pages 113–120. IEEE. 

- Furukawa, T., Mori, K., Arino, K., Hayashi, K., and Shirakawa, N. (2015). Identifying the evolutionary process of emerging technologies: A chronological network 

237 

analysis of world wide web conference sessions. _Technological Forecasting and Social Change_ , 91:280–294. 

- Fusch, P. I. and Ness, L. R. (2015). Are we there yet? data saturation in qualitative research. _The Qualitative Report_ , 20(9):1408. 

- Gao, W. and Wong, K.-F. (2006). Natural document clustering by clique percolation in random graphs. _Lecture notes in computer science_ , 4182:119. 

- Gonz´alez, M. C., Herrmann, H. J., Kert´esz, J., and Vicsek, T. (2007). Community structure and ethnic preferences in school friendship networks. _Physica A: Statistical mechanics and its applications_ , 379(1):307–316. 

- Griffiths, T. L., Jordan, M. I., Tenenbaum, J. B., and Blei, D. M. (2004). Hierarchical topic models and the nested chinese restaurant process. In Thrun, S., Saul, L. K., and Sch¨olkopf, P. B., editors, _Advances in Neural Information Processing Systems 16_ , pages 17–24. MIT Press. 

- Gruhl, D., Guha, R., Liben-Nowell, D., and Tomkins, A. (2004). Information diffusion through blogspace. In _Proceedings of the 13th international conference on World Wide Web_ , pages 491–501. ACM. 

- Guimera, R. and Amaral, L. A. N. (2005). Functional cartography of complex metabolic networks. _Nature_ , 433(7028):895. 

- Guimer, R., Mossa, S., Turtschi, A., and Amaral, L. A. N. (2005). The worldwide air transportation network: Anomalous centrality, community structure, and cities’ global roles. _Proceedings of the National Academy of Sciences_ , 102(22):7794–7799. 

- Guo, H., Weingart, S., and B¨orner, K. (2011). Mixed-indicators model for identifying emerging research areas. _Scientometrics_ , 89(1):421–435. 

238 

- Hathaway, R. J. and Bezdek, J. C. (2001). Fuzzy c-means clustering of incomplete data. _IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics)_ , 31(5):735–744. 

- He, D., Zhu, X., and Parker, D. S. (2011). How does research evolve? pattern mining for research meme cycles. In _Data Mining (ICDM), 2011 IEEE 11th International Conference on_ , pages 1068–1073. IEEE. 

- He, Q., Chen, B., Pei, J., Qiu, B., Mitra, P., and Giles, L. (2009). Detecting topic evolution in scientific literature: How can citations help? In _Proceedings of the 18th ACM conference on Information and knowledge management_ , pages 957–966. ACM. 

- Herrera, M., Roberts, D. C., and Gulbahce, N. (2010). Mapping the evolution of scientific fields. _PloS one_ , 5(5):e10355. 

- Ho, J. C., Saw, E.-C., Lu, L. Y., and Liu, J. S. (2014). Technological barriers and research trends in fuel cell technologies: A citation network analysis. _Technological Forecasting and Social Change_ , 82:66–79. 

- Hofmann, T. (1999). Probabilistic latent semantic indexing. In _Proceedings of the 22nd annual international ACM SIGIR conference on Research and development in information retrieval_ , pages 50–57. ACM. 

- Holland, P. W. and Leinhardt, S. (1976). Local structure in social networks. _Sociological methodology_ , 7:1–45. 

- Holmstr¨om, E., Bock, N., and Br¨annlund, J. (2009). Modularity density of network community divisions. _Physica D: Nonlinear Phenomena_ , 238(14):1161–1167. 

- Jo, Y., Lagoze, C., and Giles, C. L. (2007). Detecting research topics via the correlation between graphs and texts. In _Proceedings of the 13th ACM SIGKDD_ 

239 

_international conference on Knowledge discovery and data mining_ , pages 370– 379. ACM. 

- Jonsson, P. F. and Bates, P. A. (2006). Global topological features of cancer proteins in the human interactome. _Bioinformatics_ , 22(18):2291–2297. 

- Jonsson, P. F., Cavanna, T., Zicha, D., and Bates, P. A. (2006). Cluster analysis of networks generated through homology: automatic identification of important protein communities involved in cancer metastasis. _BMC bioinformatics_ , 7(1):2. 

- Kahng, A. B., Lienig, J., Markov, I. L., and Hu, J. (2011). _VLSI physical design: from graph partitioning to timing closure_ . Springer Science & Business Media. 

- Kamaliha, E., Riahi, F., Qazvinian, V., and Adibi, J. (2008). Characterizing network motifs to identify spam comments. In _Data Mining Workshops, 2008. ICDMW’08. IEEE International Conference on_ , pages 919–928. IEEE. 

- Ke, W., Borner, K., and Viswanath, L. (2004). Major information visualization authors, papers and topics in the acm library. In _Information Visualization, 2004. INFOVIS 2004. IEEE Symposium on_ , pages r1–r1. IEEE. 

- Kepes, F. (2007). _Biological Networks_ . Complex systems and interdisciplinary science. World Scientific. 

- Kessler, M. M. (1963). Bibliographic coupling between scientific papers. _American Documentation_ , 14(1):10–25. 

- Kleinberg, J. (2003). Bursty and hierarchical structure in streams. _Data Mining and Knowledge Discovery_ , 7(4):373–397. 

- Kottak, C. (1991). _Cultural anthropology_ . McGraw-Hill. 

240 

- Kuhn, T. (1970). _The Structure of Scientific Revolutions_ . Foundations of the unity of science. University of Chicago Press. 

- Kuhn, T. S. and Hawkins, D. (1963). The structure of scientific revolutions. _American Journal of Physics_ , 31(7):554–555. 

- Lancichinetti, A. and Fortunato, S. (2009). Community detection algorithms: a comparative analysis. _Physical review E_ , 80(5):056117. 

- Lancichinetti, A. and Fortunato, S. (2011). Limits of modularity maximization in community detection. _Phys. Rev. E_ , 84:066122. 

- Larsen, P. O. and Von Ins, M. (2010). The rate of growth in scientific publication and the decline in coverage provided by science citation index. _Scientometrics_ , 84(3):575–603. 

- Lee, S., Baker, J., Song, J., and Wetherbe, J. C. (2010). An empirical comparison of four text mining methods. In _System Sciences (HICSS), 2010 43rd Hawaii International Conference on_ , pages 1–10. IEEE. 

- Leydesdorff, L. and Rafols, I. (2012). Interactive overlays: A new method for generating global journal maps from web-of-science data. _Journal of Informetrics_ , 6(2):318–332. 

- Leydesdorff, L., Rafols, I., and Chen, C. (2013). Interactive overlays of journals and the measurement of interdisciplinarity on the basis of aggregated journal– journal citations. _Journal of the Association for Information Science and Technology_ , 64(12):2573–2586. 

- Long, B., Xu, X., Zhang, Z., and Philip, S. Y. (2007). Community learning by graph approximation. In _Data Mining, 2007. ICDM 2007. Seventh IEEE International Conference on_ , pages 232–241. IEEE. 

241 

- Luce, R. D. and Perry, A. D. (1949). A method of matrix analysis of group structure. _Psychometrika_ , 14(2):95–116. 

- Madlock-Brown, C. R. (2014). _A framework for emerging topic detection in biomedicine_ . The University of Iowa. 

- Mane, K. K. and B¨orner, K. (2004). Mapping topics and topic bursts in pnas. _Proceedings of the National Academy of Sciences_ , 101(suppl 1):5287–5290. 

- Mathioudakis, M. and Koudas, N. (2010). Twittermonitor: trend detection over the twitter stream. In _Proceedings of the 2010 ACM SIGMOD International Conference on Management of data_ , pages 1155–1158. ACM. 

- McCloskey, D. N. (1998). _The rhetoric of economics_ . Univ of Wisconsin Press. 

- Moody, J. and White, D. R. (2003). Structural cohesion and embeddedness: A hierarchical concept of social groups. _American Sociological Review_ , pages 103–127. 

- Morinaga, S. and Yamanishi, K. (2004). Tracking dynamics of topic trends using a finite mixture model. In _Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining_ , pages 811–816. ACM. 

- Morris, S. A. (2005). Manifestation of emerging specialties in journal literature: A growth model of papers, references, exemplars, bibliographic coupling, cocitation, and clustering coefficient distribution. _Journal of the Association for Information Science and Technology_ , 56(12):1250–1273. 

- Morris, S. A., Yen, G., Wu, Z., and Asnake, B. (2003). Time line visualization of research fronts. _Journal of the Association for Information Science and Technology_ , 54(5):413–422. 

242 

- Nepusz, T., Petr´oczi, A., N´egyessy, L., and Bazs´o, F. (2008). Fuzzy communities and the concept of bridgeness in complex networks. _Physical Review E_ , 77(1):016107. 

- Newman, M. E. (2006a). Finding community structure in networks using the eigenvectors of matrices. _Physical review E_ , 74(3):036104. 

- Newman, M. E. (2006b). Modularity and community structure in networks. _Proceedings of the national academy of sciences_ , 103(23):8577–8582. 

- Newman, M. E. and Girvan, M. (2004). Finding and evaluating community structure in networks. _Physical review E_ , 69(2):026113. 

- Nordenstreng, K. (2007). Discipline or field? soul-searching in communication research. _NORDICOM Review_ , 28. 

- Nowotny, H., Scott, P. B., and Gibbons, M. T. (2013). _Re-Thinking Science: Knowledge and the Public in an Age of Uncertainty_ . John Wiley & Sons. 

- O’Callaghan, D., Harrigan, M., Carthy, J., and Cunningham, P. (2012). Identifying discriminating network motifs in youtube spam. _arXiv preprint arXiv:1202.5216_ . 

- Ohniwa, R. L., Hibino, A., and Takeyasu, K. (2010). Trends in research foci in life science fields over the last 30 years monitored by emerging topics. _Scientometrics_ , 85(1):111–127. 

- Oka, M., Abe, H., and Kato, K. (2006). Extracting topics from weblogs through frequency segments. In _Proc. of the Workshop on the Weblogging Ecosystem: Aggregation, Analysis and Dynamics_ . 

- Onnela, J.-P., Saram¨aki, J., Kert´esz, J., and Kaski, K. (2005). Intensity and coherence of motifs in weighted complex networks. _Physical Review E_ , 71(6):065103. 

243 

Osborne, F. and Motta, E. (2012). Mining semantic relations between research areas. In _International Semantic Web Conference_ , pages 410–426. Springer. 

- Osborne, F. and Motta, E. (2015). Klink-2: integrating multiple web sources to generate semantic topic networks. In _International Semantic Web Conference_ , pages 408–424. Springer. 

- Osborne, F., Motta, E., and Mulholland, P. (2013). Exploring scholarly data with rexplore. In _International semantic web conference_ , pages 460–477. Springer. 

- Osborne, F., Salatino, A., Birukou, A., and Motta, E. (2016). Automatic classification of springer nature proceedings with smart topic miner. In Groth, P., Simperl, E., Gray, A., Sabou, M., Kr¨otzsch, M., Lecue, F., Fl¨ock, F., and Gil, Y., editors, _The Semantic Web – ISWC 2016_ , pages 383–399, Cham. Springer International Publishing. 

- Osborne, F., Scavo, G., and Motta, E. (2014). Identifying diachronic topic-based research communities by clustering shared research trajectories. In _European Semantic Web Conference_ , pages 114–129. Springer. 

- Osborne, F., Thanapalasingam, T., Salatino, A., Birukou, A., and Motta, E. (2017). Smart book recommender: A semantic recommendation engine for editorial products. 

- Palla, G., Barab´asi, A.-L., and Vicsek, T. (2007a). Quantifying social group evolution. _Nature_ , 446(7136):664–667. 

- Palla, G., Der´enyi, I., Farkas, I., and Vicsek, T. (2005). Uncovering the overlapping community structure of complex networks in nature and society. _arXiv preprint physics/0506133_ . 

244 

- Palla, G., Farkas, I. J., Pollner, P., Der´enyi, I., and Vicsek, T. (2007b). Directed network modules. _New journal of physics_ , 9(6):186. 

- Papadopoulos, S., Skusa, A., Vakali, A., Kompatsiaris, Y., and Wagner, N. (2009). Bridge bounding: A local approach for efficient community discovery in complex networks. _arXiv preprint arXiv:0902.0871_ . 

- Pham, M. C., Klamma, R., and Jarke, M. (2011). Development of computer science disciplines: a social network analysis approach. _Social Network Analysis and Mining_ , 1(4):321–340. 

- Pons, P. and Latapy, M. (2005). Computing communities in large networks using random walks. In _ISCIS_ , volume 3733, pages 284–293. 

- Porter, M. A., Mucha, P. J., Newman, M. E., and Friend, A. J. (2007). Community structure in the united states house of representatives. _Physica A: Statistical Mechanics and its Applications_ , 386(1):414–438. 

- Price, D. J. D. S. (1965). Networks of scientific papers. _Science_ , pages 510–515. 

- Price, D. J. D. S. (1986). _Little science, big science... and beyond_ . Columbia University Press New York. 

- Prˇzulj, N. (2007). Biological network comparison using graphlet degree distribution. _Bioinformatics_ , 23(2):e177–e183. 

- Radicchi, F., Castellano, C., Cecconi, F., Loreto, V., and Parisi, D. (2004). Defining and identifying communities in networks. _Proceedings of the National Academy of Sciences of the United States of America_ , 101(9):2658–2663. 

- Rafols, I., Porter, A. L., and Leydesdorff, L. (2010). Science overlay maps: A new tool for research policy and library management. _Journal of the Association for Information Science and Technology_ , 61(9):1871–1887. 

245 

Raghavan, U. N., Albert, R., and Kumara, S. (2007). Near linear time algorithm to detect community structures in large-scale networks. _Physical review E_ , 76(3):036106. 

- Rao, C. R. (1982). Diversity: Its measurement, decomposition, apportionment and analysis. _Sankhy¯a: The Indian Journal of Statistics, Series A_ , pages 1–22. 

- Reichardt, J. and Bornholdt, S. (2004). Detecting fuzzy community structures in complex networks with a potts model. _Physical Review Letters_ , 93(21):218701. 

- Reichardt, J. and Bornholdt, S. (2006). Statistical mechanics of community detection. _Physical Review E_ , 74(1):016110. 

- Roche, I., Besagni, D., Fran¸cois, C., H¨orlesberger, M., and Schiebel, E. (2010). Identification and characterisation of technological topics in the field of molecular biology. _Scientometrics_ , 82(3):663–676. 

- Rosen-Zvi, M., Griffiths, T., Steyvers, M., and Smyth, P. (2004). The author-topic model for authors and documents. In _Proceedings of the 20th conference on Uncertainty in artificial intelligence_ , pages 487–494. AUAI Press. 

- Salatino, A. A. and Motta, E. (2016). Detection of embryonic research topics by analysing semantic topic networks. 

- Salatino, A. A., Osborne, F., and Motta, E. (2017). How are topics born? understanding the research dynamics preceding the emergence of new areas. _PeerJ Computer Science_ , 3:e119. 

- Salatino, A. A., Osborne, F., and Motta, E. (2018a). Augur: Forecasting the emergence of new research topics. In _Proceedings of the 18th ACM/IEEE on Joint Conference on Digital Libraries_ , JCDL ’18, pages 303–312, New York, NY, USA. ACM. 

246 

- Salatino, A. A., Thanapalasingam, T., Mannocci, A., Osborne, F., and Motta, E. (2018b). The computer science ontology: A large-scale taxonomy of research areas. In Vrandeˇci´c, D., Bontcheva, K., Su´arez-Figueroa, M. C., Presutti, V., Celino, I., Sabou, M., Kaffee, L.-A., and Simperl, E., editors, _The Semantic Web – ISWC 2018_ , pages 187–205, Cham. Springer International Publishing. 

- Salton, G. and Buckley, C. (1988). Term-weighting approaches in automatic text retrieval. _Information processing & management_ , 24(5):513–523. 

- Sayyadi, H. and Raschid, L. (2013). A graph analytical approach for topic detection. _ACM Transactions on Internet Technology (TOIT)_ , 13(2):4. 

- Schultz, J. M. and Liberman, M. (1999). Topic detection and tracking using idfweighted cosine coefficient. In _Proceedings of the DARPA broadcast news workshop_ , pages 189–192. San Francisco: Morgan Kaufmann. 

- Scupin, R. (1998). _Cultural anthropology_ . Prentice Hall. 

- Shen, Z.-Y., Sun, J., and Shen, Y.-D. (2008). Collective latent dirichlet allocation. In _Data Mining, 2008. ICDM’08. Eighth IEEE International Conference on_ , pages 1019–1024. IEEE. 

- Shibata, N., Kajikawa, Y., Takeda, Y., and Matsushima, K. (2008). Detecting emerging research fronts based on topological measures in citation networks of scientific publications. _Technovation_ , 28(11):758–775. 

- Shneider, A. M. (2009). Four stages of a scientific discipline; four types of scientist. _Trends in biochemical sciences_ , 34(5):217–223. 

- Small, H. (1973). Co-citation in the scientific literature: A new measure of the relationship between two documents. _Journal of the Association for Information Science and Technology_ , 24(4):265–269. 

247 

- Small, H. (1999). Visualizing science by citation mapping. _Journal of the Association for Information Science and Technology_ , 50(9):799. 

- Small, H., Boyack, K. W., and Klavans, R. (2014). Identifying emerging topics in science and technology. _Research Policy_ , 43(8):1450–1467. 

- Small, H. and Upham, P. (2009). Citation structure of an emerging research area on the verge of application. _Scientometrics_ , 79(2):365–375. 

- Small, H. G. (1977). A co-citation model of a scientific specialty: A longitudinal study of collagen research. _Social studies of science_ , 7(2):139–166. 

- Steyvers, M., Smyth, P., Rosen-Zvi, M., and Griffiths, T. (2004). Probabilistic authortopic models for information discovery. In _Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining_ , pages 306–315. ACM. 

- Stirling, A. (2007). A general framework for analysing diversity in science, technology and society. _Journal of the Royal Society Interface_ , 4(15):707–719. 

- Sun, X., Ding, K., and Lin, Y. (2016). Mapping the evolution of scientific fields based on cross-field authors. _Journal of Informetrics_ , 10(3):750–761. 

- Sun, X., Kaur, J., Milojevi´c, S., Flammini, A., and Menczer, F. (2013). Social dynamics of science. _Scientific reports_ , 3. 

- Surowiecki, J. (2005). _The Wisdom of Crowds: Why the Many are Smarter Than the Few_ . Abacus. 

- Takeda, Y. and Kajikawa, Y. (2009). Optics: A bibliometric approach to detect emerging research domains and intellectual bases. _Scientometrics_ , 78(3):543– 558. 

248 

- Tang, J., Zhang, J., Yao, L., Li, J., Zhang, L., and Su, Z. (2008). Arnetminer: extraction and mining of academic social networks. In _Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining_ , pages 990–998. ACM. 

- Tian, Y., Hankins, R. A., and Patel, J. M. (2008). Efficient aggregation for graph summarization. In _Proceedings of the 2008 ACM SIGMOD international conference on Management of data_ , pages 567–580. ACM. 

- Tu, Y.-N. and Seng, J.-L. (2012). Indices of novelty for emerging topic detection. _Information processing & management_ , 48(2):303–325. 

- Ugander, J., Backstrom, L., and Kleinberg, J. (2013). Subgraph frequencies: Mapping the empirical and extremal geography of large graph collections. In _Proceedings of the 22nd international conference on World Wide Web_ , pages 1307–1318. ACM. 

- Upham, S. P. and Small, H. (2010). Emerging research fronts in science and technology: patterns of new knowledge development. _Scientometrics_ , 83(1):15–38. 

- Van Eck, N. J. and Waltman, L. (2010). Software survey: Vosviewer, a computer program for bibliometric mapping. _Scientometrics_ , 84(2):523–538. 

- Wang, J., Hu, X., Tu, X., and He, T. (2012). Author-conference topic-connection model for academic network search. In _Proceedings of the 21st ACM international conference on Information and knowledge management_ , pages 2179– 2183. ACM. 

- Wang, X. and McCallum, A. (2006). Topics over time: a non-markov continuoustime model of topical trends. In _Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining_ , pages 424– 433. ACM. 

249 

- Waugh, A. S., Pei, L., Fowler, J. H., Mucha, P. J., and Porter, M. A. (2009). Party polarization in congress: A network science approach. 

- Wu, Y., Venkatramanan, S., and Chiu, D. M. (2016). Research collaboration and topic trends in computer science based on top active authors. _PeerJ Computer Science_ , 2:e41. 

- Yan, E., Ding, Y., Milojevi´c, S., and Sugimoto, C. R. (2012). Topics in dynamic research communities: An exploratory study for the field of information retrieval. _Journal of Informetrics_ , 6(1):140–153. 

- Yi, S. and Choi, J. (2012). The organization of scientific knowledge: the structural characteristics of keyword networks. _Scientometrics_ , 90(3):1015–1026. 

- Zhang, L. V., King, O. D., Wong, S. L., Goldberg, D. S., Tong, A. H., Lesage, G., Andrews, B., Bussey, H., Boone, C., and Roth, F. P. (2005). Motifs, themes and thematic maps of an integrated saccharomyces cerevisiae interaction network. _Journal of biology_ , 4(2):6. 

- Zhang, S., Wang, R.-S., and Zhang, X.-S. (2007). Identification of overlapping community structure in complex networks using fuzzy c-means clustering. _Physica A: Statistical Mechanics and its Applications_ , 374(1):483–490. 

- Zhang, Y., Friend, A. J., Traud, A. L., Porter, M. A., Fowler, J. H., and Mucha, P. J. (2008). Community structure in congressional cosponsorship networks. _Physica A: Statistical Mechanics and its Applications_ , 387(7):1705–1712. 

- Zhou, D., Ji, X., Zha, H., and Giles, C. L. (2006). Topic evolution and social interactions: how authors effect research. In _Proceedings of the 15th ACM international conference on Information and knowledge management_ , pages 248–257. ACM. 

250 

# **Index** 

|**A**||Computer Science Ontology|26, 42, 71|
|---|---|---|---|
|advanced clique percolation method|114|confusion matrix|147|
|alter nodes|121|crisp partitioning|61|
|ancestors<br>66,|72, 140|**E**||
|**B**||early stage|3, 29|
|bag of words|33|ego networks|121|
|binary network|115|ego node|121|
|broader generic|27|embryonic stage|3, 58|
|burst detection|48|evolutionary networks|104|
|**C**||**F**||
|citation networks|38, 50|fuzzy partitioning|62|
|clique<br>|79, 110|**G**||
|clique graph|117|graph|69|
|clique percolation method|110|||
|advanced|114|**I**||
|cliques|114|index of collaboration|140|
|co-authorshiop networks|52|||
|co-occurrence network|69|**K**||
|co-word analysis|31, 53|k-clique|110|
|community detection|60|k-clique adjacency graph|117|



251 

|keyword networks|40, 69|**R**||
|---|---|---|---|
|keywords|39|recall|147|
|Kuhn Thomas<br>4, 11|, 55, 218|recognised stage|3, 29|
|||related equivalent|27|
|**L**||research fronts|51|
|Latent Dirichlet Analysis (LDA)|34|Rexplore|68|
|left semijoin|150|dataset|67|
|**M**||right semijoin|150|
|modularity|155|**S**||
|**N**||scholarly data|14|
|network density|67, 82|semijoin|150|
|networks||||
|||**T**||
|binary|115|||
|||taxonomy of topics|40|
|citation|38, 50|||
|||tf-idf|3234|
|co-authorship|52||,|
|||topic||
|co-occurence|69|i||
|||definition|23|
|ego|121|i||
|||dynamics|28|
|evolutionary|104|l||
|keyword|40, 69|ontoogy<br>|26<br>|
|||topicdetection|30|
|semantic-enhanced topic|71|||
|||toicdetectionandtrackin(TDT)|32|
|topic|71|p   g||
|||topic evolution|46|
|**O**||topic models|34|
|overlapping communities|62|topic network|71|
|overlay mapping|54|triad census|82|
|**P**||**Y**||
|pace of collaboration<br>67, 79, 81|, 85, 116|year of analysis|73|
|precision|147|year of debut|72|
||2|52||



