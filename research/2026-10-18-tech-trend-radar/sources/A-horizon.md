# A BIBLIOMETRIC HORIZON SCANNING METHODOLOGY FOR IDENTIFYING EMERGING TOPICS IN THE SCIENTIFIC LITERATURE 

**Artjay Javier*** Sciligent Alexandria, Virginia, US 

```
artjay.javier@sciligent.com
```

**Beth Masimore** 

Digital Science 

Cambridge, Massachusetts, USA 

```
b.masimore@digital-science.com
```

**F.G. Serpa** 

**John Chase** 

Digital Science Cambridge, Massachusetts, USA 

Sciligent 

Cambridge, Massachusetts, USA Alexandria, Virginia, USA `j.chase@digital-science.com gino.serpa@sciligent.com` 

**John T. Rigsby** 

Naval Surface Warfare Center, Dahlgren Dahlgren, Virginia, USA `john.rigsby@navy.mil` 

**Jeffrey Solka** 

**Avory Bryant Jeffrey Solka** Naval Surface Warfare Center, Dahlgren Naval Surface Warfare Center, Dahlgren Dahlgren, Virginia, USA Dahlgren, Virginia, USA `avory.bryant@navy.mil jeffrey.solka@navy.mil` 

**Ryan J. Zelnio** Office of Naval Research Arlington, Virginia, USA `ryan.j.zelnio@navy.mil` 

## **ABSTRACT** 

A bibliometric methodology for scanning for emerging science and technology areas is described, where topics in the science, technology and innovation enterprise are discovered using _Latent Dirichlet Allocation_ , their growth rates are modeled using _first-order rate kinetics_ , and research specialization of various entities in these topics is measured using the _location quotient_ . Multiple interactive visualization interfaces that integrate these results together to assist human analysts are developed. This methodology is demonstrated by analyzing the last five years of publications, patents and grants ( _≈_ 14 _million documents_ ) showing, for example, that _deep learning for machine vision_ is the fastest growing area, and that China has a stronger focus than the U.S. in this area. 

**_K_ eywords** bibliometrics, horizon scanning, umap, mallet, latent dirichlet allocation, topic modeling, location quotient, scientometrics, natural language processing, unsupervised learning 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 

## **1 Introduction** 

Bibliometric horizon scanning[7] has long been used to assess and forecast trends[9] in the scientific and technical literature[14] as well as measure the interaction between countries, organizations and people in vast interlinked collaboration[31] and influence[11] networks. Horizon scans are often used by both public[22] and private[12] sector enterprises to strategically allocate their resources, whether that be investments, staff effort and hiring, or future policy decisions[6]. The _Organisation for Economic Co-operation and Development (OECD)_ defines horizon scanning as _a technique for detecting early signs of potentially important developments through a systematic examination of potential threats and opportunities, with emphasis on new technology and its effects._ [5] Our methodology addresses these challenges by (1) systematically ingesting a broad collection of millions of recently published science and innovation documents, (2) examining rapidly growing research and innovation areas, emphasizing small research areas that may receive less attention, (3) identifying key actors who may present both threats and opportunities, and (4) integrating human interpretation to help assess the impact of these new technologies. A key motivation informing our approach is the need for transparency and clarity to facilitate the human-machine interaction by assisting the analyst/subject matter experts examining the results of the bibliometric horizon scan to synthesize a cohesive story and assemble the evidence to support it. Therefore data visualization, simple intuitive metrics, and rapid screening and filtering techniques are central themes in our methodology. 

### **1.1 Analyzing Technical Concepts** 

The challenge of efficiently and thoroughly analyzing millions of scientific documents can be addressed with modern machine learning methods, specifically unsupervised learning which exploits patterns inherent in a collection of documents, and requires no _a priori_ knowledge, no pre-existing taxonomic structure, and no human-labeling of documents. While traditional hard clustering methods ( _i.e. k-means clustering[21]_ ) group documents into clusters that limit documents to possessing membership in only one cluster, soft clustering methods _i.e. Latent Dirichlet Allocation (LDA)_ [10] allow documents to be members of multiple topics, and likewise for topics to be composed of multiple documents. This additional flexibility is a more accurate reflection of real documents, and affords documents with strongly mixed themes an additional degree of freedom during optimization. However, a drawback of unsupervised learning is that the topics are not immediately human readable, consisting typically of lists of words with various probabilities. While recent methods[19] have made this topic labeling process more automatic, more consistent and nuanced labels can be potentially created by experienced analysts if they are given the tools to thoroughly and efficiently evaluate the topic model. While multiple open source tools provide separate avenues to visualize topic 

models[16, 30, 29], none comprehensively give the analyst (1) a 2D map of these topics revealing clusters of related topics (like the one shown in Figure 1), (2) a coherent view of both the _term/topic_ and _document/topic_ distributions, (3) a way to apply labels and aggregate topics into custom categories to further shape the appearance of the topic map, (4) reports of objective measures of the topic quality of each topic, and (5) a single web-based browser interface that performs all of the above. We discuss results from the use of one such interface (shown in Figure 2) developed for this purpose and whose agile development benefited from continuous feedback from analysts. 

### **1.2 Detecting Emerging Science and Technology** 

Methods to detect emerging sciences and technologies must be sensitive to "weak signals[8]" areas too early in their maturity to be strong enough to compete with other more mature topics, but growing at such a fast and consistent rate that their future position of dominance is very likely. It has been commonly observed that counting the number of scientific publications and patents published per year reveals a rising, superlinear trend. However, detailed modeling of the entire scientific enterprise is a complex undertaking and beyond the scope of this investigation. To simplify the problem, we model the observed superlinear growth with the simplest possible formulation by using first-order rate kinetics: the rate of growth/decay� _<u>dNdt</u>_ � is proportional to the number of publications ( _N_ ), shown in Equation 1. 



When integrated, this model predicts an exponential growth or decay in publications, over time, as shown in Equation 2, where _N_ = _N_ 0 when _t_ 0 = 0. 



To improve the human interpretability of the first-order rate equation, we rearrange it to represent the familiar value of the _Compound Annual Growth Rate (CAGR)_ popularized in finance, and sometimes called the _Year-Over-Year (YOY)_ percentage increase relative to the prior year. CAGR can be directly derived<sup>1</sup> from the _rate constant_ ( _k_ ) as: 



