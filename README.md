# Yelp-Dataset-Challenge-2015

###### 1. Task : For each yelp business, there is category information (one business may belong to multiple categories). Yelp also has the review and tip information for a particular business provided by users. 
###### Example: "categories": ["Indian", "Restaurants"]
###### For task 1, the research question is to predict categories for each business by using the review and tip information. 

*>INDEX GENERATION:*

	1. CreateTrainingAndTestCollections.java: 
		Imports the yelp data of business, review and tips into mongoDB and creates 60% training 
		collection 40% test collection. Each collection has business id, it's associated 
		categories, reviews and tips information.
				
	2. GenerateIndex.java: 
		Creates training and test indexes using lucene. For each record in the training and test 
		collections in mongoDB, Fetches the business_id, categories, combines reviews and tips, 
		then adds it to the lucene document.
			
*>QUERY GENERATION:*

	1. QueryOptimizer.java: 
		This class is used to iterate over every category (read from an input file), extract 
		tips and review information pertaining to a category from the train index, POS tag the 
		text and then extract the top query words for the category based on high TF*IDF score. 
		
		Important Functions :
		public void buildQueries(ArrayList<String> categories);
		public ArrayList<String> getNounsForCategory(String text);
		public String getConsolidatedReviewAndTipForCategory(TopDocs topdocs);

	2. ScoreCalculator.java:
		This class takes all the nound words for a given category (after POS tagging), and 
		then coputes the TF*IDF score for each nouns and returns top n nouns to form a query 
		for the given category.
		
		Important Functions :
		public Double calculateScore(String nounword, ScoreDoc[] scoredocs);
		public ArrayList<String> getTopQueryWordsForCategory(ArrayList<String> nouns, TopDocs 
		topdocs, String category);
			

	3. Tagger.java: 
		This class uses the stanford-postagger jar file to tag text and extract nouns based on 
		the english-left3words-distsim tagger model. 
		
		Important Functions :
		public ArrayList<String> tagText(String text);

*>CATEGORY PREDICTION:*

	1. CategoryPredictor.java: 
		This class read all the queries from a query file, run the queries on the test index 
		and predicts categories for business based, using different similarity algorithms.
		
		Important Functions :
		public void rank(ArrayList<String> queries, String algo);

	2. CategoryBusinessMapping.java:
		This class is used to create the ground truth file of businesses and category mapping, 
		which is to be then used for final evaluation.  
		
		Important Functions :
		public void buildGroundTruthFile();
			
###### 2. Task: Prediction of restaurant ratings with respect to user.
	a. User-Business attribute model
	
		1.PreProcessing :

			Important Files :
			Execute 'scriptFileModifier.py'
			'FeatureGenerator.py'

			Important Functions :
			GenCat(dirPath)
			featureGen()
			featureSelect()
			applyPreProc()

		2.Classifiers :

			Important Files :
			Execute 'script_classify.py'
			'algorithms.py'

			Important Functions :
			runClassifier(fileName1,fileName2,1,flag)

	b. Sentiment Analysis
		Class Name: ComputeUnigramFeatures
			This class is used to compute unigram features for sentiment analysis. Bag of words 
			assumption is used to compute frequencies of each unigram feature generated. Lucene 
			is used to remove stop words, tokenization and generation of unigram features from 
			review text.

		Class Name: ComputeBiGramFeatures
			This class is used to compute bigram features for sentiment analysis. Bag of words 
			assumption is used to compute frequencies of each bigram feature generated. Lucene 
			is used to remove stop words, tokenization and generation of bigram features from 
			review text.

		Class Name: FeatureCreation
			This class is used to generate frequency count for each feature generated through 
			feature generation program. This program computes frequencies for both bigrams as 
			well as unigrams. In multiple experiments, feature frequencies were also generated 
			for individual unigrams and bigrams.

		R File: SentimentAnalysis.R
			This file contains code to analyze train data class distribution, visualization of 
			word cloud for generated features as per ratings and run different regression 
			algorithms.
				
				
###### Evaluation
	
	1. Task 2 Evaluation.py
		Similar python code is used to generate recall and precision there with different files.

	2. Task 2 Evaluation.py
		This file contains code used to calculate different metrics used in Task 2

	3. Other files used for generating graphs.
				