CAGR is a proxy for the rate of emergence, emphasizing not the overall strength of any signal, but how fast that signal grows over time. This lack of dependency on the overall signal has the potential to make it more sensitive to so-called "weak signals." By focusing, for example, on 

> 1Consider a full growth interval (∆ _t_ = _tf − ti_ = 1) where _Ni_ has grown by a percentage amount, CAGR, to _Nf_ = (1 + _CAGR/_ 100) _Ni_ , then insert into Equation 2, then rearrange for CAGR to derive Equation 3. 

2 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 



Figure 1: Map of 10,000 topics modeled with _MALLET_ [17] using titles and abstracts from _∼_ 14M publications, patents and grants from 2014-2018 drawn from the _Dimensions_ data set, with semi-transparent colors (with overlap leading to greater saturation) corresponding to _Fields of Research (legend)_ [1], marker size proportional to the number of documents, layout using _UMAP_ [24], and final visualization with _Python 3.5/matplotlib[13]_ . Inset: Magnified portion of the fastest growing region (colors based on Compound Annual Growth Rate (CAGR)). 

topics that have high CAGR but low document frequencies, finding emerging topic areas still in their infancy is possible. More details on the statistical testing of this model appear in the Supplemental Information. 

### **1.3 Measuring Area Specialization** 



For understanding opportunities and threats, the actions of various entities in different arenas can often produce a coherent picture that describes their strengths and weaknesses. However, raw scores of their activities in different areas can be complicated by (1) scale, wherein some entities have more influence and resources than others, thus allowing smaller players to go unnoticed, and (2) the tendency for many entities to favor the same arenas resulting in their patterns to look so similar that their potentially important subtle differences are lost. 

To address these issues, the _Location Quotient[20] (LQ)_ is employed as the prime evaluation metric for determining an entity’s focus. Denoting _ni,j_ as the activity of an entity _j_ in an area _i_ , we express the focus of entity _j_ on area _i_ as _LQi,j_ (Equation 4) where the numerator is the activity of an entity normalized by the sum of its areas of interest ( _ni,j_ <u>�</u> _k_<sup>_nk,j_) and the denominator evaluates the same ratio but</sup> for all entities ( <u>�</u> _<u>l</u>_<sup>_ni,l_</sup> <u>�</u> _k,l_<sup>_nk,l_).</sup> 

LQ addresses the above concerns in the following ways: First, because LQ is normalized against the sum of an entity’s proportions in all categories, it enables scale-free comparisons between entities. Second, because it is normalized against the relative proportions of all entities over all categories, it receives a boost in its sensitivity against this global baseline. Finally, the LQ is easily interpretable: For a category where _LQ <_ 1, the entity is underrepresented relative to all others, whereas _LQ_ = 1 categories are where the entity has the same proportions to its peer average, and when _LQ >_ 1 the entity is more represented in these categories than the global average. However, the boosted sensitivity of the LQ has its drawbacks. For example, since it is doubly normalized, it can cause high error rates at low counts. As a mitigation, these errors are assessed using typical error propagation formulas[23], which aids in screening potentially spurious LQ values. 

3 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 



Figure 2: A screenshot of the interactive _Bokeh_ dashboard used by analysts to label and explore the content of the corpus as part of the _ONR Portfolio Analysis Library (OPAL) (see footnote in corresponding text for more information)_ with the following elements: (a) a drop-down menu listing topics by index, (b) terms in descending order of relative frequency for the selected topic, (c) an interactive, scalable view of the topic map using the UMAP layout, and shown with the analyst-assigned labels, (d) legend for the topic map showing super topics aggregated by different colors, (e) a document browser showing documents with a high topic probability in the selected document, (f) a detail widget showing features of both the topic and document selected. 

## **2 Materials and Methods** 

### **2.1 Source Database & Vocabulary Preparation** 

The _Dimensions_ [3] data sets were used exclusively in this work. Scientific publications with a publication date, or patents with a granted date, or grants with a start date, between 2014 to 2018 were used in this analysis. This resulted in 11 _,_ 517 _,_ 625 publications, 937 _,_ 369 grants and 1 _,_ 436 _,_ 876 patents. Titles and abstracts were extracted from the documents and processed using the following steps, which included the use of a vocabulary preparation methodology[25] based on topic-based phrases. Complete details appear in the Supplementary Information. 

threading for fast computation, topic-based phrase generation to assess topic content, and automatic generation of topic diagnostic output for objective assessment of topic model quality. Based on prior experience with this corpus and other similar corpora, it was decided to fit the corpus to 10 _,_ 000 topics to obtain distinct topics which minimize mixing between unrelated topics. 

The _topic/document_ matrix is a side-product of the topicmodeling process that reports a probabilistic topic value ( _ti,j_ ) for every topic( _i_ ) to every document( _dj_ ) for all documents( _j_ ). Since this value is normalized for any given document (<sup>�</sup> _i_<sup>_ti,j_= 1), we carried out all subsequent cal-</sup> culations over topics that require a count of documents as a sum of these topic probabilities (<sup>�</sup> _j_<sup>_ti,j_)2.For sim-</sup> 

### **2.2 Topic Modeling** 

The LDA implementation in _Machine Learning for Language Toolkit (MALLET)_ [17] was selected because of its use of Gibbs sampling for robust optimization, multi- 

> 2Furthermore, when this is summed over all documents( _j_ ) and all topics, this produces:<sup>�</sup> _i,j_<sup>_ti,j_=</sup><sup>_D_, where</sup><sup>_D_is the sum</sup> of all documents in the corpus. This is both theoretically true and empirically observed in this work 

4 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 



Figure 3: A calibration-style plot showing _CAGR(%)_ calculated using nonlinear regression with Equation 3 on the _y-axis_ and plotted with fit errors as error bars, and the traditional two-point CAGR formula on the _x-axis_ , _CAGR(%) (traditional)_ . Calibration line (orange): y = x 

plicity, we report sums obtained in this way as _Documents_ or _document counts_ , but as described above, they are not necessarily whole numbers<sup>3</sup> . 

### **2.3 Metrics** 

### **2.3.1 Compound Annual Growth Rate (CAGR)** 

CAGR was calculated by summing the number of _Documents_ (as described in the previous section) per topic per year to create a time series. Nonlinear least-squares curvefitting was then carried out using the _LMFIT_ [27] Python package to obtain optimized fit parameters and their corresponding errors for all 10 _,_ 000 topics. This technical improvement addresses issues inherent in the conventional CAGR formula which uses only two data points<sup>4</sup> , and inherently provides no estimate of error. By fitting the model to all the data points more robust and accurate calculation are achieved. Furthermore the fit parameter errors provide insight on how closely, or loosely, the data can be described by the model. 

The value of using nonlinear regression versus the traditional CAGR formula[15] can be seen in Figure 3. Several 

> 3For any given topic, _fractional document counting_ will typically undercount _whole document counting_ by a factor roughly proportional to the average number of words in the text. In this case, since we use the titles and abstracts, together they have a sum of total words of order _∼_ 10<sup>2</sup> . The cause of this undercounting is that documents contain many words that are not specific to a particular topic and since topic frequencies are based on the word count in a document, they will be proportionately affected. 

> 4The traditional CAGR formula relies only on the initial point ( _t_ 0 _, N_ 0) and the final point ( _tn, Nn_ ) such that: 



points with large errors appear outside of the calibration line - points that could not be distinguished from the others without an error estimation. Below the calibration line are points that appear with a larger apparent CAGR based on the two-point formula. These points would be regarded as false positives if a CAGR screen was used with the two-point formula. Above the calibration line are topics that would have received a lower ranking based on the two-point formula, or points that would have been missed in a CAGR screen. At high CAGR (right hand side of plot) there is a noticeable positive (upward) deviation from the calibration line, indicating a general underestimation of CAGR by the traditional formula. 

### **2.3.2 Location Quotient (LQ)** 

LQ was calculated with entities including the country, sponsor, organization, individual, or data source. Each entity’s representation in a topic was determined using _document counts_ with the LQ formula in Equation 4. 

### **2.4 Visualization & Analyst Labeling** 

To visualize the results of the topic map, several _multidimensional scaling (MDS)_ algorithms were evaluated including _Principal Component Analysis (PCA)_ and _tDistributed Stochastic Neighbor Embedding (t-SNE)_ . _Uniform Manifold Approximation and Projection (UMAP)_ [24] provided the best (and fastest) visualization based on the criteria that topics closely resembling each other would be located near each other as topic clusters. This clustering behavior can be controlled in UMAP to favor local structure over global structure by constraining the local neighborhood prior to optimization<sup>5</sup> . Custom interactive dashboard interfaces using _Plotly Dash_ [2] or _Bokeh_ [4] were developed for visualizing _MALLET’s_ outputs<sup>6</sup> . These visualizations were strongly inspired by _pyLDAvis_ [29]. To facilitate the analyst labeling process, interactive dashboards were employed using _OPAL_<sup>7</sup> . A screenshot of an example dashboard appears in Figure 2. The topic map is zoomable and displays topic information upon mouseover. It also labels each topic with the analyst-selected name, and colors the topic according to a _supertopic_ scheme devised by the analyst (described below). Upon clicking on any topic, the term distribution is shown as a horizontal bar chart, which is useful for determining the relative dominance of various words in the topic: for example, topics with a narrow distributions behave more like single terms. While many modern topic model visualizations[29, 30, 16] leave out the topic/document matrix, we implemented visualizing 

> 5The parameter _n_neighbors_ controls this local versus global tradeoff in _UMAP_ and was set to 15 (the default value) for this study. 

6These include the optimized Gibbs state file, the topic diagnostics XML file, and the topic-phrase report XML file. 

> 7 _ONR Portfolio Analysis Library (OPAL)_ is a Python-based Government Off the Shelf (GOTS) product developed by _Sciligent, LLC_ and is made available only to U.S. Government Employees and their direct support contractors. 

5 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 

this as a document browser, sorted in descending order by the fractional composition of that topic within each document. This is useful for determining if that topic is strongly represented in a single document or broadly distributed at very low fractional levels across multiple documents. Selecting any document in the browser then displays document information for further inspection, including the full abstract/description which can be useful for the analyst to understand, interpret or give context as to why the topic is represented in those documents. Last, the proximity of that topic to other topics in the topic map give some indication of the broader category of that topic. These separate elements contribute to an exploratory workflow that the analyst uses to quickly assign a topic label, to understand the structure and content of the corpus, and to discover patterns within the corpus that may not be apparent from document sampling or viewing existing categories in isolation. For example, interdisciplinary areas and applied research areas are often found in close proximity to core research areas in the topic map visualization. 

Using these dashboard interfaces, analysts labeled each topic index with two names: _Topic Name_ and _Super Topic Name_ . The _Topic Name_ is a human-readable label, typically 2-3 words, that attempts to concisely capture what the topic is about. The _Super Topic Name_ is assigned based on the goal of aggregating multiple related topics into a single umbrella term, with the goal of limiting the total number of _Super Topic_ categories to a manageable quantity ( _<_ 20). Not all topics contain technology-specific information relevant to this study and were ignored<sup>8</sup> . For static output and semi-automated batch processing of clusters of topics, _matplotlib/Python_ was used with _adjustText_ [18] to improve readability, such as the one shows in the inset of Figure 1. 

## **3 Results** 

### **3.1 Topic Diagnostics Output** 

Topic Diagnostics were examined from the _MALLET_ output to assess the quality of both the overall model as well as individual topics. The _coherence_ is a useful measure of how well the underlying documents are represented by the highest frequency terms of that topic and a potentially good indicator of topic quality[26]. From prior experience, a coherence of ⪆ _−_ 1000 is typically indicative of wellformed topics. The vast majority of topics ( _>_ 92%) are above this threshold _(See Supplemental Information)_ . 

> 8These omitted topics include those that are non-technical _(i.e. containing administrative or marketing language)_ , are mixtures of two or more unrelated topics, or are trivial _(i.e. the names of all amino acids, or a list of colors)_ , or are not indicative of a specific technology area _(i.e. clinical trials)_ . Examples appear in the Supplementary Information. 

### **3.2 Topic Map Topology** 

### **3.2.1 Global Structure** 

While the 2D Cartesian axes need not necessarily follow any particular pattern, a speculative observation consistent with repeated permutations presents some useful heuristics: One axis (in this permutation, the vertical axis) can be interpreted as a spectrum of _scale_ starting at the top with microscopic particles and ending at the bottom with societies of people. The other axis (in this permutation, horizontal axis) seems to correspond to _complexity_ , starting at the left with abstract concepts and lifeless particles and ending at complex organisms on the right. Importantly, this is not a scheme that was imposed, but which arises naturally from multidimensional scaling. It is also _not_ unique to UMAP, or the _Dimensions_ data set, or even our software development cycle<sup>9</sup> . 

### **3.2.2 Local Structure** 

The local morphology exhibits long, distinct, strand-like filaments. Topics align themselves in these one-dimensional structures with significant white space separating them. This strong clustering pattern can be emphasized with _UMAP_ , as opposed to other multi-dimensional scaling algorithms such as _PCA_ , which allows clusters of topics to be easily distinguished. This control over the local clustering also allows for the visualization of areas which are closely related, such as the relationship between _machine vision_ and _deep learning_ as shown in Figure 1 inset. 

### **3.2.3 Source Localization** 

A key concern of merging together multiple sources is that the inherent tendencies toward corpus-specific vocabularies may cause an attempt to combine them to result in undesirable phase segregation<sup>10</sup> . Our approach allows us to visualize the magnitude of any such segregation from the topic map topography: Figure 4 recolors Figure 1 according to the LQ of the source data: publications, patents or grants. As can be seen, _publications_ are distributed evenly with slightly stronger focus in _biomedicine and biology_ . Not surprisingly, _patents_ are strongly focused in _engineering and technology_ . _Grants_ are broadly distributed but have a specific focus in the _humanities_<sup>11</sup> . It can be seen that there is no strong segregation _(i.e. separated clusters with large intervening white space)_ , indicating the shared technical terminology between these corpora is stronger than differences in the language usage between them, thus 

> 9We have observed it using _both_ in PCA and t-SNE, in other S&T literature databases such as the _Web of Science_ , and simply using _pyLDAvis_ for visualization with any of the above. 

10Some of these effects were mitigated by the removal of problematic terms. For example, adding "claim," a term frequently but non-specifically in the patent literature, to the stopword list 

11Not necessarily due to increased funding, but likely to arise from less patent and publication activity. Grants are also not limited to traditional academic areas but also fund, for example, museums and other learning centers. 

6 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 



Figure 4: Topic Map of 10 _,_ 000 topics with the same layout parameters as Figure 1. Color is proportional to the _Location Quotient (LQ)_ of the data source shown in the colorbar to the right of each source: _Publications (left), Patents (middle), or Grants (right)._ 

resulting in most topics possessing mixtures of different sources. 

### **3.3 Labeling & Aggregating the Fastest Growing Topics** 

Since CAGR is a useful screen for allocating analyst labor toward potentially emerging topical areas, analysts labeled the top 200 fastest growing (highest CAGR) topics. The top 10 identified in this way shown in Table 1. Then analysts labeled each topic with a _Topic Name_ consisting of 1-4 words and a _Super Topic Name_ drawn from a controlled list of categories, such that each Super Topic is a broader category for which other topics would be held under, as shown in Table 2. This process created human-readable labels for the topics and the opportunity for analysts to apply a custom taxonomy. Here, we elected to group topics without any such agenda, and pursued only the goal of reducing the number of aggregated topics to less than an arbitrarily selected 20 super topics. 



Figure 5: A histogram of _Compound Annual Growth Rate (CAGR)_ for all 10 _,_ 000 topics modeled. Reference lines are shown for the mean growth rate and 0% growth rate, as visual indicators revealing inflationary growth by the majority of topics. Box drawn shows the top 2% of topics that are analyzed in further detail in this work. _INSET_ : Expanded view showing shape of distribution. 

### **3.4 Rapidly Emerging Science & Technology** 

The CAGR values for all 10,000 topics are plotted as a histogram shown in Figure 5. The CAGR plot has the shape of a normal distribution with the mean _±_ standard deviation of 3 _._ 5% _±_ 3 _._ 9% , removing outliers by excluding points more than three standard deviations away. The mean of the standard errors of CAGR (determined from the nonlinear regression) is 1 _._ 4%. Since the the mean standard error is less than the standard deviation of CAGR, we conclude that the spread in the distribution is statistically significant since the width of the CAGR peak is more than double that of the mean standard errors<sup>12</sup> . However, because the sizes of these errors is still somewhat comparable, the shape of the peak is not an exact representation of the underlying CAGR distribution, but likely to be convoluted with the 

> 12Since the standard deviation of CAGR ( _σ_ = 3 _._ 9) was obtained from a large sample size (10,000) the chances that the true standard deviation of the distribution is the same as the mean error ( _ϵ_ = 1 _._ 4) is negligible based on the results of statistical testing _(p-value=0)_ . 

Gaussian error function leading to line broadening and a potential loss of distinguishing features. 

### **3.5 Evaluating Weak Signals** 

Another useful factor for analytic consideration is the size of the topic, which provides an additional opportunity to screen for topics that are smaller in size, and potentially less well-known. These low-frequency count topics are the "weak signals" that are often ignored in traditional analyses that track the dominant areas and dominant entities. However, simply sifting through these low frequency count topics alone can be a tedious and time-inefficient task, as the large majority are unlikely to be emerging topics areas. However, combining this with the CAGR screen helps highlight which of these areas should be focused on: their rapid growth is a leading indicator that their limited awareness and small footprint today may be drastically different tomorrow. In Figure 6 we plot the top 200 topics based on their size and growth rate. This plot demonstrates how 

7 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 

Table 1: The top 10 fastest growing (highest CAGR) topics, including the analyst-assigned labels ( _Topic Name, Super Topic Name_ ), the _Topic Size_ (by virtual document count), the _Compound Annual Growth Rate (CAGR)_ , the topic _Coherence_ <u>, and the top 5 highest frequency terms in that topic.</u> 

|**Topic**<br>**Index**|**Topic Name**|**Super Topic**<br>**Name**|**Top Terms**|**Coherence**|**CAGR(%)**|
|---|---|---|---|---|---|
|4102|Blockchain|Technology|blockchain, transaction, bitcoin, currency,|-439|106_±_25|
|676|Neural Networks|Neural Networks|neural_network, train, cnn, deep_learning,|-365|95_±_4|
|350|Deep Learning|Neural Networks|deep_learning, deep, train, neural_network,|-412|89_±_2|
|4403|Deep Learning|Neural Networks|deep, neural_network, train, deep_learning,|-428|86_±_4|
|9356|Image Segmentation|Machine Vision|image, train, cnn, segmentation,|-356|86_±_5|
|9392|Image Classification|Machine Vision|image, train, cnn, deep, convolutional|-342|80_±_4|
|9759|Deep Learning|Neural Networks|train, deep_learning, image, deep, learn|-402|77_±_6|
|9252|Image Recognition|Machine Vision|image, cnn, recognition, classification, train|-354|75_±_3|
|3096|Machine Learning|Machine Learning|train, learning, learn, algorithm, generative|-420|53_±_7|
|1053|Perovskite Solar Cell|Solar Cells|perovskite, solar_cell, pbi, halide, film|-349|51_±_9|





Figure 6: For the top 200 (2%) fastest growing topics, the topic size (based on the number of documents) and the _Compound Annual Growth Rate (CAGR)_ , with associated fit errors shown as error bars, are plotted. The 15 fastest growing topics are labeled with the analyst-selected _Topic Name_ . _INSET_ : Expanded plot of the box drawn at the bottom left-hand side of the main figure. 

low document count, fast growing topics can be identified. Here, we can see multiple topics in _deep learning_ of significant size growing very rapidly. Of lower size and growth rate are _perovskite solar cells_ , still significant but not in the same class as the deep learning topics. Finally, if the lowest signals are examined (which are still growing significantly within the top 2% of fastest growing topics), _neutrophil to lymphocyte ratio_ and other health-related topics can be interpreted as the small, rapidly emerging topics. Some topics such as _bupivacaine_ are not well known, and may not necessarily be an emerging research area and ultimately require analyst assessment to determine the cause of their growth. Thus, this approach does not decisively identify emerging topics, but instead helps narrow the topics requiring technical due diligence, which more efficiently directs analyst effort. Another important limitation arises from analyzing only the top 2% of fastest growing topics is that closely related, but slower growing portions are not included when aggregating the topic size. For example, the super topic group _Neural Networks_ contains only the fastest growing areas, but many other slower growing areas can be placed in this grouping. 

### **3.6 Major Players & Rising Competitors** 

### **3.6.1 Areas of Specialty** 

While LQ can be calculated over many different category types in the data set, specifically aggregating over _topics_ and/or _supertopics_ allows LQ to be interpreted as an entity’s areas of topic focus, or specialization. An example using this metric is shown in Figure 7, which plots the LQ for USA and China for the super topics shown in Table 2. Each quadrant of this chart indicates areas of specialty. While the USA leads in the most areas, largely in health topics like _cancer, infectious disease_ , and _microbiome_ , China focuses on fewer topics, with clear leads in _catalysts_ and _portable energy_ . China also maintains a slight lead in AI: _neural networks_ and _machine learning_ . Both the USA and China have limited relative focus in _farming, manufacturing and electric grids_ . The fastest growing areas, _machine vision, deep learning and solar cells_ , are within 

8 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 

Table 2: The top 200 (2%) fastest growing topics aggregated up to the top 20 _Super Topics_ . _Topics_ are listed in descending order of frequency, with CAGR and associated error also listed. 

|**CAGR(%)**|**Super Topic Name**|**Top Topics**|
|---|---|---|
|77_±_3|Neural Networks|Deep Learning, Extreme Learning Machines, Neural Networks|
|60_±_4|Machine Vision|Image Classification, Hyperspectral Image Classification, Image Recognition,|
|37_±_5|Solar Cells|Perovskite Solar Cell|
|23_±_1|Catalysts|Photocatalysts, Catalysts, Oxygen Reduction, Photocatalytic Water Splitting,|
|22_±_1|Technology|Mobile Computing, Text Analytics, Cloud Computing, Internet of Things,|
|21_±_1|Cancer|Neutrophil Lymphocyte Ratio, Cancer Immunotherapy,|
|21_±_0|Gene Expression|MicroRNA, Long Noncoding RNA, CRISPR/Cas9, Exosome, Cell Free DNA,|
|21_±_2|Manufacturing|Additive Manufacturing, Manufacturing Automation, Steel Microstructure,|
|20_±_3|Machine Learning|Machine Learning, Classification, Support Vector Machines, Decision Tree,|
|20_±_1|Microbiome|Gut Microboime, Fecal Microbiota, Bacteria, Bacterial Community,|
|19_±_4|Infectious Disease|Antibiotics, Viruses, Dengue|
|19_±_2|Materials|Molybdenum Sulfide Monolayers, Metal-Organic Frameworks,|
|18_±_2|Portable Energy|Supercapacitor, Batteries, Lithium Sulfur Batteries, Lithium Batteries, s|
|17_±_3|Miscellaneous|Telescope, Fracking|
|17_±_0|Unmanned Aerial Vehicles|Unmanned Aerial Vehicles, Drones, Umanned Aerial Vehicles|
|16_±_3|Painkillers|Pain, Opioid, Bupivacaine|
|15_±_1|Farming|Farming, Crop Yield, Fertilizer|
|15_±_0|Health|Smoking, Caregiving, Elderly, Breastfeeding, Geriatric, Tobacco, Dementia,|
|15_±_1|Urbanization|Autonomous Vehicles, Urbanization, Pollution, Wastewater, Air Pollution|
|14_±_1|Electric Grids|Microgrids, Grid, High Voltage DC Converter|
|14_±_2|Sports Performance|Track & Field, Exercise, Concussion|





Figure 7: A plot of the _Location Quotients (LQ)_ of the USA and China for the fastest growing 200 (2%) topics aggregated into 20 super topics. _Quadrant I,III_ : Topics where USA and China are both well represented, or both poorly represented, respectively. _Quadrant II,IV_ : Topics where either USA or China are more represented than the other, respectively. 

China’s quadrant but relatively close to the center (1 _,_ 1), which indicates these may be areas of competition. A similar plot with similar conclusions can be constructed using authors, author organizations, funding sponsors, etc. to understand the areas of focus of all of these entities relative to each other. 

### **3.7 Applications** 

### **3.7.1 Technology Scouting** 

Horizon Scanning for Emerging Technologies is a popular exercise in the public sector[28]. Understanding the landscape of emerging technologies and their potential threats drive decisions on how resources are allocated. This methodology nominates emerging technology areas for their consideration, which can then be evaluated by subject matter experts and analysts to assess their disruptive potential. Using LQ in combination with CAGR at the country level can give some indication of rising technological threats, for example what is shown in Figure 7. Ultimately, this could inform how current resources are allocated and provide an early warning system as to what the threat may possibly be, and from where it will come from. 

For government R&D funding organizations heavily engaged in the strategic investment in various science and technology areas, understanding the landscape of major players, whether they be state actors, similar funding authorities, or research organizations is an important starting point for managing their research investment portfolio. LQ can provide information on the specialization of various entities, which can guide their decision making. For example, 

9 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 

they can be valuable when government R&D organizations are considering new research initiatives, or as a means of rapidly understanding a particular organization’s strengths during a competitive selection. Using the LQ on other grant awarding organizations, based on sponsorship mentions in publication acknowledgments, can also give the government R&D organization insight into what other government agencies are also supporting particular topic areas. This could present the opportunity for these organizations to work cooperatively. 

- [9] BETTENCOURT, L., KAISER, D., KAUR, J., CASTILLO-CHAVEZ, C., AND WOJICK, D. Population modeling of the emergence and development of scientific fields. _Scientometrics 75_ , 3 (2008), 495– 518. 

- [10] BLEI, D. M., NG, A. Y., AND JORDAN, M. I. Latent dirichlet allocation. _Journal of machine Learning research 3_ , Jan (2003), 993–1022. 

- [11] BOYACK, K. W., AND KLAVANS, R. Co-citation analysis, bibliographic coupling, and direct citation: Which citation approach represents the research front most accurately? _Journal of the American Society for information Science and Technology 61_ , 12 (2010), 2389–2404. 

## **4 Future Work** 

Due to space limitations, a full analysis and exploration of the results combined with analyst interpretations of this horizon scan will be the topic of a future report. The use of a dynamic model of topical areas offers the potential of forecasting the dominance of currently emerging science and technology areas. However, our use of first-order rate kinetics is limited to only a few years since its assumptions break down at longer timescales - thus future work will focus on developing a more comprehensive model. 

   - [12] BROWN, D. Horizon scanning and the business environment—the implications for risk management. _BT Technology Journal 25_ , 1 (2007), 208–214. 

- and technology areas. However, our use of first-order rate [13] CASWELL, T. A., DROETTBOOM, M., LEE, A., kinetics is limited to only a few years since its assumptions HUNTER, J., FIRING, E., STANSBY, D., KLYMAK, break down at longer timescales - thus future work will J., HOFFMANN, T., DE ANDRADE, E. S., VAROfocus on developing a more comprehensive model. QUAUX, N., NIELSEN, J. H., ROOT, B., ELSON, P., MAY, R., DALE, D., LEE, J.-J., SEPPÄNEN, J. K., MCDOUGALL, D., STRAW, A., HOBSON, 

- **5 Acknowledgments** P., GOHLKE, C., YU, T. S., MA, E., VINCENT, A. F., SILVESTER, S., MOAD, C., KNIAZEV, N., 

- Some of this work was generated in the course of supIVANOV, P., ERNEST, E., AND KATINS, J. mat- 

- porting the _Data and Analytics Laboratory at the Of-_ plotlib/matplotlib v3.2.0rc3, Feb. 2020. 

Some of this work was generated in the course of supporting the _Data and Analytics Laboratory at the Office of Naval Research (ONR)_ through contract number GS00Q09BGD0019 in their mission to develop better tools for research portfolio analytics. Cleared by ONR for public release: DCN: 43-895221. 

- [14] CHEN, C. Citespace ii: Detecting and visualizing emerging trends and transient patterns in scientific literature. _Journal of the American Society for information Science and Technology 57_ , 3 (2006), 359–377. 

- [15] CHOI, D. G., LEE, H., AND SUNG, T.-K. Research profiling for ‘standardization and innovation’. _Scientometrics 88_ , 1 (2011), 259–278. 

## **References** 

- [1] The australian and new zealand standard research classification - fields of research. 

   - [16] CHUANG, J., MANNING, C. D., AND HEER, J. Termite: Visualization techniques for assessing textual topic models. In _Proceedings of the international working conference on advanced visual interfaces_ (2012), pp. 74–77. 

- [2] Dash by plotly. 

- [3] Digital science. dimensions | the next evolution in linked scholarly information. 

- [4] Interactive data visualization in the browser, from python. 

   - [17] DRUCK, G., MIMNO, MCCALLUM, A., BADENESOLMEDO, C., SUTTON, C., CLAIRE, SINGH, S., YAO, L., MENDES, S. P., WUNDERLICH, M., KÖRNER, M., SOERGEL, D., RING, D., MIHAIIANCU, HUANG, M., DREVICKO, CAPDEVILA, C., RUTHERFORD, T., MISHRA, S., SOUTHERN, S., RICHARDET, R., ROCKWEILER, N., HUSSAIN, M., HARRIS, J. D., CHEN, J., TURRI, G., AND SCHNOBER, C. Mallet, Nov. 2019. 

- [5] Overview of methodologies. 

- [6] AHLQVIST, T., VALOVIRTA, V., AND LOIKKANEN, T. Innovation policy roadmapping as a systemic instrument for forward-looking policy design. _Science and Public Policy 39_ , 2 (2012), 178–190. 

- [7] AMANATIDOU, E., BUTTER, M., CARABIAS, V., KÖNNÖLÄ, T., LEIS, M., SARITAS, O., SCHAPERRINKEL, P., AND VAN RIJ, V. On concepts and methods in horizon scanning: Lessons from initiating policy dialogues on emerging issues. _Science and Public Policy 39_ , 2 (2012), 208–221. 

   - [18] FLYAMER, I., COLIN, XUE, Z., LI, A., VAZQUEZ, V., MORSHED, N., NESTE, C. V., SCAINE1, AND MSKI_IKSM. Phlya/adjusttext: Trying zenodo, Nov. 2018. 

- [8] ANSOFF, H. I. Managing strategic surprise by response to weak signals. _California management review 18_ , 2 (1975), 21–33. 

- [19] GLÄNZEL, W., AND THIJS, B. Using ‘core documents’ for detecting and labelling new emerging topics. _Scientometrics 91_ , 2 (2012), 399–416. 

10 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 

- [20] ISSERMAN, A. M. The location quotient approach to estimating regional economic impacts. _Journal of the American Institute of Planners 43_ , 1 (1977), 33–41. 

- [21] KARYPIS, G. Cluto-a clustering toolkit. Tech. rep., MINNESOTA UNIV MINNEAPOLIS DEPT OF COMPUTER SCIENCE, 2002. 

- [22] KÖNNÖLÄ, T., SALO, A., CAGNIN, C., CARABIAS, V., AND VILKKUMAA, E. Facing the future: Scanning, synthesizing and sense-making in horizon scanning. _Science and public policy 39_ , 2 (2012), 222–231. 

- [23] KU, H. H., ET AL. Notes on the use of propagation of error formulas. _Journal of Research of the National Bureau of Standards 70_ , 4 (1966). 

- [24] MCINNES, L., HEALY, J., SAUL, N., AND GROSSBERGER, L. Umap: Uniform manifold approximation and projection. _Journal of Open Source Software 3_ , 29 (2018), 861. 

- [25] MIMNO, D. Using phrases in mallet topic models. 

- [26] MIMNO, D., WALLACH, H. M., TALLEY, E., LEENDERS, M., AND MCCALLUM, A. Optimizing semantic coherence in topic models. In _Proceedings of the conference on empirical methods in natural language processing_ (2011), Association for Computational Linguistics, pp. 262–272. 

- [27] NEWVILLE, M., OTTEN, R., NELSON, A., INGARGIOLA, A., STENSITZKI, T., ALLAN, D., FOX, A., CARTER, F., MICHAŁ, PUSTAKHOD, D., RAM, Y., GLENN, DEIL, C., STUERMER, BEELEN, A., FROST, O., ZOBRIST, N., PASQUEVICH, G., HANSEN, A. L. R., SPILLANE, T., CALDWELL, S., POLLORENO, A., ANDREWHANNUM, ZIMMERMANN, J., BORREGUERO, J., FRAINE, J., DEEP 42-THOUGHT, MAIER, B. F., GAMARI, B., AND ALMARZA, A. lmfit/lmfit-py 1.0.0, Dec. 2019. 

- [28] POPPER, R., ET AL. Foresight methodology. _The handbook of technology foresight_ (2008), 44–88. 

- [29] SIEVERT, C., AND SHIRLEY, K. Ldavis: A method for visualizing and interpreting topics. In _Proceedings of the workshop on interactive language learning, visualization, and interfaces_ (2014), pp. 63–70. 

- [30] SMITH, A., HAWES, T., AND MYERS, M. Hiérarchie : Interactive visualization for hierarchical topic models. 

- [31] SUN, Y., BARBER, R., GUPTA, M., AGGARWAL, C. C., AND HAN, J. Co-author relationship prediction in heterogeneous bibliographic networks. In _2011 International Conference on Advances in Social Networks Analysis and Mining_ (2011), IEEE, pp. 121–128. 

11 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 

## **A Supplementary Information** 

A summary of the data, tools and methods used in this work appears in Table 3. 

### **A.1 Junk Topics** 

Examples of junk topics excluded in this study appear in Table 4. An explanation for the rejection of each topic appears below with the cooresponding topic index: 

- 8203: Database artifact example: abstracts which included Indonesian words 

- 4593: Example of broad, technical topics that do not specifically indicate a particular technology area. 

- 8260 and 7037: Some topics that are focused on geographic regions. 

- 4551: Example of a non-technical topic that may be relevant to other disciplines but out of scope for this study. 

- 7375: Example of a topic area that is growing in size, but due to largely non-technology reasons. 

- 7190: Low coherency topics are often not specific enough to indicate a technical area. 

- 9548: The largest topic in this study does not contain any specific terms. 

### **A.2 Topic Modeling Parameters** 

Tuning files used in _MALLET_ were developed by several analysts including the following: (1) Multi-word stoplists were developed based on common non-technical phrases found in the abstracts _i.e. copyright John Wiley and Sons_ . (2) A typical lemmatization file was modified by analysts to eliminate false matches _i.e. replacement of “ground” with “grind” was removed so that “ground truth” is not replaced with “grind truth.”_ (3) Analyst-curated multiword replacement files were used to destructively aggregate technical phrases such as _“global positioning system”_ to _“global_positioning_system.”_ These phrases were discovered through repeated topic modeling iterations of the corpus and examining the topic phrase output. 

To improve the computation speed as well as make the model more robust to noise (such as infrequently found tokens arising from text markup languages or other text artifacts), the vocabulary was further pruned based on the _inverse document frequency (IDF)_ to a fixed vocabulary size of 200 _,_ 000 tokens. All terms that occurred in more than 5% of the corpus were eliminated. The fixed vocabulary size and upper bound resulted in a lower bound cutoff of 37 occurrences. 

The following parameters were used in MALLET: (1) To allow for different topic sizes, hyper-parameter optimization was performed and carried out every 10 iterations. (2) Based on examining the _log likelihood per token (LL/token)_ generated as part of MALLET’s output, 750 iterations 



Figure 8: A histogram of the _Topic Coherence_ for all 10,000 topics modeled by _MALLET LDA_ , with the mean, median and mode of the distribution plotted as reference lines. INSET: Expanded view of distribution. 



Figure 9: Example of a particularly poor fit. Documents (Frequency) versus Year Published for _Topic 4102: Blockchain_ , including error bars (which are very similar to the size of the marker). Orange line is the best fit line based on non-linear regression. 

was selected to balance computation time with accuracy. The final optimized _LL/token_ was _−_ 7 _._ 45623. (3) Multithreading was turned on to further improve computation time. Overall, using a Linux-based system with 192GB RAM and 96 cores with a computation time of 2 days and 5 hours was achieved. A histogram of the topic coherence for all 10,000 topics appears in Figure 8. 

### **A.3 Evaluation of Fit Quality** 

Figure 9 shows a trace of a particularly poor model fit, _Topic 4102_ , which has good coherence and has terms related to _blockchain technology_ . Despite the large errors (both in CAGR and the reduced chi-squared, _χ_<sup>2</sup> _r_<sup>), the</sup> model does not appear to do too poorly a job based on visual inspection: it captures the upward trend and overall 

12 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 

Table 3: Summary of data, tools, software packages, addons and libraries employed in the analyses used in this work. 

|**Data/Analytic Method**|**Package: Addons**|
|---|---|
|Data Source<br>Topic Modeling/LDA<br>Location Quotient (LQ)|_Dimensions_[3]<br>_MALLET[17]_<br>_Python 3.81_|
|Compound Annual Growth<br>Rate (CAGR)|_Python 3.81: LMFIT[27]_|
|Topic Map Layout|_UMAP[24]_|
|Topic Map Visualization|_Plotly Dash[2], Bokeh[4]_<br>_Python 3.81: matplotlib[13]_,<br>_adjustText[18]_|



Table 4: Examples of topics excluded from the analysis 

|**Topic**<br>**Index**|**Topic Name**|**Top Terms**|**Coherence**|**Documents**|**CAGR(%)**|
|---|---|---|---|---|---|
|8203|Indonesian Articles|dan, indonesia, pada, bali, keyword|-555|2153|65_±_3|
|4593|Placebo|placebo, randomize, trial, efficacy, baseline|-407|1093|48_±_27|
|8260|Ukraine|ukraine, ukrainian, exp, national, modern|-742|1526|35_±_6|
|4551|Islam|islamic, muslim, islam, religious, qur|-531|2841|30_±_3|
|7037|Learning|student, learning, class, teach, skill|-430|1846|99_±_14|
|7375|Syrian Refugees|refugee, asylum, syrian, humanitarian, camp|-423|1672|27_±_4|
|7190|[not coherent]|dock, station, fenugreek, nectin, cancel|-2040|663|36_±_19|
|4764|[administrative terms]|correction, erratum, online, corrigendum, figure|-673|5677|36_±_10|
|9548|[nonspecific terms]|phenomenon, avoid, call, unexpected, wrong|-762|14039|3_±_0|



shape of the data, coming _"quite close"_ to all points in the curve. However, because the fitting is many error bars away from the actual points, this is negatively reflected in both the CAGR error and _χ_<sup>2</sup> _r_<sup>.</sup> 

### **A.3.1 Document Frequency Error Bars** 

Since error rates in document frequencies are difficult to estimate, the following criteria was used to estimate them: (1) they were set proportional to ( _∼ √N_ ), where _N_ is the document count, to reflect the fact that large document counts provide more statistically significant information � _<u>δNN</u>_<sup>=</sup> _~~√~~_ <u>1</u> _N_ � and (2) a scaling factor was determined by iteratively inspecting the _χ_<sup>2</sup> _r_<sup>distribution and adjusting to</sup> retrieve a _χ_<sup>2</sup> _r_<sup>distribution with a mode centered at 1</sup><sup>_._0.This</sup> procedure avoided having too many _χ_<sup>2</sup> _r_<sup>s much smaller than</sup> 1 (overestimated error bars), or automatically implying the wrong model without further evaluation. 

### **A.3.2 Analysis of Error Rate Distributions** 

Figure 10 is a plot of the CAGR percentage error (100 _×_ <u>∆</u> _CAGRCAGR_<sup>) versus (</sup><sup>_χ_</sup> _r_<sup>2).The distribution of fits across both</sup> parameters is quite broad. Horizontal dotted lines define an arbitrary band of acceptable fits (0 _._ 5 _< χ_<sup>2</sup> _r_<sup>_<_1</sup><sup>_._5), while</sup> the vertical reference line corresponds to CAGR percentage errors less than 50%. The topic model fits that satisfy both conditions reside in the "good neighborhood" (small rectangle indicated in figure). Points inside the good neighborhood can be viewed as high confidence points (good nonlinear regression and small CAGR percentage error). 



Figure 10: Plot of Reduced Chi Squared versus the Percent Error of CAGR. Solid rectangle: a guide to the eye, of good topic model fits (see description in text). For reference, the location of topic 4102: Blockchain is also shown. 

13 

Bibliometric Horizon Scanning 

_Distribution A: Approved for public release._ 

These topics can have any growth rate but what is emphasized here is the reliability of the results in that good neighborhood. Points above the rectangle but to the left of the 50% error (for example the point corresponding to the “Blockchain” topic indicated in the figure) could still be significant: even though their _χ_<sup>2</sup> _r_<sup>is large, this could be due</sup> to the difficulty in estimating the errors in the time series. Only 1 _,_ 132 of the 10 _,_ 000 (or 11%) topics modeled can be found in the "good neighborhood." From a rigorous, and purely statistical standard, the strict interpretation is that the hypothesis that the model explains the majority of the data must be rejected. This can be explained by (1) the small number of data points (5 per topic), (2) the simplicity of our exponential growth model (i.e. no constant background, no leveling off), and (3) no good estimates of document frequency errors are, requiring us to apply the above described methodology to estimate them. A more balanced interpretation is that despite these obstacles, it is encouraging that this approach did not completely fail (i.e. capturing a surprising number of good fits (11%) despite the model simplicity), and that even a very poor fit appears to be visually acceptable (Figure 9). This is a promising foundation for a more detailed growth model that captures the complexity of the scientific enterprise that should be investigated in future work. 

14 

